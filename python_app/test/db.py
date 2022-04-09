import os
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_scoped_session
from sqlalchemy.orm import sessionmaker, scoped_session
import models, schemas, async_crud

#os.environ.get("DB_URL")
async_engine = create_async_engine(os.environ.get("DB_URL"))

async def setup():
    async with async_engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.drop_all)
        await conn.run_sync(models.Base.metadata.create_all)
        
    async_session = scoped_session(
        sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=async_engine, 
            #expire_on_commit=False, 
            class_=AsyncSession
        )
    )
    return async_session
        
async_session = asyncio.run(setup())

