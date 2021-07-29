from fastapi.encoders import jsonable_encoder
from fastapi.param_functions import Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import joinedload
from sqlalchemy.orm.session import Session
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from .model import Employee
from .schema import EmployeeSchema, EmployeeCreate


router = SQLAlchemyCRUDRouter(
    schema=EmployeeSchema,
    create_schema=EmployeeCreate,
    db_model=Employee,
    db=get_database,
    prefix="employees"
)


@router.post("")
def overloaded_create_one(employee: EmployeeCreate, db: Session = Depends(get_database)):
    saved_employee = Employee(**jsonable_encoder(employee))
    db.add(saved_employee)
    db.commit()
    db.refresh(saved_employee)
    return {"message": "Saved"}


@router.get("/{item_id}")
def overloaded_create_one(item_id: int = None, db: Session = Depends(get_database)):
    found_employee = db.query(Employee).filter(
        Employee.id == item_id).options(joinedload(Employee.nationality),
                                        joinedload(Employee.bank),
                                        joinedload(Employee.marital_status),
                                        joinedload(Employee.scholarship)).first()
    if not found_employee:
        raise HTTPException(
            status_code=400, detail="Este trabajador no existe")

    return found_employee
