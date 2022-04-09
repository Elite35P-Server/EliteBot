import os
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from cogs import models

# "sqlite:///./sql_app.sqlite"
# "sqlite+aiosqlite:///:memory:"
# "postgresql://user:password@postgresserver/db"
# os.environ.get("DB_URL")
async_engine = create_async_engine(
    "sqlite+aiosqlite:///sql_app.sqlite",
    connect_args={"check_same_thread": False}
)

async def setup():
    async with async_engine.begin() as conn:
        #await conn.run_sync(models.Base.metadata.drop_all)
        await conn.run_sync(models.Base.metadata.create_all)

async_session = sessionmaker(
    autocommit=False, autoflush=True, bind=async_engine, expire_on_commit=False, class_=AsyncSession
)