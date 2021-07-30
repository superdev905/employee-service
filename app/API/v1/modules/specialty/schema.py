from pydantic import BaseModel


class SpecialtyCreate(BaseModel):
    description: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "description": ""
            }
        }


class Specialty (SpecialtyCreate):
    id: int
