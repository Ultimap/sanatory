from pydantic import BaseModel

class ParentScheme(BaseModel):
    FML: str
    contact: str
    user_id: int