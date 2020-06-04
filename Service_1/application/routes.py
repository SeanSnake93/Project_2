from application import app
from flask import render_template, request
from random import randrange
import requests

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', title = 'Spinner - Movie Database')

@app.route('/movies', methods=['GET'])
def movies():
    movieRaw = Movies.query.all()
    movieData = movieRaw.movie_title.sort()
    return render_template('home.html', movie = movieData, title = 'Spinner - Movie List', form=form)

@app.route('/movies/create', methods=['GET','POST'])
@login_required
def add():
    """
    This Page is used to allow a Logged in User, add a Movie to the Tables.
    """
    form = MovieForm()
    if form.validate_on_submit():
        data = []
        data.append(form.title.data)
        data.append(form.year.data)
        data.append(form.director.data)
        data.append(form.genre1.data)
        data.append(form.genre2.data)
        data.append(form.genre3.data)
        data.append(form.genre4.data)
        data.append(form.genre5.data)
        data.append(form.rating.data)
        data.append(form.description.data)
        delivery = requests.post('http://service_2:5001/movies/create/add', filmData=data)
        if delivery == True:
            return redirect(url_for('Movies'))
        else:
            return redirect(url_for('movies/add_a_movie'))
    return render_template('movie_editing.html', title = 'Spinner - Movie Editing', form=form)

@app.route('/movies/edit/<filmID>', methods=['GET','POST'])
@login_required
def edit(filmID):
    """
    This Page is used to allow a Logged in User, add a Movie to the Tables.
    """
    form = MovieForm()
    film = Movies.query.filter_by(id=filmID).first()
    if form.validate_on_submit():
        data = []
        data.append(form.title.data)
        data.append(form.genre1.data)
        data.append(form.genre2.data)
        data.append(form.genre3.data)
        data.append(form.genre4.data)
        data.append(form.genre5.data)
        data.append(form.rating.data)
        data.append(form.description.data)
        url = 'http://service_2:5001/movies/edit/<filmID>/update'
        delivery = requests.post(url, filmData=data)
        if delivery == True:
            return redirect(url_for('Movies'))
        else:
            return redirect(url_for('movies/edit/<filmID>'))
    elif request.method =='GET':
        form.title.data = film.movie_title
        form.year.data = film.year
        form.director.data = film.director
        form.genre1.data = film.genre1
        form.genre2.data = film.genre2
        form.genre3.data = film.genre3
        form.genre4.data = film.genre4
        form.genre5.data = film.genre5
        form.description.data = film.description
    return render_template('movie_editing.html', title = 'Spinner - Movie Editing')

@app.route('/movies/remove', methods=['GET','POST'])
@login_required
def remove(filmID):
    """
    This will be used to allow a Logged in User to delete a Movie from the Moves Table.
    """
    url = 'http://service_2:5001/movies/remove/' + str(filmID)
    deliver = requests.post(url)
    print("Delivered: ", deliver)
    return redirect(url_for('Movies'))

@app.route('/movies/randomise', methods=['GET'])
def generate():
    generated = requests.get('http://service_2:5001/movies/randomise/generate').text
    print("Recived movie to display: ", generated)
    return render_template('home.html', movie = generated, title = 'Project 2 Generator')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html', title = 'About Project 2')

User Register

User Update

User Delete

Login

Logout