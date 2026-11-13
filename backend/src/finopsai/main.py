from fastapi import FastAPI, HTTPException

from finopsai.db import database_is_ready

app = FastAPI(title="FinOpsAI API", version="0.1.0")


@app.get("/health/live")
def liveness() -> dict[str, str]:
    return {"status": "alive"}


@app.get("/health/ready")
def readiness() -> dict[str, str]:
    if not database_is_ready():
        raise HTTPException(status_code=503, detail="Database unavailable")
    return {"status": "ready"}