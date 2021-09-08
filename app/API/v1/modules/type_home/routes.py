from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from .model import TypeHome
from .schema import TypeHome as TypeHomeSchema, TypeHomeCreate
from ...helpers.seed_data import seed_data

router = SQLAlchemyCRUDRouter(
    schema=TypeHomeSchema,
    create_schema=TypeHomeCreate,
    db_model=TypeHome,
    db=get_database,
    prefix="types-home"
)


@router.post("/seed")
def seed_initial_data(db: Session = Depends(get_database)):
    list = ["NO INFORMADO",
            "CASA",
            "DEPARTAMENTO",
            "MEDIAGUA",
            "PIEZA",
            "SITIO"]
    seed_data(db, list, TypeHome)

    return {"message": "Datos creados"}
