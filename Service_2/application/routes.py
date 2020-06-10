from application import app
from flask import request, Response, jsonify
from random import randrange
import requests

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    genre = requests.get("http://service_3:5002/randomgenre").text # Call Service 3 to to return a Genre to filter a Movie form Service 4.
    print("Service 3 code:", genre) # Print/Display responce code on Terminal.#
    movie = requests.post("http://service_4:5003/movie", genre).text # With the Genre defined, filter a Movie in Service 4 related to this Genre.
    # movie = response.json()
    # add generated list table
    return Response("We have selected " + movie + " from our " + genre + " Collection.") # The Responce being sent back to be displayed on site.