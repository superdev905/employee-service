from pydantic import BaseModel


class EntityCreate(BaseModel):
    description: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "description": ""
            }
        }


class Entity (EntityCreate):
    id: int
