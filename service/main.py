from fastapi import FastAPI
from service.api.api_v1.api import router as api_router
from service.core.config import API_V1_STR, PROJECT_NAME

app = FastAPI(
    title=PROJECT_NAME,
)

app.include_router(api_router, prefix=API_V1_STR)


@app.get("/ping", summary="Check that the service is operational")
def pong():
    return {"ping": "pong! A"}
