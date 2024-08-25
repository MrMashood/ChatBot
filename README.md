# AI Chat Bot Collection

This repository contains two AI chatbot applications built with Streamlit and powered by Groq's chat completion API. These bots provide accurate and concise responses to user queries, with one supporting basic query handling and the other offering persistent chat history.

## Project Overview

### 1. `basic_chain_response.py`
- **Functionality:** A simple chatbot that responds to user queries with no memory of previous interactions.
- **Model:** `mixtral-8x7b-32768`
- **Features:**
  - Takes user input and generates a response using the Groq API.
  - Displays the response directly in the Streamlit app.

### 2. `memory_chatbot.py`
- **Functionality:** An advanced chatbot that remembers previous interactions, creating a more coherent and personalized conversation.
- **Model:** `mixtral-8x7b-32768`
- **Features:**
  - Maintains a session-based chat history.
  - Formats the conversation to keep responses concise and relevant.
  - Uses a refined prompt template to encourage follow-up questions.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/MrMashood/AI-Chat-Bot-Collection.git
    cd AI-Chat-Bot-Collection
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your API key securely:
    - Create a `.streamlit/secrets.toml` file in the root directory.
    - Add your Groq API key in the following format:
      ```toml
      [secrets]
      GROQ_API_KEY = "your_api_key_here"
      ```

## Usage

- To run `basic_chain_response.py`:
    ```bash
    streamlit run basic_chain_response.py
    ```

- To run `memory_chatbot.py`:
    ```bash
    streamlit run memory_chatbot.py
    ```

- Open your browser and go to `http://localhost:8501`.


## Author

Mashhood Ur Rehman
