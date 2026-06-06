from fastapi import FastAPI
from app.services.arxiv_service import fetch_latest_papers, search_papers
from app.ingestion.ingest_papers import ingest_latest_papers
from app.services.search_service import semantic_search

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


@app.post("/ingest")
def ingest(max_results: int = 5):
    return ingest_latest_papers(max_results)



@app.get("/papers/semantic-search")
def semantic_paper_search(query: str, limit: int = 5):
    return semantic_search(query=query, limit=limit)


