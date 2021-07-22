from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from .model import TypeSubsidy
from .schema import TypeSubsidy as TypeSubsidySchema, TypeSubsidyCreate


router = SQLAlchemyCRUDRouter(
    schema=TypeSubsidySchema,
    create_schema=TypeSubsidyCreate,
    db_model=TypeSubsidy,
    db=get_database,
    prefix="types-subsidy"
)
