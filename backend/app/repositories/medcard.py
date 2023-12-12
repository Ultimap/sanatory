from sqlalchemy import select 
from typing import List
from app.config import async_session
from app.models.models import Medcard, MedcardEntries

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
        
    async def create_medcard_entries(self, data: dict) -> MedcardEntries:
        async with async_session() as session:
            try:
                medcard = MedcardEntries(**data)
                session.add(medcard)
                await session.commit()
                return medcard
            except:
                return None
            
    async def get_all_medcard_entries(self) -> List[MedcardEntries]:
        async with async_session() as session:
            entries = await session.execute(select(MedcardEntries))
            return entries
    
    async def get_medcard_entries_by_id(self, entries_id: int) -> MedcardEntries:
        async with async_session() as session:
            entries = await session.execute(select(MedcardEntries).wher(MedcardEntries.id ==entries_id))
            return entries.scalar_one_or_none()
        
    async def get_medcard_entries_by_medcard_id(self, medcard_id: int) -> List[MedcardEntries]:
        async with async_session() as session:
            entries = await session.execute(select(MedcardEntries).where(MedcardEntries.medcard_id == medcard_id))
            return entries.scalars().all()
        
    async def delete_medcard(self, medcard: Medcard) -> bool:
        async with async_session() as session:
            try:
                await session.delete(medcard)
                await session.commit()
                return True
            except:
                return None