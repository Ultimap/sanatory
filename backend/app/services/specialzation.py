from fastapi import HTTPException
from app.repositories.specialization import SpecializationRepository
from app.schemas.specialication import SpecializationScheme

class SpecializationService:

    def __init__(self, repository: SpecializationRepository) -> None:
        self._repository = repository

    async def create_specialization(self, data: SpecializationScheme):
        specialization = await self._repository.create_specialization(data.__dict__)
        if not specialization:
            raise HTTPException(status_code=400, detail='create specialization is falled')
        return specialization
    
    async def get_all_specialization(self):
        specialization = await self._repository.get_all_specialization()
        if not specialization:
            raise HTTPException(status_code=404)
        return specialization
    
    async def get_specialization_by_id(self, specialization_id: int):
        specialization = await self._repository.get_specialization_by_id(specialization_id)
        if not specialization:
            raise HTTPException(status_code=404)
        return specialization
    
    async def delete_specialization(self, specialization_id: int):
        specialization = await self._repository.get_specialization_by_id(specialization_id)
        if not specialization:
            raise HTTPException(status_code=404)
        resul = await self._repository.delete_specialization(specialization)
        if not resul:
            raise HTTPException(status_code=409, detail='specialization connot be deleted')