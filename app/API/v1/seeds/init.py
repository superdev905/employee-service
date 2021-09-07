from fastapi.param_functions import Depends
from sqlalchemy.orm import Session
from app.database.main import get_database


def seed_base_data():
    db = get_database()
    # seed_maritalStatus(db)
    # seed_nationalities(db)
