from pydantic import BaseModel


class TypeSubsidyCreate(BaseModel):
    description: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "description": ""
            }
        }


class TypeSubsidy (TypeSubsidyCreate):
    id: int
