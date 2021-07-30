from fastapi.param_functions import Depends
from sqlalchemy.orm import joinedload
from sqlalchemy.orm.session import Session
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from .model import Specialty
from .schema import Specialty as SpecialtySchema, SpecialtyCreate


router = SQLAlchemyCRUDRouter(
    schema=SpecialtySchema,
    create_schema=SpecialtyCreate,
    db_model=Specialty,
    db=get_database,
    prefix="specialties"
)


@router.get("")
def overloaded_get_all(skip: int = 0,
                       limit: int = 20,
                       db: Session = Depends(get_database)):
   
    return db.query(Specialty).options(
        joinedload(Specialty.sub_specialties)).offset(skip).limit(limit).all()
