from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from .model import Activity
from .schema import Activity as ActivitySchema, ActivityCreate
from ...helpers.seed_data import seed_data

router = SQLAlchemyCRUDRouter(
    schema=ActivitySchema,
    create_schema=ActivityCreate,
    db_model=Activity,
    db=get_database,
    prefix="activities"
)


@router.post("/seed")
def seed_data(db: Session = Depends(get_database)):
    list = ["DUEÑA DE CASA",
            "ESTUDIANTE",
            "JUBILADO/PENSIONADO",
            "MENOR",
            "SIN ACTIVIDAD",
            "TRABAJADOR"]

    for item in list:
        found_obj = db.query(Activity).filter(
            Activity.description == item).first()
        if not found_obj:
            obj_db = Activity(description=item, created_by=1)
            db.add(obj_db)
            db.commit()
            db.refresh(obj_db)
    return {"message": "Datos creados"}
