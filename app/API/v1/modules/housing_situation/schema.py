from typing import Optional
from pydantic import BaseModel


class HousingSituationCreate(BaseModel):
    employee_id: int
    type_home_id: int
    property_home_id: int
    type_subsidy_id: str
    description: str
    is_main: Optional[bool]
    state: Optional[str]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "employee_id": 1,
                "type_home_id": 1,
                "property_home_id": 1,
                "type_subsidy_id": 1,
                "description": "Description",
            }
        }


class HousingSituationPatch(BaseModel):
    state: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "state": "DELETED",
            }
        }


class HousingSituation (HousingSituationCreate):
    id: int
