from typing import Optional
from fastapi import Request
from fastapi.param_functions import Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from .model import PensionSituation
from .schema import PensionSituation as PensionSituationSchema, PensionSituationCreate, PensionSituationPatch
from ...helpers.fetch_data import fetch_parameter_data

router = SQLAlchemyCRUDRouter(
    schema=PensionSituationSchema,
    create_schema=PensionSituationCreate,
    db_model=PensionSituation,
    db=get_database,
    prefix="pension-situations"
)


@router.get("")
def overloaded_get_all(req: Request,
                       skip: int = None,
                       limit: int = None,
                       employee_id: Optional[int] = None,
                       db: Session = Depends(get_database)):
    filters = []
    if employee_id:
        filters.append(PensionSituation.employee_id == employee_id)
    filters.append(PensionSituation.state != "DELETED")

    result = []
    list = db.query(PensionSituation).filter(
        *filters).offset(skip).limit(limit).all()
    for item in list:
        afp_isp = fetch_parameter_data(req.token,
                                       item.afp_isp_id,
                                       "afp-isp")
        isapre_fonasa = fetch_parameter_data(req.token,
                                             item.isapre_fonasa_id,
                                             "isapre-fonasa")
        result.append({**item.__dict__,
                       "afp_isp": afp_isp,
                       "isapre_fonasa": isapre_fonasa})
    
    db.close()
    return result


@router.patch('/{item_id}')
def block_one(item_id: int, patch_body: PensionSituationPatch, db: Session = Depends(get_database)):
    found_obj = db.query(PensionSituation).filter(
        PensionSituation.id == item_id).first()
    if not found_obj:
        raise HTTPException(
            status_code=400, detail="Este registro no existe")
    found_obj.state = patch_body.state
    db.add(found_obj)
    db.commit()
    db.refresh(found_obj)
    db.close()

    return found_obj
