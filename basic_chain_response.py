import streamlit as st
import requests
import os

st.title("AI Chat Bot")

api_key = st.secrets["GROQ_API_KEY"]

endpoint = "https://api.groq.com/openai/v1/chat/completions"

template = """
You are a knowledgeable and helpful AI assistant. Your goal is to provide clear, concise, and accurate answers to the questions asked by the user. Please answer the following question to the best of your ability.

Question: {question}
Answer:
"""

query = st.text_input("Enter your query here")

if query:
    # Prepare the payload for the API request
    payload = {
        "model": "mixtral-8x7b-32768",  # Specify the model
        "messages": [
            {"role": "user", "content": query}
        ],
        "max_tokens": 150,  # Length of the response
        "temperature": 0.9  # Randomness of responses
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # Send the request to the Groq API
    response = requests.post(endpoint, json=payload, headers=headers)

    # Check for successful API response
    if response.status_code == 200:
        completion = response.json()
        answer = completion["choices"][0]["message"]["content"]
        st.markdown(f"**Response:** {answer}")
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
