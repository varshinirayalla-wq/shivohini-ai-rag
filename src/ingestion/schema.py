from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class Document:
    id: str
    content: str

    # business metadata
    service_name: Optional[str]
    category: Optional[str]
    industry: Optional[str]
    tags: List[str]

    pricing_range: Optional[str]
    timeline: Optional[str]
    complexity: Optional[str]

    # media
    image_urls: List[str]
    pdf_urls: List[str]
    video_urls: List[str]
    presentation_urls: List[str]

    # system metadata
    source: str
    last_updated: str
    doc_type: str