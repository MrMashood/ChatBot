# AI Chat Bot

This is a simple AI chatbot application built with Streamlit and powered by Groq's chat completion API. The bot provides clear, concise, and accurate answers to user queries.

## Features

- **Streamlit Framework:** Used for building the interactive web app.
- **Groq API:** Integrated with Groq's `mixtral-8x7b-32768` model for generating AI responses.
- **User-Friendly Interface:** Users can input their queries and receive instant responses.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/MrMashood/ChatBot.git
    cd ChatBot
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

4. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Usage

- Open your browser and go to `http://localhost:8501`.
- Enter your query in the input box.
- The AI chatbot will generate and display a response based on your query.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

Mashhood Ur Rehman

[GitHub Profile](https://github.com/MrMashood)
