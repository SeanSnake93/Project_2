import requests, json
from flask import render_template, request, redirect, url_for, jsonify
from application import app, db, bcrypt
from application.models import Directors, Movies, Genres, GenreLink, Ratings, Users
from application.forms import MovieForm, UserLoginForm, UserRegisterForm, UserUpdateForm, GenreForm
from flask_login import login_user, current_user, logout_user, login_required
import requests

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title = 'Movie Cluster')

@app.route('/movies', methods=['GET','POST'])
def movies():
    url = requests.post('http://service_2:5001/diagnose/', tag="movies-table-all-sort").text
    allMovieData = requests.post(url).text
    return render_template('movies.html', movies=allMovieData, title = 'Movie Cluster - Library')

@app.route('/movies/randomise', methods=['GET','POST'])
def generate():
    url = requests.post('http://service_2:5001/diagnose/' tag="movies-table-random").text
    url = requests.get(url).text
    return render_template('movie_gen.html', generated=movie, title = 'Movie Cluster - Generator)

@app.route('/movies/create', methods=['GET','POST'])
def add():
    form = MovieForm()
    if form.validate_on_submit():
        url = requests.post('http://service_2:5001/diagnose', tag="movies-table-add").text
        formData = {'title':str(form.movie_title.data), 'year':str(form.year.data), 'sequal':str(form.sequal.data), 'director':str(form.director.data), 'genre1':str(form.genre1.data), 'genre3':str(form.genre3.data), 'genre4':str(form.genre4.data), 'genre5':str(form.genre5.data), 'rating':str(form.rating.data), 'description':str(form.descriptionyear.data)}
        packet = requests.post(url, data=formData).json
    return render_template('movie_editing.html', title = 'Movie Creating - Project 2', form=form)

@app.route('/movies/edit/<filmID>', methods=['GET','POST'])
def edit(movieID):
    """
    This Page is used to allow a Logged in User, add a Movie to the Tables.
    """
    form = MovieForm()
    url = requests.post('http://service_2:5001/diagnose', tag="movies-table-edit").text
    movieData = requests.post(url).text
    movie = Movies.query.filter_by(id=movieID).first()
    genres = []
    movieGenres = GenreLink.query.filter_by(movie_id=movieID).all()
    for Genre in movieGenres:
        if genre not in genres:
            genres.append(genre)
    staff = []
    filmStaff = RecordsLink.query.filter_by(id=film.id).all()





    filmRating = Ratings.query.filter_by(id=film.rating).first()
    if form.validate_on_submit():
        url = requests.post('http://service_2:5001/diagnose', tag="movies-table-edit").text
        formData = {'title':str(form.movie_title.data), 'year':str(form.year.data), 'sequal':str(form.sequal.data), 'director':str(form.director.data), 'genre1':str(form.genre1.data), 'genre3':str(form.genre3.data), 'genre4':str(form.genre4.data), 'genre5':str(form.genre5.data), 'rating':str(form.rating.data), 'description':str(form.descriptionyear.data)}
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
    return render_template('movie_editing.html', title = 'Movie Editing - Project 2', form=form)

@app.route('/movies/remove', methods=['GET','POST'])
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
        hash_pw=bcrypt.generate_password_hash(form.password.data)
        delivery = f.put('http://service_2:5001/register/user', username=form.user_name.data, email=form.email.data, first=form.first_name.data, middle=form.middle_names.data, last=form.surname.data, sex=form.sex.data, age=(str(form.age.data)), hashed=hash_pw, pin=form.remember.data).json
        if form.remember.data == True:
            return redirect(url_for('home'))
        else:
            return redirec(url_for('login'))
    return render_template('register.html', title = 'Register Project - 2', form=form)

@app.route('/user/update', methods=['GET','POST'])
def user_update(userID):
    form = UserUpdateForm()
    if form.validate_on_submit():
        userData = {'first':form.first_name.data, 'middle':form.middle_names.data, 'last':form.surname.data, 'sex':form.sex.data}
        delivery = requests.post('http://service_2:5001//user/update/<userID>', userData=userData).text
        if delivery == True:
            return redirect(url_for('movies'))
        else:
            return redirect(url_for('user/update'))
    elif request.method =='GET':
        form.first_name.data = current_user.first_name
        form.middle_names.data = current_user.middle_names
        form.surname.data = current_user.surname
        form.sex.data = current_user.sex
    return render_template('user_update.html', title='Update Account - Project 2', form=form)

@app.route('/user/delete', methods=['GET','POST'])
def user_delete(userID):
    remove_user = requests.get('http://service_2:5001/register/user/delete/<userID>').text
    return redirect(url_for('home'))

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = UserLoginForm()
    if form.validate_on_submit():
        hash_pw=bcrypt.generate_password_hash(form.password.data)
        delivery = requests.post('http://service_2:5001/login/user', email=form.email.data, hashed=hash_pw, pin=form.remember.data).text
        next_page = request.args.get('next')
        if next_page:
            return redirect(next_page)
        else:
            return redirect(url_for('home'))
    return render_template('login.html', title = 'Login - Project 2', form=form)

@app.route('/logout', methods=['GET','POST'])
def logging_out():
    status = requests.get('http://service_2:5001/logout/user/confirm').text
    logout_user()
    return redirect(url_for('home'))