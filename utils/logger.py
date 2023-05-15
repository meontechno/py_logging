import logging
from logging.handlers import SysLogHandler

def setup_logger() -> None:
    logger = logging.getLogger("Custom Logger")
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    # handler = SysLogHandler(address=(PAPERTRAIL_HOST, PAPERTRAIL_PORT))
    formatter = logging.Formatter("[%(asctime)s] [%(name)s] [%(levelname)s]\t %(message)s", "%Y-%m-%d %H:%M:%S")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


