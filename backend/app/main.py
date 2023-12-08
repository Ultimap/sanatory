from fastapi import FastAPI
from fastapi.responses import FileResponse
from app.models.models import Role
from app.config import async_session, img_folder
from app.routes.user import _user
from app.routes.specialization import _specialization
from app.routes.doctor import _doctor
from app.routes.parent import _parent
from app.routes.child import _child

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
app.include_router(_doctor)
app.include_router(_parent)
app.include_router(_child)


@app.get('/api/img/{filename}')
async def get_file(filename: str):
    return FileResponse(f'{img_folder}/{filename}')