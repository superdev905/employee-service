from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from .model import PropertyHome
from .schema import PropertyHome as PropertyHomeSchema, PropertyHomeCreate
from ...helpers.seed_data import seed_data

router = SQLAlchemyCRUDRouter(
    schema=PropertyHomeSchema,
    create_schema=PropertyHomeCreate,
    db_model=PropertyHome,
    db=get_database,
    prefix="property-home"
)


@router.post("/seed")
def seed_initial_data(db: Session = Depends(get_database)):
    list = ["NO INFORMADO",
            "ARRENDATARIO",
            "ALLEGADO",
            "PROPIETARIO DEUDOR",
            "PROPIETARIO NO DEUDOR",
            "TOMA/CAMPAMENTO",
            "CUIDADOR",
            "CASA DE FAMILIARES",
            "CASA DE AMIGOS",
            "OTRO"]
    seed_data(db, list, PropertyHome)

    return {"message": "Datos creados"}
