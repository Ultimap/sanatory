from sqlalchemy import select
from app.models.models import User
from app.config import async_session as session
from app.schemas.user import UserScheme

class UserRepositories:

    async def get_user_by_id(self, user_id: int) -> User | None:
        async with session() as db:
            user = await db.execute(select(User).where(User.id == user_id))
            return user.scalar_one_or_none()


    async def get_user_by_username(self, username: int) -> User | None:
        async with session() as db:
            user = await db.execute(select(User).where(User.username == username))
            return user.scalar_one_or_none()
    

    async def create_user(self, data: UserScheme) -> User | None:
        async with session() as db:
            try:
                user = User(**data.__dict__)
                db.add(user)
                await db.commit()
                return user
            except:
                return None
            