from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from .model import Bank
from .schema import Bank as BankSchema, BankCreate


router = SQLAlchemyCRUDRouter(
    schema=BankSchema,
    create_schema=BankCreate,
    db_model=Bank,
    db=get_database,
    prefix="banks"
)
