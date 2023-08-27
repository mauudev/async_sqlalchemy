from dataclasses import dataclass
from typing import Any, AsyncContextManager
from uuid import UUID

from async_sqlalchemy.modules.blog.domain import User
from async_sqlalchemy.modules.shared.logger import logger


@dataclass
class NewUserResponse:
    id: int
    uuid: UUID
    name: str
    email: str
    phone: str
    address: str


async def create_new_user(async_db_session: AsyncContextManager, user: Any):
    async with async_db_session as session:
        logger.info(f"Creating new user: {user}")
        user = User(
            name=user.name,
            email=user.email,
            phone=user.phone,
            address=user.address,
        )
        session.add(user)
        await session.commit()
        return NewUserResponse(
            id=user.id,
            uuid=user.uuid,
            name=user.name,
            email=user.email,
            phone=user.phone,
            address=user.address,
        )
