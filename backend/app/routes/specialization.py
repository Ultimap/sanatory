from fastapi import APIRouter, Depends
from app.schemas.specialication import SpecializationScheme
from app.services.specialzation import SpecializationService
from app.models.models import User
from app.depends import get_spec_serivce, get_current_user_is_admin
_specialization = APIRouter(prefix='/api/specialization', tags=['Specialization'])


@_specialization.get('/')
async def specialization_get(service: SpecializationService = Depends(get_spec_serivce)):
    return await service.get_all_specialization()


@_specialization.post('/create', status_code=201)
async def create_specialization(data:SpecializationScheme, 
                                service: SpecializationService = Depends(get_spec_serivce),
                                user: User = Depends(get_current_user_is_admin)):
    await service.create_specialization(data)
    return {'message': 'Success'}


@_specialization.delete('/delete/{specialization_id}')
async def delete_specialization(specialization_id: int, 
                                service: SpecializationService = Depends(get_spec_serivce),
                                user: User = Depends(get_current_user_is_admin)):
    await service.delete_specialization(specialization_id)
    return {'message': 'Success'}


@_specialization.get('/{specialization_id}')
async def specialization_get(specialization_id: int, service: SpecializationService = Depends(get_spec_serivce)):
    return await service.get_specialization_by_id(specialization_id)

