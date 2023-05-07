# from flask import g, request
# from app.services import logger
# from functools import wraps
# from app.api.auth import auth_service
# from app.models.User_model import User


# def storage_middleware(r):
#     try:
#         token = request.cookies.get("loginToken")
#         check_user(token)
#     except ValueError:
#         pass
#     return request


# async def check_user(token):
#     try:
#         user = await auth_service.validate_token(token)
#         g.user = User(**user)
#     except:
#         pass
