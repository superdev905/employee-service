from typing import Optional
from pydantic import BaseModel


class PensionSituationCreate(BaseModel):
    employee_id: int
    isapre_fonasa_id: int
    afp_isp_id: int
    is_pensioner: str
    pension_amount: Optional[float]   
    belongs_to_recognize: str
    is_main: Optional[bool]
    state: Optional[str]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "employee_id": 1,
                "isapre_fonasa_id": 1,
                "afp_isp_id": 1,
                "is_pensioner": "NO",
                "belongs_to_recognize" : "NO",
                "pension_amount": 10000,
            }
        }


class PensionSituationPatch(BaseModel):
    state: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "state": "DELETED",
            }
        }


class PensionSituation (PensionSituationCreate):
    id: int
