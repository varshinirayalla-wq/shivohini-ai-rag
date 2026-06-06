import chromadb

# Connect to ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")

# Load collection
collection = client.get_collection("shivohini_kb")

# Ask a question
query = input("Enter your question: ")

results = collection.query(
    query_texts=[query],
    n_results=3
)

print("\nRESULTS:\n")

for doc in results["documents"][0]:
    print(doc)
    print("-" * 50)