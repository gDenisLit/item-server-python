from flask import Blueprint, request
from app.services import logger, response
from . import auth_service
from app.models.User_model import User


auth_bp = Blueprint("auth", __name__)


@auth_bp.before_request
def log():
    # Log something before each request
    logger.info('Got request to auth api')
    return


@auth_bp.route("/login", methods=["POST"])
async def onLogin():
    try:
        credentials = _get_login_credentials()
        user = await auth_service.login(credentials)
        logger.info(f"user loggedin | {user.to_dict()}")
        return response.success(user.to_dict())
    except ValueError as e:
        return response.bad_request(f"Error: {e}")
    except Exception as e:
        logger.error(f"had error in item controller: {e}")
        return response.server_error()


@auth_bp.route("/signup", methods=["POST"])
async def onSignup():
    try:
        credentials = _get_signup_credentials()
        user = await auth_service.signup(credentials)
        logger.info(f"new accout | {user.to_dict()}")
        return response.success(user.to_dict())
    except ValueError as e:
        return response.bad_request(f"Error: {e}")
    except Exception as e:
        logger.error(f"error in auth controller: {e}")
        return response.server_error()


@auth_bp.route("/logout", methods=["POST"])
async def onLogout():
    try:
        return "logout"
    except Exception as e:
        logger.error(f"error in auth controller: {e}")
        return response.server_error()


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


def _get_signup_credentials():
    try:
        body = request.get_json()
        credentials = User.signup_credentials(
            body["username"],
            body["password"],
            body["fullname"],
            body["imgUrl"],
            body["isAdmin"]
        )
        return credentials
    except:
        raise ValueError("Missing credentials")
