from typing import Optional
from fastapi.param_functions import Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import joinedload
from sqlalchemy.orm.session import Session
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from .model import Specialization
from .schema import Specialization as SpecializationSchema, SpecializationCreate, SpecializationPatch


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

    return db.query(Specialization).filter(*filters).options(
        joinedload(Specialization.specialty),
        joinedload(Specialization.specialty_detail),
        joinedload(Specialization.certifying_entity)).offset(skip).limit(limit).all()


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
