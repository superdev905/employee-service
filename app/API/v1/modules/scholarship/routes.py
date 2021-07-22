from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from .model import Scholarship
from .schema import Scholarship as ScholarshipSchema, ScholarshipCreate


router = SQLAlchemyCRUDRouter(
    schema=ScholarshipSchema,
    create_schema=ScholarshipCreate,
    db_model=Scholarship,
    db=get_database,
    prefix="scholarship"
)
