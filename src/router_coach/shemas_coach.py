from pydantic import ConfigDict

from database import Shemas


class CoachShemas(Shemas):
    name: str
    type_dance: int

class CoachReturn(CoachShemas):
    id: int
    model_config = ConfigDict(from_attributes=True)
