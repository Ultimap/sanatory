from fastapi import HTTPException
from passlib.hash import pbkdf2_sha512
from datetime import datetime, timedelta
import jwt
from app.repositories.user import UserRepositories
from app.models.models import User
from app.schemas.user import UserScheme, UserLogin


class UserService:

    def __init__(self, repository: UserRepositories, expirate_time: timedelta, 
                 alghorithm: str, secret_key: str) -> None:
        self._repository = repository
        self.__EXPIRATE_TIME = expirate_time
        self.__ALGHORITM = alghorithm
        self.__SECRET_KEY = secret_key


    async def get_user_by_id(self, user_id: int) -> User:
        user = await self._repository.get_user_by_id(user_id)
        return user
    
    async def create_user(self, data: UserScheme) -> User | None:
        data.password = pbkdf2_sha512.hash(data.password)
        data = data.__dict__
        if not data['role_id']:
            data['role_id'] = 2
        user = await self._repository.create_user(data)
        if not user:
            raise HTTPException(status_code=400, detail='registration is falled')
        return user
    
    async def _get_user_by_username(self, username: str) -> User:
        user = await self._repository.get_user_by_username(username)
        return user

    async def _verify_password(self, password: str, hash_password: str) -> bool:
        return pbkdf2_sha512.verify(password, hash_password)

    async def _generate_jwt_token(self, data: dict) -> str:
        expirate = datetime.utcnow() + self.__EXPIRATE_TIME
        data.update({'exp': expirate})
        token = jwt.encode(data, self.__SECRET_KEY, algorithm=self.__ALGHORITM)
        return token

    async def login(self, data: UserLogin):
        user = await self._repository.get_user_by_username(data.username)
        if not user or not await self._verify_password(data.password, user.password): 
            raise HTTPException(status_code=400, detail='invalid password or username')
        token = await self._generate_jwt_token({'sub': data.username})
        return token
    
    async def _verify_token(self, token: str) -> dict:
        try:
            decode_data = jwt.decode(token, self.__SECRET_KEY, algorithms=[self.__ALGHORITM])
            return decode_data
        except jwt.PyJWTError:
            return None
        
    async def get_current_user(self, token: str) -> User:
        decode_data = await self._verify_token(token)
        if not decode_data:
            raise HTTPException(status_code=400, detail='invalid token')
        user = await self._get_user_by_username(decode_data.get('sub'))
        if not user:
            raise HTTPException(status_code=404, detail='user not found')
        return user
    
    async def get_current_user_is_admin(self, token: str) -> User | bool:
        user = await self.get_current_user(token)
        if user.role_id == 1:
            return user
        return False


    async def get_current_user_is_doctor(self, token: str) -> User | bool:
        user = await self.get_current_user(token)
        if user.role_id == 2:
            return user
        return False
