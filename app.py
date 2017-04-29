import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % \
                          os.path.join(BASE_DIR, 'Chinook_Sqlite.sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS = True
DEBUG = True

app = Flask(__name__, static_folder='node_modules', static_url_path='/node_modules')
app.config.from_object(__name__)
db = SQLAlchemy(app)

import views
