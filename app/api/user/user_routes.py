from flask import Blueprint
from .user_controller import UserController


class UserRoutes:
    module_name = "user"
    routes = [
        {
            "endpoint": "/",
            "methods": ["GET"],
            "handler": UserController.get_users
        },
        {
            "endpoint": "/<user_id>",
            "methods": ["GET"],
            "handler": UserController.get_user_by_id
        },
        {
            "endpoint": "/<user_id>",
            "methods": ["DELETE"],
            "handler": UserController.remove_user
        }
    ]

    def __init__(self):
        self.blueprint = Blueprint(UserRoutes.module_name, __name__)
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
