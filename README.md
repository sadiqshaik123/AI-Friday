# PDF Question Answering with LangChain, ChromaDB, and OpenRouter

## Overview

This application allows users to upload a PDF document, extract its content, create embeddings, store them in a Chroma vector database, and generate summaries using a Large Language Model (LLM).

The application is built using:

* Streamlit
* LangChain
* ChromaDB
* OpenRouter LLM
* Google Embeddings
* PDFMiner

---

## Features

* Upload PDF documents
* Extract text from PDFs
* Split text into chunks
* Generate embeddings
* Store embeddings in ChromaDB
* Retrieve relevant document chunks
* Generate document summaries using an LLM

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
* Google Embedding API Key

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

Install all required packages:

```bash
pip install streamlit
pip install pdfminer.six
pip install langchain
pip install langchain-openai
pip install langchain-community
pip install langchain-classic
pip install langchain-text-splitters
pip install chromadb
pip install httpx
pip install tiktoken
```

Or install everything at once:

```bash
pip install streamlit pdfminer.six langchain langchain-openai langchain-community langchain-classic langchain-text-splitters chromadb httpx tiktoken
```

---

## requirements.txt

```text
streamlit
pdfminer.six
langchain
langchain-openai
langchain-community
langchain-classic
langchain-text-splitters
chromadb
httpx
tiktoken
```

---

## Configure API Keys

Replace the API keys in `app.py` with your own credentials.

Example:

```python
api_key="YOUR_OPENROUTER_API_KEY"
```

```python
api_key="YOUR_EMBEDDING_API_KEY"
```

For production applications, store keys in environment variables instead of hardcoding them.

Example:

```python
import os

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
EMBEDDING_API_KEY = os.getenv("EMBEDDING_API_KEY")
```

---

## Running the Application

Do NOT run Streamlit applications using:

```bash
python app.py
```

Instead run:

```bash
streamlit run app.py
```

or

```bash
python -m streamlit run app.py
```

---

## Access the Application

After starting Streamlit, open:

```text
http://localhost:8501
```

in your browser.

---

## How to Use

1. Launch the application.
2. Upload a PDF file.
3. Wait for text extraction and vector store creation.
4. The application will generate a summary of the uploaded document.
5. Review the generated summary.

---

## Common Issues

### ModuleNotFoundError

Install missing dependencies:

```bash
pip install <package-name>
```

### No Space Left on Device

Clean pip cache:

```bash
pip cache purge
```

Delete temporary files:

```text
C:\Users\<username>\AppData\Local\Temp
```

---

## Technologies Used

* Streamlit
* LangChain
* ChromaDB
* OpenRouter
* PDFMiner
* HTTPX

---

## Author

Developed as a PDF Question Answering and Summarization application using Retrieval-Augmented Generation (RAG) concepts.
