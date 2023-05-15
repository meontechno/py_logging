import os
import logging
from logging.handlers import SysLogHandler

from dotenv import load_dotenv

load_dotenv()
config = os.environ

PAPERTRAIL_HOST = config.get("PAPERTRAIL_HOST")
PAPERTRAIL_PORT = config.get("PAPERTRAIL_PORT")


def main() -> None:
    logger = logging.getLogger("galaxy")
    logger.setLevel(logging.DEBUG)
    handler = SysLogHandler(address=(PAPERTRAIL_HOST, PAPERTRAIL_PORT))
    logger.addHandler(handler)

    logger.info("Enjoy this? Rating helps us know if we should recommend more like this.")


if __name__ == "__main__":
    main()