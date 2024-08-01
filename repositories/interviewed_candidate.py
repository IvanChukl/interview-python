from schemas import SInterviewedCandidateAdd
from datebases.interviewed_candidate import interviewed_candidates_session, InterviewedCandidateOrm
from sqlalchemy import select

class InterviewedCandidateRepository:
    @classmethod
    async def add_one(cls, data: SInterviewedCandidateAdd) -> InterviewedCandidateOrm:
        async with interviewed_candidates_session() as session:
            task_dict = data.model_dump()

            candidate = InterviewedCandidateOrm(**task_dict)
            session.add(candidate)
            await session.flush()
            await session.commit()
            return candidate

    @classmethod
    async def find_all(cls):
        async with interviewed_candidates_session() as session:
            query = select(InterviewedCandidateOrm)
            result = await session.execute(query)
            task_modules = result.scalars().all()
            return task_modules

    @classmethod
    async def find_one(cls, task_id: int):
        async with interviewed_candidates_session() as session:
            query = select(InterviewedCandidateOrm).where(InterviewedCandidateOrm.id == task_id)
            result = await session.execute(query)
            task = result.scalars().first()
            return task
