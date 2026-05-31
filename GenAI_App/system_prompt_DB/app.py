from flask import Flask, render_template, request, jsonify
import requests
from dotenv import load_dotenv
import os

app=Flask(__name__)

load_dotenv()
FAST_API_URL=os.getenv("FAST_API_URL")
# =====================================================================
# Home page
# =====================================================================
@app.route("/")
def home():
    
    return render_template("index.html")

@app.route("/ask-ai", methods=["POST"])
def ask_ai():
    
    question = request.form.get("question")
    response = requests.post(
        FAST_API_URL,
        json={
            "question": question
            }
    )
    print("FASTAPI RESPONSE:", response.json())
          
    return jsonify(response.json())

if __name__=="__main__":
    app.run(debug=True, port=5000)