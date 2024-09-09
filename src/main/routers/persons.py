from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session

from database.postgres.database_connection import get_db
from database.postgres.models import Person
from models.request_models import PersonCreate, PersonPatch
from models.response_models import PersonResponse
from utils.web import get_object_or_404

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
    person = get_object_or_404(person_id, db, Person)
    return person

@router.post(
    path='/',
    status_code=201,
)
async def create_person(person_data: PersonCreate, response: Response, db: Session = Depends(get_db)):
    created_person = Person(**person_data.model_dump())
    
    db.add(created_person)
    db.commit()
    
    response.headers["Location"] = f"/api/v1/persons/{created_person.id}"
    
    return {}
    
@router.patch(
    path='/{person_id}',
    response_model=PersonResponse,
)
async def change_person(person_id: str, person_update: PersonPatch, db: Session = Depends(get_db)):
    selected_person = get_object_or_404(person_id, db, Person)
    update_data = person_update.model_dump(exclude_unset=True)
    
    for key, value in update_data.items():
        setattr(selected_person, key, value)
        
    db.commit()
    
    return selected_person

@router.delete(
    path='/{person_id}',
    status_code=204,
)
async def delete_person(person_id: str, db: Session = Depends(get_db)):
    selected_person = get_object_or_404(person_id, db, Person)
    db.delete(selected_person)
    db.commit()