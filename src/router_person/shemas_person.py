from enum import Enum
from typing import Optional

from fastapi import File, UploadFile
from pydantic import ConfigDict

from database import Shemas
from models import Rank



class PersonShemas(Shemas):
    lastname: str
    collective_id: int
    photo: Optional[str] = None
    town: str
    rank: Rank
    scores: Optional[int] = 0

class ReturnPerson(PersonShemas):
    id: int
    model_config = ConfigDict(from_attributes=True)