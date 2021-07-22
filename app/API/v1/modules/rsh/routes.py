from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from .model import RSH
from .schema import RSH as RSHSchema, RSHCreate


router = SQLAlchemyCRUDRouter(
    schema=RSHSchema,
    create_schema=RSHCreate,
    db_model=RSH,
    db=get_database,
    prefix="rsh"
)
