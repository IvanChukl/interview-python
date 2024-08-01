from pydantic import BaseModel, ConfigDict
from typing import Optional, List

class SCandidateAdd(BaseModel):
    full_name: str
    link: str
    check_list: str
    notes: str

class SCandidate(SCandidateAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)

class SInterviewedCandidateAdd(BaseModel):
    full_name: str
    checklist_comments: dict
    interior_rating: int
    result_score: int
    grade: str
    review: str
    is_recommend: bool
    notes: str
    result_for_block: list

class SInterviewedCandidate(SInterviewedCandidateAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)