import os

from src.ingestion.metadata_extractor import extract_metadata
from src.ingestion.chunking import chunk_document
from src.embedding.embedder import get_embedding
from src.vectordb.store import store_document


def clean_metadata(metadata):
    """
    Convert metadata into ChromaDB-compatible format.
    """

    cleaned = {}

    for key, value in metadata.items():

        if value is None:
            cleaned[key] = ""

        elif isinstance(value, list):
            cleaned[key] = ", ".join(str(v) for v in value) if value else ""

        elif isinstance(value, dict):
            cleaned[key] = str(value)

        else:
            cleaned[key] = value

    return cleaned


def ingest_file(file_path):

    metadata = extract_metadata(file_path)
    metadata = clean_metadata(metadata)

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    chunks = chunk_document(
        content,
        metadata.get("doc_type", "service")
    )

    for i, chunk in enumerate(chunks):

        embedding = get_embedding(chunk)

        doc_id = f"{metadata.get('service_name', 'document')}_{i}"

        store_document(
            doc_id=doc_id,
            text=chunk,
            embedding=embedding,
            metadata=metadata
        )

        print(f"Stored: {doc_id}")


def ingest_folder(folder_path):

    for root, dirs, files in os.walk(folder_path):

        for file in files:

            if file.endswith(".txt"):

                file_path = os.path.join(root, file)

                print(f"Ingesting: {file_path}")

                ingest_file(file_path)


if __name__ == "__main__":

    print("Starting ingestion...")

    folders = [
        "data/company",
        "data/services",
        "data/faqs",
        "data/case_studies",
        "data/pricing",
        "data/proposals",
        "data/technical_docs"
    ]

    for folder in folders:

        if os.path.exists(folder):
            ingest_folder(folder)

    print("Ingestion completed.")