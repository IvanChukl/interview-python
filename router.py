from fastapi import APIRouter, Depends, HTTPException
from schemas import SCandidateAdd, SInterviewedCandidateAdd
from repository import CandidateRepository
from repositories.interviewed_candidate import InterviewedCandidateRepository
from typing import Optional, Annotated

new_candidate_router = APIRouter(
    prefix="/new_candidate"
)

interviewed_candidate = APIRouter(
    prefix="/interviewed_candidate"
)

@interviewed_candidate.post("", tags=["Interviewed candidate"])
async def add_candidate(
 candidate: SInterviewedCandidateAdd,
):
    candidate = await InterviewedCandidateRepository.add_one(candidate)
    return {"data": candidate}


@interviewed_candidate.get("/list", tags=["Interviewed candidate"])
async def get_candidates():
    candidates = await InterviewedCandidateRepository.find_all()

    return {
        "candidates": candidates
    }    

@new_candidate_router.post("", tags=["New candidates"])
async def add_candidate(
 candidate: SCandidateAdd,
):
    candidate = await CandidateRepository.add_one(candidate)
    return {"data": candidate}



@new_candidate_router.get("/list",tags=["New candidates"])
async def get_candidates():
    candidates = await CandidateRepository.find_all()

    return {
        "candidates": candidates
    }

@new_candidate_router.get("/{candidate_id}",tags=["New candidates"])
async def get_candidate(candidate_id: int):
    candidate = await CandidateRepository.find_one(candidate_id)
    if candidate is None:
        raise HTTPException(status_code=404, detail="Candidate not found")
    return {"candidate": candidate}

