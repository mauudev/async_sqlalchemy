import asyncio
import random

from faker import Faker
from sqlalchemy.orm import Session

from async_sqlalchemy.modules.blog.domain import Comment, Post, User
from async_sqlalchemy.modules.shared.database import async_db_session

fake = Faker()


async def create_fake_data():
    async with async_db_session() as session:
        users = []
        for _ in range(10):
            user = User(
                name=fake.name(),
                email=fake.email(),
                phone=fake.phone_number(),
                address=fake.address(),
            )
            session.add(user)
            await session.commit()
            users.append(user)

        posts = []
        for _ in range(20):
            user = random.choice(users)
            post = Post(
                title=fake.sentence(),
                content=fake.paragraph(),
                user_id=user.id,
                user=user,
            )
            session.add(post)
            await session.commit()
            posts.append(post)

        for _ in range(50):
            user = random.choice(users)
            post = random.choice(posts)
            comment = Comment(
                content=fake.sentence(),
                post_id=post.id,
                user_id=user.id,
                user=user,
                post=post,
            )
            session.add(comment)
            await session.commit()


asyncio.run(create_fake_data())
