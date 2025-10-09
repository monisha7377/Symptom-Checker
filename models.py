# models.py
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base

class SymptomLog(Base):
    __tablename__ = "symptom_logs"

    id = Column(Integer, primary_key=True, index=True)
    symptoms_query = Column(String, index=True)
    llm_response = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())