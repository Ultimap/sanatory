from fastapi import APIRouter, Depends
from app.schemas.specialication import SpecializationScheme
from app.services.specialzation import SpecializationService
from app.models.models import User
from app.depends import get_spec_serivce, get_current_user_is_admin
_specialization = APIRouter(prefix='/api/specialization', tags=['Specialization'])

@_specialization.post('/create', status_code=201)
async def specialization_create(data:SpecializationScheme, 
                                service: SpecializationService = Depends(get_spec_serivce),
                                user: User = Depends(get_current_user_is_admin)):
    spec = await service.create_specialization(data)
    return {'message': 'Success'}