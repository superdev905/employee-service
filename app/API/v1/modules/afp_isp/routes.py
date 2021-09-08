from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from .model import AfpIsp
from .schema import AfpIsp as AfpIspSchema, AfpIspCreate
from ...helpers.seed_data import seed_data

router = SQLAlchemyCRUDRouter(
    schema=AfpIspSchema,
    create_schema=AfpIspCreate,
    db_model=AfpIsp,
    db=get_database,
    prefix="afp-isp"
)


@router.post("/seed")
def seed_initial_data(db: Session = Depends(get_database)):
    list = ["AFP Capital",
            "AFP Cuprum",
            "AFP Habitat",
            "AFP Modelo",
            "AFP Planvital",
            "AFP Provida",
            "AFP Uno",
            "OTRo"
            ]

    seed_data(db, list, AfpIsp, "description")
    return {"message": "Datos creados"}
