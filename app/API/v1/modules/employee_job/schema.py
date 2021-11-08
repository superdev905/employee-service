

from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class EmployeeJobBase(BaseModel):
    employee_id: int
    admission_date: datetime
    business_id: int
    business_name: Optional[str]
    construction_id: int
    construction_name: Optional[str]
    contract_term: str
    contract_type: str
    leave_date: Optional[datetime] = None
    leave_motive: Optional[str] = None
    salary: float
    state: Optional[str]
    specialty_id: int
    specialty_name: Optional[str]
    specialty_detail_id: int
    specialty_detail_name: Optional[str]
    created_by: int

    class Config:
        orm_mode = True
        default_by_required = False


class EmployeeJobCreate(EmployeeJobBase):
    pass


class EmployeeJobItem(EmployeeJobBase):
    id: int

    class Config:
        allow_population_by_field_name = True


class EmployeeJobPatch(BaseModel):
    state: str

    class Config:
        orm_mode = True


class EmployeeJob (EmployeeJobBase):
    id: int
