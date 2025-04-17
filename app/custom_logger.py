import logging


def get_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(log_format))
    logger.addHandler(handler)
    return logger
