import logging
import os

import alembic.command
import sqlalchemy_utils

from config import config
from data.db.src.create_engine import create_engine
from data.logger import make_logger


if __name__ == "__main__":
    make_logger()

    logging.info("loading app")

    if not os.path.isfile(config.db_file):
        logging.info("local db not found, creating local db")
        sqlalchemy_utils.create_database(create_engine().url)

    logging.info("load app success")
    logging.info("check updates")
    ...
