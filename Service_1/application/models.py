from application import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

class Movies(db.Model):

    id = db.Column(db.Integer, Priamry_Key=True)
    movie_title = db.Column(db.String(100),nullable=False)
    year = db.Column(db.Integer, nullable=False)
    director = db.Column(db.Integer, db.ForeignKey('director.id'), nullable=False)
    rating = db.Column(db.Integer, db.ForeignKey('ratings.id'), nullable=False)
    description = db.Column(db.String(999),nullable=False)
    referenced_in_genrelink = db.relationship('GenreLink', backref='Movies_Genre', lazy=True)

    def __rept__(self):
        return ''.join([
            'Movie ID: ', str(self.id), '\r\n',
            'Title: ', str(self.movie_title), '\r\n',
            'Year: ', str(self.year), '\r\n',
            'Director: ', str(self.director), '\r\n',
            'Rating: ', str(self.rating), '\r\n',
            'Description: ', str(self.description)
        ])

class Genres(db.Model):

    id = db.Column(db.Integer, Priamry_Key=True)
    genre = db.Column(db.String(20),nullable=False)
    referenced_in_genrelink = db.relationship('GenreLink', backref='Genre', lazy=True) # Relates this table to GenreLink TABLE.

    def __rept__(self):
        return ''.join([
            'Genre ID: ', str(self.id), '\r\n',
            'Genre: ', str(self.genre)
        ])

class GenreLink(db.Model):

    id = db.Column(db.Integer, Priamry_Key=True)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'), nullable=False) # Relating the "Foreign Key" (content refrenced to in another table)
    movie_id =  db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False)

    def __rept__(self):
        return ''.join([
            'Link ID: ', str(self.id), '\r\n',
            'Genre ID: ', str(self.genre_id), '\r\n',
            'Movie ID: ', str(self.movie_id)
        ])

class Ratings(db.Model):

    id = db.Column(db.Integer, Priamry_Key=True)
    rating = db.Column(db.String(10), nullable=False)
    referenced_in_movies = db.relationship('Movies', backref='Movie_Rating', lazy=True)

    def __rept__(self):
        return ''.join([
            'Rating ID: ', str(self.id), '\r\n',
            'Rating: ', str(self.rating)
        ])

class Directors(db.Model):

    id = db.Column(db.Integer, Priamry_Key=True)
    director = db.Column(db.String(10), nullable=False)
    referenced_in_movies = db.relationship('Movies', backref='Movie_Director', lazy=True)

    def __rept__(self):
        return ''.join([
            'Rating ID: ', str(self.id), '\r\n',
            'Rating: ', str(self.rating)
        ])

class Users(db.Model):
    id = db.Column(db.Integer, Priamry_Key=True)
    email = db.Column(db.String(500),nullable=False)
    user_name = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(500),nullable=False)
    first_name = db.Column(db.String(50),nullable=False)
    middle_names = db.Column(db.String(50),nullable=True)
    surname = db.Column(db.String(50),nullable=False)
    sex = db.Column(db.String(10),nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __rept__(self):
        return ''.join([
            'User ID: ', str(self.id), '\r\n',
            'Email: ', str(self.email), '\r\n',
            'User Name: ', str(self.user_name), '\r\n',
            'Password: ', str(self.password), '\r\n',
            'First Name: ', str(self.first_name), '\r\n',
            'Middle Names: ', str(self.middle_names), '\r\n',
            'Surname: ', str(self.surname), '\r\n',
            'Sex: ', str(self.sex), '\r\n',
            'Age: ', str(self.age)
        ])