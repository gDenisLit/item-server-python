from dotenv import load_dotenv
from .db_service import DbService
from app.services.logger_service import LoggerService

load_dotenv()
db_service = DbService()
logger = LoggerService().logger
