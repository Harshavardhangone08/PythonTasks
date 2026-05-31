# ============================================================
# Gen AI App - System Prompt Bot for Library Management System
# ============================================================

# ============================================================
# Install Packages:
# pip install google-genai python-dotenv
# ============================================================

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv
import os 
from database import SessionLocal, Book, User, IssuedBook

# =====================================================================
# Load Environment Variables
# =====================================================================
load_dotenv()

# =====================================================================
# Gemini client
# =====================================================================

client=genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
model="gemini-3-flash-preview"

#FastAPI App
app=FastAPI()

#=====================================================================
# CORS
#=====================================================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Request Schema
class AIRequest(BaseModel):
    question:str

# =====================================================================
# System Prompt
# =====================================================================
System_Prompt="""
You are an AI Library Management Assistant.

You can answer questions related to:

- Books
- Authors
- Genres
- Availability
- Users
- Issued Books
- Due Dates
- Fine Information
- Library Statistics

Rules:

1. Use only the supplied database information.
2. Do not invent books or users.
3. Keep responses concise and professional.
4. If data is unavailable, clearly state it.
5. If the question is unrelated, respond:

⚠️ I can only answer library-related questions.
"""
# =====================================================================
# Home page
# =====================================================================
@app.get("/")
def home():
    
    return {"message": "AI Library Assistant"}

# =====================================================================
# AI chat
# =====================================================================
@app.post("/ai-assistant")
def ai_assistant(request:AIRequest):
    
    db= SessionLocal()
    try:
        question = request.question
        
        #Fetch library data
        books = db.query(Book).all()
        users = db.query(User).all()
        issued_books = db.query(IssuedBook).all()
        
        #Build Context
        books_context = "\n".join([
                f"""Title: {book.title}
                    Author: {book.author}
                    Genre: {book.genre}
                    Price: {book.price}
                    Available Quantity: {book.available_quantity}
                """
                for book in books
            ])
        
        user_context="\n".join([
                f"""
                    Name: {user.name}
                    Email: {user.email}
                """
                for user in users
            ])
        
        issue_context="\n".join([
                f"""
                    Status: {issue.status}
                    Fine Amount: {issue.fine_amount}
                """
                for issue in issued_books
            ])
        prompt= f""" {System_Prompt}
        ======================
        Book Data
        =======================
        {books_context}
        
        ======================
        USER DATA
        ======================
        {user_context}
        
        ======================
        Issued Book Data
        ======================
        {issue_context}
        
        ======================
        Question
        ======================
        {question}
        """
        
        #------------------------------------------------
        # Calling Gemini AI
        #------------------------------------------------
        response = client.models.generate_content(
            model=model,
            contents=prompt
        )
        
        return {
            "question": question,
            "answer": response.text
        }
        
    except Exception as e:

        error_message = str(e)

        if "429" in error_message:

            return {
                "error":
                "⚠️ Gemini API quota exceeded. Please wait for quota reset or use another API key."
                }

        return {
            "error": error_message
            }
    
    finally: 
        db.close()
        
if __name__=="__main__":
    import uvicorn
    
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)