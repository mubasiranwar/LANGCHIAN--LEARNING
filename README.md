🌟 LangChain Practice Repository
Hands-on LLMs, Chat Models, Embeddings, RAG, ChromaDB & Agentic AI
<p align="center"> <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" /> <img src="https://img.shields.io/badge/LangChain-Latest-yellow?logo=chainlink" /> <img src="https://img.shields.io/badge/ChromaDB-Vector%20DB-green?logo=database" /> <img src="https://img.shields.io/badge/HuggingFace-Models-orange?logo=huggingface" /> <img src="https://img.shields.io/badge/OpenRouter-LLMs-purple?logo=apacheairflow" /> </p>
📘 Overview

This repository contains my complete learning journey of LangChain, including real practical examples of:

LLM initialization

Chat models

Chains & RunnableSequences

Embeddings

Vector databases (ChromaDB)

PDF/Text document loaders

Query pipelines

Structured outputs

Real RAG-ready code examples

All code is organized cleanly for industry-level learning.

📂 Folder Structure
LANGCHAIN/
│
├── 1.LLMS/
│   └── llm.py
│
├── 2.CHATS-MODELS/
│   ├── chain.py
│   ├── chatmodel.py
│   ├── conditional.py
│   ├── hugging_face_chatmodel.py
│   ├── gemini.py
│   ├── parallel_chain.py
│   ├── runablesequence.py
│   └── strutureout.py
│
├── 3.EMBIDDING-MODELS/
│   ├── chromaEmbd.py
│   ├── example.txt
│   ├── Notes.pdf
│   └── query_chroma.py
│
├── 4.CHOROMADB/
│   └── p1.py
│
├── 5.Documents_loader/
│   ├── Directory_load.py
│   ├── adden_load.py
│   ├── cricket.txt
│   ├── Andrew Ng Deep Learning Notes.pdf
│   └── How To Use AI Agents in 2025.pdf
│
└── .venv/

🚀 Quick Start
1️⃣ Clone Repo
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

2️⃣ Virtual Environment
python -m venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate  # Mac/Linux

3️⃣ Install Requirements
pip install -r requirements.txt

4️⃣ Setup API Keys

Create .env:

OPENROUTER_API_KEY=your_key
HUGGINGFACE_API_KEY=your_key

🔥 Featured Topics
💬 LLMs & ChatModels

OpenRouter LLM

HuggingFace ChatModels

Gemini

Structured output

Conditional routing

⚙️ Chains

Basic chain

Parallel chains

RunnableSequence

🧠 Embeddings

Sentence Transformers

Storing & querying embeddings

Document similarity search

🗂️ Document Loading

PDF loader

Directory loader

TXT loader

Preprocessing for RAG

🗄️ Vector Store

ChromaDB

Creating collections

Querying vectors

Persisting database

📊 Technologies Used
Category	Tools
LLMs	OpenRouter, Gemini, HuggingFace
Framework	LangChain
Vector DB	ChromaDB
Embeddings	Sentence Transformers
Language	Python
Utilities	dotenv, pydantic
🛠️ Run Examples
▶️ ChatModel
python 2.CHATS-MODELS/chatmodel.py

▶️ Load Directory of Files
python 5.Documents_loader/Directory_load.py

▶️ Query Chroma
python 3.EMBIDDING-MODELS/query_chroma.py

🚧 Future Additions

Full Agent-based Tool Calling

RAG Pipeline (Complete End-to-End)

Streamlit Chatbot UI

FastAPI Backend

Automatic evaluation of RAG results

🤝 Contributing

Pull requests and suggestions are always welcome.

⭐ Support

If you like this project, consider giving it a star ⭐ on GitHub — it helps a lot!
