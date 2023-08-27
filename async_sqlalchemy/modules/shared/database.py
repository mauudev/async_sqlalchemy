import os
from contextlib import asynccontextmanager, contextmanager
from datetime import datetime
from functools import cache
from typing import AsyncContextManager, Callable, ContextManager
from uuid import UUID, uuid4

from sqlalchemy import QueuePool
from sqlalchemy.dialects.postgresql import UUID as UUID_PG
from sqlalchemy.engine import Engine, create_engine
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import (
    Mapped,
    Session,
    mapped_column,
    registry,
    scoped_session,
    sessionmaker,
)

from .logger import logger

# casco pero salva
DATABASE_POOL_SIZE = os.getenv("DATABASE_POOL_SIZE", "10")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
DATABASE_URL_ASYNC = f"postgresql+asyncpg://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"


reg = registry()


@reg.mapped_as_dataclass(kw_only=True)
class Entity:
    __abstract__ = True

    id: Mapped[int | None] = mapped_column(
        primary_key=True, default=None, nullable=False, autoincrement=True
    )
    uuid: Mapped[UUID] = mapped_column(UUID_PG(), index=True, default_factory=uuid4)
    created_at: Mapped[datetime] = mapped_column(default_factory=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        default_factory=datetime.utcnow, onupdate=datetime.utcnow
    )


@cache
def build_engine() -> Engine:
    return create_engine(
        DATABASE_URL,
        poolclass=QueuePool,
        pool_size=int(DATABASE_POOL_SIZE),
    )


@cache
def db_connection_pool() -> Callable[[], Session]:
    logger.debug("Creating DB Session ..")
    session_factory = sessionmaker(
        bind=build_engine(), autocommit=False, autoflush=True
    )
    return session_factory


@contextmanager
def db_session() -> ContextManager[Session]:
    session: Session = db_connection_pool()()
    try:
        yield session

    except Exception as e:
        logger.error("Database error, rolling back", exc_info=True)
        session.rollback()
        raise e

    finally:
        session.close()


@cache
def build_async_engine() -> Engine:
    return create_async_engine(
        DATABASE_URL_ASYNC,
        poolclass=QueuePool,
        pool_size=int(DATABASE_POOL_SIZE),
    )


@cache
def db_connection_pool_async() -> Callable[[], AsyncSession]:
    logger.debug("Creating DB AsyncSession ..")
    session_factory = async_sessionmaker(
        bind=build_async_engine(),
        autocommit=False,
        autoflush=True,
        expire_on_commit=False,
    )
    return session_factory


@asynccontextmanager
async def async_db_session() -> AsyncContextManager[AsyncSession]:
    session: AsyncSession = db_connection_pool_async()()
    try:
        yield session

    except Exception as e:
        logger.error("Database error, rolling back", exc_info=True)
        await session.rollback()
        raise e

    finally:
        await session.close()
