from flask import render_template

from app import app
from data import menu


@app.route('/')
def index():
    return render_template('index.html', main_manu=menu)
