import chromadb
from src.embedding.embedder import get_embedding

client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_collection("shivohini_rag")


def retrieve(query, top_k=5, filters=None):

    query_embedding = get_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        where=filters  # optional metadata filtering
    )

    output = []

    for i in range(len(results["documents"][0])):

        output.append({
            "content": results["documents"][0][i],
            "metadata": results["metadatas"][0][i],
            "score": results["distances"][0][i]
        })

    return output