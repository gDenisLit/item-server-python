from pymongo import MongoClient
import os


class DbService:
    def __init__(self):
        self.db = None
        self.connect()

    def connect(self):
        db_url = os.getenv("ATLAS_URL")
        db_name = os.getenv("DB_NAME")

        if not db_url or not db_name:
            raise ValueError("Missing dbUrl or dbName")

        self.db = MongoClient(db_url)[db_name]

    def get_collection(self, collection_name):
        return self.db[collection_name]
