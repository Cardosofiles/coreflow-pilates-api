from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings

app = FastAPI(title=settings.APP_NAME)

app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "API online"}
