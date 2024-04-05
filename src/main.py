from contextlib import asynccontextmanager

from fastapi import FastAPI
from orm import async_dalete_tables, insert_data, async_create_tables, view_all
from router_type_dance.router_dance import router as router_dance
from router_coach.router_coach import app as router_coach
from router_collective.router_collective import app as router_collective
from router_person.router_person import app as router_person

@asynccontextmanager
async def lifespan(app: FastAPI):
    await async_dalete_tables()
    await async_create_tables()
    await insert_data()
    yield



app = FastAPI(lifespan=lifespan)

@app.get('/view_all')
async def view_all_info():
    return await view_all()

app.include_router(router_dance)
app.include_router(router_coach)
app.include_router(router_collective)
app.include_router(router_person)
