import httpx
import feedparser

from app.core.config import settings
from app.models.paper import Paper


def fetch_latest_papers(max_results: int = 5):
    params = {
        "search_query": "cat:cs.AI OR cat:cs.CL OR cat:cs.LG OR cat:cs.IR",
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }

    headers = {
        "User-Agent": "ResearchOpsAI/0.1 (mailto:shimamaleki95@gmail.com)"
    }

    response = httpx.get(
        settings.ARXIV_BASE_URL,
        params=params,
        headers=headers,
        timeout=30,
    )

    try:
        response.raise_for_status()
    except httpx.HTTPStatusError as error:
        if error.response.status_code == 429:
            print("arXiv rate limit reached. Please wait and try again later.")
            return []

        raise

    feed = feedparser.parse(response.text)

    papers = []

    for entry in feed.entries:
        papers.append(
            Paper(
                title=entry.title,
                summary=entry.summary,
                link=entry.link,
                category=(
                    entry.tags[0]["term"]
                    if hasattr(entry, "tags") and entry.tags
                    else "unknown"
                ),
            )
        )

    return papers


def search_papers(query: str, max_results: int = 5):
    params = {
        "search_query": f'all:"{query}"',
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }

    headers = {
        "User-Agent": "ResearchOpsAI/0.1 (mailto:shimamaleki95@gmail.com)"
    }

    response = httpx.get(
        settings.ARXIV_BASE_URL,
        params=params,
        headers=headers,
        timeout=30,
    )

    try:
        response.raise_for_status()
    except httpx.HTTPStatusError as error:
        if error.response.status_code == 429:
            print("arXiv rate limit reached. Please wait and try again later.")
            return []

        raise

    feed = feedparser.parse(response.text)

    papers = []

    for entry in feed.entries:
        papers.append(
            Paper(
                title=entry.title,
                summary=entry.summary,
                link=entry.link,
                category=(
                    entry.tags[0]["term"]
                    if hasattr(entry, "tags") and entry.tags
                    else "unknown"
                ),
            )
        )

    return papers