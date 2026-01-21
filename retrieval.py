import pandas as pd
import numpy as np
import faiss
import re
from sentence_transformers import SentenceTransformer

# Load data
df = pd.read_csv("products_1000.csv")

# Normalize text
df["text"] = (df["name"] + " " + df["description"] + " " + df["category"]).str.lower()

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(df["text"].tolist(), show_progress_bar=False)

# FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))


def extract_budget(query):
    match = re.search(r"under\s*(\d+)", query)
    return int(match.group(1)) if match else None


def detect_category(query):
    q = query.lower()

    if "tv" in q or "television" in q:
        return "television"
    if "phone" in q or "smartphone" in q:
        return "smartphone"
    if "laptop" in q:
        return "laptop"
    if "headphone" in q or "earphone" in q:
        return "headphones"
    if "watch" in q:
        return "watch"

    return None



def retrieve_products(query, k=5):
    query = query.lower()
    budget = extract_budget(query)
    category = detect_category(query)

    q_emb = model.encode([query])
    _, idxs = index.search(np.array(q_emb), 30)

    results = []

    for idx in idxs[0]:
        product = df.iloc[idx].to_dict()

        if category and category not in product["category"].lower():
            continue

        if budget and product["price"] > budget:
            continue

        results.append(product)

        if len(results) == k:
            break

    return results
