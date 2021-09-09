from typing import Optional
from fastapi.encoders import jsonable_encoder
from fastapi.param_functions import Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import joinedload
from sqlalchemy.orm.session import Session
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from .model import Specialization
from .schema import Specialization as SpecializationSchema, SpecializationCreate, SpecializationPatch
from ...helpers.fetch_data import fetch_parameter_data

router = SQLAlchemyCRUDRouter(
    schema=SpecializationSchema,
    create_schema=SpecializationCreate,
    db_model=Specialization,
    db=get_database,
    prefix="specialization"
)


@router.get("")
def overloaded_get_all(skip: int = 0,
                       limit: int = 20,
                       employee_id: Optional[int] = None,
                       db: Session = Depends(get_database)):
    filters = []
    if employee_id:
        filters.append(Specialization.employee_id == employee_id)
    filters.append(Specialization.state == "CREATED")
    result = []
    query_list = db.query(Specialization).filter(
        *filters).offset(skip).limit(limit).all()
    for item in query_list:
        entity = fetch_parameter_data(
            item.certifying_entity_id, "entities") if item.certifying_entity_id else None
        result.append({**item.__dict__,
                       "specialty": fetch_parameter_data(item.specialty_id, "specialties"),
                       "specialty_detail": fetch_parameter_data(item.specialty_detail_id, "sub-specialties"),
                       "certifying_entity": entity})

    return result


@router.put('/{item_id}')
def update_one(item_id: int, update_body: SpecializationCreate, db: Session = Depends(get_database)):
    found_obj = db.query(Specialization).filter(
        Specialization.id == item_id).first()
    if not found_obj:
        raise HTTPException(
            status_code=400, detail="Este registro no existe")

    obj_data = jsonable_encoder(found_obj)

    if isinstance(update_body, dict):
        update_data = update_body
    else:
        update_data = update_body.dict(exclude_unset=True)
    for field in obj_data:
        if field in update_data:
            setattr(found_obj, field, update_data[field])
    db.add(found_obj)
    db.commit()
    db.refresh(found_obj)

    return found_obj


@router.patch('/{item_id}')
def block_one(item_id: int, patch_body: SpecializationPatch, db: Session = Depends(get_database)):
    found_obj = db.query(Specialization).filter(
        Specialization.id == item_id).first()
    if not found_obj:
        raise HTTPException(
            status_code=400, detail="Este registro no existe")
    found_obj.state = patch_body.state
    db.add(found_obj)
    db.commit()
    db.refresh(found_obj)

    return found_obj
