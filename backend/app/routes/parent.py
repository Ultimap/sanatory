from fastapi import APIRouter, Depends
from app.models.models import User
from app.services.parent import ParentService
from app.depends import get_parent_service, get_current_user_is_doctor, get_current_user_is_admin

_parent = APIRouter(prefix='/api/parent', tags=['Parent'])


@_parent.get('/')
async def get_all_parent(parent_service: ParentService = Depends(get_parent_service),
                         user: User = Depends(get_current_user_is_doctor)):
    return await parent_service.get_all_parent()


@_parent.delete('/delete/{parent_id}')
async def delete_parent(parent_id: int, parent_service: ParentService = Depends(get_parent_service),
                         user: User = Depends(get_current_user_is_doctor)):
    await parent_service.delete_parent(parent_id)
    return {'meesage': 'Success'}


@_parent.get('/{parent_id}')
async def get_all_parent(parent_id: int, parent_service: ParentService = Depends(get_parent_service),
                         user: User = Depends(get_current_user_is_doctor)):
    return await parent_service.get_parent_by_id(parent_id)