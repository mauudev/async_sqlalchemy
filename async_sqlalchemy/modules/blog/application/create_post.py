from dataclasses import dataclass
from typing import Any, AsyncContextManager
from uuid import UUID

from async_sqlalchemy.modules.blog.domain import Post, User
from async_sqlalchemy.modules.shared import exceptions
from async_sqlalchemy.modules.shared.logger import logger


@dataclass
class NewPostResponse:
    id: int
    uuid: UUID
    title: str
    content: str
    user_id: int


async def create_new_post(async_db_session: AsyncContextManager, post: Any):
    async with async_db_session as session:
        logger.info(f"Creating new post: {post}")
        related_user = await session.get(User, post.user_id)
        if not related_user:
            raise exceptions.NotFoundError(f"User not found")
        post = Post(
            title=post.title,
            content=post.content,
            user_id=post.user_id,
            user=related_user,
        )
        session.add(post)
        await session.commit()
        return NewPostResponse(
            id=post.id,
            uuid=post.uuid,
            title=post.title,
            content=post.content,
            user_id=post.user_id,
        )
