import pymongo
from typing import Dict, Any


MONGO_HOST = "mongodb://localhost:27017/"


class MongoCon(pymongo.MongoClient):
    def __init__(self):
        super().__init__(MONGO_HOST)

    def get_results(self, query: Dict[str, Any], limit: int = 30, select: Dict[str, int] = None) -> list:
        return list(self["api_tester"]["tests"].find(query, select).limit(limit).sort("datetime", -1))
