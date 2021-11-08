from datetime import datetime
from typing import Literal, Optional
from pydantic import BaseModel
from faker import Faker

fake = Faker()


class EmployeeBase(BaseModel):
    run: str
    names: str
    paternal_surname: str
    maternal_surname: Optional[str]
    born_date: datetime
    gender: str
    marital_status_id: int
    scholarship_id: int
    disability: str
    credential_disability: Optional[str]
    recognize: str
    nationality_id: int
    alive: str
    bank_id: Optional[int]
    account_type: Optional[str]
    account_number: Optional[str]
    state: Optional[str]
    rsh: str
    rsh_percentage: Optional[str]
    created_by: int
    rsh_status: Optional[Literal["", "REALIZADO", "EN TRÁMITE", "EN TRAMITE"]]
    disability_type: Optional[Literal["",
                                      'DISCAPACIDAD FISICA O MOTORA',
                                      'DISCAPACIDAD SENSORIAL',
                                      'DISCAPACIDAD INTELECTUAL',
                                      'DISCAPACIDAD PSÍQUICA'
                                      ]]
    disability_percentage: Optional[str]

    class Config:
        orm_mode = True


class EmployeeCreate(EmployeeBase):
    class Config:
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
                "recognize": "NO",
                "nationality_id": 1,
                "alive": "SI",
                "bank_id": 1,
                "account_type": "CUENTA CORRIENTE",
                "account_number": fake.bban(),
                "rsh": "NO",
                "rsh_percentage": "T",
                "created_by": int
            }
        }


class EmployeeItem(EmployeeBase):
    int: str

    class Config:
        orm_mode = True
        default_by_required = False


class EmployeePatch (BaseModel):
    state: Optional[str]

    class Config:
        orm_mode = True


class EmployeeSchema (EmployeeCreate):
    id: int

    class Config:
        orm_mode = True
