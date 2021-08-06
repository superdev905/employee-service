from typing import Optional
from fastapi.param_functions import Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import joinedload
from sqlalchemy.orm.session import Session
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from .model import HousingSituation
from .schema import HousingSituation as HousingSituationSchema, HousingSituationCreate, HousingSituationPatch


router = SQLAlchemyCRUDRouter(
    schema=HousingSituationSchema,
    create_schema=HousingSituationCreate,
    db_model=HousingSituation,
    db=get_database,
    prefix="housing-situation"
)


@router.get("")
def overloaded_get_all(skip: int = 0,
                       limit: int = 20,
                       employee_id: Optional[int] = None,
                       db: Session = Depends(get_database)):
    filters = []
    if employee_id:
        filters.append(HousingSituation.employee_id == employee_id)
    filters.append(HousingSituation.state != "DELETED")
    return db.query(HousingSituation).filter(*filters).options(
        joinedload(HousingSituation.type_home),
        joinedload(HousingSituation.property_home),
        joinedload(HousingSituation.type_subsidy)).offset(skip).limit(limit).all()


@router.patch('/{item_id}')
def block_one(item_id: int, patch_body: HousingSituationPatch, db: Session = Depends(get_database)):
    found_obj = db.query(HousingSituation).filter(
        HousingSituation.id == item_id).first()
    if not found_obj:
        raise HTTPException(
            status_code=400, detail="Este registro no existe")
    found_obj.state = patch_body.state
    db.add(found_obj)
    db.commit()
    db.refresh(found_obj)

    return found_obj
