# Basic LLM Chatbot using LangChain and OpenRouter

## Overview

This project is a simple command-line chatbot built using LangChain and OpenRouter.

The chatbot accepts user input from the terminal, sends it to a Large Language Model (LLM) through OpenRouter, and displays the AI-generated response.

---

## Features

* Interactive command-line chatbot
* Powered by OpenRouter
* Uses LangChain ChatOpenAI integration
* Continuous conversation loop
* Exit command to stop the application

---

## Project Structure

```text
project/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Prerequisites

* Python 3.10 or higher
* Internet connection
* OpenRouter API Key

---

## Create Virtual Environment

### Windows

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Linux / Mac

```bash
python -m venv .venv
source .venv/bin/activate
```

---

## Install Dependencies

Install the required packages:

```bash
pip install langchain-openai
pip install langchain-core
pip install httpx
```

Or install everything at once:

```bash
pip install langchain-openai langchain-core httpx
```

---

## requirements.txt

```text
langchain-openai
langchain-core
httpx
```

---

## Application Code

```python
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

import httpx

client = httpx.Client(verify=False)

llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    model="openrouter/free",
    api_key="YOUR_OPENROUTER_API_KEY",
    http_client=client
)

while True:
    user_input = input("User: ")

    if user_input.lower() == "exit":
        break

    print("AI:", llm.invoke(user_input).content)
```

---

## Configure API Key

Replace the API key in the code:

```python
api_key="YOUR_OPENROUTER_API_KEY"
```

For production applications, use environment variables instead.

Example:

```python
import os

api_key = os.getenv("OPENROUTER_API_KEY")
```

### Windows

```powershell
set OPENROUTER_API_KEY=your_api_key
```

### Linux / Mac

```bash
export OPENROUTER_API_KEY=your_api_key
```

---

## Running the Application

Run the chatbot using:

```bash
python app.py
```

---

## Sample Execution

```text
User: Hi
AI: Hello! How can I assist you today?

User: What is Artificial Intelligence?
AI: Artificial Intelligence (AI) is a branch of computer science that enables machines to perform tasks that typically require human intelligence.

User: exit
```

---

## How It Works

1. The user enters a question or message.
2. The input is sent to OpenRouter through LangChain.
3. The selected LLM processes the request.
4. The AI response is returned and displayed in the terminal.
5. The process repeats until the user enters `exit`.

---

## Common Issues

### ModuleNotFoundError

Install the missing package:

```bash
pip install <package-name>
```

### SSL Certificate Errors

If SSL verification issues occur, the application uses:

```python
httpx.Client(verify=False)
```

for development purposes.

### Invalid API Key

Verify that your OpenRouter API key is valid and active.

---

## Technologies Used

* Python
* LangChain
* OpenRouter
* HTTPX

---

## Future Enhancements

* Conversation memory
* Chat history persistence
* Streamlit web interface
* Multi-model selection
* RAG (Retrieval-Augmented Generation) support

---

## Author

Developed as a beginner-friendly LangChain chatbot demonstrating OpenRouter integration and conversational AI.
