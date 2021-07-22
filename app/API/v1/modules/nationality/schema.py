from pydantic import BaseModel


class NationalityCreate(BaseModel):
    description: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "description": ""
            }
        }


class Nationality (NationalityCreate):
    id: int
