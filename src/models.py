from enum import Enum
from typing import Annotated, Optional
from sqlalchemy import ForeignKey
from database import Base
from sqlalchemy.orm import mapped_column, Mapped

intpk = Annotated[int, mapped_column(primary_key=True)]

class TypeDance(Base):
    __tablename__='type_dancing'

    id: Mapped[intpk]
    name: Mapped[str]

class Coach(Base):
    __tablename__='coach'

    id: Mapped[intpk]
    name: Mapped[str]
    type_dance: Mapped[int] = mapped_column(ForeignKey('type_dancing.id', ondelete='CASCADE'))


class Collective(Base):
    __tablename__ = 'collective'
    
    id: Mapped[intpk]
    name: Mapped[str]
    name_coach: Mapped[int]= mapped_column(ForeignKey('coach.id', ondelete='CASCADE'))
    founded: Mapped[int]

class Rank(Enum):
    E ='E'
    D ='D'
    C ='C'
    B ='B'
    A ='A'
    S ='S'
    M ='М'

class Person(Base):
    __tablename__ = 'person'

    id: Mapped[intpk]
    lastname: Mapped[str]
    collective_id: Mapped[int]= mapped_column(ForeignKey('collective.id', ondelete='CASCADE'))
    photo: Mapped[str]
    town: Mapped[str]
    rank: Mapped[Rank] 
    scores: Mapped[Optional[int]]

