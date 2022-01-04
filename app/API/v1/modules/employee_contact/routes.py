from typing import Optional
from fastapi import Request, APIRouter, Query
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from fastapi.exceptions import HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from .model import EmployeeContact
from .schema import EmployeeContact as EmployeeContactSchema, EmployeeContactCreate, EmployeeContactPatch
from ...helpers.fetch_data import fetch_parameter_data, fetch_parameter_public
from ...helpers.crud import get_updated_obj

router = SQLAlchemyCRUDRouter(
    schema=EmployeeContactSchema,
    create_schema=EmployeeContactCreate,
    db_model=EmployeeContact,
    db=get_database,
    prefix="employee-contacts"
)


@router.get("")
def get_all(
        req: Request,
        skip: int = None,
        limit: int = None,
        employee_run: Optional[str] = None,
        db: Session = Depends(get_database)):
    filters = []
    if employee_run:
        filters.append(EmployeeContact.employee_run == employee_run)
    filters.append(EmployeeContact.state != "DELETED")

    result = []
    list = db.query(EmployeeContact).filter(
        *filters).offset(skip).limit(limit).all()

    for item in list:
        result.append(
            {**item.__dict__,
             "region": fetch_parameter_data(req.token, item.region_id, "regions"),
             "commune": fetch_parameter_data(req.token, item.commune_id, "communes")})
    return result


@router.post("")
def overloaded_create_one(contact: EmployeeContactCreate, db: Session = Depends(get_database)):

    if db.query(EmployeeContact).filter(EmployeeContact.email == contact.email).first():
        raise HTTPException(
            status_code=400, detail="Este correo ya está registrado")

    obj_relative = jsonable_encoder(contact)
    db_obj = EmployeeContact(**obj_relative)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


@router.patch('/{item_id}')
def block_one(item_id: int, patch_body: EmployeeContactPatch,  db: Session = Depends(get_database)):
    found_employee = db.query(EmployeeContact).filter(
        EmployeeContact.id == item_id).first()
    if not found_employee:
        raise HTTPException(
            status_code=400, detail="Este empleado no existe")
    found_employee.state = patch_body.state

    db.add(found_employee)
    db.commit()
    db.refresh(found_employee)

    return found_employee


public_router = APIRouter(prefix="/employee-contact",
                          tags=["Consultas web"])


@public_router.get("")
def get_all(employee_run: Optional[str] = Query(None, alias="employeeRun"),
            db: Session = Depends(get_database)):

    filters = []
    if employee_run:
        filters.append(EmployeeContact.employee_run == employee_run)
    filters.append(EmployeeContact.state != "DELETED")

    contact = db.query(EmployeeContact).filter(*filters).first()

    result = {**contact.__dict__,
              "region": fetch_parameter_public(contact.region_id, "regions"),
              "commune": fetch_parameter_public(contact.commune_id, "communes")} if contact else None

    return result


@public_router.put("/{id}")
def update_contact(id: int,
                   body: EmployeeContactSchema,
                   db: Session = Depends(get_database)):
    contact = db.query(EmployeeContact).filter(
        EmployeeContact.id == id).first()
    if not contact:
        raise HTTPException(
            status_code=400, detail="Este contacto no existe")
    contact = get_updated_obj(contact, body)

    db.add(contact)
    db.commit()
    db.refresh(contact)

    return contact
