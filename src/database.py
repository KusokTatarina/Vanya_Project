import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from sqlalchemy import URL, create_engine, text
from config import settings, Settings




sync_egine = create_engine(
    url=Settings.db_url_psyncpg(),
    echo= True)

async_egine = create_async_engine(
    url=Settings.db_url_asyncpg(),
    echo= True)

sync_session = sessionmaker(sync_egine)
async_session = async_sessionmaker(async_egine)

class Base(DeclarativeBase):
    pass