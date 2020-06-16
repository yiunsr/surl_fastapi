from __future__ import with_statement

import os
import sys

from alembic import context
from alembic.config import Config
from alembic.script.base import ScriptDirectory
from alembic.runtime.environment import EnvironmentContext

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from sqlalchemy.engine import create_engine

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


try:
    config = context.config  # noqa
except Exception:
    ini_path = os.path.join(
         os.path.dirname(
             os.path.abspath(__file__)), "../alembic.ini")
    ini_path = os.path.abspath(ini_path)
    config = Config(ini_path)


from config.env_config import AppConfig
from app.db.base import Base  # noqa

target_metadata = Base.metadata

def get_url():
    return AppConfig.DATABASE_URL


def run_migrations_offline():
    """Run migrations in 'offline' mode.
    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.
    Calls to context.execute() here emit the given string to the
    script output.
    """
    print("== offline ==")
    global config
    url = get_url()
    script = ScriptDirectory.from_config(config)

    def do_upgrade(revision, context):
        return script._upgrade_revs(script.get_heads(), revision)

    env = EnvironmentContext(config, script=script)
    connectable = create_engine(url)
    connection = connectable.connect()
    config = env.configure(
        url=url, target_metadata=target_metadata,
        fn=do_upgrade,
        dialect_name="postgresql",
        transactional_ddl=False,
        as_sql=False,
        connection=connection,
        )
    context = env.get_context()

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.
    In this scenario we need to create an Engine
    and associate a connection with the context.
    """
#     connectable = engine_from_config(
#         config.get_section(config.config_ini_section),
#         prefix='sqlalchemy.',
#         poolclass=pool.NullPool)
    global config
    script = ScriptDirectory.from_config(config)
    env = EnvironmentContext(config, script=script)

    def do_upgrade(revision, context):
        return script._upgrade_revs(script.get_heads(), revision)

    url = get_url()
    connectable = create_engine(url)
    with connectable.connect() as connection:
        config = env.configure(
            connection=connection,
            url=url, target_metadata=target_metadata,
            )

        with context.begin_transaction():
            context.run_migrations()



if __name__ == '__main__':
    run_migrations_offline()
else:
    if context.is_offline_mode():
        run_migrations_offline()
    else:
        run_migrations_online()