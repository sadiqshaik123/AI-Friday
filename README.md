
# RAG Chatbot with OpenRouter

## Install

pip install -r requirements.txt

## Configure

1. Put your details in my_details.txt
2. Run:

python chatbot_rag.py

3. Enter your OpenRouter API key when prompted.

## Architecture

my_details.txt
    ↓
Chunking
    ↓
Embeddings (MiniLM)
    ↓
FAISS Vector Database
    ↓
Similarity Search
    ↓
DeepSeek R1 (OpenRouter)
    ↓
Answer
