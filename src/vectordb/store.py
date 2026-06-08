import chromadb

# initialize persistent client
client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection("shivohini_rag")


def store_document(doc_id, text, embedding, metadata):
    """
    Store document into ChromaDB
    """

    collection.add(
        ids=[doc_id],
        documents=[text],
        embeddings=[embedding],
        metadatas=[metadata]
    )