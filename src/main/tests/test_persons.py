import sys
import os
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.postgres.database_connection import BaseModel, get_db
from app import app

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

BaseModel.metadata.create_all(bind=engine)

@pytest.fixture(scope="function")
def db_session():
    connection = engine.connect()
    transaction = connection.begin()
    db = TestingSessionLocal(bind=connection)
    yield db
    db.close()
    transaction.rollback()
    connection.close()

@pytest.fixture(scope="module")
def client():
    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c

def test_get_persons_empty(client):
    response = client.get("/api/v1/persons/")
    assert response.status_code == 200
    assert response.json() == []

def test_create_person(client):
    person_data = {
        "name": "John Doe",
        "address": "123 Main St",
        "work": "Software Engineer",
        "age": 30
    }
    response = client.post("/api/v1/persons/", json=person_data)
    assert response.status_code == 201
    location = response.headers["Location"]
    assert location is not None

def test_get_person(client):
    person_data = {
        "name": "John Doe",
        "address": "123 Main St",
        "work": "Software Engineer",
        "age": 30
    }
    post_response = client.post("/api/v1/persons/", json=person_data)
    person_id = post_response.headers["Location"].split("/")[-1]

    response = client.get(f"/api/v1/persons/{person_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == person_data["name"]
    assert data["address"] == person_data["address"]
    assert data["work"] == person_data["work"]
    assert data["age"] == person_data["age"]

def test_patch_person(client):
    person_data = {
        "name": "John Doe",
        "address": "123 Main St",
        "work": "Software Engineer",
        "age": 30
    }
    post_response = client.post("/api/v1/persons/", json=person_data)
    person_id = post_response.headers["Location"].split("/")[-1]

    updated_data = {"name": "Jane Doe"}
    response = client.patch(f"/api/v1/persons/{person_id}", json=updated_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Jane Doe"

def test_delete_person(client):
    person_data = {
        "name": "John Doe",
        "address": "123 Main St",
        "work": "Software Engineer",
        "age": 30
    }
    post_response = client.post("/api/v1/persons/", json=person_data)
    person_id = post_response.headers["Location"].split("/")[-1]

    response = client.delete(f"/api/v1/persons/{person_id}")
    assert response.status_code == 204

    response = client.get(f"/api/v1/persons/{person_id}")
    assert response.status_code == 404
