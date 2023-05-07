from app.services import db, logger
from bson.objectid import ObjectId
from app.models.Item_model import Item
from app.models.FilterBy_model import FilterBy
from typing import List


class ItemService:
    def __init__(self):
        self.collection_name = "item"
        self.collection = self._get_collection()

    async def query(self, filter_by: FilterBy) -> List[dict[str, str]]:
        criteria = self._build_criteria(filter_by)
        cursor = self.collection.find(criteria)

        items = []
        for document in cursor:
            item = Item(**document).to_dict()
            items.append(item)

        return items

    async def get_by_id(self, id: str) -> Item:
        try:
            item = self.collection.find_one({"_id": ObjectId(id)})
            return Item(**item) if item else None
        except:
            raise ValueError("Invalid id")

    async def remove(self, id: str) -> str:
        try:
            self.collection.delete_one({"_id": ObjectId(id)})
            return id
        except:
            raise ValueError("Invalid id")

    async def add(self, item_dto: dict[str, str]) -> Item:
        self.collection.insert_one(item_dto)
        return Item(**item_dto)

    async def update(self, id: str, item_dto: dict[str, str]) -> Item:
        try:
            self.collection.update_one(
                {"_id": ObjectId(id)},
                {"$set": item_dto}
            )
            return Item(id, **item_dto)
        except:
            raise ValueError("Invalid item object")

    def _build_criteria(self, filter_by):
        criteria = {}
        if filter_by.txt:
            criteria['name'] = {
                '$regex': filter_by.txt,
                '$options': 'i'
            }
        return criteria

    def _get_collection(self):
        try:
            collection = db.get_collection(self.collection_name)
            return collection
        except Exception as e:
            logger.error(f"error in item service: {e}")
