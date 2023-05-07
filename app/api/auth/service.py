import bcrypt
from app.api.user import user_service
from app.models.User_model import User


class AuthService:

    async def login(self, credentials: dict[str, str]) -> User:
        error_msg = "Wrong credentials"

        user = await user_service.get_by_username(credentials["username"])
        if user:
            raise ValueError(error_msg)

        correct = bcrypt.checkpw(
            credentials["password"].encode('utf-8'),
            user.password.encode('utf-8')
        )

        if not correct:
            raise ValueError(error_msg)

        return user

    async def signup(self, credentials: dict[str, str]) -> User:

        user = await user_service.get_by_username(credentials["username"])
        if user:
            raise ValueError("username is already taken")

        hashed_password = bcrypt.hashpw(
            credentials["password"].encode(),
            bcrypt.gensalt(10)
        )
        credentials["password"] = hashed_password
        return await user_service.add_user(credentials)

    async def get_login_token(user: User) -> str:
        return "user"
