from fastapi import FastAPI
from src.api.retrieval import retrieve

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Shivohini RAG API is running"}


@app.get("/search")
def search(
    query: str,
    top_k: int = 5,
    category: str = None,
    industry: str = None
):
    try:

        if category and industry:
            filters = {
                "$and": [
                    {"category": category},
                    {"industry": industry}
                ]
            }

        elif category:
            filters = {
                "category": category
            }

        elif industry:
            filters = {
                "industry": industry
            }

        else:
            filters = None

        return retrieve(
            query=query,
            top_k=top_k,
            filters=filters
        )

    except Exception as e:
        return {
            "error": str(e)
        }