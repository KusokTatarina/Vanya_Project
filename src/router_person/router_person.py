from base64 import b64decode
from io import BytesIO
import os
from fastapi import APIRouter, Depends, File, UploadFile
from typing import Annotated, Optional

from router_person.shemas_person import Rank
from router_person.repository_person import RepositoryPerson
from router_person.shemas_person import PersonShemas, ReturnPerson
from config import SAVE_PATH


app = APIRouter(
    prefix='/person', 
    tags=['Участники']
    )

@app.post('/')
async def add_person(data: Annotated[PersonShemas, Depends()], photo: UploadFile = File(...)):
    data.photo = os.path.join(SAVE_PATH, photo.filename)
    with open(data.photo, "wb") as f:
        content = await photo.read()
        f.write(content)
    return await RepositoryPerson.add_person(data)
    

@app.get('/one')
async def get_one_person(id:int):
    return await RepositoryPerson.get_one_person(id)
    

@app.get('/all')
async def get_all_person():
    return await RepositoryPerson.get_all_person()

@app.put('/')
async def update_person(data: Annotated[ReturnPerson, Depends()], photo: UploadFile = File(...)):
    data.photo = os.path.join(SAVE_PATH, photo.filename)
    with open(data.photo, "wb") as f:
        content = await photo.read()
        f.write(content)
    return await RepositoryPerson.update_person(data)

@app.delete('/')
async def delete_person(id: int):
    return await RepositoryPerson.delete_person(id)