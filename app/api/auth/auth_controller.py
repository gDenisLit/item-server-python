from flask import jsonify, Blueprint, request
from app.services import logger_service
from .auth_service import login
from app.models.User_model import User

auth_bp = Blueprint("auth", __name__)


@auth_bp.before_request
def log():
    # Log something before each request
    logger_service.info('Got request to auth api')
    return


@auth_bp.route("/login", methods=["POST"])
async def onLogin():
    try:
        body = request.get_json()
        credentials = User.login_credentials(
            body["username"],
            body["password"]
        )

        user = await login(credentials)
        logger_service.info(f"user loggedin | {user.to_dict()}")

        return jsonify(user.to_dict()), 203
    except Exception as e:
        logger_service.error(f"error in user controller: {e}")
        return jsonify({"message": f"Internal error"}), 500


@auth_bp.route("/signup", methods=["POST"])
async def onSignup():
    try:
        return "signup"
    except Exception as e:
        logger_service.error(f"error in user controller: {e}")
        return jsonify({"message": f"Internal error"}), 500


@auth_bp.route("/logout", methods=["POST"])
async def onLogout():
    try:
        return "logout"
    except Exception as e:
        logger_service.error(f"error in user controller: {e}")
        return jsonify({"message": f"Internal error"}), 500
