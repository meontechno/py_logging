import logging
from logging.handlers import SysLogHandler

PAPERTRAIL_HOST = "logs2.papertrailapp.com"
PAPERTRAIL_PORT = 12686


def main() -> None:
    logger = logging.getLogger("galaxy")
    logger.setLevel(logging.DEBUG)
    handler = SysLogHandler(address=(PAPERTRAIL_HOST, PAPERTRAIL_PORT))
    logger.addHandler(handler)

    logger.info("Monte Rissle beaten and drowned")


if __name__ == "__main__":
    main()