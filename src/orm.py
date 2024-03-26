from sqlalchemy import insert, text, select
from sqlalchemy.orm import joinedload, relationship

from database import sync_engine, async_engine, sync_session, async_session, Base
from models import Coach, Collective, Person, TypeDance

def sync_create_tables():
    sync_engine.echo = True
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)


async def async_create_tables():
        async with async_engine.begin() as conn:
            # await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

async def async_dalete_tables():
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)


async def return_one_object(models, id:int):
    async with async_session() as session:
        query = select(models).filter_by(id=id)
        result = await session.execute(query)
        result = result.scalar_one()
        return result
    
async def view_all():
    async with async_session() as session:
        # qery =  await session.query(TypeDance, Coach, Collective, Person).\
        # join(Coach, TypeDance.id == Coach.type_dance).\
        # join(Collective, Coach.id == Collective.name_coach).\
        # join(Person, Collective.id == Person.collective_id).\
        # options(joinedload(TypeDance.coach), joinedload(Coach.collective), joinedload(Collective.person))
        # results = query.all()
        query = (
        select(
            TypeDance.name.label('Type_Dance'),
            Coach.name.label('Coach'),
            Collective.name.label('Collective'),
            Person.lastname.label('Person_lastname'),
            Person.photo.label('Person_photo'),
            Person.town.label('Person_town'),
            Person.rank.label('Person_rank'),
            Person.scores.label('Person_scores')
        )
        .select_from(TypeDance)
        .join(Coach, TypeDance.id == Coach.type_dance)
        .join(Collective, Coach.id == Collective.name_coach)
        .join(Person, Collective.id == Person.collective_id)
            )
        rows = await session.execute(query)
        return rows.all()
