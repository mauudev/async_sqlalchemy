from dataclasses import dataclass
from typing import Any, AsyncContextManager
from uuid import UUID

from async_sqlalchemy.modules.blog.domain import Comment, Post, User
from async_sqlalchemy.modules.shared import exceptions


@dataclass
class NewCommentResponse:
    id: int
    uuid: UUID
    content: str
    post_id: int
    user_id: int


async def create_new_comment(async_db_session: AsyncContextManager, comment: Any):
    async with async_db_session as session:
        related_user = await session.get(User, comment.user_id)
        related_post = await session.get(Post, comment.post_id)
        if not related_user or not related_post:
            raise exceptions.NotFoundError(f"User or post not found")
        comment = Comment(
            content=comment.content,
            post_id=comment.post_id,
            user_id=comment.user_id,
            user=related_user,
            post=related_post,
        )
        session.add(comment)
        await session.commit()
        return NewCommentResponse(
            id=comment.id,
            uuid=comment.uuid,
            content=comment.content,
            post_id=comment.post_id,
            user_id=comment.user_id,
        )
