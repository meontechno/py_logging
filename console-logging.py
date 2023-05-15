import logging


def main() -> None:
    logging.basicConfig(
        level=logging.WARNING,
        format="[%(asctime)s] [%(levelname)s]\t %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    logging.info("Two worlds are colliding")
    logging.warning("Two worlds are colliding")
    logging.error("Two worlds are colliding")


if __name__ == "__main__":
    main()