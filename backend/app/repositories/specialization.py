from sqlalchemy import select
from typing import List
from app.config import async_session
from app.models.models import Specialization

class SpecializationRepository:

    async def create_specialization(self, data: dict) -> Specialization | None:
        async with async_session() as session:
            try:
                specialization = Specialization(**data)
                session.add(specialization)
                await session.commit()
                return specialization
            except:
                return None
            
    async def get_all_specialization(self) -> List[Specialization]:
        async with async_session() as session:
            try:
                specialization = await session.execute(select(Specialization))
                return specialization.scalars().all()
            except:
                return None
            
    async def get_specialization_by_id(self, specialization_id: int) -> Specialization:
        async with async_session() as session:
            try:
                specialization = specialization = await session.execute(select(Specialization).where(Specialization.id == specialization_id))
                return specialization.scalar_one_or_none()
            except:
                return None
            
    async def delete_specialization(self, specialization: Specialization) -> bool:
        async with async_session() as session:
            try:
                await session.delete(specialization)
                await session.commit()
                return True
            except:
                return False