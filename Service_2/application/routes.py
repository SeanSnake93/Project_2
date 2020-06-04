from application import app
from random import randrange
import requests


@app.route('/generate', methods=['GET'])
def generate():
    genre = requests.get('http://service_3:5002/randomgenre').text # Call Service 3 to to return a Genre to filter a Movie form Service 4.
    print("Service 3 Output:", genre) # Print/Display selection on Terminal.
    url = 'http://service_4:5003/' + genre # Create a variable to hold the new URL to be requested against.
    movie = requests.get(url).text # With the Genre defined, filter a Movie in Service 4 related to this Genre.
    print("Service 4 Output:", movie) # Print the Movie found in Service 4.
    return "We have selected " + movie + " from our " + genre + " Collection." # The Responce being sent back to be displayed on site.