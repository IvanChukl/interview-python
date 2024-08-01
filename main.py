from fastapi import FastAPI,Depends
from pydantic import BaseModel
from typing import Optional, Annotated
from contextlib import asynccontextmanager
from datebase import create_tables, delete_tables
from datebases.interviewed_candidate import interviewed_create_tables, interviewed_delete_tables
from schemas import SCandidateAdd
from router import new_candidate_router as new_candidate_router
from router import interviewed_candidate as interviewed_candidate
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    await interviewed_delete_tables()
    await interviewed_create_tables()
    await create_tables()
    yield


app = FastAPI(lifespan=lifespan)

allowed_origins = [
    "http://localhost",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(new_candidate_router)
app.include_router(interviewed_candidate)