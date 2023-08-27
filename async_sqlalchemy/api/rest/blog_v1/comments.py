from dataclasses import asdict

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from async_sqlalchemy.modules.blog.application import create_new_comment
from async_sqlalchemy.modules.shared.database import async_db_session

from . import models as api_model

router = APIRouter(prefix="/comments", tags=["comments"])


@router.post(
    "/create",
    response_model=api_model.ResNewComment,
    operation_id="create_comment",
)
async def create_comment(
    comment_req: api_model.ReqNewComment,
    async_session: AsyncSession = Depends(async_db_session),
) -> api_model.ResNewComment:
    new_comment = await create_new_comment(async_session, comment_req)
    return api_model.ResNewComment(**asdict(new_comment))
