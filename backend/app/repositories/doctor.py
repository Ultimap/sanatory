from sqlalchemy import select
from app.models.models import Doctor
from app.config import async_session
from app.schemas.doctor import DoctorScheme

class DoctorRepository:

    async def get_doctor_by_id(self, doctor_id) -> Doctor:
        async with async_session() as session:
            doctor = await session.execute(select(Doctor).where(Doctor.id == doctor_id))
            return doctor.scalar_one_or_none()
        
    async def create_doctor(self, data: dict) -> Doctor:
        async with async_session() as session:
            try:
                doctor = Doctor(**data)
                session.add(doctor)
                await session.commit()
                return doctor
            except:
                return None