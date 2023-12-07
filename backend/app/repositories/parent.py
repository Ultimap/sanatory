from sqlalchemy import select
from typing import List
from app.models.models import Parent
from app.config import async_session

class ParentRepository:

    async def create_parent(self, data: dict) -> Parent | None:
        async with async_session() as session:
            try:
                parent = Parent(**data)
                session.add(parent)
                await session.commit()
                return parent
            except:
                return None
            
    async def get_all_parent(self) -> List[Parent] | None:
        async with async_session() as session:
            try:
                parent = await session.execute(select(Parent))
                return parent.scalars().all()
            except:
                return None
            
    async def get_parent_by_id(self, parent_id: int) -> Parent | None:
        async with async_session() as session:
            try:
                parent = await session.execute(select(Parent).where(Parent.id == parent_id))
                return parent.scalar_one_or_none()
            except:
                return None
            
    async def delete_parent(self, parent: Parent) -> bool:
        async with async_session() as session:
            try:
                await session.delete(parent)
                await session.commit()
                return True
            except:
                return False
            
    async def get_parent_by_user(self, user_id: int) -> Parent:
        async with async_session() as session:
            try:
                parent = await session.execute(select(Parent).where(Parent.user_id == user_id))
                return parent.scalar_one_or_none()
            except:
                return None