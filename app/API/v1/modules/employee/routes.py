
from typing import Optional
from fastapi.encoders import jsonable_encoder
from fastapi.param_functions import Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import joinedload
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.elements import and_, or_
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from app.settings import SERVICES
from ..employee_job.model import EmployeeJob
from ..housing_situation.model import HousingSituation
from ..pension_situation.model import PensionSituation
from .model import Employee
from .schema import EmployeeSchema, EmployeeCreate, EmployeePatch
from .services import get_bank, get_marital_status, fetch_data

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
    saved_employee = Employee(**jsonable_encoder(employee))
    db.add(saved_employee)
    db.commit()
    db.refresh(saved_employee)
    return saved_employee


@router.get("/{item_id}")
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
    bank_details = get_bank(
        found_employee.bank_id) if found_employee.bank_id else None
    return {**found_employee.__dict__,
            "bank": bank_details,
            "marital_status": get_marital_status(found_employee.marital_status_id),
            "nationality": fetch_data(found_employee.nationality_id, "nationalities"),
            "scholarship": fetch_data(found_employee.scholarship_id, "scholarship"),
            "current_job": current_job,
            "house_status": house_status,
            "pension_status": pension_status}


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
