from flask import request
from app.services import logger, response
from .auth_service import AuthService
from app.models.User_model import User


class AuthController:

    @staticmethod
    async def login():
        try:
            credentials = AuthController._get_login_credentials()
            user = await AuthService.login(credentials)
            logger.info(f"user loggedin | {user.to_dict()}")

            token = await AuthService.get_login_token(user)
            return response.login_success(token, user.to_dict())

        except ValueError as e:
            return response.bad_request(f"Error: {e}")

        except Exception as e:
            logger.error(f"had error in item controller: {e}")
            return response.server_error()

    @staticmethod
    async def singup():
        try:
            credentials = AuthController._get_signup_credentials()
            user = await AuthService.signup(credentials)
            logger.info(f"new accout | {user.to_dict()}")

            token = await AuthService.get_login_token(user)
            return response.login_success(token, user.to_dict())

        except ValueError as e:
            return response.bad_request(f"Error: {e}")

        except Exception as e:
            logger.error(f"error in auth controller: {e}")
            return response.server_error()

    @staticmethod
    async def logout():
        try:
            return response.logout_success()
        except Exception as e:
            logger.error(f"error in auth controller: {e}")
            return response.server_error()

    @staticmethod
    def _get_login_credentials():
        try:
            body = request.get_json()
            credentials = User.login_credentials(
                body["username"],
                body["password"]
            )
            return credentials
        except:
            raise ValueError("Missing credentials")

    @staticmethod
    def _get_signup_credentials():
        try:
            body = request.get_json()
            credentials = User.signup_credentials(
                body["username"],
                body["password"],
                body["fullname"],
                body["imgUrl"],
            )
            return credentials
        except:
            raise ValueError("Missing credentials")
