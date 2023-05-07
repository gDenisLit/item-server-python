from .db_service import DbService
from app.services.logger_service import LoggerService
from .response_service import ResponseService

db = DbService()
logger = LoggerService().logger
response = ResponseService()
