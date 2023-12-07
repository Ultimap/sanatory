from pydantic import BaseModel
from typing import Optional

class UserScheme(BaseModel):
    username: str
    password: str
    role_id: Optional[int] = None

class UserLogin(BaseModel):
    username: str
    password: str
    
class DoctorRigisterScheme(BaseModel):
    first_name: str
    midle_name: str
    last_name: str
    experience: int
    specialization_id: int 