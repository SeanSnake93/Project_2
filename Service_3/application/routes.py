from application import app, db
from application.models import Genres
from flask import request, Response
from random import randint

@app.route('/randomgenre', methods=['GET', 'POST'])
def randomgenre():
    length = Genres.query.count() #Count number of records in genre
    ran = randint(1, length) # Generate random num between 1 and length
    genreRow = Genres.query.filter_by(id = ran).first() # Find genreID and genre where genre ID = random number
    return genreRow.genre # Return random genre