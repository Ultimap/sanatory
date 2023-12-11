from sqlalchemy import select 
from typing import List
from app.config import async_session
from app.models.models import Medcard

class MedcardRepository:

    async def create_medcard(self, data: dict) -> Medcard | None:
        async with async_session() as session:
            try:
                medcard = Medcard(**data)
                session.add(medcard)
                await session.commit()
                return medcard
            except:
                return None

    async def get_all_medcard(self) -> List[Medcard]:
        async with async_session() as session:
            medcrad = await session.execute(select(Medcard))
            return medcrad.scalars().all()

    async def get_medcard_by_id(self, medcard_id: int) -> Medcard:
        async with async_session() as session:
            medcard = await session.execute(select(Medcard).where(Medcard.id == medcard_id))
            return medcard.scalar_one_or_none()