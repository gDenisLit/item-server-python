from flask import request
from app.services import logger
from functools import wraps


def logger_middleware(func):
    @wraps(func)
    async def decorate_func(*args, **kwargs):
        logger.info(f"{request.method} request to {request.path}")
        return await func(*args, **kwargs)
    return decorate_func
