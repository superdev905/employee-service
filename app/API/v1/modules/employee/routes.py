from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from .model import Employee
from .schema import Employee as EmployeeSchema, EmployeeCreate


router = SQLAlchemyCRUDRouter(
    schema=EmployeeSchema,
    create_schema=EmployeeCreate,
    db_model=Employee,
    db=get_database,
    prefix="employees"
)
