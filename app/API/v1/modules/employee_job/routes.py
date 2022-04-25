from typing import List, Optional
from fastapi.encoders import jsonable_encoder
from fastapi.param_functions import Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from .model import EmployeeJob
from .schema import EmployeeJob as EmployeeJobSchema, EmployeeJobItem, EmployeeJobCreate, EmployeeJobPatch


router = SQLAlchemyCRUDRouter(
    schema=EmployeeJobSchema,
    create_schema=EmployeeJobCreate,
    db_model=EmployeeJob,
    db=get_database,
    prefix="employee-jobs"
)


@router.get("", response_model=List[EmployeeJobItem])
def overloaded_get_all(skip: int = None,
                       limit: int = None,
                       employee_id: Optional[str] = None,
                       db: Session = Depends(get_database)):
    filters = []
    if employee_id:
        filters.append(EmployeeJob.employee_id == employee_id)
    filters.append(EmployeeJob.state == "CREATED")
    return db.query(EmployeeJob).filter(*filters).offset(skip).limit(limit).order_by(EmployeeJob.admission_date.desc()).all()


@router.put('/{item_id}')
def update_one(item_id: int, update_body: EmployeeJobCreate, db: Session = Depends(get_database)):
    found_job = db.query(EmployeeJob).filter(
        EmployeeJob.id == item_id).first()
    if not found_job:
        raise HTTPException(
            status_code=400, detail="Este trabajo no existe")

    obj_data = jsonable_encoder(found_job)

    if isinstance(update_body, dict):
        update_data = update_body
    else:
        update_data = update_body.dict(exclude_unset=True)
    for field in obj_data:
        if field in update_data:
            setattr(found_job, field, update_data[field])

    db.add(found_job)
    db.commit()
    db.refresh(found_job)
    db.close()

    return found_job


@router.patch('/{item_id}')
def block_one(item_id: int, patch_body: EmployeeJobPatch, db: Session = Depends(get_database)):
    found_job = db.query(EmployeeJob).filter(
        EmployeeJob.id == item_id).first()
    if not found_job:
        raise HTTPException(
            status_code=400, detail="Este trabajo no existe")

    found_job.state = patch_body.state
    db.add(found_job)
    db.commit()
    db.refresh(found_job)
    db.close()

    return found_job
