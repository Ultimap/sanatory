from fastapi import HTTPException
from app.repositories.parent import ParentRepository
from app.schemas.parent import ParentScheme

class ParentService:

    def __init__(self, repository: ParentRepository) -> None:
        self._repository = repository

    async def create_parent(self, data: ParentScheme):
        parent = await self._repository.create_parent(data.__dict__)
        if not parent:
            raise HTTPException(status_code=400, detail='create parent is falled')
        return parent
    
    async def get_all_parent(self):
        parents = await self._repository.get_all_parent()
        if not parent:
            raise HTTPException(status_code=404)
        data = []
        for parent in parents:
            data.append(
                {
                    'FML': parent.FML,
                    'contact': parent.contact,
                }
            )
        return data

    async def get_parent_by_id(self, parent_id: int):
        parent = await self._repository.get_parent_by_id(parent_id)
        if not parent:
            raise HTTPException(status_code=404)
        return {'FML': parent.FML, 'contact': parent.contact}
    
    async def delete_parent(self, parent_id: int) -> None:
        parent = await self._repository.get_parent_by_id(parent_id)
        if not parent:
            raise HTTPException(status_code=404)
        resul = await self._repository.delete_parent(parent)
        if not resul:
            raise HTTPException(status_code=409, detail='parent cannot be deleted')
        
    async def get_parent_by_user(self, user_id: int):
        parent = await self._repository.get_parent_by_user(user_id)
        if not parent:
            raise HTTPException(status_code=404)
        return parent