
"""
RAG Chatbot using OpenRouter + FAISS + Text File Knowledge Base
"""

from openai import OpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


class RAGChatBot:

    def __init__(self, api_key):
        self.client = OpenAI(
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1"
        )

        self.model = "openrouter/free"
        self.vector_store = self.load_knowledge_base()

    def load_knowledge_base(self):
        with open("my_details.txt", "r", encoding="utf-8") as file:
            text = file.read()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )

        chunks = splitter.split_text(text)
        documents = [Document(page_content=chunk) for chunk in chunks]

        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        return FAISS.from_documents(documents, embeddings)

    def retrieve_context(self, question):
        docs = self.vector_store.similarity_search(question, k=3)
        return "\n\n".join(doc.page_content for doc in docs)

    def ask(self, question):
        context = self.retrieve_context(question)

        prompt = f"""
Answer only using the context below.

Context:
{context}

Question:
{question}

If the answer is unavailable, say:
'I don't have that information.'
"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content


def main():
    api_key = ""

    bot = RAGChatBot(api_key)

    print("\nRAG Chatbot Ready (type exit to quit)\n")

    while True:
        question = input("You: ")

        if question.lower() == "exit":
            break

        answer = bot.ask(question)
        print("\nBot:", answer, "\n")


if __name__ == "__main__":
    main()
