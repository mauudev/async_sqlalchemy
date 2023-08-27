from uuid import UUID

from pydantic import BaseModel


class ReqNewUser(BaseModel):
    name: str
    email: str
    phone: str | None
    address: str | None


class ResNewUser(BaseModel):
    id: int
    uuid: UUID
    name: str
    email: str
    phone: str | None
    address: str | None


class ReqNewPost(BaseModel):
    title: str
    content: str
    user_id: int


class ResNewPost(BaseModel):
    id: int
    uuid: UUID
    title: str
    content: str
    user_id: int


class ReqNewComment(BaseModel):
    content: str
    post_id: int
    user_id: int


class ResNewComment(BaseModel):
    id: int
    uuid: UUID
    content: str
    post_id: int
    user_id: int
