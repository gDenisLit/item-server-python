from app.services import db
from app.models.User_model import User
from app.services import logger
from bson.objectid import ObjectId
from typing import List


class UserService:

    def __init__(self):
        self.collection_name = "user"
        self.collection = self._get_collection()

    async def query(self) -> List[dict[str, str]]:
        cursor = self.collection.find({})
        users = []
        for document in cursor:
            item = User(**document).to_dict()
            users.append(item)

        return users

    async def get_by_username(self, username: str) -> User | None:
        try:
            user = self.collection.find_one({"username": username})
            return User(**user) if user else None
        except:
            raise ValueError("No match found")

    async def get_by_id(self, id: str) -> User | None:
        try:
            user = self.collection.find_one({"_id": ObjectId(id)})
            return User(**user) if user else None
        except:
            raise ValueError("No match found")

    async def add_user(self, credentials: dict[str, str]) -> User:
        self.collection.insert_one(credentials)
        return User(**credentials)

    async def remove(self, id: str) -> str:
        try:
            self.collection.delete_one({"_id": ObjectId(id)})
            return id
        except:
            raise ValueError("Invalid id")

    def _get_collection(self):
        try:
            collection = db.get_collection(self.collection_name)
            return collection
        except Exception as e:
            logger.error(f"error in user service: {e}")
