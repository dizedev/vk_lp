from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

import config

DB_CONNECT_URL = f"postgresql+asyncpg://{config.psql_login}:{config.psql_password}@{config.psql_host}/{config.psql_database}"
engine = create_async_engine(DB_CONNECT_URL)
async_session = async_sessionmaker(engine)
