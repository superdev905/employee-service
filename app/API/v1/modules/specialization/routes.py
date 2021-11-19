from typing import Optional
from fastapi import Request
from fastapi.encoders import jsonable_encoder
from fastapi.param_functions import Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from .model import Specialization
from .schema import Specialization as SpecializationSchema, SpecializationCreate, SpecializationPatch
from ...helpers.fetch_data import fetch_parameter_data
from ...helpers.crud import get_updated_obj
from ..attachment.services import delete_attachment, disable_attachment, save_attachment


router = SQLAlchemyCRUDRouter(
    schema=SpecializationSchema,
    create_schema=SpecializationCreate,
    db_model=Specialization,
    db=get_database,
    prefix="specialization"
)


@router.get("")
def overloaded_get_all(req: Request,
                       skip: int = 0,
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
        entity = fetch_parameter_data(req.token,
                                      item.certifying_entity_id, "entities") if item.certifying_entity_id else None
        result.append({**item.__dict__,
                       "specialty": fetch_parameter_data(req.token, item.specialty_id, "specialties"),
                       "specialty_detail": fetch_parameter_data(req.token, item.specialty_detail_id, "sub-specialties"),
                       "certifying_entity": entity})

    return result


@router.post('')
def create(body: SpecializationCreate, db: Session = Depends(get_database)):

    obj_data = jsonable_encoder(body)
    if body.certification_file:
        file = save_attachment(db, body.certification_file, body.created_by)
        obj_data["certification_file_id"] = file.id

    del obj_data["certification_file"]

    saved_data = Specialization(**obj_data)

    db.add(saved_data)
    db.commit()
    db.refresh(saved_data)

    return saved_data


@router.put('/{item_id}')
async def update_one(req: Request,
                     item_id: int,
                     body: SpecializationCreate,
                     db: Session = Depends(get_database)):

    found_obj = db.query(Specialization).filter(
        Specialization.id == item_id).first()
    if not found_obj:
        raise HTTPException(
            status_code=400, detail="Este registro no existe")

    updated_body = jsonable_encoder(body)
    old_attachment = None
    new_attachment = None

    if body.certification_file:
        if found_obj.certification_file:
            if found_obj.certification_file.file_key != body.certification_file.file_key:
                old_attachment = found_obj.certification_file
                disable_attachment(db, found_obj.certification_file_id)
                new_attachment = save_attachment(
                    db, body.certification_file, body.created_by)
        else:
            new_attachment = save_attachment(
                db, body.certification_file, body.created_by)
    del updated_body["certification_file"]

    updated_spec = get_updated_obj(found_obj, updated_body)
    if new_attachment:
        updated_spec.certification_file_id = new_attachment.id
    db.add(updated_spec)
    db.commit()
    db.refresh(updated_spec)

    if old_attachment:
        delete_attachment(req.token, old_attachment)

    return updated_spec


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
