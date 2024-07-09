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

    def get_all_sessions(self):
        pipeline = [
            {
                "$group": {
                    "_id": "$session_id",
                    "mongo_id": {"$first": "$_id"},
                    "last_datetime": {"$max": "$datetime"},
                    "success_rate": {
                        "$avg": {
                            "$cond": [{"$eq": ["$status", True]}, 1, 0]
                        }
                    },
                    "all_errors": {"$push": "$errors"}
                }
            },
            {
                "$project": {
                    "session_id": "$_id",
                    "_id": "$mongo_id",
                    "success_rate": {"$multiply": ["$success_rate", 100]},
                    "datetime": "$last_datetime",
                    "has_errors": {
                        "$anyElementTrue": {
                            "$map": {
                                "input": "$all_errors",
                                "as": "err",
                                "in": {"$gt": [{"$size": "$$err"}, 0]}
                            }
                        }
                    }
                }
            },
            {
                "$sort": {"datetime": -1}
            },
            {
                "$limit": 15
            }
        ]
        return list(self["api_tester"]["tests"].aggregate(pipeline))

    def get_all_services(self):
        pipeline = [
            {
                "$group": {
                    "_id": "$service",
                    "success_rate": {
                        "$avg": {
                            "$cond": [{"$eq": ["$status", True]}, 1, 0]
                        }
                    }
                }
            },
            {
                "$project": {
                    "service": "$_id",
                    "_id": 0,
                    "success_rate": {"$multiply": ["$success_rate", 100]} 
                }
            },
            {
                "$sort": {"service": 1}
            }
        ]
        return list(self["api_tester"]["tests"].aggregate(pipeline))

