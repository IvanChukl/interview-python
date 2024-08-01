from typing import Optional
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, Boolean, JSON

engine = create_async_engine(
    "sqlite+aiosqlite:///interviewed_candidates.db"
)

interviewed_candidates_session = async_sessionmaker(engine, expire_on_commit=False)


class Model(DeclarativeBase):
    pass

class InterviewedCandidateOrm(Model):
    __tablename__ = "interviewed_candidates"

    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(String)
    checklist_comments: Mapped[Optional[dict]] = mapped_column(JSON)
    interior_rating: Mapped[int]= mapped_column(Integer)
    result_score: Mapped[int] = mapped_column(Integer)
    grade: Mapped[str] = mapped_column(String)
    review: Mapped[str] = mapped_column(String)
    is_recommend: Mapped[bool] = mapped_column(Boolean)
    notes: Mapped[Optional[str]] = mapped_column(String)
    result_for_block: Mapped[list] = mapped_column(JSON)

async def interviewed_create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)

async def interviewed_delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)
