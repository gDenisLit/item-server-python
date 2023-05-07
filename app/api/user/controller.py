from flask import Blueprint
from app.services import logger, response
from . import user_service

user_bp = Blueprint("user", __name__)


@user_bp.before_request
def log():
    # Log something before each request
    logger.info('Got request to user api')
    return


@user_bp.route("/", methods=["GET"])
async def get_users():
    try:
        users = await user_service.query()
        return response.success(users)
    except Exception as e:
        logger.error(f"had error in user controller: {e}")
        return response.server_error()


@user_bp.route("/<user_id>", methods=["GET"])
async def get_user_by_id(user_id: str):
    try:
        user = await user_service.get_by_id(user_id)
        return response.success(user.to_dict())
    except ValueError as e:
        return response.bad_request(e)
    except Exception as e:
        logger.error(f"had error in user controller: {e}")
        return response.server_error()


@user_bp.route("/<user_id>", methods=["DELETE"])
async def remove_user(user_id: str):
    try:
        removed_id = await user_service.remove(user_id)
        return response.success(removed_id)
    except ValueError as e:
        return response.bad_request(e)
    except Exception as e:
        logger.error(f"had error in user controller: {e}")
        return response.server_error()
