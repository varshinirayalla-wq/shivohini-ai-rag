import chromadb

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_collection("shivohini_rag")

print("Document count:", collection.count())