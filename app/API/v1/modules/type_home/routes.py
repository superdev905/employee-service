from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from .model import TypeHome
from .schema import TypeHome as TypeHomeSchema, TypeHomeCreate


router = SQLAlchemyCRUDRouter(
    schema=TypeHomeSchema,
    create_schema=TypeHomeCreate,
    db_model=TypeHome,
    db=get_database,
    prefix="types-home"
)
