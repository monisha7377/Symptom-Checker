# crud.py
from sqlalchemy.orm import Session
import models

def create_log_entry(db: Session, symptoms: str, response: str):
    db_log = models.SymptomLog(symptoms_query=symptoms, llm_response=response)
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log