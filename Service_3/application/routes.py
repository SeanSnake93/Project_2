from application import app
from random import randrange


@app.route('/randomgenre', methods=['GET'])
def randomgenre():
    genre = ['Action', 'Adventure', 'Animated', 'Childrens', 'Comedy', 'Documentary', 'Drama', 'Fantasy', 'Horror', 'Musical', 'Romance', 'Science Fiction', 'War', 'Western']
    ranger = len(genre)
    print(ranger)
    return genre[randrange(int(ranger))]