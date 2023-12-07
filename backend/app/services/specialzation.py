from fastapi import HTTPException
from app.repositories.specialization import SpecializationRepository
from app.schemas.specialication import SpecializationScheme

class SpecializationService:

    def __init__(self, repository: SpecializationRepository) -> None:
        self._repository = repository

    async def create_specialization(self, data: SpecializationScheme):
        specialization = await self._repository.create_specialization(data.__dict__)
        if not specialization:
            raise HTTPException(status_code=400, detail='create is falled')
        return specialization
    
