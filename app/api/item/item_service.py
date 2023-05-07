from app.services import db, logger
from bson.objectid import ObjectId
from app.models.Item_model import Item
from app.models.FilterBy_model import FilterBy
from typing import List


class ItemService:

    collection_name = "item"

    @staticmethod
    async def query(filter_by: FilterBy) -> List[dict[str, str]]:
        collection = ItemService._get_collection()
        criteria = ItemService._build_criteria(filter_by)
        cursor = collection.find(criteria)

        items = []
        for document in cursor:
            item = Item(**document).to_dict()
            items.append(item)

        return items

    @staticmethod
    async def get_by_id(id: str) -> Item:
        try:
            collection = ItemService._get_collection()
            item = collection.find_one({"_id": ObjectId(id)})
            return Item(**item) if item else None
        except:
            raise ValueError("Invalid id")

    @staticmethod
    async def remove(id: str) -> str:
        try:
            collection = ItemService._get_collection()
            collection.delete_one({"_id": ObjectId(id)})
            return id
        except:
            raise ValueError("Invalid id")

    @staticmethod
    async def add(item_dto: dict[str, str]) -> Item:
        collection = ItemService._get_collection()
        collection.insert_one(item_dto)
        return Item(**item_dto)

    @staticmethod
    async def update(id: str, item_dto: dict[str, str]) -> Item:
        try:
            collection = ItemService._get_collection()
            collection.update_one(
                {"_id": ObjectId(id)},
                {"$set": item_dto}
            )
            return Item(id, **item_dto)
        except:
            raise ValueError("Invalid item object")

    @staticmethod
    def _build_criteria(filter_by):
        criteria = {}
        if filter_by.txt:
            criteria['name'] = {
                '$regex': filter_by.txt,
                '$options': 'i'
            }
        return criteria

    @staticmethod
    def _get_collection():
        try:
            collection = db.get_collection(ItemService.collection_name)
            return collection
        except Exception as e:
            logger.error(f"error in item service: {e}")
