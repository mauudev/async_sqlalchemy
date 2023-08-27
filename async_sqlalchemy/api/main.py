import os

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from async_sqlalchemy.api.rest.error_handlers import add_error_handler
from async_sqlalchemy.api.rest.route_builder import build_routes
from async_sqlalchemy.modules.shared.logger import logger

API_PORT = os.getenv("API_PORT", "8000")
API_HOST = os.getenv("API_HOST", "0.0.0.0")

app = FastAPI()
app = add_error_handler(app)
app = build_routes(app)


@app.get("/")
async def root():
    return {"message": "Hello from main server !"}


class PayloadSample(BaseModel):
    name: str
    lastname: str


def start_server():
    logger.info(f"Started server running on port: {API_PORT}")
    uvicorn.run(
        "async_sqlalchemy.api.main:app",
        host=API_HOST,
        port=int(API_PORT),
        log_level="info",
        reload=True,
    )


if __name__ == "__main__":
    start_server()
