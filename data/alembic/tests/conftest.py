import pytest

from data.alembic.src.get_alembic_config import get_alembic_config


@pytest.fixture()
def alembic_config(memory_db_url):
    """
    Alembic configuration object, bound to temporary database.
    """
    return get_alembic_config(memory_db_url)
