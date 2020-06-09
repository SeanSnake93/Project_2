import requests, json
from flask import request, redirect, url_for, jsonify
from application import app, db, bcrypt
from application.models import Directors, Movies, Genres, GenreLink, Ratings, Users
from flask_login import login_user, current_user, logout_user, login_required
import requests


@app.route('/movies/randomise/generate', methods=['GET'])
def generate_movie():
    genre = requests.get('http://service_3:5002/movies/randomise/generate/random_genre').text # Call Service 3 to to return a Genre to filter a Movie form Service 4.
    print("Service 3 Output:", genre) # Print/Display selection on Terminal.
    url = 'http://service_4:5003/movies/randomise/generate/' + genre # Create a variable to hold the new URL to be requested against.
    movie = requests.get(url).text # With the Genre defined, filter a Movie in Service 4 related to this Genre.
    print("Service 4 Output:", movie) # Print the Movie found in Service 4.
    return "We have selected " + movie + " from our " + genre + " Collection." # The Responce being sent back to be displayed on site.

@app.route('/movies/create/add', methods=['GET', 'POST'])
def add_movie(filmData):
    url = 'http://service_4:5003/movies/create/add/' + filmData[0]
    status = requests.post(url, title=filmData[0], year=filmData[1], director=filmData[2], rating=filmData[8], description=filmData[9]).text # With the Genre defined, filter a Movie in Service 4 related to this Genre.
    print("Movie Added:", status)
    if status == False:
        return status
    else:
        filmID = Movies.query.filter_by(movie_title=filmData[0]).first().id
        url = 'http://service_3:5002/movies/create/add/' + str(filmID)
        status = requests.post(url, genre1=filmData[3], genre2=filmData[4], genre3=filmData[5], genre4=filmData[6], genre5=filmData[7]).text
        print("Genres Added:", status)
        return status

@app.route('/movies/edit/<filmID>/update', methods=['GET', 'POST'])
def change_movie(filmData):
    status = requests.post('http://service_4:5003/movies/edit/<filmID>/update/movie', title=filmData[0], year=filmData[1], director=filmData[2], rating=filmData[8], description=filmData[9]).text # With the Genre defined, filter a Movie in Service 4 related to this Genre.
    print("Movie Added:", status)
    if status == False:
        return status
    else:
        filmID = Movies.query.filter_by(movie_title=filmData[0]).first().id
        status = requests.post('http://service_3:5002/movies/edit/<filmID>/update/genre', genre1=filmData[3], genre2=filmData[4], genre3=filmData[5], genre4=filmData[6], genre5=filmData[7]).text
        print("Genres Added:", status)
        return status

@app.route('/movies/remove/<filmID>', methods=['GET', 'POST'])
def remove_movie(filmID):
    genrelinkData = GenreLink.query.filter_by(movie_id=filmID).all().id
    deleted = requests.post('http://service_3:5002/movies/remove/<filmID>/genre', remove=genrelinkData).text
    print("Links Deleted: ", deleted)
    deleted = requests.post('http://service_4:5003/movies/remove/<filmID>/movie', remove=genrelinkData).text
    print("Movie Deleted: ", deleted)
    return True

@app.route('/register/user', methods=['GET', 'POST'])
def register_user():
    data = request.get_json()
    status = requests.post('http://service_5:5004/register/user/create', data=data).text # sending dump, getting back True
    print('Status: ', status)
    if status == 'True':
        json_data = data # json data = dump
        logged_in = login_user(data={'email':json_data['email'], 'password':json_data['password'], 'remember':json_data['remember']})
        return logged_in
    else:
        return status

@app.route('/user/update/<userID>', methods=['GET', 'POST'])
def user_update_content(userID, userData):
    changes = requests.post('http://service_5:5004/user/update/<userID>/commit', userID=userID, userData=userData).text
    return render_template('user_update.html', title = 'Update Account - Project 2')

@app.route('/user/delete/<userID>', methods=['GET', 'POST'])
def user_delete_content(userID):
    remove = Users.query.filter_by(id=userID).first()
    terminated = requests.post('http://service_5:5004/user/delete/<userID>/commit', userID=userID, account=remove).text
    return terminated

@app.route('/login/user', methods=['GET', 'POST'])
def login_user(data):
    status = requests.post('http://service_5:5004/login/user/varify', data=data)
    print('status: ', status)
    return status

@app.route('/logout/user', methods=['GET'])
def logging_out_user():
    status = requests.get('http://service_5:5004/logout/user/confirm').text
    logout_user()
    return status