import os


class Config:
    def __init__(self):
        self.db_uri = os.getenv("ATLAS_URL")
        self.db_name = os.getenv("DB_NAME")
        self.secret_key = os.getenv("CRYPTER_KEY")
        self.port = os.getenv("PORT")
        self.dev_env = os.getenv("DEV_ENV")
        self.algo = os.getenv("ENCODE_ALGO")
