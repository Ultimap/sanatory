from fastapi import APIRouter, Depends, UploadFile, File
from app.models.models import User
from app.schemas.child import ChildScheme, ChildRegisterScheme, AddMedcardScheme
from app.services.child import ChildService
from app.services.parent import ParentService
from app.depends import get_child_service, get_current_user, get_parent_service, get_current_user_is_doctor


_child = APIRouter(prefix='/api/child', tags=['Child'])


@_child.post('/add', status_code=201)
async def create_child(child_data: ChildRegisterScheme, 
                       child_service: ChildService = Depends(get_child_service),
                       parent_service: ParentService = Depends(get_parent_service),
                       user: User = Depends(get_current_user)):
    child_data = child_data.__dict__
    child_data['FML'] = f'{child_data.get("first_name")} {child_data.get("midle_name")} {child_data.get("last_name")}'
    for _ in ('first_name', 'midle_name', 'last_name'):
        del child_data[_]
    parent_data = await parent_service.get_parent_by_user(user.id)
    await child_service.create_child(ChildScheme(**child_data, parent_id=parent_data.id))
    return {'meesage': "Success"}


@_child.get('/')
async def get_all_child(child_service: ChildService = Depends(get_child_service),
                        user: User = Depends(get_current_user_is_doctor)):
    return await child_service.get_all_child()


@_child.get('/me')
async def get_child_by_me(
                        child_service: ChildService = Depends(get_child_service),
                        parent_service: ParentService = Depends(get_parent_service),
                        user: User = Depends(get_current_user)):
    parent = await parent_service.get_parent_by_user(user.id)
    return await child_service.get_child_by_parent(parent.id)


@_child.get('/{child_id}')
async def get_child_by_id(child_id: int,
                        child_service: ChildService = Depends(get_child_service),
                        user: User = Depends(get_current_user_is_doctor)):
    return await child_service.get_child_by_id(child_id)


@_child.put('/{child_id}/add/img')
async def child_upload_img(child_id: int,
                           img: UploadFile = File(...), 
                           child_service: ChildService = Depends(get_child_service),
                           parent_service: ParentService = Depends(get_parent_service),
                           user: User = Depends(get_current_user)):
    parent = await parent_service.get_parent_by_user(user.id)
    await child_service.upload_img(child_id, img, parent.id, user)
    return {'message': 'Success'}


@_child.delete('/{child_id}/delete')
async def delete_child(child_id: int, 
                       child_service: ChildService = Depends(get_child_service),
                       parent_service: ParentService = Depends(get_parent_service),
                       user: User = Depends(get_current_user)):
    parent = await parent_service.get_parent_by_user(user.id)
    await child_service.delete_child(child_id, parent.id)
    return {'message': 'Success'}



@_child.put('/{child_id}/add/medcard')
async def add_medcard(child_id: int, data: AddMedcardScheme,
                       child_service: ChildService = Depends(get_child_service),
                       user: User = Depends(get_current_user_is_doctor)):
    
    await child_service.add_medcard(child_id=child_id, medcard_id=data.medcard_id)
    return {'message': 'Success'}