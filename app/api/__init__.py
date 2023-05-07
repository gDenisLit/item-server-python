from .item.controller import item_bp
from .auth.controller import auth_bp
from .user.controller import user_bp


class ApiRoutes:
    def __init__(self):
        self.item = {
            "blueprint": item_bp,
            "url_prefix": "/api/item"
        }
        self.auth = {
            "blueprint": auth_bp,
            "url_prefix": "/api/auth"
        }
        self.user = {
            "blueprint": user_bp,
            "url_prefix": "/api/user"
        }


routes = ApiRoutes()
