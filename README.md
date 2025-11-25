# AI Assistant Toolkit

An interactive AI assistant built with **LangChain** and **OpenAI's Chat API**. This assistant can perform basic arithmetic calculations, greet users, and respond dynamically to user input.

## Features

- **Calculator Tool**: Perform addition, subtraction, multiplication, and division.
- **Greeting Tool**: Get personalized greetings.
- **Streamed Responses**: See AI responses in real-time.
- **Interactive Console**: Chat directly in the terminal.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai-assistant-toolkit.git
cd ai-assistant-toolkit

Install required packages:
pip install -r requirements.txt
Set up environment variables:

Create a .env file in the root directory.
Add your OpenAI API key:
OPENAI_API_KEY=your_openai_api_key

Usage
Run the assistant:
python main.py
Type any message to interact with the assistant.
Use commands like add, subtract, multiply, divide for calculations.
Type quit to exit.

Example
Welcome! I'm your AI assistant. Type 'quit' to exit.
You can ask me to perform calculations or chat with me.
You: add 5 and 10
Assistant: The result of 5 + 10 is 15.
You: greet Alice
Assistant: Hello, Alice! How can I assist you today?
