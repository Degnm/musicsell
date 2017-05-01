from flask import render_template

from app import app, db
from data import menu


@app.route('/')
def index():
    authors_count = db.engine.execute('''
    SELECT COUNT(*)
    FROM Artist
    ''')
    albums_count = db.engine.execute('''
    SELECT COUNT(*)
    FROM Album
    ''')
    genres_count = db.engine.execute('''
       SELECT COUNT(*)
       FROM Genre
       ''')
    return render_template('index.html', **{
        'author_count': authors_count.scalar(),
        'main_menu': menu,
        'album_count': albums_count.scalar(),
        'genre_count': genres_count.scalar(),
    })


@app.route('/artists')
def all_artists():
    artists = db.engine.execute('''
    SELECT *
    FROM Artist
    ''')
    return render_template('artists.html', artists=artists.fetchall())
