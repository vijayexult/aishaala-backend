import redis.asyncio as redis

from aishaala_backend import settings
from utils.classes import SingletonMeta

class RedisService(metaclass=SingletonMeta):
    def __init__(self):
        self._conn = None

    async def connect(self):
        self._conn = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)

    async def disconnect(self):
        await self._conn.aclose()

    async def get(self, key: str):
        return await self._conn.get(key)

    async def set(self, key: str, value: str):
        await self._conn.set(key, value)

    async def delete(self, key: str):
        await self._conn.delete(key)
