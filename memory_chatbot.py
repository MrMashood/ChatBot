import streamlit as st
import requests
import os

api_key = st.secrets["GROQ_API_KEY"]
os.environ["GROQ_API_KEY"] = api_key

endpoint = "https://api.groq.com/openai/v1/chat/completions"

# Initialize message history if not already present
if 'msgs' not in st.session_state:
    st.session_state.msgs = []
    # Initial message from AI
    initial_message = "Hello! I'm here to assist you with any questions or tasks. How can I help you today?"
    st.session_state.msgs.append({"role": "assistant", "content": initial_message})

# Template for AI responses
template = """
You are a knowledgeable AI assistant having a friendly conversation with a human. 
Your goal is to provide clear, concise, and informative answers. 
Keep responses brief but meaningful, avoiding unnecessary details while ensuring the user feels engaged and informed. 
If the user needs more information, encourage them to ask follow-up questions.

{chat_history}
Human: {human_input}
AI: 
"""

def format_chat_history(messages):
    """Formats chat history for the prompt."""
    return "\n".join([f"{msg['role'].capitalize()}: {msg['content']}" for msg in messages])

for msg in st.session_state.msgs:
    st.chat_message(msg["role"]).write(msg["content"])

if user_input := st.chat_input():
    st.session_state.msgs.append({"role": "user", "content": user_input})
    
    chat_history = format_chat_history(st.session_state.msgs)
    formatted_prompt = template.format(chat_history=chat_history, human_input=user_input)
    
    payload = {
        "model": "mixtral-8x7b-32768",  # Specify desired model
        "messages": [{"role": "user", "content": formatted_prompt}],
        "max_tokens": 100,  # Limit response length
        "temperature": 0.6  # Focus responses with lower temperature
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    response = requests.post(endpoint, json=payload, headers=headers)

    if response.status_code == 200:
        completion = response.json()
        answer = completion["choices"][0]["message"]["content"]
        
        st.session_state.msgs.append({"role": "assistant", "content": answer})
        
        st.chat_message("assistant").write(answer)
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
