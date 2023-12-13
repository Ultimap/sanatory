from fastapi import HTTPException, UploadFile
from app.models.models import User
from app.repositories.child import ChildRepository
from app.schemas.child import ChildScheme
from app.util.file import add_img
class ChildService:

    def __init__(self, repository: ChildRepository) -> None:
        self._repository = repository

    async def get_all_child(self):
        child = await self._repository.get_all_child()
        if not child:
            raise HTTPException(status_code=404)
        return child
    
    async def get_child_by_id(self, child_id: int):
        child = await self._repository.get_child_by_id(child_id)
        if not child:
            raise HTTPException(status_code=404)
        return child
    
    async def create_child(self, data: ChildScheme):
        data = data.__dict__
        if not data['medcard_id']:
            del data['medcard_id']
        child = await self._repository.create_child(data)
        if not child:
            raise HTTPException(status_code=400, detail='add child is falled')
        return child
    
    async def get_child_by_parent(self, parent_id: int):
        child = await self._repository.get_child_by_parent(parent_id)
        if not child:
            raise HTTPException(status_code=404)
        return child
    
    async def upload_img(self, child_id: int, img: UploadFile, parent_id: int, user: User):
        child = await self.get_child_by_id(child_id)
        if user.role_id != 1:
            if child.parent_id != parent_id:
                raise HTTPException(status_code=403)
        resul = await self._repository.upload_img(child_id, img.filename)
        if not resul:
            raise HTTPException(status_code=400, detail='upload img if falled')
        await add_img(img)
    
    async def delete_child(self, child_id: int, parent_id: int):
        child = await self._repository.get_child_by_id(child_id)
        if child.parent_id != parent_id:
            raise HTTPException(status_code=403)
        result = await self._repository.delete_child(child)
        if not result:
            raise HTTPException(status_code=409, detail='remove child is falled')
        
    async def add_medcard(self, child_id: int, medcard_id: int):
        child = await self.get_child_by_id(child_id)
        result = await self._repository.add_medcard(child_id, medcard_id)
        if not result:
            raise HTTPException(status_code=400, detail='add medcard for child is falled')
        
    async def get_child_by_FML(self, FML: str):
        child = await self._repository.get_child_by_FML(FML)
        if not child:
            raise HTTPException(status_code=404)
        return child
    