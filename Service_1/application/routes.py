from application import app
from application.models import Genres, Movies, Generated
from flask import render_template
import requests

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    generated = requests.get('http://service_2:5001/generate').text # Requesting service 2 to Generate a responce from Services 3 and 4.
    return render_template('home.html', movie = generated, title = 'Generator')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html', title = 'About')

@app.route('/history', methods=['GET'])
def history():
    logs = Generated.query.all()
    return render_template('history.html', history=logs, title = 'Gen History')

@app.route('/sql_data', methods=['GET'])
def sql_data():
    options = Genres.query.all()
    library = Movies.query.all()
    return render_template('movies_and_genre.html', movies=library, genres=options, title = 'Project 2 Data')