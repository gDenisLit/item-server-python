from app.services import db_service
from bson.objectid import ObjectId
from app.models.Item_model import Item


collection_name = 'item'


async def query(filter_by):
    criteria = _build_criteria(filter_by)
    collection = db_service.get_collection(collection_name)
    cursor = collection.find(criteria)
    items = []
    for document in cursor:
        item = Item(
            _id=document['_id'],
            name=document['name'],
            price=document['price'],
            img_url=document['imgUrl']
        )
        items.append(item)

    return items


async def get_by_id(id):
    collection = db_service.get_collection(collection_name)
    item = collection.find_one({"_id": ObjectId(id)})
    return item


async def remove(id):
    collection = db_service.get_collection(collection_name)
    res = collection.delete_one({"_id": ObjectId(id)})
    print(res.deleted_count)
    return id


async def add(item_dto):
    collection = db_service.get_collection(collection_name)
    res = collection.insert_one(item_dto)
    item = Item(
        _id=res.inserted_id,
        name=item_dto["name"],
        price=item_dto["price"],
        img_url=item_dto["imgUrl"]
    )
    return item


async def update(id, item_dto):
    collection = db_service.get_collection(collection_name)
    print(id)
    collection.update_one({"_id": ObjectId(id)}, {"$set": item_dto})
    item = Item(
        _id=id,
        name=item_dto["name"],
        price=item_dto["price"],
        img_url=item_dto["imgUrl"]
    )
    return item


def _build_criteria(filter_by):
    criteria = {}
    if filter_by.txt:
        criteria['name'] = {'$regex': filter_by['txt'], '$options': 'i'}
    return criteria
