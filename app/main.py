from fastapi import FastAPI

app = FastAPI(title="ResearchOps AI")


@app.get("/health")
def health_check():
    return {"status": "ok"}





