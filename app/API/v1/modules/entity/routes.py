from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from .model import Entity
from .schema import Entity as EntitySchema, EntityCreate


router = SQLAlchemyCRUDRouter(
    schema=EntitySchema,
    create_schema=EntityCreate,
    db_model=Entity,
    db=get_database,
    prefix="entities"
)
