from pydantic import ConfigDict
from database import Shemas


class CollectiveShemas(Shemas):
    name: str
    name_coach: int
    founded: int

class CollectiveReturn(CollectiveShemas):
    id : int
    model_config = ConfigDict(from_attributes=True)