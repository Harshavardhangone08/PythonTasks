# ============================================================
# 🚀 Streamlit GPT Style Chat UI
# ============================================================

#import necessary libraries
import streamlit as st
import requests
from dotenv import load_dotenv
import os

# ============================================================
# Page Config
# ============================================================
st.set_page_config(
    page_title="Chat with AI",
    page_icon="🤖",
    layout="wide"
)

# ============================================================
# FastAPI Backend URL
# ============================================================

load_dotenv()
FASTAPI_URL=os.getenv("FASTAPI_URL")

# ============================================================
# Session State
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "processing" not in st.session_state:
    st.session_state.processing = False
    

# ============================================================
# Title
# ============================================================

st.markdown(
    '<div class="title">🤖 GenAI Chat</div>',
    unsafe_allow_html=True
)

# ============================================================
# Display Messages
# ============================================================

for chat in st.session_state.messages:
    print(chat)
    if chat["role"] == "user":
        st.markdown(
            f"""
            <div style="display:flex; justify-content:flex-end;">
                <div class="user-msg">
                    👤  {chat['content']}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    else :
        st.markdown(
            f"""
            <div style="display:flex; justify-content:flex-start;">
                <div class="bot-msg">
                    🤖 {chat['content']}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# ============================================================
# Chat Input
# ============================================================

question=st.chat_input(
    "Ask anything...",
    disabled=st.session_state.processing
)

# ============================================================
# Process Question
# ============================================================

if question:
    
    st.session_state.processing = True

    # ========================================================
    # Add User Message
    # ========================================================
    
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })
    
    st.rerun()
    
# ============================================================
# Generate Response
# ============================================================

if st.session_state.processing:
    
    last_message=st.session_state.messages[-1]
    
    if last_message["role"] == "user":
        
        with st.spinner("Thinking ...."):
            try:
                response = requests.post(
                    FASTAPI_URL,
                    json = {
                        "question": last_message["content"]
                    }
                )
                data=response.json()
                
                answer = data.get(
                    "answer",
                    "No response generated."
                )
            except Exception as e:
                answer = str(e)
                
        # ====================================================
        # Add Bot Response
        # ====================================================
        st.session_state.messages.append({
            "role":"assistant",
            "content": answer   
        })
        
        # ====================================================
        # Enable Input
        # ====================================================
        
        st.session_state.processing = False
        
        st.rerun()
        