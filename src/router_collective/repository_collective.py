from sqlalchemy import delete, insert, select, update
from orm import return_one_object
from router_collective.shemas_collective import CollectiveReturn, CollectiveShemas
from database import async_session
from models import Collective



class RepositoryCollective:
    @classmethod
    async def add_collective(cls, data: CollectiveShemas)->CollectiveReturn:
        async with async_session() as session:
            add_collective = data.model_dump()
            add_collective = Collective(**add_collective)
            session.add(add_collective)
            await session.commit()
            await session.refresh(add_collective)
            return await return_one_object(Collective, add_collective.id)

    @classmethod
    async def get_one_collective(cls, id:int) -> CollectiveReturn:
        async with async_session() as session:
            query = select(Collective).filter_by(id=id)
            result = await session.execute(query)
            result = result.scalar_one()
            return result
        
    @classmethod
    async def get_all_collective(cls) -> list[CollectiveReturn]:
        async with async_session() as session:
            query = select(Collective)
            result = await session.execute(query)
            result = result.scalars().all()
            result = [CollectiveReturn.model_validate(coll) for coll in result]
            return result
        
    @classmethod
    async def update_collective(cls, data: CollectiveReturn) -> CollectiveReturn:
        async with async_session() as session:
            stmt = update(Collective).filter_by(id=data.id).values(
                name=data.name, name_coach=data.name_coach, founded=data.founded
                )
            await session.execute(stmt)
            query = select(Collective).filter_by(id=data.id)
            result = await session.execute(query)
            return await return_one_object(Collective, data.id)
            
        
    @classmethod
    async def delete_collective(cls, id:int) -> CollectiveReturn:
        async with async_session() as session:
            delte_coll = await session.get(Collective, id)
            await session.delete(delte_coll)
            await session.commit()
            # stmt = delete(Collective).filter_by(id=id)
            # await session.execute(stmt)
            return await return_one_object(Collective, id)
