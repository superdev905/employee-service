from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from .model import Bank
from .schema import Bank as BankSchema, BankCreate
from ...helpers.seed_data import seed_data

router = SQLAlchemyCRUDRouter(
    schema=BankSchema,
    create_schema=BankCreate,
    db_model=Bank,
    db=get_database,
    prefix="banks"
)


@router.post("/seed")
def seed_initial_data(db: Session = Depends(get_database)):
    list = ["BancoEstado",
            "BBVA",
            "Citibank N.A. Chile",
            "Corpbanca",
            "Credichile",
            "Credit Suisse Consultas y Asesorias Limitada",
            "Deutsche Bank",
            "ING Bank N.V.",
            "Redbanc",
            "Santander Banefe",
            "Scotiabank Sud Americano",
            "Scotiabank Sud Americano",
            "UBS AG in Santiago de Chile"]
    seed_data(db, list, Bank)

    return {"message": "Datos creados"}
