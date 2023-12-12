from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

async_engine = create_async_engine('sqlite+aiosqlite:///backend.db')

async_session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)

SECRET_KEY = 'asvcxzadsfsa'

ALGORITH = 'HS256'

oauth2scheme = OAuth2PasswordBearer('/api/user/login')

img_folder = '/img'