from flask import jsonify, Blueprint, request
from app.services import logger
from app.models.User_model import User

user_bp = Blueprint("user", __name__)
