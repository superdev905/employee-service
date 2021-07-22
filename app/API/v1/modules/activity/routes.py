from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from .model import Activity
from .schema import Activity as ActivitySchema, ActivityCreate


router = SQLAlchemyCRUDRouter(
    schema=ActivitySchema,
    create_schema=ActivityCreate,
    db_model=Activity,
    db=get_database,
    prefix="activities"
)
