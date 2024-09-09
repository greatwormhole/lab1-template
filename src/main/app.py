from fastapi import FastAPI

from database.postgres.database_connection import BaseModel, engine
from routers.persons import router as person_router

BaseModel.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(person_router)