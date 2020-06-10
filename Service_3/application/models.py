from application import db

class Genres(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(20), nullable=False)
    
    def __rept__(self):
        return ''.join([
            'Genre ID: ', str(self.id), '\r\n',
            'Genre: ', str(self.genre)
        ])

class Movies(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    movie_title = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    genre1 = db.Column(db.String(20), nullable=False)
    genre2 = db.Column(db.String(20), nullable=False)
    genre3 = db.Column(db.String(20), nullable=False)
    genre4 = db.Column(db.String(20), nullable=False)
    genre5 = db.Column(db.String(20), nullable=False)

    def __rept__(self):
        return ''.join([
            'Movie ID: ', str(self.id), '\r\n',
            'Title: ', str(self.movie_title), '\r\n',
            'Year: ', str(self.year), '\r\n',
            'genre1: ', str(self.genre1), '\r\n',
            'genre2: ', str(self.genre2), '\r\n',
            'genre3: ', str(self.genre3), '\r\n',
            'genre4: ', str(self.genre4), '\r\n',
            'genre5: ', str(self.genre5)
        ])