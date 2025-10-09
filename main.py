import os
import logging
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from dotenv import load_dotenv
from sqlalchemy.orm import Session
import google.generativeai as genai
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import crud, models
from database import SessionLocal, engine

# Create all tables
models.Base.metadata.create_all(bind=engine)

# Load environment variables
load_dotenv(dotenv_path="./.env")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Configure Google Gemini API
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise RuntimeError("❌ GOOGLE_API_KEY not found in .env file. Please add it.")
genai.configure(api_key=api_key)

# Initialize FastAPI app
app = FastAPI(
    title="Healthcare Symptom Checker API",
    description="An API that takes user symptoms, returns potential conditions using Gemini, and logs the interaction.",
    version="1.1"
)
app.mount("/static", StaticFiles(directory="static"), name="static")
# Request model
class SymptomCheckRequest(BaseModel):
    symptoms: str

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Prompt template
PROMPT_TEMPLATE = """
You are a helpful medical information assistant. Your role is to provide potential conditions based on symptoms for educational purposes ONLY. You are not a substitute for a real medical professional.

IMPORTANT: Start your entire response with this mandatory disclaimer, exactly as written:
'IMPORTANT DISCLAIMER: This information is for educational purposes only and is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or another qualified health provider with any questions you may have regarding a medical condition.'

Based on the symptoms provided below, suggest 3 to 5 potential conditions.
For each condition:
1. Provide the condition's name.
2. Add a severity tag based on the typical nature of the condition: (Mild), (Moderate), or (Serious).
3. Provide a brief, easy-to-understand explanation (2-3 sentences).

After listing the potential conditions, provide a section called "**Recommended Next Steps**" with general, safe advice like "Consult a healthcare professional" or "Monitor your symptoms". Do not suggest specific treatments or medications.

User's Symptoms: "{user_symptoms}"

"""

# Main endpoint
@app.post("/check-symptoms")
async def check_symptoms(request: SymptomCheckRequest, db: Session = Depends(get_db)):
    if not request.symptoms or len(request.symptoms.strip()) < 10:
        raise HTTPException(status_code=400, detail="Please provide a more detailed description of your symptoms.")

    try:
        full_prompt = PROMPT_TEMPLATE.format(user_symptoms=request.symptoms)
        model = genai.GenerativeModel("gemini-2.5-flash")

        logging.info("Prompt sent to Gemini:")
        logging.info(full_prompt)

        response = model.generate_content(full_prompt)

        # Handle Gemini API response correctly
        if hasattr(response, "text"):
            llm_result = response.text
        elif hasattr(response, "candidates") and response.candidates:
            llm_result = response.candidates[0].content.parts[0].text
        else:
            llm_result = str(response)

        logging.info("Gemini Response:")
        logging.info(llm_result)

        # Save interaction in DB
        crud.create_log_entry(db=db, symptoms=request.symptoms, response=llm_result)

        return {"result": llm_result}

    except Exception as e:
        logging.error(f"Error during model call: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"AI model error: {e}")

# Root endpoint
# THIS IS THE CORRECT CODE
from fastapi.responses import FileResponse # Make sure this import is at the top of your file!

@app.get("/")
async def read_index():
    return FileResponse('static/index.html')
