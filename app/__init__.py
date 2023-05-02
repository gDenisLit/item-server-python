import os
from flask import Flask
from dotenv import load_dotenv
from app.api.item.item_controller import item_bp


def init_app():
    load_dotenv()
    
    app = Flask(__name__)
    port = os.getenv("PORT")
    debug = os.getenv("DEV_ENV")

    @app.route("/health", methods=["GET"])
    def health(): return "OK"

    app.register_blueprint(item_bp, url_prefix="/api/item")
    app.run(port=port, debug=debug)
