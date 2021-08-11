from typing import Optional
from fastapi.encoders import jsonable_encoder
from fastapi.param_functions import Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import joinedload
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.elements import and_, or_
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from .model import Employee
from .schema import EmployeeSchema, EmployeeCreate, EmployeePatch


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
        formatted_search = "%{}%".format(search)

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
        Employee.id == item_id).options(joinedload(Employee.nationality),
                                        joinedload(Employee.bank),
                                        joinedload(Employee.marital_status),
                                        joinedload(Employee.scholarship)).first()
    if not found_employee:
        raise HTTPException(
            status_code=400, detail="Este trabajador no existe")

    return found_employee


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
