from typing import Optional
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from fastapi.encoders import jsonable_encoder
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from .model import EmployeeContact
from .schema import EmployeeContact as EmployeeContactSchema, EmployeeContactCreate


router = SQLAlchemyCRUDRouter(
    schema=EmployeeContactSchema,
    create_schema=EmployeeContactCreate,
    db_model=EmployeeContact,
    db=get_database,
    prefix="employee-contacts"
)


@router.get("")
def overloaded_get_all(skip: int = None,
                       limit: int = None,
                       employee_run: Optional[str] = None,
                       db: Session = Depends(get_database)):
    filters = []
    if employee_run:
        filters.append(EmployeeContact.employee_run == employee_run)

    return db.query(EmployeeContact).filter(*filters).offset(skip).limit(limit).all()


@router.post("")
def overloaded_create_one(contact: EmployeeContactCreate, db: Session = Depends(get_database)):
    obj_relative = jsonable_encoder(contact)
    db_obj = EmployeeContact(**obj_relative)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
