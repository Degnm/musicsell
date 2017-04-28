import os

from flask import Flask

DEBUG = True

app = Flask(__name__, static_folder='node_modules', static_url_path='/node_modules')
app.config.from_object(__name__)

import views
