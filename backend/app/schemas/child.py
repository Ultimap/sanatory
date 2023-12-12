from pydantic import BaseModel
from typing import Optional


class ChildScheme(BaseModel):
    FML: str
    parent_id: int
    medcard_id: Optional[int] = None


class ChildRegisterScheme(BaseModel):
    first_name: str
    midle_name: str
    last_name: str
    medcard_id: Optional[int] = None


class AddMedcardScheme(BaseModel):
    medcard_id: int