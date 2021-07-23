from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from faker import Faker

fake = Faker()


class EmployeeCreate(BaseModel):
    run: str
    names: str
    paternal_surname: str
    maternal_surname: str
    born_date: datetime
    gender: str
    marital_status_id: int
    scholarship_id: int
    disability: str
    credential_disability: str
    nationality_id: int
    alive: str
    bank_id: Optional[int]
    account_type: Optional[str]
    account_number: Optional[str]
    rsh: str
    rsh_percentage: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "run": "14.643.954-3",
                "names": fake.name(),
                "paternal_surname": fake.name().split()[1],
                "maternal_surname": fake.name().split()[1],
                "born_date": datetime.now(),
                "gender": "MASCULINO",
                "marital_status_id": 1,
                "scholarship_id": 1,
                "disability": "NO",
                "credential_disability": "NO",
                "nationality_id": 1,
                "alive": "SI",
                "bank_id": 1,
                "account_type": "CUENTA CORRIENTE",
                "account_number": fake.bban(),
                "rsh": "NO",
                "rsh_percentage": "T"
            }
        }


class Employee (EmployeeCreate):
    id: int
