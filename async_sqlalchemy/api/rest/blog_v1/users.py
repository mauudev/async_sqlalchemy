from dataclasses import asdict

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from async_sqlalchemy.modules.blog.application import create_new_user
from async_sqlalchemy.modules.shared.database import async_db_session

from . import models as api_model

router = APIRouter(prefix="/users", tags=["users"])


@router.post(
    "/create",
    response_model=api_model.ResNewUser,
    operation_id="register_user",
)
async def register_user(
    user_req: api_model.ReqNewUser,
    async_session: AsyncSession = Depends(async_db_session),
) -> api_model.ResNewUser:
    new_user = await create_new_user(async_session, user_req)
    return api_model.ResNewUser(**asdict(new_user))
