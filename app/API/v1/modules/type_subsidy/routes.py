from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from .model import TypeSubsidy
from .schema import TypeSubsidy as TypeSubsidySchema, TypeSubsidyCreate
from ...helpers.seed_data import seed_data


router = SQLAlchemyCRUDRouter(
    schema=TypeSubsidySchema,
    create_schema=TypeSubsidyCreate,
    db_model=TypeSubsidy,
    db=get_database,
    prefix="types-subsidy"
)


@router.post("/seed")
def seed_initial_data(db: Session = Depends(get_database)):
    list = ["SIN SUBSIDIO",
            "BÁSICO SERVIU",
            "BÁSICO PRIVADO",
            "PET",
            "UNIFICADO",
            "LEASING HABITACIONAL",
            "RENOVACION URBANA",
            "OTRO"]
    seed_data(db, list, TypeSubsidy)

    return {"message": "Datos creados"}
