from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask_openid import OpenID
import os
from config import basedir

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))

from app import time_machine, blog, models





