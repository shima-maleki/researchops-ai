from openai import OpenAI

from app.core.config import settings
from app.services.search_service import semantic_search


client = OpenAI(api_key=settings.OPENAI_API_KEY)


def answer_question(question: str, limit: int = 3):
    papers = semantic_search(query=question, limit=limit)

    if not papers:
        return {
            "question": question,
            "answer": "No relevant papers were found in Qdrant yet. Please run ingestion first using POST /ingest.",
            "sources": [],
        }

    context = ""

    for paper in papers:
        context += f"""
Title: {paper["title"]}
Summary: {paper["summary"]}
Link: {paper["link"]}
Category: {paper["category"]}
---
"""

    prompt = f"""
You are ResearchOps AI, an assistant that answers questions using research paper context.

Question:
{question}

Relevant papers:
{context}

Answer clearly and cite paper titles when useful.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful AI research assistant."},
            {"role": "user", "content": prompt},
        ],
    )

    return {
        "question": question,
        "answer": response.choices[0].message.content,
        "sources": papers,
    }