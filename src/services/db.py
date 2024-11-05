import contextlib

from typing import AsyncIterator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncConnection, AsyncSession, async_sessionmaker

from aishaala_backend import settings
from utils.classes import SingletonMeta


class PostgresService(metaclass=SingletonMeta):
    def __init__(self):
        self.postgres_server=settings.POSTGRES_SERVER
        self.postgres_port=settings.POSTGRES_PORT
        self.postgres_db=settings.POSTGRES_DB
        self.postgres_user=settings.POSTGRES_USER
        self.postgres_password=settings.POSTGRES_PASSWORD
        self.database_url=f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}@{self.postgres_server}:{self.postgres_port}/{self.postgres_db}"
        self.engine = create_async_engine(self.database_url, echo=True)
        self._sessionmaker = async_sessionmaker(autocommit=False, bind=self.engine)

    async def disconnect(self):
        if self.engine is not None:
            await self.engine.dispose()

        self.engine = None
        self._sessionmaker = None

    @contextlib.asynccontextmanager
    async def connect(self) -> AsyncIterator[AsyncConnection]:
        if self.engine is None:
            raise Exception("PostgresDBService is not initialized")

        async with self.engine.begin() as connection:
            try:
                yield connection
            except Exception:
                await connection.rollback()
                raise

    @contextlib.asynccontextmanager
    async def session(self) -> AsyncIterator[AsyncSession]:
        if self._sessionmaker is None:
            raise Exception("PostgresDBService is not initialized")

        session = self._sessionmaker()
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
            
    async def get_session(self) -> AsyncIterator[AsyncSession]:
        async with self.session() as session:
            yield session
