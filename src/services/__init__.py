from .db import PostgresService
from .cache import RedisService

postgres = PostgresService()
redis = RedisService()

__all__ = ["redis", "postgres"]
