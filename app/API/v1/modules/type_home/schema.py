from pydantic import BaseModel


class TypeHomeCreate(BaseModel):
    description: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "description": ""
            }
        }


class TypeHome (TypeHomeCreate):
    id: int
