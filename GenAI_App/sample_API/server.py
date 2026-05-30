#import neccessary dependencies 
# pip install google-genai

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from google import genai
import os
from dotenv import load_dotenv


#load environment variables from .env file
load_dotenv()

# ------------------------------------------------------------
# 🚀 Create FastAPI App
# ------------------------------------------------------------
app = FastAPI()

app.add_middleware( 
CORSMiddleware, 
allow_origins=["*"], # Change in production 
allow_credentials=True, 
allow_methods=["*"], 
allow_headers=["*"], 
)
# ============================================================
# Gemini Client
# ============================================================

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY"),
)

model = "gemini-3-flash-preview"

class Question(BaseModel):
    question:str

@app.get("/")
def home():
    return {"message": "GenAI application using FastAPI"} 

@app.post("/generate_response")
def ask(data:Question):
    
    response=client.models.generate_content(
        model=model,
        contents=data.question
    )
    
    return {
        "question":data.question,
        "answer":response.text
    }
    
if __name__=="__main__":
    import uvicorn
    
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)