from typing import Annotated
from fastapi import APIRouter, Depends

from router_collective.repository_collective import RepositoryCollective
from router_collective.shemas_collective import CollectiveShemas, CollectiveReturn

app = APIRouter(
    prefix='/collective',
    tags=['Коллектив']
)

@app.post('/')
async def add_collective(data: Annotated[CollectiveShemas, Depends()])->str:
    add_coll = await RepositoryCollective.add_collective(data)
    return add_coll

@app.get('/one')
async def get_one_collective(id: int) -> CollectiveReturn:
    get_one = await RepositoryCollective.get_one_collective(id)
    return get_one

@app.get('/all')
async def get_all_collective() -> list[CollectiveReturn]:
    get_all = await RepositoryCollective.get_all_collective()
    return get_all

@app.put('/')
async def update_collective(data: Annotated[CollectiveReturn, Depends()]):
    up_collective = await RepositoryCollective.update_collective(data)
    return up_collective

@app.delete('')
async def delete_collective(id: int):
    del_collective = await RepositoryCollective.delete_collective(id)
    return del_collective