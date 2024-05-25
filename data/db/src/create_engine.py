import typing

from sqlalchemy import URL, create_engine as _create_engine, Engine


def create_engine(url: typing.Union[URL, str] = None, echo=False) -> Engine:
    return _create_engine(url=url or "sqlite:///resources/local.sqlite", echo=echo, pool_pre_ping=True)
