from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class EmployeeJobCreate(BaseModel):
    employee_id: int
    admission_date: datetime
    business_id: int
    business_name: Optional[str]
    construction_id: int
    construction_name: Optional[str]
    contract_term: str
    contract_type: str
    leave_date: Optional[datetime]
    leave_motive: Optional[str]
    salary: float
    state: Optional[str]

    class Config:
        orm_mode = True


class EmployeeJobPatch(BaseModel):
    state: str

    class Config:
        orm_mode = True


class EmployeeJob (EmployeeJobCreate):
    id: int
