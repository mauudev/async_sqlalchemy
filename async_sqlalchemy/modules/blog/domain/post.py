from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from async_sqlalchemy.modules.shared.database import Entity, reg


@reg.mapped_as_dataclass(kw_only=True)
class Post(Entity):
    __tablename__ = "posts"

    title: Mapped[str] = mapped_column(nullable=True, default=None)
    content: Mapped[str] = mapped_column(nullable=True, default=None)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship("User", back_populates="posts", lazy="joined")
    comments: Mapped[List["Comment"]] = relationship(
        "Comment", default_factory=list, back_populates="post", lazy="joined"
    )
