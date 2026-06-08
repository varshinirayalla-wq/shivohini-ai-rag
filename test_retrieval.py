from src.api.retrieval import retrieve

query = "AI development services"

results = retrieve(query)

for r in results:
    print("\n--- RESULT ---")
    print(r["content"])
    print(r["metadata"])
    print(r["score"])