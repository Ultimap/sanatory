from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException
from datetime import timedelta
from app.config import async_session, ALGORITH, SECRET_KEY, oauth2scheme
from app.repositories.user import UserRepositories
from app.services.user import UserService
from app.repositories.specialization import SpecializationRepository
from app.services.specialzation import SpecializationService
from app.repositories.doctor import DoctorRepository
from app.services.doctor import DoctorService

async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

SECRET_KEY = 'osbvsiohgjbsdgb'

user_repository = UserRepositories()

user_service = UserService(user_repository, expirate_time=timedelta(days=3), 
                           alghorithm=ALGORITH, secret_key=SECRET_KEY)

async def get_user_service() -> UserService:
    return user_service


async def get_current_user(token: str = Depends(oauth2scheme)):
    return await user_service.get_current_user(token)

async def get_current_user_is_admin(token: str = Depends(oauth2scheme)):
    user = await user_service.get_current_user_is_admin(token)
    if not user:
        raise HTTPException(status_code=403)
    return user
    
    
async def get_current_user_is_doctor(token: str = Depends(oauth2scheme)):
    user = await user_service.get_current_user_is_doctor(token)
    if not user:
        raise HTTPException(status_code=403)
    return user

specialization_repository = SpecializationRepository()

specialization_service = SpecializationService(specialization_repository)

async def get_spec_serivce() -> SpecializationService:
    return specialization_service

doctor_repository = DoctorRepository()

doctor_service = DoctorService(doctor_repository)

async def get_doctor_serivce() -> DoctorService:
    return doctor_service