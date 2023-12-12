from pydantic import BaseModel
from typing import Optional


class MedcardScheme(BaseModel):
    unique_key: str


class CreateMedcardScheme(MedcardScheme):
    first_name: str
    midle_name: str
    last_name: str
    child_id: Optional[int] = None


class CreateMedcardEntriesScheme(BaseModel):
    title: str
    description: str


class MedcardEntriesScheme(CreateMedcardEntriesScheme):
    medcard_id: int
    