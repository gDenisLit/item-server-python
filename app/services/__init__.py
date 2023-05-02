from dotenv import load_dotenv
from .db_service import DbService

load_dotenv()
db_service = DbService()
