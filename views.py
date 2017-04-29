from flask import render_template

from app import app, db
from data import menu


@app.route('/')
def index():
    authors_count = db.engine.execute('''
    SELECT COUNT(*)
    FROM Artist
    ''')
    return render_template('index.html', **{
        'author_count': authors_count.scalar(),
        'main_menu': menu,
    })
