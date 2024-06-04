import typing

from alembic.script import ScriptDirectory

from data.alembic.src.get_alembic_config import get_alembic_config


def get_revisions(url: typing.Optional[str] = None):
    config = get_alembic_config(url=url)

    revisions_dir = ScriptDirectory.from_config(config)

    revisions = list(revisions_dir.walk_revisions("base", "heads"))
    revisions.reverse()
    return revisions
