from datetime import datetime
from typing import Literal, Optional
from pydantic import BaseModel
from faker import Faker

fake = Faker()


class EmployeeRelativeCreate(BaseModel):
    employee_run: str
    run: str
    names: str
    paternal_surname: str
    maternal_surname: str
    born_date: datetime
    gender: str
    marital_status_id: int
    scholarship_id: int
    nationality_id: int
    relationship_id: int
    legal_charge: str
    job_id: int
    rsh: Optional[str]
    rsh_percentage_id: Optional[int] = None
    rsh_status: Optional[Literal["", "REALIZADO", "EN TRÁMITE", "EN TRAMITE"]]
    state: Optional[str]
    is_main: Optional[bool]
    created_by: int
    phone: Optional[str]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "employee_id": 1,
                "legal_charge": "NO",
                "phone": '999990099'
            }
        }


class EmployeeRelative (EmployeeRelativeCreate):
    id: int
