from pydantic import BaseModel


class SubSpecialtyCreate(BaseModel):
    description: str
    parent_specialty_id: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "description": "",
                "parent_specialty_id": 1,
            }
        }


class SubSpecialty (SubSpecialtyCreate):
    id: int
