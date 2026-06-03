# Basic Python Chatbot

A simple AI chatbot built using Python and OpenAI-compatible APIs.

## Features

* Uses OpenAI-compatible SDK
* Supports custom Base URL
* Supports OpenRouter free models
* Maintains conversation history
* Beginner-friendly code
* Fully documented

---

## Installation

### 1. Create Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / Mac

```bash
python -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## OpenRouter Configuration

This project is configured to work with OpenRouter.

### Create an OpenRouter Account

Visit:

https://openrouter.ai/

Generate an API key from the dashboard.

### Configuration

Update the following values in `chatbot.py`:

```python
API_KEY = "YOUR_OPENROUTER_API_KEY"

BASE_URL = "https://openrouter.ai/api/v1"

MODEL = "meta-llama/llama-3.3-70b-instruct:free"
```

---

## Available Free Models

### Llama 3.3 70B

```python
MODEL = "meta-llama/llama-3.3-70b-instruct:free"
```

### DeepSeek R1

```python
MODEL = "deepseek/deepseek-r1:free"
```

### Auto-Routed Free Model

```python
MODEL = "openrouter/free"
```

OpenRouter automatically selects an available free model.

---

## Example Configuration

```python
API_KEY = "sk-or-v1-xxxxxxxxxxxxxxxx"

BASE_URL = "https://openrouter.ai/api/v1"

MODEL = "deepseek/deepseek-r1:free"
```

---

## Run the Chatbot

```bash
python chatbot.py
```

Example:

```text
You: Hello

Bot: Hi! How can I help you today?
```

---

## Project Structure

```text
basic-chatbot/
│
├── chatbot.py
├── requirements.txt
└── README.md
```

---

## Notes

* Never commit API keys to GitHub.
* Store secrets in a `.env` file for production projects.
* OpenRouter provides access to multiple models through a single API.
* The code works with any OpenAI-compatible provider by changing the Base URL and Model name.
