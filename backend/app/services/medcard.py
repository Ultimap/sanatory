from fastapi import HTTPException
from app.repositories.medcard import MedcardRepository
from app.schemas.medcard import MedcardScheme, MedcardEntriesScheme
class MedcardService:

    def __init__(self, repository: MedcardRepository) -> None:
        self._repository = repository

    async def get_all_medcard(self):
        medcard = await self._repository.get_all_medcard()
        if not medcard:
            raise HTTPException(status_code=404)
        data = []
        for x in medcard:
            data.append({
                'medcard': x,
                'entries': await self._repository.get_medcard_entries_by_medcard_id(x.id)
            })
        return data
    
    async def get_medcard_by_id(self, medcard_id: int):
        medcard = await self._repository.get_medcard_by_id(medcard_id)
        if not medcard:
            raise HTTPException(status_code=404)
        entries = await self._repository.get_medcard_entries_by_medcard_id(medcard_id=medcard.id)
        data = {
            'medcard': medcard,
            'entries': entries
        }
        return data
    
    async def create_medcard(self, data: MedcardScheme):
        medcrad = await self._repository.create_medcard(data.__dict__)
        if not medcrad:
            raise HTTPException(status_code=400, detail='create medcard is falled')
        return medcrad
    
    async def create_medcard_entries(self, data: MedcardEntriesScheme):
        entries = await self._repository.create_medcard_entries(data.__dict__)
        if not entries:
            raise HTTPException(status_code=400, detail='create entries is falled')
        return entries
    
    async def delete_medcard(self, medcard_id: int):
        medcard = await self._repository.get_medcard_by_id(medcard_id)
        if not medcard:
            raise HTTPException(status_code=404)
        result = await self._repository.delete_medcard(medcard)
        if not result:
            raise HTTPException(status_code=409, detail='remove medcard is falled')