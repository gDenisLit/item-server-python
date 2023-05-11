from app.services import logger
from functools import wraps
from flask import request


def log_request(func):
    @wraps(func)
    async def decorate_func(*args, **kwargs):
        logger.info(
            f"Request URL: {request.url}, Request Method: {request.method}")
        return await func(*args, **kwargs)
    return decorate_func
