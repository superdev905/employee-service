from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from .model import Scholarship
from .schema import Scholarship as ScholarshipSchema, ScholarshipCreate
from ...helpers.seed_data import seed_data

router = SQLAlchemyCRUDRouter(
    schema=ScholarshipSchema,
    create_schema=ScholarshipCreate,
    db_model=Scholarship,
    db=get_database,
    prefix="scholarship"
)


@router.post("/seed")
def seed_initial_data(db: Session = Depends(get_database)):
    list = ["NO INFORMADO",
            "1° BÁSICO",
            "2° BÁSICO",
            "3° BÁSICO",
            "4° BÁSICO",
            "5° BÁSICO",
            "6° BÁSICO",
            "7° BÁSICO",
            "8° BÁSICO",
            "1° MEDIO",
            "2° MEDIO",
            "3° MEDIO",
            "4° MEDIO",
            "5° MEDIO",
            "ANALFABETO",
            "ESPECIAL",
            "KINDER",
            "LEE Y ESCRIBE",
            "PRE KINDER",
            "SALA CUNA",
            "TÉC/COM/IND COMPLETA",
            "TÉC/COM/IND INCOMPLETA",
            "UNIVERSITARIA COMPLETA",
            "UNIVERSITARIA INCOMPLETA"]
    seed_data(db, list, Scholarship)

    return {"message": "Datos creados"}
