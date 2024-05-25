import pytest
from sqlalchemy import Engine
from sqlalchemy.orm import sessionmaker

from data.db.src.create_engine import create_engine
from data.db.src.create_session_maker import create_session_maker
from data.db.src.get_alembic_config import get_alembic_config


@pytest.fixture
def memory_db_url() -> str:
    return "sqlite://"


@pytest.fixture
def test_engine(memory_db_url) -> Engine:
    engine = create_engine(memory_db_url)

    try:
        yield engine
    finally:
        engine.dispose()


@pytest.fixture()
def alembic_config(memory_db_url):
    """
    Alembic configuration object, bound to temporary database.
    """
    return get_alembic_config(memory_db_url)
