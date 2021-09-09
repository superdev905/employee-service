from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from faker import Faker

fake = Faker()


class EmployeeContactCreate(BaseModel):
    address: str
    number: str
    latitude: float
    longitude: float
    region_id: int
    commune_id: int
    housing_group: Optional[str]
    block: Optional[str]
    department: Optional[str]
    mobile_phone: Optional[str]
    landline_phone: Optional[str]
    other_phone: Optional[str]
    email: str
    is_confirmed: Optional[bool]
    employee_run: str
    state: Optional[str]
    is_main: bool
    confirmation_date: datetime
    created_by: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "address": fake.street_address(),
                "number": fake.building_number(),
                "longitude": fake.longitude(),
                "latitude": fake.latitude(),
                "region_id": 1,
                "commune_id": 1,
                "housing_group": "Condominio",
                "block": "Block ejemplo",
                "department": "Departamento",
                "mobile_phone": "",
                "landline_phone": "",
                "other_phone": "",
                "email": fake.ascii_company_email(),
                "is_confirmed": False,
                "employee_id": 1,
                "is_main": True
            }
        }


class EmployeeContactPatch(BaseModel):
    state: Optional[str]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "state": "DELETED",
            }
        }


class EmployeeContact (EmployeeContactCreate):
    id: int
