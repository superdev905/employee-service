from pydantic import BaseModel


class IsapreFonasaCreate(BaseModel):
    description: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "description": "Fonasa 1"
            }
        }


class IsapreFonasa (IsapreFonasaCreate):
    id: int
