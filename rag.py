from sentence_transformers import SentenceTransformer
import faiss
import pandas as pd
import numpy as np
import re

# -------------------------------
# LOAD DATA
# -------------------------------
df = pd.read_csv("products_1000.csv")

df.fillna("", inplace=True)

# Ensure required columns exist
required_cols = {"name", "description", "price", "category"}
if not required_cols.issubset(df.columns):
    raise ValueError(f"CSV must contain columns: {required_cols}")

# -------------------------------
# EMBEDDING MODEL
# -------------------------------
model = SentenceTransformer("all-MiniLM-L6-v2")

texts = (df["name"] + " " + df["description"]).tolist()
embeddings = model.encode(texts, convert_to_numpy=True)

# -------------------------------
# FAISS INDEX
# -------------------------------
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# -------------------------------
# QUERY PARSER
# -------------------------------
def extract_budget(query):
    match = re.search(r"under\s*(\d+)", query.lower())
    return int(match.group(1)) if match else None


# -------------------------------
# MAIN PIPELINE (THIS WAS MISSING)
# -------------------------------
def rag_pipeline(query, top_k=5):
    query_embedding = model.encode([query], convert_to_numpy=True)

    distances, indices = index.search(query_embedding, top_k)

    results = []
    budget = extract_budget(query)

    for idx in indices[0]:
        product = df.iloc[idx]

        # Budget filtering
        if budget and product["price"] > budget:
            continue

        results.append({
            "name": product["name"],
            "description": product["description"],
            "price": int(product["price"]),
            "category": product["category"]
        })

    return results
