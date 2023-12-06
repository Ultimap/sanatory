from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.models import Role
from app.depends import get_session
from app.config import async_session
from app.routes.user import _user


app = FastAPI()


@app.on_event("startup")
async def startup_event():
    try:
        async with async_session() as session:
            session.add(Role(name='Doctor'))
            session.add(Role(name='Parent'))
            await session.commit()
    except:
        ...

app.include_router(_user)