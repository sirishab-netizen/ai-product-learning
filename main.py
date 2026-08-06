from fastapi import FastAPI

app = FastAPI(title="AI Job Copilot")


@app.get("/health")
def health():
    return {"status": "ok"}