import pytest
from alembic.command import downgrade, upgrade
from alembic.config import Config
from alembic.script import Script

from data.alembic.src.get_revisions import get_revisions


@pytest.mark.parametrize("revision", get_revisions())
def test_migrations_stairway(alembic_config: Config, revision: Script):
    upgrade(alembic_config, revision.revision)
    downgrade(alembic_config, revision.down_revision or "-1")
    upgrade(alembic_config, revision.revision)
