from typing import Optional
from fastapi.param_functions import Depends
from fastapi.exceptions import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import joinedload
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import and_
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from ...helpers.fetch_data import fetch_parameter_data
from .model import EmployeeRelative
from .schema import EmployeeRelative as EmployeeRelativeSchema, EmployeeRelativeCreate


router = SQLAlchemyCRUDRouter(
    schema=EmployeeRelativeSchema,
    create_schema=EmployeeRelativeCreate,
    db_model=EmployeeRelative,
    db=get_database,
    prefix="employee-relatives"
)


def is_run_taken(db: Session, run: str, excluded_id: int):
    if(run == ""):
        return False

    filters = []
    if(excluded_id):
        filters.append(EmployeeRelative.id != excluded_id)
    filters.append(EmployeeRelative.run == run)
    print(filters)
    return bool(db.query(EmployeeRelative).filter(and_(*filters)).first())


@router.get("/{item_id}")
def get_one(item_id: int, db: Session = Depends(get_database)):

    db_obj = db.query(EmployeeRelative).filter(
        EmployeeRelative.id == item_id).first()

    if not db_obj:
        raise HTTPException(
            status_code=400, detail="Este familiar no está registrado")

    relationship = fetch_parameter_data(
        db_obj.relationship_id, "relationships")

    return {**db_obj.__dict__, "relationship": relationship["description"]}


@router.post("")
def overloaded_create_one(relative_in: EmployeeRelativeCreate, db: Session = Depends(get_database)):
    invalid_run = is_run_taken(db, relative_in.run, None)

    if invalid_run:
        raise HTTPException(
            status_code=400, detail="Este RUN ya esta registrado")

    obj_relative = jsonable_encoder(relative_in)
    db_obj = EmployeeRelative(**obj_relative)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


@router.put("/{item_id}")
def overloaded_update_one(item_id: int, relative_in: EmployeeRelativeCreate, db: Session = Depends(get_database)):

    db_obj = db.query(EmployeeRelative).filter(
        EmployeeRelative.id == item_id).first()

    if not db_obj:
        raise HTTPException(
            status_code=400, detail="Este familiar no está registrado")
    invalid_run = is_run_taken(db, relative_in.run, db_obj.id)

    if invalid_run:
        raise HTTPException(
            status_code=400, detail="Este RUN ya esta registrado")

    obj_data = jsonable_encoder(db_obj)

    if isinstance(relative_in, dict):
        update_data = relative_in
    else:
        update_data = relative_in.dict(exclude_unset=True)
    for field in obj_data:
        if field in update_data:
            setattr(db_obj, field, update_data[field])
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


@router.get("")
def overloaded_get_all(skip: int = None,
                       limit: int = None,
                       employee_run: Optional[str] = None,
                       db: Session = Depends(get_database)):
    filters = []
    if employee_run:
        filters.append(EmployeeRelative.employee_run == employee_run)

    return db.query(EmployeeRelative).filter(*filters).offset(skip).limit(limit).all()


@router.patch('/{item_id}/block')
def block_one(item_id: int, db: Session = Depends(get_database)):
    found_employee = db.query(EmployeeRelative).filter(
        EmployeeRelative.id == item_id).first()
    if not found_employee:
        raise HTTPException(
            status_code=400, detail="Este empleado no existe")
    found_employee.state = "DELETED"

    db.commit()
    db.refresh(found_employee)

    return found_employee
