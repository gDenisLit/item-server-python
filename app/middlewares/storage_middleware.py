from flask import g, request
from app.api.auth.auth_service import AuthService


async def store():
    try:
        token = request.cookies.get("loginToken")
        user = await AuthService.validate_token(token)
        if user:
            g.user = user
    except ValueError:
        pass
