import logging


def main() -> None:
    logging.basicConfig(
        level=logging.DEBUG,
        format="[%(asctime)s] [%(levelname)s]\t %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename="basic-logs.log",
    )

    logging.info("Who just meets a guy and moves him right away?")
    logging.debug("Who just meets a guy and moves him right away?")
    logging.warning("Who just meets a guy and moves him right away?")
    logging.error("Who just meets a guy and moves him right away?")


if __name__ == "__main__":
    main()