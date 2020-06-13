from application import app # Import the app into routes
import requests # Enables the site to ask external locations for data

@app.route('/generate', methods=['GET'])
def generate():
    genre = requests.get('http://service_3:5002/randomgenre').text # Request Servive 3 to produce a random Genre.
    url = 'http://service_4:5003/' + genre # With the responce from Service 3 creat an API to request data from Service 4.
    movie = requests.get(url).text # With the API created, filter a Movie from Service 4 that matches the Genre recived. It is a GET request as data is sent through the API.
    return "We have selected " + movie + " from our " + genre + " Collection." # The Responce collected form Service 3 and 4 are sent back within the context of this sentence.