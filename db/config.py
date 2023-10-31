from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

import config

DB_CONNECT_URL = f"postgresql+asyncpg://{config.DB_LOGIN}:{config.DB_PASSWORD}@{config.DB_HOST}/{config.DB_NAME}"
engine = create_async_engine(DB_CONNECT_URL)
async_session = async_sessionmaker(engine)
