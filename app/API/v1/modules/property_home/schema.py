from pydantic import BaseModel


class PropertyHomeCreate(BaseModel):
    description: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "description": ""
            }
        }


class PropertyHome (PropertyHomeCreate):
    id: int
