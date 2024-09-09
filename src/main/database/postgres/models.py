from sqlalchemy import Column, Integer, String
from .database_connection import BaseModel

class Person(BaseModel):
    __tablename__ = 'persons'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    address = Column(String)
    work = Column(String)
    age = Column(Integer)