from pydantic import BaseModel
from fastapi import UploadFile


class DoctorScheme(BaseModel):
    FML: str
    experience: int
    specialization_id: int
    user_id: int


    
    
  