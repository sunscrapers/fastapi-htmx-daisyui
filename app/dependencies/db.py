import contextlib
from typing import Any
from typing import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from app.core import config


class DBSessionManager:
    def __init__(self, host: str, engine_kwargs: dict[str, Any] = {}):
        self.engine = create_async_engine(host, **engine_kwargs)
        self.sessionmaker = async_sessionmaker(autocommit=False, bind=self.engine)

    @contextlib.asynccontextmanager
    async def session(self) -> AsyncIterator[AsyncSession]:
        if self.sessionmaker is None:
            raise Exception("DBSessionManager is not initialized")

        session = self.sessionmaker()
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            print("closed")
            await session.close()


sessionmanager = DBSessionManager(config.DATABASE_URL)


async def get_db():
    async with sessionmanager.session() as session:
        yield session
