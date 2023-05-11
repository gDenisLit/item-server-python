from .auth_middleware import require_auth
from .logger_middleware import log_request
from .storage_middleware import store
from .admin_middleware import require_admin


class Middlewares:
    log = log_request
    auth = require_auth
    store = store
    admin = require_admin
