from application import app, db
from flask import request, Response, jsonify
from application.models import Generated
import requests

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    movie = "failed"
    while movie == "failed":
        ggenre = requests.get("http://service_3:5002/randomgenre").text # Call Service 3 to to return a Genre to filter a Movie form Service 4.
        movie = requests.post("http://service_4:5003/movie", ggenre).text # With the Genre defined, filter a Movie in Service 4 related to this Genre.
        generatedData = Generated(title = movie, genre = ggenre)
    db.session.add(generatedData)
    db.session.commit()
    return Response("We have selected " + movie + " from our " + ggenre + " Collection.") # The Responce being sent back to be displayed on site.
