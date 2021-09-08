from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from .model import IsapreFonasa
from .schema import IsapreFonasa as IsapreFonasaSchema, IsapreFonasaCreate
from ...helpers.seed_data import seed_data

router = SQLAlchemyCRUDRouter(
    schema=IsapreFonasaSchema,
    create_schema=IsapreFonasaCreate,
    db_model=IsapreFonasa,
    db=get_database,
    prefix="isapre-fonasa"
)


@router.post("/seed")
def seed_initial_data(db: Session = Depends(get_database)):
    list = ["Isapre",
            "Fonasa"
            ]
    seed_data(db, list, IsapreFonasa)

    return {"message": "Datos creados"}
