import pymongo
from . import MONGO_HOST
from bson.objectid import ObjectId


class MongoCon(pymongo.MongoClient):
    def __init__(self):
        super().__init__(MONGO_HOST)

    def get_document_by_id(self, id: str) -> dict:
        return self["api_tester"]["tests"].find_one({'_id': ObjectId(id)})

    def get_results(self, query: dict = None, limit: int = 30, select: dict = None) -> list:
        return list(self["api_tester"]["tests"].find(query, select).limit(limit).sort("datetime", -1))
