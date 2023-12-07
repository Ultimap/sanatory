from fastapi import FastAPI
from app.models.models import Role
from app.config import async_session
from app.routes.user import _user
from app.routes.specialization import _specialization

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    try:
        async with async_session() as session:
            session.add(Role(name='Admin'))
            session.add(Role(name='Doctor'))
            session.add(Role(name='Parent'))
            await session.commit()
    except:
        ...

app.include_router(_user)
app.include_router(_specialization)