from app.core.config import settings
from app.services.embedding_service import create_embedding
from app.services.qdrant_service import get_qdrant_client


def semantic_search(query: str, limit: int = 5):
    query_vector = create_embedding(query)

    client = get_qdrant_client()

    results = client.query_points(
        collection_name=settings.QDRANT_COLLECTION,
        query=query_vector,
        limit=limit,
    )

    papers = []

    for result in results.points:
        papers.append(
            {
                "score": result.score,
                "title": result.payload.get("title"),
                "summary": result.payload.get("summary"),
                "link": result.payload.get("link"),
                "category": result.payload.get("category"),
            }
        )

    return papers