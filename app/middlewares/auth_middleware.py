from app.services import logger
from functools import wraps
from flask import request, g
from app.services import response


def require_auth(func):
    @wraps(func)
    async def decorate_func(*args, **kwargs):
        try:
            user = g.user
            if user:
                return await func(*args, **kwargs)
        except:
            return response.unauthorized()

    return decorate_func
