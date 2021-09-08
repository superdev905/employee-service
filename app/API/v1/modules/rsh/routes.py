from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from .model import RSH
from .schema import RSH as RSHSchema, RSHCreate
from ...helpers.seed_data import seed_data

router = SQLAlchemyCRUDRouter(
    schema=RSHSchema,
    create_schema=RSHCreate,
    db_model=RSH,
    db=get_database,
    prefix="rsh"
)


@router.post("/seed")
def seed_initial_data(db: Session = Depends(get_database)):
    list = ["EN PROCESO",
            "HASTA 40 %",
            "41 % A 50 %",
            "51 % A 60 %",
            "61 % A 70 %",
            "71 % A 80 %",
            "81 % A 90 %",
            "91 % A 100 %"]
    seed_data(db, list, RSH)

    return {"message": "Datos creados"}
