# Command-Line-Interface-Chatbot

-A simple command-line chatbot built with Python that connects to a locally running Ollama server and allows users to interact with an AI model directly through the terminal.
<br>
-Features
Interactive command-line chat
Uses a locally hosted Ollama model
Configurable Ollama URL and model using environment variables
Handles API errors and connection issues
Exit using exit, quit, or Ctrl+C
<br>
-Technologies Used
Python
Ollama
Requests
Qwen 2.5 3B
<br>
How It Works
The application takes input from the user through the terminal and sends the prompt to the Ollama API. Ollama processes the prompt using the selected language model and returns the generated response, which is displayed in the terminal.
<br>
-Setup
1. Install Dependencies
pip install requests <br>
2. Install and Run Ollama
Make sure Ollama is installed and running on your system. <br>
Pull the required model:
ollama pull qwen2.5:3b <br>
3. Run the Application 
python main.py <br>
Environment Variable
The application uses the following default settings:
OLLAMA_URL=http://ollama:11434
MODEL=qwen2.5:3b
<br>
<br>
Project Purpose:
This project demonstrates how Python can communicate with a locally hosted Large Language Model (LLM) through an API and provide a simple terminal-based chatbot interface.
