from qdrant_client.models import PointStruct

from app.core.config import settings
from app.services.arxiv_service import fetch_latest_papers
from app.services.embedding_service import create_embedding
from app.services.qdrant_service import (
    ensure_collection_exists,
    get_qdrant_client,
)


def ingest_latest_papers(max_results: int = 5):
    ensure_collection_exists()

    papers = fetch_latest_papers(max_results=max_results)

    client = get_qdrant_client()

    points = []

    for index, paper in enumerate(papers):
        text = f"{paper.title}\n\n{paper.summary}"
        vector = create_embedding(text)

        points.append(
            PointStruct(
                id=index,
                vector=vector,
                payload={
                    "title": paper.title,
                    "summary": paper.summary,
                    "link": paper.link,
                    "category": paper.category,
                },
            )
        )

    if points:
        client.upsert(
            collection_name=settings.QDRANT_COLLECTION,
            points=points,
        )

    return {
        "ingested_count": len(points),
        "collection": settings.QDRANT_COLLECTION,
    }