from fastapi import HTTPException, UploadFile
from app.repositories.doctor import DoctorRepository
from app.schemas.doctor import DoctorScheme, DoctorScheme
from app.util.file import add_img
class DoctorService:

    def __init__(self, repository: DoctorRepository) -> None:
        self._repository = repository

    async def create_doctor(self, data: DoctorScheme):
        doctor = await self._repository.create_doctor(data.__dict__)
        if not doctor:
            raise HTTPException(status_code=400, detail='create doctor is falled')
        return doctor
    
    async def get_doctor_by_id(self, doctor_id: int):
        doctor = await self._repository.get_doctor_by_id(doctor_id)
        if not doctor:
            raise HTTPException(status_code=404)
        data = {
            'id': doctor.id,
            'FML': doctor.FML,
            'img': doctor.img,
            'spacialization': doctor.specialization_id
        }
        return data
    
    async def get_all_doctor(self):
        doctors = await self._repository.get_all_doctor()
        if not doctors:
            raise HTTPException(status_code=404)
        data = []
        for doctor in doctors:
            data.append(
                {
                    'id': doctor.id,
                    'FML': doctor.FML,
                    'img': doctor.img,
                    'spacialization': doctor.specialization_id
                }
            )
        return data
    
    async def upload_img(self, doctor_id: int, img: UploadFile):
        if not await self._repository.upload_img(doctor_id, img.filename):
            raise HTTPException(status_code=400, detail='upload img is faled')
        await add_img(img)

    async def get_doctor_by_user(self, user_id: int):
        doctor = await self._repository.get_parent_by_user(user_id)
        if not doctor:
            raise HTTPException(status_code=404)
        return doctor
    
    async def delete_doctor(self, doctor_id: int):
        doctor = await self._repository.get_doctor_by_id(doctor_id)
        if not doctor:
            raise HTTPException(status_code=404)
        result = await self._repository.delete_doctor(doctor)
        if not result:
            raise HTTPException(status_code=409, detail='remove doctor is falled')