import json
from app.models.Item_model import Item
from bson.objectid import ObjectId


class ItemEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Item):
            return {
                "_id": str(obj._id),
                "name": obj.name,
                "price": obj.price,
                "imgUrl": obj.img_url
            }
        elif isinstance(obj, ObjectId):
            return str(obj)
        else:
            raise TypeError(
                f"Object of type {obj.__class__.__name__} is not JSON serializable")
