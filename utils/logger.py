import os
import logging
from logging.handlers import SysLogHandler

from dotenv import load_dotenv

load_dotenv()
config = os.environ

PAPERTRAIL_HOST = config.get("PAPERTRAIL_HOST")
PAPERTRAIL_PORT = int(config.get("PAPERTRAIL_PORT"))


def setup_logger() -> logging.Logger:
    logger = logging.getLogger("DEVICE_ID")
    logger.setLevel(logging.DEBUG)
    # handler = logging.StreamHandler()
    handler = SysLogHandler(address=(PAPERTRAIL_HOST, PAPERTRAIL_PORT))
    formatter = logging.Formatter("[%(asctime)s] [%(name)s] [%(levelname)s]\t %(message)s", "%Y-%m-%d %H:%M:%S")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
