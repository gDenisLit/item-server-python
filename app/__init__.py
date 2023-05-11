from flask import Flask
from .config import config
from .api import Blueprints
from .services import response
from .middlewares.storage_middleware import store
# from .middlewares.logger_middleware import logger_middleware


class ItemServer:
    def __init__(self):
        self.app = Flask(__name__)
        self.port = config.port
        self.debug = config.dev_env

        self.register_routes()

    def register_routes(self):
        @self.app.route("/health", methods=["GET"])
        def health(): return response.success()

        self.app.before_request(store)

        self.app.register_blueprint(**Blueprints.item)
        self.app.register_blueprint(**Blueprints.auth)
        self.app.register_blueprint(**Blueprints.user)

    def run(self):
        self.app.run(
            port=self.port,
            debug=self.debug
        )
