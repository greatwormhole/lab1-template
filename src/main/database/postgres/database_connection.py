from os import environ
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = f"postgresql://{environ['POSTGRES_USER']}:{environ['POSTGRES_PASSWORD']}@postgres:{environ['POSTGRES_PORT']}/{environ['POSTGRES_DB']}"

engine = create_engine(DATABASE_URL)

local_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

BaseModel = declarative_base()

schema_metadata = MetaData()

def get_db():
    db = local_session()
    try:
        yield db
    finally:
        db.close()