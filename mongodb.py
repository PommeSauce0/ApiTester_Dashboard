import pymongo


MONGO_HOST = "mongodb://localhost:27017/"


class MongoCon(pymongo.MongoClient):
    def __init__(self):
        super().__init__(MONGO_HOST)

    def get_results(self, query: dict, limit: int = 30) -> list:
        return list(self["api_tester"]["tests"].find(query).limit(limit).sort("datetime", -1))
