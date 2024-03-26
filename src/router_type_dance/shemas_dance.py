from enum import Enum
from typing import Optional

from pydantic import ConfigDict
from database import Shemas

class TypeBallet(Shemas):
    name: str

class ReturnType(TypeBallet):
    id: int
    model_config = ConfigDict(from_attributes=True)

