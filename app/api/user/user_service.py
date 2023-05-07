from app.services import db_service
from app.models.User_model import User

collection_name = "user"


async def get_by_username(username: str) -> User | None:
    collection = db_service.get_collection(collection_name)
    user = collection.find_one({"username": username})
    return User(**user) if user else None


async def add_user(credentials: dict[str, str]) -> User:
    collection = db_service.get_collection(collection_name)
    collection.insert_one(credentials)
    return User(**credentials)
