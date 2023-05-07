import bcrypt
import jwt
from jwt.exceptions import DecodeError
from app.api.user.user_service import UserService
from app.models.User_model import User
from app.config import config
from typing import Optional


class AuthService:

    @staticmethod
    async def login(credentials: dict[str, str]) -> User:
        error_msg = "Wrong credentials"

        user = await UserService.get_by_username(credentials["username"])
        if not user:
            raise ValueError(error_msg)

        correct = bcrypt.checkpw(
            credentials["password"].encode('utf-8'),
            user.password.encode('utf-8')
        )

        if not correct:
            raise ValueError(error_msg)

        return user

    @staticmethod
    async def signup(credentials: dict[str, str]) -> User:

        user = await UserService.get_by_username(credentials["username"])
        if user:
            raise ValueError("username is already taken")

        hashed_password = bcrypt.hashpw(
            credentials["password"].encode(),
            bcrypt.gensalt(10)
        )
        credentials["password"] = hashed_password
        return await UserService.add_user(credentials)

    @staticmethod
    async def get_login_token(user: User) -> str:
        token = jwt.encode(
            user.to_dict(),
            config.secret_key,
            algorithm="HS256"
        )
        return token

    @staticmethod
    async def validate_token(token: str) -> Optional[dict]:
        try:
            user = jwt.decode(
                token,
                config.secret_key,
                algorithms=["HS256"]
            )
            return user
        except DecodeError:
            raise ValueError("Invalid login token")
