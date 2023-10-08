"""Services module."""

from aioredis import Redis


class Service:
    def __init__(self, redis: Redis) -> None:
        self._redis = redis

    async def get_music(self, request_id: str) -> str:
        return await self._redis.get(request_id)

    async def set_music(self, request_id: str, song_bytes: bytes) -> None:
        await self._redis.set(request_id, song_bytes)
