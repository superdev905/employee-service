from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from sqlalchemy.orm import relationship
from faker import Faker

fake = Faker()
"""
employee_id = Column(Integer,
                         ForeignKey('employee.id'), nullable=False)
    admission_date = Column(DateTime, nullable=False)
    business_id = Column(Integer, nullable=False)
    construction_id = Column(Integer, nullable=False)
    contract_term = Column(String(50), nullable=False)
    contract_type = Column(String(50), nullable=False)
    leave_date = Column(DateTime)
    leave_motive = Column(String(120))
    salary = Column(Float, nullable=False)"""


class EmployeeJobCreate(BaseModel):
    employee_id: int
    admission_date: datetime
    business_id: int
    construction_id: int
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
