from flask import jsonify, Blueprint, request
from app.models.FilterBy_model import FilterBy
from app.services import logger, response
from app.models.Item_model import Item
from . import item_service


item_bp = Blueprint("item", __name__)


@item_bp.before_request
def log():
    # Log something before each request
    logger.info('Got request to item api')
    return


@item_bp.route("/", methods=["GET"])
async def get_items():
    try:
        filter_by = FilterBy(
            txt=request.args.get("txt", "")
        )
        items = await item_service.query(filter_by)
        return response.success(items)
    except Exception as e:
        logger.error(f"error in item controller: {e}")
        return response.server_error()


@item_bp.route("/<item_id>", methods=["GET"])
async def get_item_by_id(item_id: str):
    try:
        item = await item_service.get_by_id(item_id)
        return response.success(item.to_dict())
    except Exception as e:
        logger.error(f"error in item controller: {e}")
        return response.server_error()


@item_bp.route("/<item_id>", methods=["DELETE"])
async def remove_item(item_id: str):
    try:
        removed_id = await item_service.remove(item_id)
        return response.success(removed_id)
    except Exception as e:
        logger.error(f"error in item controller: {e}")
        return response.server_error()


@item_bp.route("/", methods=["POST"])
async def add_item():
    try:
        body = request.get_json()
        item_dto = Item.item_dto(
            body["name"],
            body["price"],
            body["imgUrl"]
        )

        item = await item_service.add(item_dto)
        return response.created(item.to_dict())
    except Exception as e:
        logger.error(f"error in item controller: {e}")
        return response.server_error()


@item_bp.route("/", methods=["PUT"])
async def update_item():
    try:
        body = request.get_json()
        id = body["_id"]

        item_dto = Item.item_dto(
            body["name"],
            body["price"],
            body["imgUrl"]
        )

        item = await item_service.update(id, item_dto)
        if not item:
            return jsonify({"error": f"Invalid ID"}), 403

        return response.created(item.to_dict())
    except Exception as e:
        logger.error(f"error in item controller: {e}")
        return response.server_error()
