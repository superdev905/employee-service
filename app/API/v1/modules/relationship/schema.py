from pydantic import BaseModel


class RelationshipCreate(BaseModel):
    description: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "description": ""
            }
        }


class Relationship (RelationshipCreate):
    id: int
