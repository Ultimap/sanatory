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
from app.repositories.parent import ParentRepository
from app.services.parent import ParentService
from app.repositories.child import ChildRepository
from app.services.child import ChildService
from app.repositories.medcard import MedcardRepository
from app.services.medcard import MedcardService


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

user_repository = UserRepositories()

user_service = UserService(user_repository, expirate_time=timedelta(days=3), 
                           alghorithm=ALGORITH, secret_key=SECRET_KEY)


specialization_repository = SpecializationRepository()

specialization_service = SpecializationService(specialization_repository)


doctor_repository = DoctorRepository()

doctor_service = DoctorService(doctor_repository)


parent_repository = ParentRepository()

parent_service = ParentService(parent_repository)


child_repository = ChildRepository()

child_service = ChildService(child_repository)


medcard_repository = MedcardRepository()

medcard_service = MedcardService(medcard_repository)



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


async def get_spec_serivce() -> SpecializationService:
    return specialization_service


async def get_doctor_serivce() -> DoctorService:
    return doctor_service


async def get_parent_service() -> ParentService:
    return parent_service


async def get_child_service() -> ChildService:
    return child_service


async def get_medcard_service() -> MedcardService:
    return medcard_service