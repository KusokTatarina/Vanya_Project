
import asyncio
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from sqlalchemy import URL, create_engine, text
from config import db_url_asyncpg, db_url_psycopg




sync_engine = create_engine(
    # url="postgresql+psycopg://postgres:072309Dd@localhost:5432/ballet",
    url=db_url_psycopg,
    echo= True)

async_engine = create_async_engine(
    url=db_url_asyncpg,
    echo= True)

sync_session = sessionmaker(sync_engine)
async_session = async_sessionmaker(async_engine)

class Base(DeclarativeBase):
    pass

class Shemas(BaseModel):
    pass