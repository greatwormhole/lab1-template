from pydantic import BaseModel
from typing import Optional

class PersonCreate(BaseModel):
    name: str
    address: str
    work: str
    age: int
    
    class Config:
        orm_mode: True
        
class PersonPatch(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    work: Optional[str] = None
    age: Optional[int] = None
    
    class Config:
        orm_mode: True