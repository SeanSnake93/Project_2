from application import app
from application.models import Genres, Movies, Generated
from flask import render_template
from random import randrange
import requests

# Home is the basis of my project, a button that will take use of 3 additional Services to produce a random movie based of a Genre.

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    generated = requests.get('http://service_2:5001/generate').text # Requesting service 2 to Generate a responce from Services 3 and 4.
    print("Recived movie to display: ", generated) # print/display the details expected on site in the terminal.
    return render_template('home.html', movie = generated, title = 'Generator')

# About is a general overview of the project functions. Visit the about.html for more.

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