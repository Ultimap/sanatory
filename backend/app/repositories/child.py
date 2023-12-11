from sqlalchemy import select, update
from typing import List
from app.models.models import Child
from app.config import async_session

class ChildRepository:

    async def get_child_by_id(self, child_id) -> Child | None:
        async with async_session() as session:
            child = await session.execute(select(Child).where(Child.id == child_id))
            return child.scalar_one_or_none()
        
    async def get_all_child(self) -> List[Child]:
        async with async_session() as session:
            child = await session.execute(select(Child))
            return child.scalars().all()
        
    async def create_child(self, data: dict) -> Child | None: 
        async with async_session() as session:
            try:
                child = Child(**data)
                session.add(child)
                await session.commit()
                return child
            except:
                return None
            
    async def get_child_by_parent(self, parent_id: int) -> List[Child]:
        async with async_session() as session:
            child = await session.execute(select(Child).where(Child.parent_id == parent_id))
            return child.scalars().all()
        
    async def upload_img(self, child_id: int, filename: str) -> bool:
        async with async_session() as session:
            try: 
                await session.execute(update(Child).values(img=filename).where(Child.id == child_id))
                await session.commit()
                return True
            except:
                return None
            
    async def delete_child(self, child: Child) -> bool:
        async with async_session() as session:
            try:
                await session.delete(child)
                await session.commit()
                return True
            except:
                return None
            
    async def add_medcard(self, child_id: int, medcard_id: int):
        async with async_session() as session:
            try: 
                await session.execute(update(Child).values(medcard_id=medcard_id).where(Child.id == child_id))
                await session.commit()
                return True
            except:
                return None
            
    async def get_child_by_FML(self, FML: str) -> Child:
        async with async_session() as session:
            child = await session.execute(select(Child).where(Child.FML == FML))
            return child.scalar_one_or_none()