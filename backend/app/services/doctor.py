from fastapi import HTTPException
from app.repositories.doctor import DoctorRepository
from app.schemas.doctor import DoctorScheme

class DoctorService:

    def __init__(self, repository: DoctorRepository) -> None:
        self._repository = repository

    async def create_doctor(self, data: DoctorScheme):
        doctor = await self._repository.create_doctor(data.__dict__)
        if not doctor:
            raise HTTPException(status_code=400)
        return doctor
    
