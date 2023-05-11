from app.services import logger, response
from .user_service import UserService
from app.middlewares import Middlewares


class UserController:

    @staticmethod
    @Middlewares.log
    @Middlewares.admin
    async def get_users():
        try:
            users = await UserService.query()
            return response.success(users)
        except Exception as e:
            logger.error(f"had error in user controller: {e}")
            return response.server_error()

    @staticmethod
    @Middlewares.log
    @Middlewares.admin
    async def get_user_by_id(user_id: str):
        try:
            user = await UserService.get_by_id(user_id)
            return response.success(user.to_dict())
        except ValueError as e:
            return response.bad_request(e)
        except Exception as e:
            logger.error(f"had error in user controller: {e}")
            return response.server_error()

    @staticmethod
    @Middlewares.log
    @Middlewares.admin
    async def remove_user(user_id: str):
        try:
            removed_id = await UserService.remove(user_id)
            return response.success(removed_id)
        except ValueError as e:
            return response.bad_request(e)
        except Exception as e:
            logger.error(f"had error in user controller: {e}")
            return response.server_error()
