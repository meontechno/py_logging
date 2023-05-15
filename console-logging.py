import logging


def main() -> None:
    logging.basicConfig(
        level=logging.WARNING,
        format="[%(asctime)s] [%(levelname)s]\t %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    logging.info("Enjoy this? Rating helps us know if we should recommend more like this.")
    logging.warning("Enjoy this? Rating helps us know if we should recommend more like this.")
    logging.error("Enjoy this? Rating helps us know if we should recommend more like this.")


if __name__ == "__main__":
    main()