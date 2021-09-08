from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from .model import MaritalStatus
from .schema import MaritalStatus as MaritalStatusSchema, MaritalStatusCreate
from ...helpers.seed_data import seed_data

router = SQLAlchemyCRUDRouter(
    schema=MaritalStatusSchema,
    create_schema=MaritalStatusCreate,
    db_model=MaritalStatus,
    db=get_database,
    prefix="marital-status"
)


@router.post("/seed")
def seed_initial_data(db: Session = Depends(get_database)):
    list = ["NO INFORMADO",
            "CASADO",
            "DIVORCIADO",
            "DIVORCIADO CONVIVIENTE",
            "SEPARADO",
            "SEPARADO CONVIVIENTE",
            "SOLTERO",
            "SOLTERO CONVIVIENTE",
            "VIUDO",
            "FALLECIDO"]
    seed_data(db, list, MaritalStatus)

    return {"message": "Datos creados"}
