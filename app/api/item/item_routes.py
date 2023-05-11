from flask import Blueprint
from .item_controller import ItemController


class ItemRoutes:
    module_name = "item"
    routes = [
        {
            "url": "/",
            "endpoint": "get_items",
            "methods": ["GET"],
            "handler": ItemController.get_items,
        },
        {
            "url": "/<item_id>",
            "endpoint": "get_item_by_id",
            "methods": ["GET"],
            "handler": ItemController.get_item_by_id,
        },
        {
            "url": "/<item_id>",
            "endpoint": "remove_item",
            "methods": ["DELETE"],
            "handler": ItemController.remove_item,
        },
        {
            "url": "/",
            "endpoint": "add_item",
            "methods": ["POST"],
            "handler": ItemController.add_item,
        },
        {
            "url": "/",
            "endpoint": "update_item",
            "methods": ["PUT"],
            "handler": ItemController.update_item,
        },
    ]

    def __init__(self):
        self.blueprint = Blueprint(ItemRoutes.module_name, __name__)

        for route in self.routes:
            self.blueprint.add_url_rule(
                route['url'],
                endpoint=route['endpoint'],
                view_func=route['handler'],
                methods=route['methods']
            )
