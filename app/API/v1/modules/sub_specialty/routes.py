from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from .model import SubSpecialty
from .schema import SubSpecialty as SubSpecialtySchema, SubSpecialtyCreate


router = SQLAlchemyCRUDRouter(
    schema=SubSpecialtySchema,
    create_schema=SubSpecialtyCreate,
    db_model=SubSpecialty,
    db=get_database,
    prefix="sub-specialties"
)
