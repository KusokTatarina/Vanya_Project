from sqlalchemy import delete, select, text
from database import async_session, async_engine
from router_type_dance.shemas_dance import TypeBallet, ReturnType
from models import TypeDance
from orm import return_one_object

class DanceRepository:
    @classmethod
    async def add_one_dance(cls, data: TypeBallet) -> int:
        async with async_session() as session:
            type_dict = data.model_dump()
            dance = TypeDance(**type_dict)
            session.add(dance)
            await session.commit()
            await session.refresh(dance)
            return await return_one_object(TypeDance, dance.id)


    @classmethod
    async def get_all_dance(cls) -> list[ReturnType]:
        async with async_session() as session:
            query = select(TypeDance)
            result = await session.execute(query)
            dance_model = result.scalars().all()
            dance_shema = [ReturnType.model_validate(dance) for dance in dance_model]
            return dance_shema


    @classmethod
    async def get_one_dance(cls, id: int) -> ReturnType:
        async with async_session() as session:
            query = select(TypeDance).filter_by(id=id)
            result = await session.execute(query)
            dance_model = result.scalar_one()
            return dance_model


    @classmethod
    async def update_dance(cls, data: ReturnType):
            async with async_session() as session:
                up_type = await session.get(TypeDance, data.id)
                up_type.name = data.name
                await session.commit()
                await session.refresh(up_type)
                return up_type


    @classmethod
    async def delete_dance(cls, id):
            async with async_session() as session:
                del_type = await session.get(TypeDance, id)
                ret = await return_one_object(TypeDance, id)
                await session.delete(del_type)   
                await session.commit()
                return ret
