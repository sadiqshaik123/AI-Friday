import streamlit as st
from pdfminer.high_level import extract_text
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_classic.chains import RetrievalQA

import tempfile
import os
import httpx

client = httpx.Client(verify=False)

llm= ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    model="openrouter/free",
    api_key="",
    http_client=client
)

embedding_model = OpenAIEmbeddings(
    base_url="https://googleapis.com",
    model="gemini-embedding-001",
    api_key="",
    http_client=client
)

st.set_page_config(page_title="PDF Question Answering", layout="wide")

st.title("PDF Question Answering with LangChain and OpenRouter")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_file_path = tmp_file.name

    text = extract_text(tmp_file_path)
    os.remove(tmp_file_path)

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_text(text)

    with st.spinner("Creating vector store..."):
        vectorstore = Chroma.from_texts(chunks, embedding_model)
    retriever = vectorstore.as_retriever()
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    summary_prompt = "Summarize the following text:\n\n{text}"

    with st.spinner("Generating summary..."):
        summary = qa_chain.invoke(summary_prompt.format(text=text))
    st.subheader("Summary")
    st.write(summary)