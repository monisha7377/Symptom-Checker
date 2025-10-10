# database.py

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load environment variables from .env file for local development
load_dotenv()

# Use the deployed DATABASE_URL from Render if it exists.
# If not, fall back to a local SQLite database file.
SQLALCHEMY_DATABASE_URL = os.getenv("postgresql://symptom_checker_db_user:DNxYBDggtTLCARPSYPVfP8NSsFNufGbB@dpg-d3ka4gd6ubrc73dq63g0-a/symptom_checker_db", "sqlite:///./symptom_checker.db")

# Create the SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a SessionLocal class, which will be our actual database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class. Our ORM models will inherit from this class.
Base = declarative_base()