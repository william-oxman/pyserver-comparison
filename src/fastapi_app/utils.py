import json

from aioredis import create_redis_pool
from motor.motor_asyncio import AsyncIOMotorClient


class DataStore:
    def __init__(self,
                 mongo_host,
                 mongo_port,
                 redis_host):
        self.mongo_client = AsyncIOMotorClient(
            f'mongodb://{mongo_host}:{mongo_port}'
        )
        self.db = self.mongo_client.example_db
        self.collection = self.db.example_collection
        self.redis = None

    async def init_redis(self, redis_host):
        self.redis = await create_redis_pool(redis_host)

    async def get(self, key):
        if cached := await self.redis.get(key):
            return json.loads(cached)

        return await self.collection.find_one({'key': key})


datastore = DataStore(
    mongo_host='0.0.0.0',
    mongo_port='27017',
    redis_host='127.0.0.1',
)
