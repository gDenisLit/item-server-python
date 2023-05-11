from flask import Blueprint
from .auth_controller import AuthController


class AuthRoutes:
    module_name = "auth"
    routes = [
        {
            "url": "/login",
            "endpoint": "login",
            "methods": ["POST"],
            "handler": AuthController.login
        },
        {
            "url": "/signup",
            "endpoint": "signup",
            "methods": ["POST"],
            "handler": AuthController.singup
        },
        {
            "url": "/logout",
            "endpoint": "logout",
            "methods": ["POST"],
            "handler": AuthController.logout
        },
    ]

    def __init__(self):
        self.blueprint = Blueprint(AuthRoutes.module_name, __name__)

        for route in self.routes:
            self.blueprint.add_url_rule(
                route['url'],
                endpoint=route['endpoint'],
                view_func=route['handler'],
                methods=route['methods']
            )
