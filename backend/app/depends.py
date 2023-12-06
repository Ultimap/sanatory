from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from datetime import timedelta
from app.config import async_session, ALGORITH, SECRET_KEY, oauth2scheme
from app.repositories.user import UserRepositories
from app.services.user import UserService

async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

SECRET_KEY = 'osbvsiohgjbsdgb'

user_repository = UserRepositories()

user_service = UserService(user_repository, expirate_time=timedelta(days=3), 
                           alghorithm=ALGORITH, secret_key=SECRET_KEY)

async def get_user_service() -> UserService:
    return user_service


async def get_user_by_jwt(token: str = Depends(oauth2scheme)):
    user_service.get_current_user(token)