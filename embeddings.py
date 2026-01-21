from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from products import products

model = SentenceTransformer("all-MiniLM-L6-v2")

texts = [
    f"{p['name']} {p['category']} {p['description']} Price {p['price']}"
    for p in products
]

embeddings = model.encode(texts)

index = faiss.IndexFlatL2(len(embeddings[0]))
index.add(np.array(embeddings))

faiss.write_index(index, "product_index.faiss")

