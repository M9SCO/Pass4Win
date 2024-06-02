import typing

from sqlalchemy import URL, create_engine as _create_engine, Engine

from config import config


def create_engine(url: typing.Union[URL, str] = None, echo=False) -> Engine:
    return _create_engine(url=url or config.db_url, echo=echo, pool_pre_ping=True)
