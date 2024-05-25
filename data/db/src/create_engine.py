import typing

from sqlalchemy import URL, create_engine as _create_engine, Engine


def create_engine(url: typing.Union[URL, str] = None) -> Engine:
    return _create_engine(url=url or "sqlite:///resources/local.sqlite", echo=False, pool_pre_ping=True)
