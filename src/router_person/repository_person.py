from sqlalchemy import insert, select, update
from database import async_session
from models import Person
from router_person.shemas_person import PersonShemas, ReturnPerson
from orm import return_one_object


class RepositoryPerson:



    # @classmethod
    # async def add_person(cls, lastname, collective_id, saved_file_path, town, rank, scores):
    #     async with async_session() as session:
    #         file = Person(lastname, collective_id, saved_file_path, town, rank, scores)
    #         session.add(file)
    #         await session.commit()
    #         return 200
    
    @classmethod
    async def add_person(cls, data: PersonShemas):
        async with async_session() as session:
    #         stmt = insert(Person).values(lastname = data.lastname,
    # collective_id = data.collective_id,
    # photo = data.photo,
    # town = data.town,
    # rank = data.rank,
    # scores = data.scores)
            # await session.execute(stmt)
            # await session.commit()
            add_pers = Person(**data.model_dump())
            session.add(add_pers)
            await session.commit()
            return 200
            # sel = select(Person).filter_by(id=add_pers.id)
            # result = await session.execute(sel)
            # result = result.scalar_one()
            # return result
    

    @classmethod
    async def get_one_person(cls, id: int) -> ReturnPerson:
        async with async_session() as session:
            return await return_one_object(Person, id=id)
            # query = select(Person).filter_by(id=id)
            # result = await session.execute(query)
            # result = result.scalar_one()
            # return result
        
    @classmethod
    async def get_all_person(cls):
        async with async_session() as session:
            get_all = select(Person)
            result = await session.execute(get_all)
            result = result.scalars().all()
            result = [ReturnPerson.model_validate(person) for person in result]
            return result
        
    @classmethod
    async def update_person(cls, data: ReturnPerson):
        async with async_session() as session:
            stmt = update(Person).values(lastname = data.lastname,
    collective_id = data.collective_id,
    photo = data.photo,
    town = data.town,
    rank = data.rank,
    scores = data.scores)
            result = await session.execute(stmt)
            await session.commit()
            return 200
            # query = select(Person).filter_by(id=ReturnPerson.id)
            # result = await session.execute(query)
            # result = result.scalar_one()
            # return result
        
    @classmethod
    async def delete_person(cls, id: int):
        async with async_session() as session:
            # await session.refresh()
            # obj = await return_one_object(Person, id)
            del_person = await session.get(Person, id)
            await session.delete(del_person)
            await session.commit()
            return 200