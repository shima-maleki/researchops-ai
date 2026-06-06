from app.services.embedding_service import create_embedding

embedding = create_embedding("Artificial intelligence is transforming research.")

print(len(embedding))