from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from .model import Relationship
from .schema import Relationship as RelationshipSchema, RelationshipCreate


router = SQLAlchemyCRUDRouter(
    schema=RelationshipSchema,
    create_schema=RelationshipCreate,
    db_model=Relationship,
    db=get_database,
    prefix="relationships"
)
