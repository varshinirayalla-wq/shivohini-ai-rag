def chunk_document(text, chunk_type="service"):
    """
    Simple chunking strategy for RAG system
    """

    if not text:
        return []

    # SERVICE → keep whole document together
    if chunk_type == "service":
        return [text]

    # FAQ → split by question blocks
    if chunk_type == "faq":
        return text.split("\n\n")

    # DEFAULT → basic chunking
    chunk_size = 500
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]