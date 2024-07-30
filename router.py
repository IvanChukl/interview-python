from fastapi import APIRouter, Depends, HTTPException
from schemas import SCandidateAdd
from repository import CandidateRepository
from typing import Optional, Annotated

router = APIRouter(
    prefix="/candidate"
)


@router.post("", tags=["New candidates"])
async def add_candidate(
 candidate: Annotated[SCandidateAdd, Depends()],
):
    candidate_id = await CandidateRepository.add_one(task)
    return {"ok": True, "candidate_id": candidate_id}


@router.get("/list",tags=["New candidates"])
async def get_candidates():
    candidates = await CandidateRepository.find_all()

    return {
        "candidates": candidates
    }

@router.get("/{candidate_id}",tags=["New candidates"])
async def get_candidate(task_id: int):
    candidate = await CandidateRepository.find_one(task_id)
    if candidate is None:
        raise HTTPException(status_code=404, detail="Candidate not found")
    return {"candidate": candidate}

