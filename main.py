import logging

from data.logger import make_logger

if __name__ == "__main__":
    make_logger()

    logging.info("loading app")
    ...
    logging.info("load app success")
    logging.info("check updates")
    ...
