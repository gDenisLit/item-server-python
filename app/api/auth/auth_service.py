import bcrypt
from app.api.user.user_service import get_by_username
from app.models.User_model import User


async def login(credentials: dict[str, str]) -> User:
    error_msg = "Wrong credentials"

    user = await get_by_username(credentials["username"])
    if not user:
        raise ValueError(error_msg)

    correct = bcrypt.checkpw(
        credentials["password"].encode('utf-8'),
        user.password.encode('utf-8')
    )

    if not correct:
        raise ValueError(error_msg)

    return user
