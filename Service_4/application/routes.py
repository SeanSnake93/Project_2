from application import app, db
from application.models import Movies
from flask import request, Response, jsonify
from random import randrange
import requests

@app.route('/movie', methods=['GET', 'POST'])
def generatemovie():
    movie = []
    genre = request.data.decode("utf-8")
    films = Movies.query.filter_by(genre1=genre).all()
    films += Movies.query.filter_by(genre2=genre).all()
    films += Movies.query.filter_by(genre3=genre).all()
    films += Movies.query.filter_by(genre4=genre).all()
    films += Movies.query.filter_by(genre5=genre).all()
    if len(films) >= 1:
        for film in films:
            movie.append(film.movie_title)
        return str(movie[randrange(len(movie))])
    else:
        return "failed"
