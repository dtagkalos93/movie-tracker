from fastapi import FastAPI

from app.api.v1 import health

app = FastAPI(
    title="Movie Library",
    version="0.1.0",
    description="Backend API for managing a personal movie library.",
    openapi_tags=[
        {"name": "Health", "description": "Health check endpoints"},
        # Add more tags later like "Movies", "Users", etc.
    ],
)

app.include_router(health.router)
