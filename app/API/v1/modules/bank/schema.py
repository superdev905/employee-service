from pydantic import BaseModel


class BankCreate(BaseModel):
    description: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "description": ""
            }
        }


class Bank (BankCreate):
    id: int
