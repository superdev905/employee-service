from typing import Optional
from fastapi import Request
from fastapi.param_functions import Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from .model import HousingSituation
from .schema import HousingSituation as HousingSituationSchema, HousingSituationCreate, HousingSituationPatch
from ...helpers.fetch_data import fetch_parameter_data

router = SQLAlchemyCRUDRouter(
    schema=HousingSituationSchema,
    create_schema=HousingSituationCreate,
    db_model=HousingSituation,
    db=get_database,
    prefix="housing-situation"
)


@router.get("")
def overloaded_get_all(
        req: Request,
        skip: int = 0,
        limit: int = 20,
        employee_id: Optional[int] = None,
        db: Session = Depends(get_database)):
    filters = []
    if employee_id:
        filters.append(HousingSituation.employee_id == employee_id)
    filters.append(HousingSituation.state != "DELETED")
    result = []
    list = db.query(HousingSituation).filter(
        *filters).offset(skip).limit(limit).all()
    for item in list:
        type_home = fetch_parameter_data(req.token,
                                         item.type_home_id,
                                         "types-home")
        property_home = fetch_parameter_data(req.token,
                                             item.property_home_id,
                                             "property-home")
        type_subsidy = fetch_parameter_data(req.token,
                                            item.type_subsidy_id,
                                            "types-subsidy")
        result.append({**item.__dict__,
                       "type_home": type_home,
                       "property_home": property_home,
                       "type_subsidy": type_subsidy})
    
    db.close()
    return result


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
    db.close()

    return found_obj
