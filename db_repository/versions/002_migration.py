from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
interval = Table('interval', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('category', String(length=32)),
    Column('start', Integer),
    Column('stop', Integer),
    Column('elapsed', Integer),
    Column('note', String(length=255)),
    Column('user_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['interval'].columns['user_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['interval'].columns['user_id'].drop()
