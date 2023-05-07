from flask import Blueprint
from .auth_controller import AuthController


class AuthRoutes:
    module_name = "auth"
    routes = [
        {
            "endpoint": "/login",
            "methods": ["POST"],
            "handler": AuthController.login
        },
        {
            "endpoint": "/signup",
            "methods": ["POST"],
            "handler": AuthController.singup
        },
        {
            "endpoint": "/logout",
            "methods": ["POST"],
            "handler": AuthController.logout
        },
    ]

    def __init__(self):
        self.blueprint = Blueprint(AuthRoutes.module_name, __name__)
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
