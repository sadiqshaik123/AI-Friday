# RAG Chatbot – Explanation

## What is RAG?

RAG stands for **Retrieval-Augmented Generation**.

Instead of relying only on the LLM's training data, RAG retrieves relevant information from an external knowledge source and provides it to the LLM before generating a response.

### Traditional LLM

```text
User Question
      ↓
      LLM
      ↓
    Answer
```

### RAG

```text
User Question
      ↓
Retrieve Relevant Data
      ↓
Provide Context
      ↓
      LLM
      ↓
    Answer
```

---

# Where RAG is Used in This Project

## Step 1: Load Knowledge Base

```python
with open("my_details.txt", "r", encoding="utf-8") as file:
    text = file.read()
```

### Purpose

Loads the external knowledge source.

Example:

```text
Name: Shaik Sadiq
Company: TCS
Experience: 2.3 Years
Skills:
Java
Spring Boot
Vert.x
```

This file becomes the knowledge base for the chatbot.

This is the first step of RAG.

---

## Step 2: Split Text into Chunks

```python
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_text(text)
```

### Purpose

Large documents are split into smaller pieces called chunks.

Example:

```text
Chunk 1:
Name: Shaik Sadiq
Company: TCS

Chunk 2:
Skills:
Java
Spring Boot
Vert.x
```

Chunking helps retrieve only relevant information.

This is part of the Retrieval process.

---

## Step 3: Convert Chunks into Documents

```python
documents = [
    Document(page_content=chunk)
    for chunk in chunks
]
```

### Purpose

Converts plain text chunks into LangChain Document objects.

These documents can then be embedded and stored in a vector database.

---

## Step 4: Create Embeddings

```python
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
```

### Purpose

Converts text into vectors (numerical representations).

Example:

```text
"Java Developer"
      ↓

[0.12, -0.45, 0.67, ...]
```

Vectors help the system understand semantic meaning instead of exact keyword matching.

This is a core RAG component.

---

## Step 5: Create Vector Database

```python
FAISS.from_documents(
    documents,
    embeddings
)
```

### Purpose

Stores document vectors inside FAISS.

FAISS allows fast similarity search.

Example:

```text
Question:
"What company does Sadiq work for?"

FAISS finds:

"Company: TCS"
```

This is where Retrieval capability is created.

---

## Step 6: Retrieve Relevant Context

```python
docs = self.vector_store.similarity_search(
    question,
    k=3
)
```

### Purpose

When a user asks a question:

```text
What company does Sadiq work for?
```

FAISS searches the vector database and returns the most relevant chunks.

Example result:

```text
Company: TCS
Experience: 2.3 Years
```

This is the actual Retrieval step of RAG.

---

## Step 7: Build Prompt with Retrieved Context

```python
context = self.retrieve_context(question)
```

```python
prompt = f"""
Answer only using the context below.

Context:
{context}

Question:
{question}
"""
```

### Purpose

Inject retrieved information into the LLM prompt.

Example:

```text
Context:
Company: TCS

Question:
Where does Sadiq work?
```

This is the Augmentation step of RAG.

---

## Step 8: Generate Answer

```python
response = self.client.chat.completions.create(
    model=self.model,
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)
```

### Purpose

The LLM receives:

* User Question
* Retrieved Context

and generates the final answer.

Example:

```text
Question:
Where does Sadiq work?

Retrieved Context:
Company: TCS

Answer:
Sadiq works at TCS.
```

This is the Generation step of RAG.

---

# Complete RAG Flow

```text
my_details.txt
       ↓
Read File
       ↓
Chunking
       ↓
Embeddings
       ↓
FAISS Vector Store
       ↓
User Question
       ↓
Similarity Search
       ↓
Retrieve Top Chunks
       ↓
Build Prompt
       ↓
OpenRouter LLM
       ↓
Final Answer
```

---

# Why This Project is RAG

This project satisfies all three components of RAG:

### Retrieval

```python
similarity_search()
```

Retrieves relevant chunks.

### Augmentation

```python
Context:
{context}
```

Injects retrieved data into the prompt.

### Generation

```python
client.chat.completions.create()
```

LLM generates the final response.

Therefore, this project is a complete basic implementation of a Retrieval-Augmented Generation (RAG) chatbot using:

* OpenRouter
* FAISS
* HuggingFace Embeddings
* LangChain
* Text File Knowledge Base
