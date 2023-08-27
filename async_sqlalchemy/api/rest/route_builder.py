from fastapi import FastAPI

from async_sqlalchemy.api.rest.blog_v1.comments import router as comments_router
from async_sqlalchemy.api.rest.blog_v1.posts import router as posts_router
from async_sqlalchemy.api.rest.blog_v1.users import router as users_router


def build_routes(app: FastAPI) -> FastAPI:
    app.include_router(users_router, prefix="/v1")
    app.include_router(comments_router, prefix="/v1")
    app.include_router(posts_router, prefix="/v1")
    return app
