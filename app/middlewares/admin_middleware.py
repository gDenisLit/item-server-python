from functools import wraps
from flask import g
from app.services import response
from app.models.User_model import User


def require_admin(func):
    @wraps(func)
    async def decorate_func(*args, **kwargs):
        try:
            user: User = g.user
            if user.is_admin:
                return await func(*args, **kwargs)
            else:
                return response.unauthorized()
        except:
            return response.unauthorized()

    return decorate_func
