from application import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

# ------ START - of - MOVIES ------

class Movies(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    movie_title = db.Column(db.String(100),nullable=False)
    year = db.Column(db.Integer, nullable=False)
    sequel_id = db.Column(db.Integer, db.ForeignKey('sequal.id'), nullable=True)
    rating_id = db.Column(db.Integer, db.ForeignKey('ratings.id'), nullable=False)
    description = db.Column(db.String(999),nullable=False)
    referenced_in_genrelink = db.relationship('GenreLink', backref='Movies_Genre', lazy=True)
    referenced_in_genrelink = db.relationship('RecordsLink', backref='Movies_Staff', lazy=True)

    def __rept__(self):
        return ''.join([
            'Movie ID: ', str(self.id), '\r\n',
            'Title: ', str(self.movie_title), '\r\n',
            'Year: ', str(self.year), '\r\n',
            'sequel: ', str(self.sequel_id), '\r\n',
            'Rating: ', str(self.rating_id), '\r\n',
            'Description: ', str(self.description)
        ])

# ------ START - of - GENRE ------ # many Genres can exist on one movie, the link holds all the data withough the need to hold it in the movie tabel

class GenreLink(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'), nullable=False) # Relating the "Foreign Key" (content refrenced to in another table)
    movie_id =  db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False)

    def __rept__(self):
        return ''.join([
            'Link ID: ', str(self.id), '\r\n',
            'Genre ID: ', str(self.genre_id), '\r\n',
            'Movie ID: ', str(self.movie_id)
        ])

class Genres(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(20),nullable=False)
    referenced_in_genrelink = db.relationship('GenreLink', backref='Genre', lazy=True) # Relates this table to GenreLink TABLE.

    def __rept__(self):
        return ''.join([
            'Genre ID: ', str(self.id), '\r\n',
            'Genre: ', str(self.genre)
        ])

# ------ START - of - STAFF ------ # many recods may exist to one movie. This keeys the relationship a 1 to many by being the sourse of the many.

class RecordLink(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    record_id = db.Column(db.Integer, db.ForeignKey('genres.id'), nullable=False) # Relating the "Foreign Key" (content refrenced to in another table)
    movie_id =  db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False)
    title = db.Column(db.String(50), nullable=True)

    def __rept__(self):
        return ''.join([
            'Link ID: ', str(self.id), '\r\n',
            'Genre ID: ', str(self.genre_id), '\r\n',
            'Movie ID: ', str(self.movie_id)
        ])

# ------ START - of - RATING ------ # 1 to many

class Ratings(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.String(10), nullable=False)
    referenced_in_movies = db.relationship('Movies', backref='Movie_Rating', lazy=True)

    def __rept__(self):
        return ''.join([
            'Rating ID: ', str(self.id), '\r\n',
            'Rating: ', str(self.rating)
        ])

# ------ START - of - SEQUAL ------ # 1 to one

class Sequal(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    original_movie_id = db.Column(db.Integer, db.ForeignKey('movoies.id'), nullable=False)
    referenced_in_movies = db.relationship('Movies', backref='Movie_Sequal', lazy=True)

    def __rept__(self):
        return ''.join([
            'Rating ID: ', str(self.id), '\r\n',
            'Rating: ', str(self.rating)
        ])

# ------ END -- of -- MOVIES ------

# ------------------------------------------------------------------------------------------------------------------------

# ------ START - of - USERS ------

class Accounts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(500),nullable=False)
    user_name = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(500),nullable=False)
    record = db.Column(db.Integer, db.ForeignKey('Records.id'), nullable=False)
    
    def __rept__(self):
        return ''.join([
            'User ID: ', str(self.id), '\r\n',
            'Email: ', str(self.email), '\r\n',
            'User Name: ', str(self.user_name), '\r\n',
            'Password: ', str(self.password), '\r\n',
            'Record: ', str(self.record)
        ])

class Records(db.Model):
    first_name = db.Column(db.String(50),nullable=False)
    middle_names = db.Column(db.String(99),nullable=True)
    surname = db.Column(db.String(50),nullable=False)
    sex = db.Column(db.String(10),nullable=False)
    age = db.Column(db.Integer, nullable=False)
    referenced_in_account = db.relationship('Accounts', backref='User_Record', lazy=True)
    referenced_in_link = db.relationship('RecordsLink', backref='Movie_Role', lazy=True)

    def __rept__(self):
        return ''.join([
            'First Name: ', str(self.first_name), '\r\n',
            'Middle Names: ', str(self.middle_names), '\r\n',
            'Surname: ', str(self.surname), '\r\n',
            'Sex: ', str(self.sex), '\r\n',
            'Age: ', str(self.age)
        ])

# ------ END -- of -- USERS ------