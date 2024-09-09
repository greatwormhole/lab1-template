from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.postgres.database_connection import get_db
from database.postgres.models import Person

router = APIRouter(
    prefix='/api/v1/persons',
    tags=['Persons'],
)

@router.get(
    path='/',
)
async def get_persons(db: Session = Depends(get_db)):
    return db.query(Person).all()

@router.get(
    path='/{person_id}',
)
async def get_person(person_id: str, db: Session = Depends(get_db)):
    return

@router.post(
    path='/',
)
async def create_person(db: Session = Depends(get_db)):
    return

@router.patch(
    path='/{person_id}'
)
async def change_person(person_id: str, db: Session = Depends(get_db)):
    return

@router.delete(
    path='/{person_id}'
)
async def delete_person(person_id: str, db: Session = Depends(get_db)):
    return