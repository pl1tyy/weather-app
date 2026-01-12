# app/utils/cache.py
from aiocache import Cache
from app.core.config import settings

cache = Cache(Cache.MEMORY, ttl=settings.CACHE_TTL)