from sqlalchemy import select
from app.config import async_session
from app.models.models import Specialization

class SpecializationRepository:

    async def create_specialization(self, data: dict) -> Specialization | None:
        async with async_session() as session:
            try:
                specialization = Specialization(**data)
                session.add(specialization)
                await session.commit()
                return specialization
            except:
                return None