from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing import Optional, List
from sqlalchemy import String, JSON
from sqlalchemy.dialects.postgresql import ARRAY

engine = create_async_engine(
    "sqlite+aiosqlite:///candidates.db"
)

new_session = async_sessionmaker(engine, expire_on_commit=False)

class Model(DeclarativeBase):
    pass

class CandidateOrm(Model):
    __tablename__ = "candidates"

    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str]
    link: Mapped[str]
    check_list: Mapped[str]
    notes: Mapped[str]



async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)

async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)
