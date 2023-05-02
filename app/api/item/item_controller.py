import json
from flask import jsonify, Blueprint, request
from .item_service import query, get_by_id, remove, update, add
from app.models.FilterBy_model import FilterBy
from app.encoders.Item_encoder import ItemEncoder
from app.dtos.Item_dto import ItemDTO
from app.services import logger_service

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
        json_data = json.dumps(items, cls=ItemEncoder)
        return json_data, 200
    except Exception as e:
        logger_service.error(f"error in item controller: {e}")
        return jsonify({"message": f"Internal server error"}), 500


@item_bp.route("/<item_id>", methods=["GET"])
async def get_item_by_id(item_id):
    try:
        item = await get_by_id(item_id)
        json_data = json.dumps(item, cls=ItemEncoder)
        return json_data, 200
    except Exception as e:
        logger_service.error(f"error in item controller: {e}")
        return jsonify({"message": f"Internal error"}), 500


@item_bp.route("/<item_id>", methods=["DELETE"])
async def remove_item(item_id):
    try:
        id = await remove(item_id)
        return jsonify({"removedId": id}), 201
    except Exception as e:
        logger_service.error(f"error in item controller: {e}")
        return jsonify({"message": f"Internal error"}), 500


@item_bp.route("/", methods=["POST"])
async def add_item():
    try:
        body = request.get_json()
        item_dto = ItemDTO(
            name=body["name"],
            price=body["price"],
            img_url=body["imgUrl"]
        ).to_dict()

        item = await add(item_dto)
        json_data = json.dumps(item, cls=ItemEncoder)
        return json_data, 201
    except Exception as e:
        logger_service.error(f"error in item controller: {e}")
        return jsonify({"message": f"Internal error"}), 500


@item_bp.route("/", methods=["PUT"])
async def update_item():
    try:
        body = request.get_json()
        id = body["_id"]
        item_dto = ItemDTO(
            name=body["name"],
            price=body["price"],
            img_url=body["imgUrl"]
        ).to_dict()

        item = await update(id, item_dto)
        json_data = json.dumps(item, cls=ItemEncoder)
        return json_data, 201
    except Exception as e:
        logger_service.error(f"error in item controller: {e}")
        return jsonify({"message": f"Internal error"}), 500
