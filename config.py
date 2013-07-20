from private_config import DATABASE_PASSWORD
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = "postgresql://switch:{0}@localhost:5432/switch".format(DATABASE_PASSWORD)
# The above probably isn't quite right, but will work as a starting point

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')