from fastapi import FastAPI,Depends
from pydantic import BaseModel
from typing import Optional, Annotated
from contextlib import asynccontextmanager
from datebase import create_tables, delete_tables
from schemas import SCandidateAdd
from router import router as tasks_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    await create_tables()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)