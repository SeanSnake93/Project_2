from application import app
from flask import render_template, request
import requests
import random

# Home is the basis of my project, a button that will take use of 3 additional Services to produce a random movie based of a Genre.

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    Generated = requests.get('http://localhost:5001/generate') # Requesting service 2 to Generate a responce from Services 3 and 4.
    print(response) # print/display the details expected on site in the terminal.
    Output = Generated.text # Display on site  the contents of Service 2.
    return render_template('home.html', Movie = Output, title = 'Project 2 Generater')

# About is a general overview of the project functions. Visit the about.html for more.

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html', title = 'About Project 2')