from app.ingestion.ingest_papers import ingest_latest_papers

result = ingest_latest_papers(max_results=1)

print(result)