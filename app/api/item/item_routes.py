from flask import Blueprint
from .item_controller import ItemController


class ItemRoutes:
    module_name = "item"
    routes = [
        {
            "endpoint": "/",
            "methods": ["GET"],
            "handler": ItemController.get_items
        },
        {
            "endpoint": "/<item_id>",
            "methods": ["GET"],
            "handler": ItemController.get_item_by_id
        },
        {
            "endpoint": "/<item_id>",
            "methods": ["DELETE"],
            "handler": ItemController.remove_item
        },
        {
            "endpoint": "/",
            "methods": ["POST"],
            "handler": ItemController.add_item
        },
        {
            "endpoint": "/",
            "methods": ["PUT"],
            "handler": ItemController.update_item
        },
    ]

    def __init__(self):
        self.blueprint = Blueprint(ItemRoutes.module_name, __name__)
        for route in self.routes:
            self.register_route(route)
            self.add_rule(route)

    def register_route(self, route):
        self.blueprint.route(
            rule=route["endpoint"],
            methods=route["methods"],
        )(route["handler"])

    def add_rule(self, route):
        self.blueprint.add_url_rule(
            route["endpoint"],
            view_func=route["handler"]
        )
