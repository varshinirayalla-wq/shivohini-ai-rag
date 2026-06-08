import os
import json

# Map documents to metadata files
METADATA_MAP = {
    "company_overview.txt": "company_metadata.json",
    "industries_served.txt": "company_metadata.json",
    "mission_vision.txt": "company_metadata.json",
    "team_info.txt": "company_metadata.json",

    "chatbot_service.txt": "ai_chatbot_metadata.json",
    "automation_service.txt": "workflow_automation_metadata.json",
    "rag_service.txt": "rag_solution_metadata.json",

    "faqs.txt": "company_metadata.json",
    "pricing.txt": "company_metadata.json",
    "case_study_1.txt": "company_metadata.json"
}


def extract_metadata(file_path):
    """
    Extract metadata for a document.
    """

    filename = os.path.basename(file_path)

    metadata_file = METADATA_MAP.get(filename)

    # Try loading metadata JSON
    if metadata_file:

        metadata_path = os.path.join("metadata", metadata_file)

        if os.path.exists(metadata_path):

            try:
                with open(metadata_path, "r", encoding="utf-8") as f:
                    metadata = json.load(f)

                return metadata

            except Exception as e:
                print(f"Metadata error in {metadata_file}: {e}")

    # Fallback metadata
    service_name = (
        filename
        .replace(".txt", "")
        .replace("_", " ")
        .title()
    )

    return {
        "service_name": service_name,
        "category": "General",
        "industry": "General",
        "tags": [],

        "pricing_range": "",
        "timeline": "",
        "complexity": "",

        "image_urls": [],
        "pdf_urls": [],
        "presentation_urls": [],
        "video_urls": [],

        "source": file_path,
        "document_type": "service"
    }