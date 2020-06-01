from application import app
import requests


@app.route('/generate', methods=['GET'])
def generate():
    Genre = requests.get('http://localhost:5002/generategenre')# Call Service 3 to to return a Genre to filter a Movie form Service 4.
    print("Service 3 Output:", Genre) # Print/Display selection on Terminal.
    Movie = requests.get('http://localhost:5003/generatemovie', genre = Genre) # With the Genre defined, filter a Movie in Service 4 related to this Genre.
    print("Service 4 Output:", Movie) # Print the Movie found in Service 4.
    Output = "We have selected", Movie.text, "from our", Genre.text, "Collection." # The Responce being sent back to be displayed on site.
    return Output