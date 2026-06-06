import os
import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="shivohini_metadata_kb"
)

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

        if not file.endswith(".txt"):
            continue

        filepath = os.path.join(folder, file)

        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()

        embedding = model.encode(text)

        metadata = {
            "source": filepath,
            "document_type": folder.split("/")[-1],
            "service_name": file.replace(".txt", ""),
            "category": "AI Services",
            "industry": "General",
            "pricing_range": "Custom",
            "complexity_level": "Medium"
        }

        collection.add(
            ids=[filepath],
            documents=[text],
            embeddings=[embedding.tolist()],
            metadatas=[metadata]
        )

        print(f"Indexed: {filepath}")

print("Metadata indexing completed")