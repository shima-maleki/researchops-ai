from app.services.arxiv_service import fetch_latest_papers

papers = fetch_latest_papers(max_results=3)

print(len(papers))

for paper in papers:
    print(paper["title"])
    print(paper["category"])
    print("---")