from app.services import db
from app.models.User_model import User


class UserService:

    def __init__(self):
        self.collection_name = "user"

    async def get_by_username(self, username: str) -> User | None:
        collection = db.get_collection(self.collection_name)
        user = collection.find_one({"username": username})
        return User(**user) if user else None

    async def add_user(self, credentials: dict[str, str]) -> User:
        collection = db.get_collection(self.collection_name)
        collection.insert_one(credentials)
        return User(**credentials)
