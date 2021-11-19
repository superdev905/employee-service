from sqlalchemy.orm.session import Session
from fastapi.encoders import jsonable_encoder
from sqlalchemy.sql.elements import and_
from app.settings import SERVICES
from ...helpers.fetch_data import delete_file_from_store
from .model import Attachment


def get_employee_files(db: Session,  id: int):

    return db.query(Attachment).filter(and_(Attachment.data_id == id, Attachment.source_system == "TRABAJADORES", Attachment.is_active == True)).all()


def save_attachment(db: Session, obj: dict, user_id: int):
    obj_attachment = jsonable_encoder(obj, by_alias=False)
    obj_attachment["created_by"] = user_id
    new_attachment = Attachment(**obj_attachment)

    db.add(new_attachment)
    db.commit()
    db.refresh(new_attachment)
    return new_attachment


def delete_attachment(token: str, attachment):
    delete_file_from_store(token, attachment.file_key)


def disable_attachment(db: Session, id: int):
    found_attachment = db.query(Attachment).filter(Attachment.id == id).first()
    found_attachment.is_active = False
    db.add(found_attachment)
    db.commit()
    db.refresh(found_attachment)
