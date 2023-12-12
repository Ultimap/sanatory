from fastapi import APIRouter, Depends
from app.services.medcard import MedcardService
from app.depends import get_medcard_service, get_child_service, get_current_user_is_doctor
from app.schemas.medcard import CreateMedcardScheme, MedcardScheme, MedcardEntriesScheme, CreateMedcardEntriesScheme
from app.services.child import ChildService
from app.models.models import User

_medcard = APIRouter(prefix='/api/medcard', tags=['Medcard'])


@_medcard.post('/create', status_code=201)
async def create_medcard(data: CreateMedcardScheme, 
                         medcard_service: MedcardService = Depends(get_medcard_service),
                         child_service: ChildService = Depends(get_child_service),
                         user: User = Depends(get_current_user_is_doctor)
                         ):
    if data.child_id:
        child = await child_service.get_child_by_id(data.child_id)
    else:
        FML = f"{data.first_name} {data.midle_name} {data.last_name}"
        child = await child_service.get_child_by_FML(FML)
    medcard = await medcard_service.create_medcard(MedcardScheme(unique_key=data.unique_key))
    await child_service.add_medcard(child_id=child.id, medcard_id=medcard.id)
    return {'message': 'Success'}


@_medcard.post('/{medcard_id}/add/entries')
async def create_medcard_entries(medcard_id: int, data: CreateMedcardEntriesScheme,
                                 medcard_service: MedcardService = Depends(get_medcard_service),
                                 user: User = Depends(get_current_user_is_doctor)):
    await medcard_service.create_medcard_entries(MedcardEntriesScheme(medcard_id=medcard_id, **data.__dict__))
    return {'message': 'Success'}


@_medcard.get('/')
async def get_all_medcard(medcard_service: MedcardService = Depends(get_medcard_service),
                          user: User = Depends(get_current_user_is_doctor)):
    return await medcard_service.get_all_medcard()


@_medcard.get('/{medcard_id}')
async def get_all_medcard(medcard_id: int,
                          medcard_service: MedcardService = Depends(get_medcard_service),
                          user: User = Depends(get_current_user_is_doctor)):
    return await medcard_service.get_medcard_by_id(medcard_id)


@_medcard.delete('/{medcard_id}/delete')
async def delete_medcard(medcard_id: int,
                         medcard_service: MedcardService = Depends(get_medcard_service),
                         user: User = Depends(get_current_user_is_doctor)):
    await medcard_service.delete_medcard(medcard_id)
    return {'message': 'Success'}

