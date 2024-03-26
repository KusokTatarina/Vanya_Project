from typing import Annotated
from fastapi import APIRouter, Depends

from router_type_dance.repository_dance import DanceRepository
from router_type_dance.shemas_dance import ReturnType, TypeBallet


router = APIRouter(
    prefix='/type_dance',
    tags=['Танцы']
)


@router.post('')
async def add_dance(dance: Annotated[TypeBallet, Depends()]):
    dance_id = await DanceRepository.add_one_dance(dance)
    return {'code': 200, 'Details': f'Вы добавили танец {dance.name} c id={dance_id}'}


@router.get('/all')
async def get_all_dance() -> list[ReturnType]:
    all_dance = await DanceRepository.get_all_dance()
    return all_dance


@router.get('/one')
async def get_one_dance(id: int) -> ReturnType:
    one_dance = await DanceRepository.get_one_dance(id)
    return one_dance


@router.put('')
async def update_dance(data: Annotated[ReturnType, Depends()]):
    all_dance = await DanceRepository.update_dance(data)
    return all_dance


@router.delete('')
async def delete_dance(id: int):
    all_dance = await DanceRepository.delete_dance(id)
    return 404