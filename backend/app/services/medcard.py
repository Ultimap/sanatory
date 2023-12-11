from fastapi import HTTPException
from app.repositories.medcard import MedcardRepository
from app.schemas.medcard import MedcardScheme
class MedcardService:

    def __init__(self, repository: MedcardRepository) -> None:
        self._repository = repository

    async def get_all_medcard(self):
        medcard = await self._repository.get_all_medcard()
        if not medcard:
            raise HTTPException(status_code=404)
        return medcard
    
    async def get_medcard_by_id(self, medcard_id: int):
        medcard = await self._repository.get_medcard_by_id(medcard_id)
        if not medcard:
            raise HTTPException(status_code=404)
        return medcard
    
    async def create_medcard(self, data: MedcardScheme):
        medcrad = await self._repository.create_medcard(data.__dict__)
        if not medcrad:
            raise HTTPException(status_code=400, detail='create medcard is falled')
        return medcrad