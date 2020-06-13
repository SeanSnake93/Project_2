from application import app # Import the app into routes
from random import randrange # enable me to recive a random option within a list

@app.route('/randomgenre', methods=['GET'])
def randomgenre():
    genre = ['Action', 'Adventure', 'Animated',
        'Childrens', 'Comedy', 'Documentary',
        'Drama', 'Fantasy', 'Horror', 'Musical',
        'Romance', 'Science Fiction', 'War', 'Western'
    ] # Define a static list for my project to run on.
    return genre[randrange(int(genre))] # Return a random value from the list above.