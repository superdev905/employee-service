from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from ..attachment.schema import AttachmentCreate


class SpecializationCreate(BaseModel):
    employee_id: int
    specialty_id: int
    specialty_detail_id: int
    is_self_taught: str
    certifying_entity_id: Optional[int] = None
    is_certificated: str
    certificated_date: Optional[datetime] = None
    state: Optional[str]
    created_by: int
    certification_file: Optional[AttachmentCreate]

    class Config:
        orm_mode = True


class SpecializationPatch(BaseModel):
    state: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "state": "DELETED",
            }
        }


class Specialization (SpecializationCreate):
    id: int
