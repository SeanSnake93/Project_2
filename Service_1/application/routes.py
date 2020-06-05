from flask import render_template, request, redirect, url_for
from application import app, db, bcrypt
from application.models import Directors, Movies, Genres, GenreLink, Ratings, Users
from application.forms import MovieForm, UserLoginForm, UserRegisterForm, UserUpdateForm, GenreForm
from flask_login import login_user, current_user, logout_user, login_required
from random import randrange
import requests

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', title = 'Movie Database - Project 2')

@app.route('/movies', methods=['GET'])
def movies():
    movieRaw = Movies.query.all()
    movieData = movieRaw.movie_title.sort()
    return render_template('movies.html', movie = movieData, title = 'Movie List - Project 2', form=form)

@app.route('/movies/randomise', methods=['GET','POST'])
def generate():
    generated = requests.get('http://service_2:5001/movies/randomise/generate').text
    print("Recived movie to display: ", generated)
    return render_template('movie_gen.html', movie = generated, title = 'Movie Generator - Project 2')

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
        data.append(form.genre.genre1.data)
        data.append(form.genre.genre2.data)
        data.append(form.genre.genre3.data)
        data.append(form.genre.genre4.data)
        data.append(form.genre.genre5.data)
        data.append(form.rating.data)
        data.append(form.description.data)
        delivery = requests.post('http://service_2:5001/movies/create/add', filmData=data).text
        if delivery == True:
            return redirect(url_for('movies'))
        else:
            return redirect(url_for('movies/create'))
    return render_template('movie_editing.html', title = 'Movie Creating - Project 2', form=form)

@app.route('/movies/edit/<filmID>', methods=['GET','POST'])
@login_required
def edit(filmID):
    """
    This Page is used to allow a Logged in User, add a Movie to the Tables.
    """
    form = MovieForm()
    film = Movies.query.filter_by(id=filmID).first()
    filmGenre = GenreLink.query.filter_by(movie_id=filmID).all()
    filmDirector = Directors.query.filter_by(id=film.director).first()
    filmRating = Ratings.query.filter_by(id=film.rating).first()
    if form.validate_on_submit():
        data = []
        data.append(form.title.data)
        data.append(form.year.data)
        data.append(form.director.data)
        data.append(form.genre.genre1.data)
        data.append(form.genre.genre2.data)
        data.append(form.genre.genre3.data)
        data.append(form.genre.genre4.data)
        data.append(form.genre.genre5.data)
        data.append(form.rating.data)
        data.append(form.description.data)
        url = 'http://service_2:5001/movies/edit/<filmID>/update'
        delivery = requests.post(url, filmData=data).text
        if delivery == True:
            return redirect(url_for('movies'))
        else:
            return redirect(url_for('movies/edit/<filmID>'))
    elif request.method =='GET':
        form.title.data = film.movie_title
        form.year.data = film.year
        form.director.data = fimDirector.director
        form.genre.genre1.data = filmGenre[0]
        form.genre.genre2.data = filmGenre[1]
        form.genre.genre3.data = filmGenre[2]
        form.genre.genre4.data = filmGenre[3]
        form.genre.genre5.data = filmGenre[4]
        form.rating.data = filmRating.rating
        form.description.data = film.description
    return render_template('movie_editing.html', title = 'Movie Editing - Project 2')

@app.route('/movies/remove', methods=['GET','POST'])
@login_required
def remove(filmID):
    """
    This will be used to allow a Logged in User to delete a Movie from the Moves Table.
    """
    url = 'http://service_2:5001/movies/remove/' + str(filmID)
    deliver = requests.get(url).text
    print("Delivered: ", deliver)
    return redirect(url_for('movies'))

@app.route('/about', methods=['GET','POST'])
def about():
    return render_template('about.html', title = 'About - Project 2')

@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = UserRegisterForm()
    if form.validate_on_submit():
        data = []
        data.append(form.email.data)
        data.append(form.user_name.data)
        data.append(form.first_name.data)
        data.append(form.middle_names.data)
        data.append(form.surname.data)
        data.append(form.sex.data)
        data.append(str(form.age.data))
        hash_pw=bcrypt.generate_password_hash(form.password.data)
        delivery = requests.post('http://service_2:5001/register/user', userData=data, hashed=hash_pw, pin=form.remember.data).text
        if form.remember.data == True:
            return redirect(url_for('home'))
        else:
            return redirec(url_for('login'))
    return render_template('register.html', title = 'Register Project - 2')

@app.route('/user/update', methods=['GET','POST'])
@login_required
def user_update(userID):
    form = UserUpdateForm()
    my_user = current_user.id
    if form.validate_on_submit():
        data = []
        data.append(form.first_name.data)
        data.append(form.middle_names.data)
        data.append(form.surname.data)
        data.append(form.sex.data)
        url = 'http://service_2:5001//user/update/<userID>'
        delivery = requests.post(url, userData=data).text
        if delivery == True:
            return redirect(url_for('movies'))
        else:
            return redirect(url_for('user/update'))
    elif request.method =='GET':
        form.first_name.data = my_user.first_name
        form.middle_names.data = my_user.middle_names
        form.surname.data = my_user.surname
        form.sex.data = my_user.sex
    return render_template('user_update.html', title = 'Update Account - Project 2')

@app.route('/user/delete', methods=['GET','POST'])
@login_required
def user_delete(uderID):
    remove_user = requests.get('http://service_2:5001/register/user/delete/<userID>').text
    return redirect(url_for('home'))

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = UserLoginForm()
    if form.validate_on_submit():
        delivery = requests.post('http://service_2:5001/login/user', email=form.email.data, hashed=hash_pw, pin=form.remember.data).text
        next_page = request.args.get('next')
        if next_page:
            return redirect(next_page)
        else:
            return redirect(url_for('home'))
    return render_template('login.html', title = 'Login - Project 2')

@app.route('/logout', methods=['GET','POST'])
@login_required
def logging_out():
    status = requests.get('http://service_2:5001/logout/user/confirm').text
    logout_user()
    return redirect(url_for('home'))