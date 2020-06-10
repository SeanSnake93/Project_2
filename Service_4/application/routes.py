from application import app, db
from application.models import Movies
from flask import request, Response, jsonify
from random import randrange
import requests

@app.route('/movie', methods=['GET', 'POST'])
def generatemovie():
    movie = Movies.query.filter_by(genre1 = request.data.decode("utf-8")).first()
    return movie.movie_title