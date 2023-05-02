from app.services import db_service
from bson.objectid import ObjectId
from app.models.User_model import User

collection_name = "user"


async def get_by_username(username: str) -> User:
    collection = db_service.get_collection(collection_name)
    user = collection.find_one({"username": username})
    user = User(**user)
    return user
