from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from async_sqlalchemy.modules.shared.database import Entity, reg

from .comment import Comment
from .post import Post


@reg.mapped_as_dataclass(kw_only=True)
class User(Entity):
    __tablename__ = "users"

    name: Mapped[str] = mapped_column(nullable=True, default=None)
    email: Mapped[str] = mapped_column(nullable=True, default=None)
    phone: Mapped[str] = mapped_column(nullable=True, default=None)
    address: Mapped[str] = mapped_column(nullable=True, default=None)
    posts: Mapped[List["Post"]] = relationship(
        "Post", default_factory=list, back_populates="user", lazy="joined"
    )
    comments: Mapped[List["Comment"]] = relationship(
        "Comment", default_factory=list, back_populates="user", lazy="joined"
    )
