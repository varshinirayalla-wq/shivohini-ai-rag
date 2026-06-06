import os
import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create ChromaDB client
client = chromadb.PersistentClient(path="./chroma_db")

# Create collection
collection = client.get_or_create_collection(
    name="shivohini_kb"
)

# Folders to index
folders = [
    "data/company",
    "data/services",
    "data/faqs",
    "data/case_studies",
    "data/pricing"
]

for folder in folders:

    if not os.path.exists(folder):
        continue

    for file in os.listdir(folder):

        filepath = os.path.join(folder, file)

        if not file.endswith(".txt"):
            continue

        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()

        embedding = model.encode(text)

        collection.add(
            ids=[filepath],
            documents=[text],
            embeddings=[embedding.tolist()],
            metadatas=[{
                "source": filepath,
                "document_type": folder.split("/")[-1]
            }]
        )

        print(f"Indexed: {filepath}")

print("All documents indexed successfully!")