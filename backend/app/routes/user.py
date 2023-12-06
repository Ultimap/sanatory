from fastapi import APIRouter, Depends
from app.services.user import UserService
from app.schemas.user import UserScheme, UserLogin
from app.depends import get_user_service

_user = APIRouter(prefix='/api/user', tags=['User'])


@_user.post('/register', status_code=201)
async def register(data: UserScheme, service: UserService = Depends(get_user_service)):
    user = await service.create_user(data)
    return {'message': 'Success'}

@_user.post('/login')
async def login(data: UserLogin, service: UserService = Depends(get_user_service)):
    token = await service.login(data)
    return {'access_token': token}