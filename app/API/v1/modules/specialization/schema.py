from datetime import datetime
from typing import Optional
from pydantic import BaseModel

"""
employee_id = Column(Integer,
                         ForeignKey('employee.id'), nullable=False)
    specialty_id = Column(Integer,
                          ForeignKey('specialty.id'), nullable=False)
    specialty_detail_id = Column(Integer,
                                 ForeignKey('sub_specialty.id'), nullable=False)
    is_self_taught = Column(String(2), nullable=False)
    certifying_entity_id = Column(Integer,
                                  ForeignKey('entity.id'))
    is_certificated = Column(String(2))
    certification_url = Column(String(255))
    certificated_date = Column(DateTime)"""


class SpecializationCreate(BaseModel):
    employee_id: int
    specialty_id: int
    specialty_detail_id: int
    is_self_taught: str
    certifying_entity_id: Optional[int]
    is_certificated: str
    certification_url: Optional[str] = ''
    certificated_date: datetime
    state: Optional[str]

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
