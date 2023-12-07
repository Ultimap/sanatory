from fastapi import APIRouter, Depends
from app.services.user import UserService
from app.services.doctor import DoctorService
from app.schemas.user import UserScheme, UserLogin, DoctorRigisterScheme
from app.schemas.doctor import DoctorScheme
from app.depends import get_user_service, get_doctor_serivce

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

@_user.post('/login')
async def login(data: UserLogin, service: UserService = Depends(get_user_service)):
    token = await service.login(data)
    return {'access_token': token}