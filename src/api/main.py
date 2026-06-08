from fastapi import FastAPI
from src.api.retrieval import retrieve

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Shivohini RAG API is running"}

@app.get("/search")
def search(query: str, top_k: int = 5):
    return retrieve(query, top_k=top_k)