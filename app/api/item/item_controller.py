from flask import jsonify, Blueprint, request
from .item_service import ItemService

item_bp = Blueprint("item", __name__)


@item_bp.route("/", methods=["GET"])
async def get_items():
    try:
        items = await ItemService.query()
        return jsonify(items), 200
    except Exception as e:
        print(f"error: {e}")
        return jsonify({"message": f"Internal error"}), 500


@item_bp.route("/<item_id>", methods=["GET"])
async def get_item_by_id(item_id):
    try:
        item = await ItemService.get_by_id(item_id)
        return jsonify(item), 200
    except Exception as e:
        print(f"error: {e}")
        return jsonify({"message": f"Internal error"}), 500


@item_bp.route("/<item_id>", methods=["DELETE"])
async def remove_item(item_id):
    try:
        id = await ItemService.remove_item(item_id)
        return jsonify({"removedId": id}), 201
    except Exception as e:
        print(f"error: {e}")
        return jsonify({"message": f"Internal error"}), 500


@item_bp.route("/", methods=["POST"])
async def add_item():
    try:
        body = request.get_json()
        item = await ItemService.add_item(body)
        return jsonify(item), 201
    except Exception as e:
        print(f"error: {e}")
        return jsonify({"message": f"Internal error"}), 500


@item_bp.route("/", methods=["PUT"])
async def update_item():
    try:
        body = request.get_json()
        item = await ItemService.update_item(body)
        return jsonify(item), 201
    except Exception as e:
        print(f"error: {e}")
        return jsonify({"message": f"Internal error"}), 500
