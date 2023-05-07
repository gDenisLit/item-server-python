from flask import jsonify, Blueprint, request
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
        body = request.get_json()
        credentials = User.login_credentials(
            body["username"],
            body["password"]
        )

        user = await auth_service.login(credentials)
        logger.info(f"user loggedin | {user.to_dict()}")
        return response.success()

    except Exception as e:
        logger.error(f"error in auth controller: {e}")
        return response.server_error()


@auth_bp.route("/signup", methods=["POST"])
async def onSignup():
    try:
        body = request.get_json()
        credentials = User.signup_credentials(
            body["username"],
            body["password"],
            body["fullname"],
            body["imgUrl"],
            body["isAdmin"]
        )

        user = await auth_service.signup(credentials)
        logger.info(f"new accout | {user.to_dict()}")
        return response.success()

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
