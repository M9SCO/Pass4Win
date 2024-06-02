import typing
import types

import alembic.config

from data.alembic.src.alembic_get_revisions import make_alembic_config


def get_alembic_config(url: typing.Optional[str] = None) -> alembic.config.Config:
    """
    Provides Python object, representing alembic.ini file.
    """
    cmd_options = types.SimpleNamespace(
        config="alembic.ini",
        name="alembic",
        pg_url=url,
        raiseerr=False,
        x=None,
    )

    return make_alembic_config(cmd_options)
