from flask import Blueprint
from .user_controller import UserController


class UserRoutes:
    module_name = "user"
    routes = [
        {
            "url": "/",
            "endpoint": "get_users",
            "methods": ["GET"],
            "handler": UserController.get_users
        },
        {
            "url": "/<user_id>",
            "endpoint": "get_user_by_id",
            "methods": ["GET"],
            "handler": UserController.get_user_by_id
        },
        {
            "url": "/<user_id>",
            "endpoint": "remove_user",
            "methods": ["DELETE"],
            "handler": UserController.remove_user
        }
    ]

    def __init__(self):
        self.blueprint = Blueprint(UserRoutes.module_name, __name__)

        for route in self.routes:
            self.blueprint.add_url_rule(
                route['url'],
                endpoint=route['endpoint'],
                view_func=route['handler'],
                methods=route['methods']
            )
