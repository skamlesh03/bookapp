"""
module to create database session
"""
from sqlalchemy.orm import Session
from typing import List, Optional
from schema import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from models import Base

# Database URL
#DATABASE_URL = "postgresql://postgres:admin@host.docker.internal:5433/gutendex_utf" ### url to run docker image locally
#DATABASE_URL = "postgresql://postgres:admin@localhost/gutendex_utf" ###  url to test in local without docker
DATABASE_URL = "postgresql://postgres:admin@postgres-service:5432/gutendex_utf" ###  url for kubernetes

# Create the database engine and sessionmaker
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Initialize the database
Base.metadata.create_all(bind=engine)

def get_db():
    """
    method to return db session
    """
    db = SessionLocal()  # Create a session instance from the sessionmaker
    try:
        yield db  # Yield the session
    finally:
        db.close()  # Close the session