from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from .model import MaritalStatus
from .schema import MaritalStatus as MaritalStatusSchema, MaritalStatusCreate


router = SQLAlchemyCRUDRouter(
    schema=MaritalStatusSchema,
    create_schema=MaritalStatusCreate,
    db_model=MaritalStatus,
    db=get_database,
    prefix="marital-status"
)
