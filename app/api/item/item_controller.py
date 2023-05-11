from flask import request
from app.models.FilterBy_model import FilterBy
from app.services import logger, response
from app.models.Item_model import Item
from .item_service import ItemService
from app.middlewares import Middlewares


class ItemController:

    @staticmethod
    @Middlewares.log
    async def get_items():
        try:
            filter_by = FilterBy(
                txt=request.args.get("txt", "")
            )
            items = await ItemService.query(filter_by)
            return response.success(items)
        except Exception as e:
            logger.error(f"had error in item controller: {e}")
            return response.server_error()

    @staticmethod
    async def get_item_by_id(item_id: str):
        try:
            item = await ItemService.get_by_id(item_id)
            return response.success(item.to_dict())
        except ValueError as e:
            return response.bad_request(f"{e}")
        except Exception as e:
            logger.error(f"had error in item controller: {e}")
            return response.server_error()

    @staticmethod
    @Middlewares.auth
    async def remove_item(item_id: str):
        try:
            removed_id = await ItemService.remove(item_id)
            return response.success(removed_id)
        except ValueError as e:
            return response.bad_request(f"{e}")
        except Exception as e:
            logger.error(f"had error in item controller: {e}")
            return response.server_error()

    @staticmethod
    async def add_item():
        try:
            item_dto = ItemController._get_item_dto()
            item = await ItemService.add(item_dto)
            return response.created(item.to_dict())
        except ValueError as e:
            return response.bad_request(f"{e}")
        except Exception as e:
            logger.error(f"had error in item controller: {e}")
            return response.server_error()

    @staticmethod
    async def update_item():
        try:
            id = ItemController._get_id()
            item_dto = ItemController._get_item_dto()
            item = await ItemService.update(id, item_dto)
            return response.created(item.to_dict())
        except ValueError as e:
            return response.bad_request(f"{e}")
        except Exception as e:
            logger.error(f"had error in item controller: {e}")
            return response.server_error()

    @staticmethod
    def _get_item_dto():
        try:
            body = request.get_json()
            item_dto = Item.item_dto(
                body["name"],
                body["price"],
                body["imgUrl"]
            )
            return item_dto
        except:
            raise ValueError("Invalid item object")

    @staticmethod
    def _get_id():
        try:
            body = request.get_json()
            return body["_id"]
        except:
            raise ValueError("Invalid id")
