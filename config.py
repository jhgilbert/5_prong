from private_config import DATABASE_PASSWORD
from private_config import SECRET_CSRF_KEY
import os
basedir = os.path.abspath(os.path.dirname(__file__))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URI = "postgresql://switch:{0}@localhost:5432/switch".format(DATABASE_PASSWORD)
# The above probably isn't quite right, but will work as a starting point

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# in case I wind up using the sessionmaker ...

switch_engine = create_engine("postgresql://switch:{0}@localhost:5432/switch".format(DATABASE_PASSWORD))

Session = sessionmaker(bind=switch_engine)

CSRF_ENABLED = True
SECRET_KEY = SECRET_CSRF_KEY
