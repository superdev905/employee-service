from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from .model import Entity
from .schema import Entity as EntitySchema, EntityCreate
from ...helpers.seed_data import seed_data


router = SQLAlchemyCRUDRouter(
    schema=EntitySchema,
    create_schema=EntityCreate,
    db_model=Entity,
    db=get_database,
    prefix="entities"
)


@router.post("/seed")
def seed_initial_data(db: Session = Depends(get_database)):
    list = ["Entidad 1",
            "Entidad 3",
            "Entidad 2"
            ]
    seed_data(db, list, Entity)

    return {"message": "Datos creados"}
