import streamlit as st
import requests
import os

# Retrieve API key from Streamlit secrets and set it as an environment variable
api_key = st.secrets["GROQ_API_KEY"]
os.environ["GROQ_API_KEY"] = api_key

# Define the API endpoint
endpoint = "https://api.groq.com/openai/v1/chat/completions"

# Initialize message history if not already present in session state
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

# Display the chat history
for msg in st.session_state.msgs:
    st.chat_message(msg["role"]).write(msg["content"])

# Handle user input and AI response
if user_input := st.chat_input():
    # Immediately display the user's input in the chat
    st.session_state.msgs.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    # Prepare the formatted prompt for the AI
    chat_history = format_chat_history(st.session_state.msgs)
    formatted_prompt = template.format(chat_history=chat_history, human_input=user_input)
    
    payload = {
        "model": "mixtral-8x7b-32768",  # Specify the desired model
        "messages": [{"role": "user", "content": formatted_prompt}],
        "max_tokens": 100,  # Limit response length
        "temperature": 0.6  # Focus responses with lower temperature
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # Send the request to the API
    response = requests.post(endpoint, json=payload, headers=headers)

    if response.status_code == 200:
        completion = response.json()
        answer = completion["choices"][0]["message"]["content"]
        
        # Display the AI's response in the chat
        st.session_state.msgs.append({"role": "assistant", "content": answer})
        st.chat_message("assistant").write(answer)
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
