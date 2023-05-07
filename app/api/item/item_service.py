from app.services import db_service
from bson.objectid import ObjectId
from app.models.Item_model import Item
from app.models.FilterBy_model import FilterBy
from typing import List

collection_name = 'item'


async def query(filter_by: FilterBy) -> List[dict[str, str]]:
    criteria = _build_criteria(filter_by)
    collection = db_service.get_collection(collection_name)
    cursor = collection.find(criteria)

    items = []
    for document in cursor:
        item = Item(**document).to_dict()
        items.append(item)

    return items


async def get_by_id(id: str) -> Item:
    collection = db_service.get_collection(collection_name)
    item = collection.find_one({"_id": ObjectId(id)})
    return Item(**item) if item else None


async def remove(id: str) -> dict[str, str | int]:
    collection = db_service.get_collection(collection_name)
    res = collection.delete_one({"_id": ObjectId(id)})
    return {
        "deletedCount": res.deleted_count,
        "deletedId": id
    }


async def add(item_dto: dict[str, str]) -> Item:
    collection = db_service.get_collection(collection_name)
    collection.insert_one(item_dto)
    return Item(**item_dto)


async def update(id: str, item_dto: dict[str, str]) -> Item:
    collection = db_service.get_collection(collection_name)
    collection.update_one({"_id": ObjectId(id)}, {"$set": item_dto})
    return Item(id, **item_dto)


def _build_criteria(filter_by):
    criteria = {}
    if filter_by.txt:
        criteria['name'] = {'$regex': filter_by.txt, '$options': 'i'}
    return criteria
