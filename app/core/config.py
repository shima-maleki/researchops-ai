from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    OPENAI_API_KEY: str = ""
    QDRANT_URL: str = ""
    QDRANT_API_KEY: str = ""
    QDRANT_COLLECTION: str = "research_papers"
    OPENAI_EMBEDDING_MODEL: str = "text-embedding-3-small"
    ARXIV_BASE_URL: str = "https://export.arxiv.org/api/query"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()
