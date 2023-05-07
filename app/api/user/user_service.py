from app.services import db
from app.models.User_model import User
from app.services import logger
from bson.objectid import ObjectId
from typing import List


class UserService:

    collection_name = "user"

    @staticmethod
    async def query() -> List[dict[str, str]]:
        collection = UserService._get_collection()
        cursor = collection.find({})
        users = []
        for document in cursor:
            item = User(**document).to_dict()
            users.append(item)

        return users

    @staticmethod
    async def get_by_username(username: str) -> User | None:
        try:
            collection = UserService._get_collection()
            user = collection.find_one({"username": username})
            return User(**user) if user else None
        except:
            raise ValueError("No match found")

    @staticmethod
    async def get_by_id(id: str) -> User | None:
        try:
            collection = UserService._get_collection()
            user = collection.find_one({"_id": ObjectId(id)})
            return User(**user) if user else None
        except:
            raise ValueError("No match found")

    @staticmethod
    async def add_user(credentials: dict[str, str]) -> User:
        collection = UserService._get_collection()
        collection.insert_one(credentials)
        return User(**credentials)

    @staticmethod
    async def remove(id: str) -> str:
        try:
            collection = UserService._get_collection()
            collection.delete_one({"_id": ObjectId(id)})
            return id
        except:
            raise ValueError("Invalid id")

    @staticmethod
    def _get_collection():
        try:
            collection = db.get_collection(UserService.collection_name)
            return collection
        except Exception as e:
            logger.error(f"error in user service: {e}")
