from application import app
import random


@app.route('/randomGenre', methods=['GET'])
def generategenre():
	Genre = ['Action', 'Adventure', 'Animated', 'Childrens', 'Comedy', 'Documentary', 'Drama', 'Fantasy', 'Horror', 'Musical', 'Romance', 'Science Fiction', 'War','Western']
	Ranger = len(Genre) - 1
    return Genre[random.randrange(Ranger)]