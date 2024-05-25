import pytest
from alembic.command import downgrade, upgrade
from alembic.config import Config
from alembic.script import Script, ScriptDirectory

from data.db.src.get_alembic_config import get_alembic_config


def get_revisions():
    config = get_alembic_config()

    revisions_dir = ScriptDirectory.from_config(config)

    revisions = list(revisions_dir.walk_revisions("base", "heads"))
    revisions.reverse()
    return revisions


@pytest.mark.parametrize("revision", get_revisions())
def test_migrations_stairway(alembic_config: Config, revision: Script):
    upgrade(alembic_config, revision.revision)
    downgrade(alembic_config, revision.down_revision or "-1")
    upgrade(alembic_config, revision.revision)
