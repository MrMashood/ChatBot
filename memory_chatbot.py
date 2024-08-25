import streamlit as st
import requests
import os

# Set up Groq API key securely
api_key = st.secrets["GROQ_API_KEY"]  # Ensure you have your API key in Streamlit secrets
os.environ["GROQ_API_KEY"] = api_key

# Define the endpoint for Groq's chat completion API
endpoint = "https://api.groq.com/openai/v1/chat/completions"

# Initialize message history (a persistent list to store messages)
if 'msgs' not in st.session_state:
    st.session_state.msgs = []
    # Initial message from the AI if no previous messages exist
    initial_message = "Hello! I'm here to assist you with any questions or tasks. How can I help you today?"
    st.session_state.msgs.append({"role": "assistant", "content": initial_message})

# Refined Prompt Template for Concise Responses
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
    """Formats the chat history for the template."""
    return "\n".join([f"{msg['role'].capitalize()}: {msg['content']}" for msg in messages])

# Display chat history
for msg in st.session_state.msgs:
    st.chat_message(msg["role"]).write(msg["content"])

# Handle new user input
if user_input := st.chat_input():
    # Append the user's input to the messages
    st.session_state.msgs.append({"role": "user", "content": user_input})
    
    # Format the chat history for the prompt
    chat_history = format_chat_history(st.session_state.msgs)
    formatted_prompt = template.format(chat_history=chat_history, human_input=user_input)
    
    # Create the request payload for Groq API
    payload = {
        "model": "mixtral-8x7b-32768",  # Replace with the desired model
        "messages": [{"role": "user", "content": formatted_prompt}],
        "max_tokens": 100,  # Adjust as needed for brevity
        "temperature": 0.6  # Lower temperature for more focused responses
    }

    # Set headers with API key
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # Make the API call to Groq for chat completion
    response = requests.post(endpoint, json=payload, headers=headers)

    # Check for successful response
    if response.status_code == 200:
        completion = response.json()
        answer = completion["choices"][0]["message"]["content"]
        
        # Append the assistant's response to the messages
        st.session_state.msgs.append({"role": "assistant", "content": answer})
        
        # Display the assistant's response
        st.chat_message("assistant").write(answer)
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
