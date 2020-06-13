from application import app # Import the app into routes
from flask import render_template, request # Allow Flask to display a front end webpage and enable the site to cope with requests to popen pages
import requests # enables the site to ask external locations for data


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET']) # Nothing is being sent, only recived so this is not a POST
def home():
    generated = requests.get('http://service_2:5001/generate').text # Requesting service 2 to Generate a responce from Services 3 and 4 and return it.
    return render_template('home.html', movie = generated, title = 'Project 2 Generator') # display the content recived on the home page with a title Project 2 Generator.

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html', title = 'About Project 2') # Just displays the contents of about.html with a title About Project 2.