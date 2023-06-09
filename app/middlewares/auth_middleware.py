from functools import wraps
from flask import g
from app.services import response
from app.models.User_model import User


def require_auth(func):
    @wraps(func)
    async def decorate_func(*args, **kwargs):
        try:
            user: User = g.user
            if user:
                return await func(*args, **kwargs)
        except:
            return response.unauthorized()

    return decorate_func
