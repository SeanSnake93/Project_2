from flask import request, redirect
from application import app, db, bcrypt
from application.models import Directors, Movies, Genres, GenreLink, Ratings, Users
from flask_login import login_user, current_user, logout_user, login_required
from random import randrange
import requests

# ------- START - Functions -------

def rating_check(submitting):
    """
    Taking the data from the Rrouts table. Checking to see if what is submitted matches content in Genre.genre field.
    """
    confirm = ""
    ratings_content = Ratings.query.all()
    ratings = ratings_content.rating
    if submitting == "":
        return confirm
    else:
        for rating in ratings:
            if submitting in rating:
                confirm = submitting
            else:
                continue
    return confirm

# ------- END --- Functions -------

@app.route('/movies/randomise/generate/<genre>', methods=['GET', 'POST'])
def generate_movie_content(genre):
    filt = []
    movies = Movies.query.all()
    for movie in movies:
        if genre in movie:
            title = movie.movie_title
            filt.append(title)
            print(title, "has been appended.")
        else:
            continue
    ranger = len(filt)
    return filt[randrange(ranger)]

@app.route('/movies/create/add/<filmID>', methods=['GET','POST'])
@login_required
def add_movie_content(title, year, director, rating, description):
    """
    This Page is used to allow a Logged in User, add a Movie to the Tables.
    """
    if form.validate_on_submit():
        directors = Directors.query.all()
        create_director = True
        for entry in directors:
            if director in entry:
                create_director = False
            else:
                continue
        if create_director == True:
            directorCreate = Directors(
                director = director
            )
            db.session.add(directorCreate)
        db.session.commit()
        directorData = Directors.query.filter_by(director=director).first()
        check_rating = rating_check(rating)
        ratingData = Ratings.query.filter_by(rating=check_rating).first()
        if ratingData != None:
            moviesData = Movies(
                movie_title = title,
                year = year,
                director = directorData.id,
                rating = ratingData.id,
                description = description
            )
            db.session.add(moviesData)
    db.session.commit()
    return True

@app.route('/movies/edit/<filmID>/update/movie', methods=['GET','POST'])
@login_required
def change_movie_content(title, year, director, rating, description):
    """
    This Page is used to allow a Logged in User, add a Movie to the Tables.
    """
    if form.validate_on_submit():
        directors = Directors.query.all()
        create_director = True
        for entry in directors:
            if director in entry:
                create_director = False
            else:
                continue
        if create_director == True:
            directorCreate = Directors(
                director = director
            )
            db.session.add(directorCreate)
        db.session.commit()
        directorData = Directors.query.filter_by(director=director).first()
        check_rating = rating_check(rating)
        ratingData = Ratings.query.filter_by(rating=check_rating).first()
        if ratingData != None:
            moviesData = Movies(
                movie_title = title,
                year = year,
                director = directorData.id,
                rating = ratingData.id,
                description = description
            )
            db.session.add(moviesData)
    db.session.commit()
    return True

@app.route('/movies/remove/<filmID>/movie', methods=['GET','POST'])
@login_required
def remove_movie_content(filmID):
    movieData = Movies.query.filter_by(id=filmID).first()
    db.session.delete(movieData)
    db.session.commit()
    return True