# ============================================================
# Gen AI App - System Prompt Bot
# ============================================================

# ============================================================
# Install Packages:
# pip install google-genai python-dotenv
# ============================================================
from google import genai
from dotenv import load_dotenv
import os

# ============================================================
# Load Environment Variables
# ============================================================

load_dotenv()

# ============================================================
# Check Question Relevance
# ============================================================

def is_python_related(question: str) -> bool:
    
    prompt=f"""
    
    You are a strict classifier.

    Return ONLY YES or NO.

    Return YES only if the question is clearly related to:
    - Python Programming
    - Java Programming
    - FastAPI
    - Flask
    - AI/ML
    - GenAI

    Return NO for:
    - Greetings
    - Random text
    - Gibberish
    - Unclear inputs
    - Personal conversation
    - Non-technical topics

    Examples:

    Question: What is a Python dictionary?
    Answer: YES

    Question: Explain FastAPI dependency injection
    Answer: YES

    Question: Hi
    Answer: NO

    Question: define C and its use cases or other programming languages
    Answer: NO

    Question:
    {question}

    Answer:
    """
    client=genai.Client(
        api_key=os.getenv("GEMINI_API_KEY"),
    )
    
    try:
        response=client.models.generate_content(
             model="gemini-3-flash-preview",
            contents=prompt,
         )
    except Exception as e:
        print(f"Error:{e}")
        return False
    
    answer=response.text.strip().upper()
    
    return answer == "YES"

# ============================================================
# Generate Response
# ============================================================

def generate(question: str):
    
    # Restrict Non-Technical Questions
    if not is_python_related(question):
        
        print(
            "\n⚠️ I'm currently designed to provide responses only for python platform-related learning queries.\n"
            "Please contact the administration team for further assistance.\n"
            )
        
        return
    
    #Gemini client
    client=genai.Client(
        api_key=os.getenv("GEMINI_API_KEY"),
    )
    
    model="gemini-3-flash-preview"
    
    #Sytem prompt
    system_prompt = """
    You are an AI learning assistant.
    Respond to the user's question with clear, concise, and beginner-friendly explanations if the question is related to Python, programming, development, APIs, AI/ML, or technical concepts.

    Rules:
    - Respond only to valid learning/platform-related queries.
    - Be clear and beginner friendly.
    - If a question is unrelated, politely deny it.
    - Keep responses clean and structured.
    """
    
    full_prompt = f"""
    {system_prompt}
    
    user question:
    {question}
    """
    
    # Streaming Response
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=full_prompt,
    ):
        if chunk.text:
            print(chunk.text, end="")
    
# ============================================================
# Main
# ============================================================

if __name__=="__main__":
    while True:
        question=input("\nEnter your question(or type 'exit' to quit): ")
        
        if question.lower() == "exit":
            print("\n Goodbye..!")
            break
    
        generate(question)
