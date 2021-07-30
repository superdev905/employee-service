from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from .model import PropertyHome
from .schema import PropertyHome as PropertyHomeSchema, PropertyHomeCreate


router = SQLAlchemyCRUDRouter(
    schema=PropertyHomeSchema,
    create_schema=PropertyHomeCreate,
    db_model=PropertyHome,
    db=get_database,
    prefix="property-home"
)
