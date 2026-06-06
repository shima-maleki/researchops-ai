from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

from app.core.config import settings


VECTOR_SIZE = 1536


def get_qdrant_client():
    return QdrantClient(
        url=settings.QDRANT_URL,
        api_key=settings.QDRANT_API_KEY,
    )


def ensure_collection_exists():
    client = get_qdrant_client()

    collections = client.get_collections().collections
    collection_names = [collection.name for collection in collections]

    if settings.QDRANT_COLLECTION not in collection_names:
        client.create_collection(
            collection_name=settings.QDRANT_COLLECTION,
            vectors_config=VectorParams(
                size=VECTOR_SIZE,
                distance=Distance.COSINE,
            ),
        )
    return True