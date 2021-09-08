from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from .model import Nationality
from .schema import Nationality as NationalitySchema, NationalityCreate
from ...helpers.seed_data import seed_data

router = SQLAlchemyCRUDRouter(
    schema=NationalitySchema,
    create_schema=NationalityCreate,
    db_model=Nationality,
    db=get_database,
    prefix="nationalities"
)


@router.post("/seed")
def seed_initial_data(db: Session = Depends(get_database)):
    list = ["ARGENTINO",
            "BOLIVIANO",
            "CHILENO",
            "COLOMBIANO",
            "COSTARRICENSE",
            "CUBANO",
            "DOMINICANO",
            "ECUATORIANO",
            "GUATEMALTECO",
            "HONDUREÑO",
            "MEXICANO",
            "NICARAGÜENSE",
            "PANAMEÑO",
            "PARAGUAYO",
            "PERUANO",
            "PUERTORRIQUEÑO",
            "SALVADOREÑO",
            "URUGUAYO",
            "VENEZOLANO"]
    seed_data(db, list, Nationality)

    return {"message": "Datos creados"}
