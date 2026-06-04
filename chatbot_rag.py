"""
RAG Chatbot using TCS GenAI Lab + FAISS

Features:
- User enters API key at runtime
- Uses TCS DeepSeek model
- Uses TCS Embedding model
- Uses FAISS vector database
- Uses local text knowledge base
"""

import os

# Fix OpenMP conflicts on Windows
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
os.environ["OMP_NUM_THREADS"] = "1"

from getpass import getpass

import httpx

from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS


class RAGChatBot:

    def __init__(self, api_key):

        self.http_client = httpx.Client(
            verify=False,
            timeout=60.0
        )

        # TCS LLM
        self.llm = ChatOpenAI(
            base_url="https://genailab.tcs.in",
            model="azure_ai/genailab-maas-DeepSeek-V3-0324",
            api_key=api_key,
            http_client=self.http_client,
            temperature=0.2
        )

        # TCS Embedding Model
        self.embeddings = OpenAIEmbeddings(
            base_url="https://genailab.tcs.in",
            model="azure/genailab-maas-text-embedding-3-large",
            api_key=api_key,
            http_client=self.http_client,
            check_embedding_ctx_length=False
        )

        self.vector_store = self.load_knowledge_base()

    def load_knowledge_base(self):

        file_path = "my_details.txt"

        if not os.path.exists(file_path):
            raise FileNotFoundError(
                f"Knowledge base file not found: {file_path}"
            )

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:
            text = file.read()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )

        chunks = splitter.split_text(text)

        documents = [
            Document(page_content=chunk)
            for chunk in chunks
        ]

        return FAISS.from_documents(
            documents,
            self.embeddings
        )

    def retrieve_context(self, question):

        docs = self.vector_store.similarity_search(
            question,
            k=3
        )

        return "\n\n".join(
            doc.page_content
            for doc in docs
        )

    def ask(self, question):

        try:

            context = self.retrieve_context(question)

            prompt = f"""
You are a Retrieval-Augmented Generation assistant.

Use ONLY the context below.

CONTEXT:
{context}

QUESTION:
{question}

RULES:
1. Answer only from the context.
2. Do not hallucinate.
3. If information is unavailable reply exactly:

I don't have that information.
"""

            response = self.llm.invoke(prompt)

            return response.content

        except Exception as e:

            return f"Error: {str(e)}"


def main():

    print("=" * 60)
    print("TCS GenAI Lab - RAG Chatbot")
    print("=" * 60)

    api_key = getpass(
        "Enter your GenAI API Key: "
    ).strip()

    if not api_key:
        print("API Key is required.")
        return

    try:

        print("\nLoading knowledge base...")

        chatbot = RAGChatBot(api_key)

        print("Knowledge base loaded successfully.")
        print("=" * 60)

        while True:

            question = input(
                "\nYou: "
            ).strip()

            if not question:
                continue

            if question.lower() in [
                "exit",
                "quit"
            ]:
                print("\nGoodbye!")
                break

            answer = chatbot.ask(question)

            print("\nBot:", answer)

    except Exception as e:

        print("\nStartup Error:")
        print(str(e))


if __name__ == "__main__":
    main()