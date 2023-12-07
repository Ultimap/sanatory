from sqlalchemy import select, update
from typing import List
from app.models.models import Doctor
from app.config import async_session

class DoctorRepository:

    async def get_doctor_by_id(self, doctor_id) -> Doctor:
        async with async_session() as session:
            doctor = await session.execute(select(Doctor).where(Doctor.id == doctor_id))
            return doctor.scalar_one_or_none()
        
    async def get_all_doctor(self) -> List[Doctor]:
        async with async_session() as session:
            doctor = await session.execute(select(Doctor))
            return doctor.scalars().all()

    async def create_doctor(self, data: dict) -> Doctor:
        async with async_session() as session:
            try:
                doctor = Doctor(**data)
                session.add(doctor)
                await session.commit()
                return doctor
            except:
                return None
        
    async def doctor_update_img_by_FML(self, FML: str, filename: str) -> bool | None:
        async with async_session() as session:
            try: 
                await session.execute(update(Doctor).values(img=filename).where(Doctor.FML == FML))
                await session.commit()
                return True
            except:
                return None

    async def get_doctor_by_user(self, user_id: int) -> Doctor:
        async with async_session() as session:
            try:
                doctor = await session.execute(select(Doctor).where(Doctor.user_id == user_id))
                return doctor.scalar_one_or_none()
            except:
                return None