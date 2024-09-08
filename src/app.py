from fastapi import FastAPI
from fastapi import APIRouter

app = FastAPI()
router = APIRouter()

@app.get(
    path='/persons/',
)
async def get_persons():
    return

@app.get(
    path='/persons/{person_id}',
)
async def get_person(person_id: str):
    return

@app.post(
    path='persons',
)
async def create_person():
    return

@app.patch(
    path='/person/{person_id}'
)
async def change_person(person_id: str):
    return

app.delete(
    path='/person/{person_id}'
)
async def delete_person(person_id: str):
    return