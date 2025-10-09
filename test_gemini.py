import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()  # loads GOOGLE_API_KEY from .env

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("❌ No GOOGLE_API_KEY found in environment.")
    exit()

genai.configure(api_key=api_key)

# Check available models
print("✅ API key loaded successfully!")
print("Listing available models:\n")

for model in genai.list_models():
    if "generateContent" in model.supported_generation_methods:
        print("✔", model.name)
