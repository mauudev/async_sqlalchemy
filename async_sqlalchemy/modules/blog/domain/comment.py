from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from async_sqlalchemy.modules.shared.database import Entity, reg


@reg.mapped_as_dataclass(kw_only=True)
class Comment(Entity):
    __tablename__ = "comments"

    content: Mapped[str] = mapped_column(nullable=True, default=None)
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    post: Mapped["Post"] = relationship(
        "Post", back_populates="comments", lazy="joined"
    )
    user: Mapped["User"] = relationship(
        "User", back_populates="comments", lazy="joined"
    )
