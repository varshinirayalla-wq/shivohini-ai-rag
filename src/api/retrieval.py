import chromadb
from datetime import datetime
from src.embedding.embedder import get_embedding

client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_collection("shivohini_rag")


def retrieve(query, top_k=5, filters=None):

    query_embedding = get_embedding(query)

    if filters:
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            where=filters
        )
    else:
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

    output = []

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]
    distances = results.get("distances", [[]])[0]

    query_lower = query.lower()

    for i in range(len(documents)):

        metadata = metadatas[i] if i < len(metadatas) else {}

        content = documents[i]

        # Hybrid Search + Basic Re-ranking
        keyword_score = 0

        query_words = query_lower.split()

        for word in query_words:
            if word in content.lower():
                keyword_score += 0.1

        final_score = (
            distances[i] - keyword_score
            if i < len(distances)
            else None
        )

        output.append({

            "content": content,

            "retrieval_timestamp": datetime.utcnow().isoformat(),

            "metadata": {
                "service_name": metadata.get("service_name"),
                "category": metadata.get("category"),
                "industry": metadata.get("industry"),
                "tags": metadata.get("tags"),
                "pricing_range": metadata.get("pricing_range"),
                "timeline": metadata.get("timeline"),
                "complexity": metadata.get("complexity"),
                "document_type": metadata.get("document_type"),
                "source": metadata.get("source"),
                "last_updated": metadata.get("last_updated")
            },

            "media": {
                "image_urls": metadata.get("image_urls", ""),
                "pdf_urls": metadata.get("pdf_urls", ""),
                "presentation_urls": metadata.get("presentation_urls", ""),
                "video_urls": metadata.get("video_urls", "")
            },

            "score": final_score
        })

    output.sort(key=lambda x: x["score"])

    return output