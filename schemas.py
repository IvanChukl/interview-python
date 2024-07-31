from pydantic import BaseModel, ConfigDict
from typing import Optional, List

class SCandidateAdd(BaseModel):
    full_name: str
    link: str
    check_list: List[str]
    notes: str

class SCandidate(SCandidateAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)