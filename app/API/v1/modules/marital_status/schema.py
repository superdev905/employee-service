from pydantic import BaseModel


class MaritalStatusCreate(BaseModel):
    description:str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "description": ""
            }
        }


class MaritalStatus (MaritalStatusCreate):
    id: int
