from pydantic import BaseModel
from typing import Optional


class MedcardScheme(BaseModel):
    unique_key: str


class CreateMedcardScheme(MedcardScheme):
    first_name: Optional[str] = None
    midle_name: Optional[str] = None
    last_name: Optional[str] = None
    child_id: Optional[int] = None


class CreateMedcardEntriesScheme(BaseModel):
    title: str
    description: str


class MedcardEntriesScheme(CreateMedcardEntriesScheme):
    medcard_id: int
    