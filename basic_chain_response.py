import streamlit as st
import requests
import os

# Streamlit app title
st.title("AI Chat Bot")

# Securely set the Groq API key
api_key = st.secrets["GROQ_API_KEY"]

# Define the endpoint for Groq's chat completion API
endpoint = "https://api.groq.com/openai/v1/chat/completions"

# Define the enhanced prompt template
template = """
You are a knowledgeable and helpful AI assistant. Your goal is to provide clear, concise, and accurate answers to the questions asked by the user. Please answer the following question to the best of your ability.

Question: {question}
Answer:
"""

# User query input
query = st.text_input("Enter your query here")

# Generate and display response if a query is provided
if query:
    # Create the request payload for Groq API
    payload = {
        "model": "mixtral-8x7b-32768",  # Replace with the desired model
        "messages": [
            {"role": "user", "content": query}
        ],
        "max_tokens": 150,  # Adjust as needed
        "temperature": 0.9  # Adjust as needed
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
        # Extract and display the response
        answer = completion["choices"][0]["message"]["content"]
        st.markdown(f"**Response:** {answer}")
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
