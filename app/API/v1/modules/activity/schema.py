from pydantic import BaseModel


class ActivityCreate(BaseModel):
    description: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "description": ""
            }
        }


class Activity (ActivityCreate):
    id: int
