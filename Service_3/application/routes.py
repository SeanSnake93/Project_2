from application import app
from flask import request, Responce
from random import randrange

@app.route('/randomgenre', methods=['GET'])
def randomgenre():
    data = Genre.query.all().genre
    return Responce(data[randrange(len(data))], mimetype='text/plain')