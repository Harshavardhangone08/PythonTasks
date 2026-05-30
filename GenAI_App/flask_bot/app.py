from flask import Flask, request, render_template, jsonify
import os
import requests
from dotenv import load_dotenv

app=Flask(__name__)

load_dotenv()
FASTAPI_URL = os.getenv("FASTAPI_URL")

@app.route("/")
def home():
    return render_template("index.html")
 
@app.route("/generate_response", methods=["POST"])
def generate_response():
    
    data=request.get_json()
    question=data.get("question")
    
    try:
        response=requests.post(
            FASTAPI_URL,
            json={
                "question":question
            }
        )
        
        result=response.json()
        
        return jsonify({
            "response": result.get("answer")
        })
        
    except Exception as e:
        return jsonify({
            "response": str(e)
        })

# ============================================================
# Run Flask App
# ============================================================

if __name__=="__main__":
    app.run(debug=True, port=5000)