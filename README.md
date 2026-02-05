# 🛒AI-E-Commerce-Support-Agent

An AI-powered e-commerce support application that helps users find products using natural language queries.
The system uses a retrieval-based (RAG) approach to return results from a structured product catalog.

-------------------------------------------------------------------------------------------------------

# ✨ Key Features

🔍 Retrieval-based product search using a structured product dataset

🧠 RAG architecture with strict grounding on product data

🖥️ Interactive Streamlit UI 

📦 Supports 1000+ products via CSV-based catalog

🏷️ Category-aware filtering (phones, laptops, TVs, headphones, wearables)

-----------------------------------------------------------------------------------------------------

# 🧰Tech Stack

Python

Streamlit – Web UI

Sentence Transformers – Embeddings

FAISS – Vector Search

Pandas 

RAG Architecture

-----------------------------------------------------------------------------------------------------

# Architecture 

User Query
   ->
Sentence Transformer (Embeddings)
   ->
FAISS Vector Search
   ->
Relevant Products
   ->
Response Generation (RAG)
   ->
UI Rendering (Streamlit)

----------------------------------------------------------------------------------------------------

# 🚀 Getting Started

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/ananyasamal812-commit/AI-E-Commerce-Support-Agent.git
cd AI-E-Commerce-Support-Agent

2️⃣ Create & Activate Virtual Environment

python -m venv venv

.\venv\Scripts\activate  #Windows

source venv/bin/activate  #Mac/Linux

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Run the App

streamlit run app.py





--------------------------------------------------------------------------------------------------------


# 🧪 Sample Queries

Suggest a smartphone under 30000

Best laptop

Recommend headphones

Suggest a TV

Best smartwatch

---------------------------------------------------------------------------------------------------------



