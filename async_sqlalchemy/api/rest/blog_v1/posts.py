from dataclasses import asdict

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from async_sqlalchemy.modules.blog.application import create_new_post
from async_sqlalchemy.modules.shared.database import async_db_session

from . import models as api_model

router = APIRouter(prefix="/posts", tags=["posts"])


@router.post(
    "/create",
    response_model=api_model.ResNewPost,
    operation_id="create_post",
)
async def create_post(
    post_req: api_model.ReqNewPost,
    async_session: AsyncSession = Depends(async_db_session),
) -> api_model.ResNewPost:
    new_post = await create_new_post(async_session, post_req)
    return api_model.ResNewPost(**asdict(new_post))
