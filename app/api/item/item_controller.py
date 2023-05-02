import json
from flask import jsonify, Blueprint, request
from .item_service import query, get_by_id, remove, update, add
from app.models.FilterBy_model import FilterBy
from app.encoders.Item_encoder import ItemEncoder
from app.services import logger_service
from app.models.Item_model import Item

item_bp = Blueprint("item", __name__)


@item_bp.before_request
def log():
    # Log something before each request
    logger_service.info('Got request to item api')
    return


@item_bp.route("/", methods=["GET"])
async def get_items():
    try:
        filter_by = FilterBy(
            txt=request.args.get("txt", "")
        )
        items = await query(filter_by)
        return jsonify(items), 200
    except Exception as e:
        logger_service.error(f"error in item controller: {e}")
        return jsonify({"message": f"Internal server error"}), 500


@item_bp.route("/<item_id>", methods=["GET"])
async def get_item_by_id(item_id: str):
    try:
        item = await get_by_id(item_id)
        if not item:
            return jsonify({"error": f"Item not found"}), 403

        return jsonify(item.to_dict()), 200
    except Exception as e:
        logger_service.error(f"error in item controller: {e}")
        return jsonify({"message": f"Internal error"}), 500


@item_bp.route("/<item_id>", methods=["DELETE"])
async def remove_item(item_id: str):
    try:
        res = await remove(item_id)
        return jsonify(res), 201
    except Exception as e:
        logger_service.error(f"error in item controller: {e}")
        return jsonify({"message": f"Internal error"}), 500


@item_bp.route("/", methods=["POST"])
async def add_item():
    try:
        body = request.get_json()
        item_dto = Item.item_dto(
            body["name"],
            body["price"],
            body["imgUrl"]
        )

        item = await add(item_dto)
        if not item:
            return jsonify({"error": f"Invalid ID"}), 403
        
        return jsonify(item.to_dict()), 201
    except Exception as e:
        logger_service.error(f"error in item controller: {e}")
        return jsonify({"message": f"Internal error"}), 500


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

        item = await update(id, item_dto)
        return jsonify(item.to_dict()), 201
    except Exception as e:
        logger_service.error(f"error in item controller: {e}")
        return jsonify({"message": f"Internal error"}), 500
