from pydantic import BaseModel


class RSHCreate(BaseModel):
    description: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "description": ""
            }
        }


class RSH (RSHCreate):
    id: int
