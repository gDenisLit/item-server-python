from app.services import db
from bson.objectid import ObjectId
from app.models.Item_model import Item
from app.models.FilterBy_model import FilterBy
from typing import List


class ItemService:
    def __init__(self):
        self.collection_name = "item"

    async def query(self, filter_by: FilterBy) -> List[dict[str, str]]:
        criteria = self._build_criteria(filter_by)
        collection = db.get_collection(self.collection_name)
        cursor = collection.find(criteria)

        items = []
        for document in cursor:
            item = Item(**document).to_dict()
            items.append(item)

        return items

    async def get_by_id(self, id: str) -> Item:
        collection = db.get_collection(self.collection_name)
        item = collection.find_one({"_id": ObjectId(id)})
        return Item(**item) if item else None

    async def remove(self, id: str) -> str:
        collection = db.get_collection(self.collection_name)
        collection.delete_one({"_id": ObjectId(id)})
        return id

    async def add(self, item_dto: dict[str, str]) -> Item:
        collection = db.get_collection(self.collection_name)
        collection.insert_one(item_dto)
        return Item(**item_dto)

    async def update(self, id: str, item_dto: dict[str, str]) -> Item:
        collection = db.get_collection(self.collection_name)
        collection.update_one({"_id": ObjectId(id)}, {"$set": item_dto})
        return Item(id, **item_dto)

    def _build_criteria(self, filter_by):
        criteria = {}
        if filter_by.txt:
            criteria['name'] = {
                '$regex': filter_by.txt,
                '$options': 'i'
            }
        return criteria
