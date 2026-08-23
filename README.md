# Command-Line-Interface-Chatbot

-A simple command-line chatbot built with Python that connects to a locally running Ollama server and allows users to interact with an AI model directly through the terminal.
<br> <br>
-Features <br>
Interactive command-line chat <br>
Uses a locally hosted Ollama model <br>
Configurable Ollama URL and model using environment variables <br>
Handles API errors and connection issues <br> 
Exit using exit, quit, or Ctrl+C <br> <br>
--Technologies Used <br>
Python <br>
Ollama <br>
Requests <br>
Qwen 2.5 3B <br>
How It Works <br>
The application takes input from the user through the terminal and sends the prompt to the Ollama API. Ollama processes the prompt using the selected language model and returns the generated response, which is displayed in the terminal. <br> <br>
--Setup <br>
1. Install Dependencies <br>
pip install requests <br>
2. Install and Run Ollama <br>
Make sure Ollama is installed and running on your system. <br>
Pull the required model: <br>
ollama pull qwen2.5:3b <br>
3. Run the Application <br>
python main.py <br>
Environment Variable <br>
The application uses the following default settings: <br>
OLLAMA_URL=http://ollama:11434,
MODEL=qwen2.5:3b
<br> <br>
Project Purpose: <br>
This project demonstrates how Python can communicate with a locally hosted Large Language Model (LLM) through an API and provide a simple terminal-based chatbot interface.
