from flask import Flask
from .config import config
from .api import routes
from .services import response


class ItemServer:
    def __init__(self):
        self.app = Flask(__name__)
        self.port = config.port
        self.debug = config.dev_env

        self.register_routes()

    def register_routes(self):
        @self.app.route("/health", methods=["GET"])
        def health(): return response.success()

        self.app.register_blueprint(**routes.item)
        self.app.register_blueprint(**routes.auth)
        self.app.register_blueprint(**routes.user)

    def run(self):
        self.app.run(
            port=self.port,
            debug=self.debug
        )
