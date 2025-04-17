import logging
from logging.handlers import RotatingFileHandler
from app.config import APP_ENV


def setup_logging():
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    environment = APP_ENV

    if environment == 'production':
        log_level = logging.INFO
        log_file = "app_logs_prod.log"
    else:
        log_level = logging.DEBUG
        log_file = "app_logs_dev.log"

    logging.basicConfig(
        level=log_level,
        format=log_format,
        handlers=[
            logging.StreamHandler(),
            RotatingFileHandler(log_file, maxBytes=10000000, backupCount=5)
        ]
    )
