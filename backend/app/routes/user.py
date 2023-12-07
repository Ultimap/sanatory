from fastapi import APIRouter, Depends
from app.services.user import UserService
from app.services.doctor import DoctorService
from app.services.parent import ParentService
from app.schemas.user import UserScheme, UserLogin, DoctorRigisterScheme, ParentRegistorScheme
from app.schemas.doctor import DoctorScheme
from app.schemas.parent import ParentScheme
from app.depends import get_user_service, get_doctor_serivce, get_parent_service

_user = APIRouter(prefix='/api/user', tags=['User'])


@_user.post('/register/doctor', status_code=201)
async def register_doctor(userdata: UserScheme, doctor_data: DoctorRigisterScheme, 
                   user_service: UserService = Depends(get_user_service),
                   doctor_serivce: DoctorService = Depends(get_doctor_serivce)
                   ):
    user = await user_service.create_user(userdata)
    doctor_data = doctor_data.__dict__
    doctor_data['FML'] = f'{doctor_data.get('first_name')} {doctor_data.get('midle_name')} {doctor_data.get('last_name')}'
    for _ in ('first_name', 'midle_name', 'last_name'):
        del doctor_data[_]
    await doctor_serivce.create_doctor(DoctorScheme(**doctor_data, user_id=user.id))
    return {'message': 'Success'}


@_user.post('/register/user', status_code=201)
async def register_user(userdata: UserScheme, parent_data: ParentRegistorScheme, 
                   user_service: UserService = Depends(get_user_service),
                   parent_serivce: ParentService = Depends(get_parent_service)
                   ):
    user = await user_service.create_user(userdata)
    parent_data = parent_data.__dict__
    parent_data['FML'] = f'{parent_data.get('first_name')} {parent_data.get('midle_name')} {parent_data.get('last_name')}'
    for _ in ('first_name', 'midle_name', 'last_name'):
        del parent_data[_]
    await parent_serivce.create_parent(ParentScheme(**parent_data, user_id=user.id))
    return {'message': 'Success'}



@_user.post('/login')
async def login(data: UserLogin, service: UserService = Depends(get_user_service)):
    token = await service.login(data)
    return {'access_token': token}