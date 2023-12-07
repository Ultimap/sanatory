from sqlalchemy import select, update
from typing import List
from app.models.models import Child
from app.config import async_session

class ChildRepository:

    async def get_child_by_id(self, child_id) -> Child:
        async with async_session() as session:
            doctor = await session.execute(select(Child).where(Child.id == child_id))
            return doctor.scalar_one_or_none()
        
    async def get_all_child(self) -> List[Child]:
        async with async_session() as session:
            doctor = await session.execute(select(Child))
            return doctor.scalars().all()