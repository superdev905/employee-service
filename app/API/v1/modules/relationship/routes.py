from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from .model import Relationship
from .schema import Relationship as RelationshipSchema, RelationshipCreate
from ...helpers.seed_data import seed_data


router = SQLAlchemyCRUDRouter(
    schema=RelationshipSchema,
    create_schema=RelationshipCreate,
    db_model=Relationship,
    db=get_database,
    prefix="relationships"
)


@router.post("/seed")
def seed_initial_data(db: Session = Depends(get_database)):
    list = ["NO INFORMADO",
            "CÓNYUGE",
            "CONVIVIENTE",
            "HIJO",
            "HIJA",
            "PADRE",
            "MADRE",
            "ABUELO/A",
            "HERMANO/A",
            "CUÑADO/A",
            "PRIMO/A",
            "SUEGRO/A",
            "NIETO",
            "OTRO",
            "HIJASTRO/A"]
    seed_data(db, list, Relationship, "description")

    return {"message": "Datos creados"}
