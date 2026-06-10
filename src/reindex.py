import os
from src.ingestion.pipeline import ingest_folder


def reindex():

    folders = [
        "data/company",
        "data/services",
        "data/faqs",
        "data/case_studies",
        "data/pricing"
    ]

    print("Starting Re-indexing...")

    for folder in folders:

        if os.path.exists(folder):
            print(f"Processing {folder}")
            ingest_folder(folder)

    print("Re-indexing Complete")


if __name__ == "__main__":
    reindex()