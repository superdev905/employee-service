from pydantic import BaseModel


class ScholarshipCreate(BaseModel):
    description: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "description": ""
            }
        }


class Scholarship (ScholarshipCreate):
    id: int
