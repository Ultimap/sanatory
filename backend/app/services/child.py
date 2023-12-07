from fastapi import HTTPException
from app.repositories.child import ChildRepository

class ChildService:

    def __init__(self, repository: ChildRepository) -> None:
        self._repository = repository

    async def get_all_child(self):
        return await self._repository.get_all_child()
    
    async def get_child_by_id(self, child_id: int):
        child = await self._repository.get_child_by_id(child_id)
        if not child:
            raise HTTPException(status_code=404)
        return child
    