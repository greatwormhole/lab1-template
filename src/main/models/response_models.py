from pydantic import BaseModel

class PersonResponse(BaseModel):
    id: int
    name: str
    address: str
    work: str
    age: int
    
    class Config:
        orm_mode: True