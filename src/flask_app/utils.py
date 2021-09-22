import json

from pymongo import MongoClient
from redis import Redis


class DataStore:
    def __init__(self,
                 mongo_host,
                 mongo_port,
                 redis_host):
        self.redis = Redis(host=redis_host)
        self.mongo_client = MongoClient(
            f'mongodb://{mongo_host}:{mongo_port}/', maxPoolSize=200
        )
        self.collection = self.mongo_client.example_db.example_collection

    def get(self, key):
        if cached := self.redis.get(key):
            return json.loads(cached)

        return self.collection.find_one({'key': key})


datastore = DataStore(
    mongo_host='0.0.0.0',
    mongo_port='27017',
    redis_host='127.0.0.1',
)
