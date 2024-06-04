import logging
import os

from alembic.command import upgrade
from sqlalchemy import select

from config import config
from data.alembic.src.get_alembic_config import get_alembic_config
from data.alembic.src.get_revisions import get_revisions
from data.db.models import AlembicVersion
from data.db.src.open_session import open_session
from data.logger import make_logger

if __name__ == "__main__":
    make_logger()

    logging.info("loading app")

    revisions = get_revisions()
    alembic_config = get_alembic_config()
    if not os.path.isfile(config.db_file):
        logging.info("local db not found, creating local db")
        # sqlalchemy_utils.create_database(config.db_url)
        [upgrade(alembic_config, revision.revision) for revision in get_revisions()]

    logging.info("check actual db version")
    with open_session() as session:
        current_version = session.execute(select(AlembicVersion.version_num)).one()[0]
        if current_version != revisions[-1].revision:
            logging.info("db version is not actual, updating")
            needed = []
            for revision in revisions[::-1]:
                if revision.revision == current_version:
                    break
                needed.append(revision.revision)
            for revision in needed[::-1]:
                upgrade(alembic_config, revision)


    logging.info("load app success")
    logging.info("check updates")
    ...
