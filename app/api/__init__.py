from .item.item_routes import ItemRoutes
from .auth.auth_routes import AuthRoutes
from .user.user_routes import UserRoutes

item = ItemRoutes()
auth = AuthRoutes()
user = UserRoutes()

class Blueprints:
    item = {
        "blueprint": item.blueprint,
        "url_prefix": "/api/item"
    }
    auth = {
        "blueprint": auth.blueprint,
        "url_prefix": "/api/auth"
    }
    user = {
        "blueprint": user.blueprint,
        "url_prefix": "/api/user"
    }
