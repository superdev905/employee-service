from dateutil import parser
from datetime import datetime
from typing import List, Optional
from fastapi import Request, APIRouter, Query
from fastapi.encoders import jsonable_encoder
from fastapi.param_functions import Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.elements import and_, or_
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from app.settings import SERVICES
from ..employee_job.model import EmployeeJob
from ..housing_situation.model import HousingSituation
from ..pension_situation.model import PensionSituation
from ..employee_contact.model import EmployeeContact
from ..specialization.model import Specialization
from ..attachment.services import get_employee_files
from ..attachment.schema import AttachmentItem
from .model import Employee, EmployeeRevision
from .schema import EmployeeRevisionCreate, EmployeeSchema, EmployeeCreate, EmployeePatch, EmployeeValidate
from ...helpers.fetch_data import fetch_parameter_data, fetch_parameter_public, fetch_service, fetch_users_service
from .services import filter_attachments, get_bank, get_marital_status, fetch_data

router = SQLAlchemyCRUDRouter(
    schema=EmployeeSchema,
    create_schema=EmployeeCreate,
    db_model=Employee,
    db=get_database,
    prefix="employees"
)


@router.get("")
def get_all(skip: int = 0, limit: int = 30,
            search: Optional[str] = None,
            state: Optional[str] = None,
            include_total: Optional[bool] = False,
            db: Session = Depends(get_database)):
    state_filters = []
    if state:
        state_filters.append(Employee.state == state)
    str_filters = []
    if(search):
        formatted_search = "{}%".format(search)

        str_filters.append(Employee.names.ilike(formatted_search))
        str_filters.append(Employee.paternal_surname.ilike(formatted_search))
        str_filters.append(Employee.maternal_surname.ilike(formatted_search))
        str_filters.append(Employee.run.ilike(formatted_search))
    total = 0
    if(include_total):
        total = len(db.query(Employee).filter(
            and_(*state_filters, or_(*str_filters))).all())

    list = db.query(Employee).filter(and_(*state_filters, or_(*str_filters))
                                     ).order_by(Employee.created_at.desc()).offset(skip).limit(limit).all()

    return {"docs": list, "total": total} if include_total == True else list


@router.post("")
def overloaded_create_one(employee: EmployeeCreate, db: Session = Depends(get_database)):
    found_employee = db.query(Employee).filter(
        Employee.run == employee.run).first()
    if found_employee:
        raise HTTPException(
            status_code=400, detail="Este run ya esta registrado")

    saved_employee = Employee(**jsonable_encoder(employee))
    db.add(saved_employee)
    db.commit()
    db.refresh(saved_employee)
    return saved_employee


@router.get("/{item_id}")
def get_one(req: Request, item_id: int = None, db: Session = Depends(get_database)):
    found_employee = db.query(Employee).filter(
        Employee.id == item_id).first()
    if not found_employee:
        raise HTTPException(
            status_code=400, detail="Este trabajador no existe")
    current_job = db.query(EmployeeJob).filter(and_(EmployeeJob.employee_id == item_id,
                                                    EmployeeJob.state != "DELETED")).order_by(EmployeeJob.created_at.desc()).first()
    house_status = db.query(HousingSituation).filter(and_(HousingSituation.employee_id == item_id,
                                                          HousingSituation.state != "DELETED")).order_by(HousingSituation.created_at.desc()).first()
    pension_status = db.query(PensionSituation).filter(and_(PensionSituation.employee_id == item_id,
                                                            PensionSituation.state != "DELETED")).order_by(PensionSituation.created_at.desc()).first()
    bank_details = fetch_parameter_data(req.token,
                                        found_employee.bank_id,
                                        "banks") if found_employee.bank_id else None
    specialty = db.query(Specialization).filter(
        Specialization.employee_id == item_id).order_by(Specialization.created_at.desc()).first()

    contact = db.query(EmployeeContact).filter(
        EmployeeContact.employee_run == found_employee.run).first()

    return {**found_employee.__dict__,
            "bank": bank_details,
            "marital_status": fetch_parameter_data(req.token, found_employee.marital_status_id, "marital-status"),
            "nationality": fetch_parameter_data(req.token, found_employee.nationality_id,  "nationalities"),
            "scholarship": fetch_parameter_data(req.token, found_employee.scholarship_id, "scholarship"),
            "current_job": current_job,
            "house_status": house_status,
            "pension_status": pension_status,
            "specialty": specialty,
            "contact": contact}


@router.post("/{item_id}/revision")
def create_revision(req: Request,
                    body: EmployeeRevisionCreate,
                    item_id: int = None,
                    db: Session = Depends(get_database)):
    found_employee = db.query(Employee).filter(
        Employee.id == item_id).first()
    if not found_employee:
        raise HTTPException(
            status_code=400, detail="Este trabajador no existe")
    assistance = fetch_users_service(req.token, body.assistance_id)
    assistance_names = "%s %s" % (
        assistance["names"], assistance["paternalSurname"])

    new_revision = jsonable_encoder(body, by_alias=False)
    new_revision["assistance_names"] = assistance_names.upper()
    new_revision["created_by"] = req.user_id

    db_revision = EmployeeRevision(**new_revision)

    db.add(db_revision)
    db.commit()
    db.refresh(db_revision)

    return db_revision


@router.put("/{item_id}")
def overloaded_update_one(item_id: int, update_body: EmployeeCreate, db: Session = Depends(get_database)):
    found_employee = db.query(Employee).filter(
        Employee.id == item_id).first()
    if not found_employee:
        raise HTTPException(
            status_code=400, detail="Este trabajador no existe")

    obj_data = jsonable_encoder(found_employee)

    if isinstance(update_body, dict):
        update_data = update_body
    else:
        update_data = update_body.dict(exclude_unset=True)
    for field in obj_data:
        if field in update_data:
            setattr(found_employee, field, update_data[field])
    db.add(found_employee)
    db.commit()
    db.refresh(found_employee)
    return found_employee


@router.patch("/{item_id}")
def patch_one(item_id: int, patch_body: EmployeePatch, db: Session = Depends(get_database)):
    found_employee = db.query(Employee).filter(
        Employee.id == item_id).first()
    if not found_employee:
        raise HTTPException(
            status_code=400, detail="Este trabajador no existe")

    obj_data = jsonable_encoder(found_employee)

    if isinstance(patch_body, dict):
        update_data = patch_body
    else:
        update_data = patch_body.dict(exclude_unset=True)
    for field in obj_data:
        if field in update_data:
            setattr(found_employee, field, update_data[field])

    db.add(found_employee)
    db.commit()
    db.refresh(found_employee)
    return found_employee


@router.get("/{item_id}/attachments", response_model=List[AttachmentItem])
def get_attachments(req: Request,
                    item_id: int,
                    start_date: datetime = Query(None, alias="startDate"),
                    end_date: datetime = Query(None, alias="endDate"),
                    db: Session = Depends(get_database)):

    all_files = []

    employee_files = get_employee_files(db, item_id)
    for file in employee_files:
        all_files.append({**file.__dict__, "module": "Trabjadores"})

    assistance_files = fetch_service(req.token, SERVICES["assistance"] +
                                     "/attachments?employee_id=%s" % format(item_id))
    for item in assistance_files:
        all_files.append({**item, "module": "Asistencia"})

    scholarship_files = fetch_service(req.token, SERVICES["scholarship"] +
                                      "/attachments?employee_id=%s" % format(item_id))
    for current in scholarship_files:
        all_files.append({**current, "module": "Becas"})

    return filter_attachments(all_files, start_date, end_date)


public_router = APIRouter(prefix="/employee",
                          tags=["Consultas web"])


@public_router.post("/validate")
def validate_rut(body: EmployeeValidate, db: Session = Depends(get_database)):
    found_employee = db.query(Employee).filter(
        Employee.run == body.rut).first()
    if not found_employee:
        raise HTTPException(
            status_code=400, detail="Este trabajador no existe")
    return {"employeeId": found_employee.id}


@public_router.get("/{item_id}")
def get_one(item_id: int = None, db: Session = Depends(get_database)):
    found_employee = db.query(Employee).filter(
        Employee.id == item_id).first()
    if not found_employee:
        raise HTTPException(
            status_code=400, detail="Este trabajador no existe")
    current_job = db.query(EmployeeJob).filter(and_(EmployeeJob.employee_id == item_id,
                                                    EmployeeJob.state != "DELETED")).order_by(EmployeeJob.created_at.desc()).first()
    house_status = db.query(HousingSituation).filter(and_(HousingSituation.employee_id == item_id,
                                                          HousingSituation.state != "DELETED")).order_by(HousingSituation.created_at.desc()).first()
    pension_status = db.query(PensionSituation).filter(and_(PensionSituation.employee_id == item_id,
                                                            PensionSituation.state != "DELETED")).order_by(PensionSituation.created_at.desc()).first()
    bank_details = fetch_parameter_public(found_employee.bank_id,
                                          "banks") if found_employee.bank_id else None

    specialty = db.query(Specialization).filter(
        Specialization.employee_id == item_id).order_by(Specialization.created_at.desc()).first()

    contact = db.query(EmployeeContact).filter(
        EmployeeContact.employee_run == found_employee.run).first()

    print('osjdisdjsijdisj', fetch_parameter_public(
        found_employee.marital_status_id, "marital-status"))

    return {**found_employee.__dict__,
            "bank": bank_details,
            "marital_status": fetch_parameter_public(found_employee.marital_status_id, "marital-status"),
            "nationality": fetch_parameter_public(found_employee.nationality_id,  "nationalities"),
            "scholarship": fetch_parameter_public(found_employee.scholarship_id, "scholarship"),
            "current_job": current_job,
            "house_status": house_status,
            "pension_status": pension_status,
            "specialty": specialty,
            "contact": contact}
