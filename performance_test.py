import time
from src.api.retrieval import retrieve

start = time.time()

results = retrieve("AI chatbot")

end = time.time()

print(f"Results Found: {len(results)}")
print(f"Latency: {end - start:.4f} seconds")
