from sqlalchemy import delete, insert, select
from database import async_session
from models import Coach
from router_coach.shemas_coach import CoachReturn, CoachShemas


class RepositoryCoach:
    @classmethod
    async def add_one_coach(cls, data: CoachShemas):
        async with async_session() as sess:
            query = insert(Coach).values(name=data.name, type_dance=data.type_dance)
            await sess.execute(query)
            await sess.commit()
            # new_coach = data.model_dump()
            # result = Coach(**new_coach)
            # sess.add(new_coach)
            # await sess.commit()
            # await sess.refresh(result)
            # return result.id        


    @classmethod
    async def get_all_coach(cls):
        async with async_session() as sess:
            query = select(Coach)
            result = await sess.execute(query)
            result = result.scalars().all()
            result = [CoachReturn.model_validate(coach) for coach in result]
            return result

    @classmethod
    async def get_one_coach(cls, id:int):
        async with async_session() as sess:
            query = select(Coach).filter_by(id=id)
            result = await sess.execute(query)
            result = result.scalar_one()
            return result
        
        
    @classmethod
    async def update_coach(cls, data: CoachReturn):
        async with async_session() as sess:
            up_coach = await sess.get(Coach, data.id)
            up_coach.name, up_coach.type_dance = data.name, data.type_dance
            await sess.commit()
            await sess.refresh(up_coach)
            return up_coach.id
        
    @classmethod
    async def delete_coach(cls, id: int):
            async with async_session() as session:
                # query = delete(Coach).filter_by(id=id)
                # await session.execute(query)
                # await session.commit()
                del_coach = await session.get(Coach, id)
                await session.delete(del_coach)   
                await session.commit()

            