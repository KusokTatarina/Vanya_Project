from typing import Annotated
from fastapi import APIRouter, Depends

from router_coach.repository_coach import RepositoryCoach
from router_coach.shemas_coach import CoachReturn, CoachShemas

app = APIRouter(
    prefix='/coach',
    tags=['Тренерs']
)

@app.get("/all")
async def get_all_coach() -> list[CoachReturn]:
    result = await RepositoryCoach.get_all_coach()
    return result


@app.get("/one")
async def get_one_coach(id: int) -> CoachReturn:
    result = await RepositoryCoach.get_one_coach(id)
    return result

@app.post('/')
async def add_coach(data: Annotated[CoachShemas, Depends()]):
    add_coach = await RepositoryCoach.add_one_coach(data)
    return f"Вы добавили тренера {data.name} с id={add_coach}"

@app.put('/')
async def update_coach(data: Annotated[CoachReturn, Depends()]):
    up_coach = await RepositoryCoach.update_coach(data)
    return f"Вы обновили Тренера с id={up_coach} на {data.name} по танцам с id={data.type_dance}"

@app.delete('/')
async def delete_coach(id: int):
    del_coach = await RepositoryCoach.delete_coach(id)
    return f"Вы удалили Тренера с {id=}"