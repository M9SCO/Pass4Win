import pytest
from sqlalchemy import Engine

from data.db.src.create_engine import create_engine


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
