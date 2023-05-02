import os
import logging


class LoggerService:
    logs_dir = "./logs"
    logger = None


    def __init__(self):
        if not os.path.exists(self.logs_dir):
            os.makedirs(self.logs_dir)

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        fh = logging.FileHandler(os.path.join(self.logs_dir, "backend.log"))
        fh.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s")

        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
