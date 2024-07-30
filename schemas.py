from pydantic import BaseModel
from typing import Optional

class SCandidateAdd(BaseModel):
    full_name: str
    link: str
    check_list: str
    notes: str

class STask(SCandidateAdd):
    id: int