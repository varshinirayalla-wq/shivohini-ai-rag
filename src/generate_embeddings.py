from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

text = """
AI Chatbot Development Service
"""

embedding = model.encode(text)

print("Embedding Dimension:", len(embedding))
print(embedding[:10])