import streamlit as st
import requests
import os

# Set the page layout and title
st.set_page_config(page_title="AI Chat Bot", layout="centered", initial_sidebar_state="expanded")

# Define the API endpoint
endpoint = "https://api.groq.com/openai/v1/chat/completions"

# Add a title and a description
st.title("AI Chat Bot")
st.write("Welcome to the AI Chat Bot. Ask any question, and I'll do my best to provide a clear, concise, and accurate answer.")

# Input for user query
query = st.text_input("Enter your query below:")

# Sidebar for additional settings
st.sidebar.title("Settings")
# API Key is now directly fetched from secrets, no need to show it in the sidebar
api_key = st.secrets["GROQ_API_KEY"]

# Model selection without options (user can enter model name manually if needed)
model = st.sidebar.text_input("Model", value="mixtral-8x7b-32768", help="Enter the model name (default: mixtral-8x7b-32768)")

max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=500, value=150)
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)

# Button to submit the query
if st.button("Submit"):
    if query:
        # Prepare the payload for the API request
        payload = {
            "model": model,  # Specify the model
            "messages": [
                {"role": "user", "content": query}
            ],
            "max_tokens": max_tokens,  # Length of the response
            "temperature": temperature  # Randomness of responses
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
            st.markdown(f"### Response:\n{answer}")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    else:
        st.warning("Please enter a query.")

# Footer
st.markdown("---")
st.write("Developed by Mashhood Ur Rehman")
