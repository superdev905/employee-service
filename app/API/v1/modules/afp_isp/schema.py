from pydantic import BaseModel


class AfpIspCreate(BaseModel):
    description: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "description": "Fonasa 1"
            }
        }


class AfpIsp (AfpIspCreate):
    id: int
