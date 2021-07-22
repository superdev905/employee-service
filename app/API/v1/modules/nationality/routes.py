from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from .model import Nationality
from .schema import Nationality as NationalitySchema, NationalityCreate


router = SQLAlchemyCRUDRouter(
    schema=NationalitySchema,
    create_schema=NationalityCreate,
    db_model=Nationality,
    db=get_database,
    prefix="nationalities"
)
