from sqlalchemy import select

from database import async_engine, async_session, Base
from models import Coach, Collective, Person, Rank, TypeDance

# def sync_create_tables():
#     sync_engine.echo = True
#     Base.metadata.drop_all(sync_engine)
#     Base.metadata.create_all(sync_engine)


async def async_create_tables():
        async with async_engine.begin() as conn:
            # await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

async def async_dalete_tables():
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)

async def insert_data():
     async with async_session() as session:
        #   type_dance = [
        #        {'name': 'Классический балет'},
        #        {'name': 'Современный балет'}
        #   ]
        #   stmt = insert(TypeDance).values(type_dance)

        type_dance1 = TypeDance(name='Классический балет') # id:1
        type_dance2 = TypeDance(name='Современный балет') # id:2

        coach1 = Coach(name='Иван Иванов Иванович', type_dance=1) # id:1
        coach2 = Coach(name='Гарик Гариков Гарикович', type_dance=2) # id:2

        collective1 = Collective(name='Очень классные ребята', name_coach=1, founded=2001)
        collective2 = Collective(name='Не очень классные ребята', name_coach=2, founded=2074)

        person1 = Person(lastname='Никифоров', collective_id=1, 
                        photo=r'C:\Users\nicki\Desktop\VanyaProject\coach_pictures\9.jpg', 
                        town='Псков', rank=Rank.M, scores=100)
        person2 = Person(lastname='Попов', collective_id=2,
                        photo=r'C:\Users\nicki\Desktop\VanyaProject\coach_pictures\scale_1200.jpg',
                        town='Солярка', rank=Rank.E, scores=0)
        
        session.add_all([type_dance1, type_dance2])
        await session.commit()
        
        session.add_all([coach1, coach2])
        await session.commit()

        session.add_all([collective1, collective2])
        await session.commit()

        session.add_all([person1, person2])
        await session.commit()
          


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
        .join(Coach, TypeDance.id == Coach.type_dance)
        .join(Collective, Coach.id == Collective.name_coach)
        .join(Person, Collective.id == Person.collective_id)
            )
        rows = await session.execute(query)
        return rows.all()
