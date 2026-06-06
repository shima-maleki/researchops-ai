from fastapi import FastAPI
from app.services.arxiv_service import fetch_latest_papers, search_papers

app = FastAPI(title="ResearchOps AI")


@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/papers/latest")
def latest_papers():
    return fetch_latest_papers(max_results=5)

@app.get("/papers/search")
def search_research_papers(query: str):
    return search_papers(query=query, max_results=5)





