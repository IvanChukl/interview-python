from datebase import new_session, CandidateOrm
from main import SCandidateAdd
from sqlalchemy import select


class CandidateRepository:
    @classmethod
    async def add_one(cls, data: SCandidateAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()

            candidate = CandidateOrm(**task_dict)
            session.add(candidate)
            await session.flush()
            await session.commit()
            return candidate

    @classmethod
    async def find_all(cls):
        async with new_session() as session:
            query = select(CandidateOrm)
            result = await session.execute(query)
            task_modules = result.scalars().all()
            return task_modules

    @classmethod
    async def find_one(cls, task_id: int):
        async with new_session() as session:
            query = select(CandidateOrm).where(CandidateOrm.id == task_id)
            result = await session.execute(query)
            task = result.scalars().first()
            return task

