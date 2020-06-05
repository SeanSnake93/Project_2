from datetime import date
from flask_wtf import FlaskForm
from wtfforms import InterField, StringField, SubmitField, PasswordField, BooleanField
from etfforms.validators import DataRequired, Length, Email, EqualTo, ValidateError, Optional
from application import app, db
from application.models import Directors, Genres, GenreLink, Movies, Ratings, Users
from flask_login import current_user

class MovieForm(FlaskForms):

    movie_title = StringField("Title",
        validators=[
            DataRequired().
            Length(min=1, max=100)
        ]
    )

    limit = Now.year + 1

    year = IntegerField("Year", CHOICES = [(i) for i in range(1878, limit)]
        validators=[
            DataRequired()
        ]
    )

    director = StringField("Title",
        validators=[
            DataRequired().
            Length(min=1, max=100)
        ]
    )

    allgenres = Genres.query.all()

    genre1 = StringField(
        "Genre #1",
        available=[]
        for genre in allgenres.Genre:
            if form.genre2.data in genre or form.genre3.data in genre or form.genre4.data in genre or form.genre5.data in genre:
                continue
            else:
                available.append(genre)
        CHOICES=[
            available
        ],
        validators=[
            DataRequired()
            Length(min=3, max=20)
        ]
    )

    genre2 = StringField("Genre #2",
        available=[]
        for genre in allgenres.Genre:
            if form.genre1.data in genre or form.genre3.data in genre or form.genre4.data in genre or form.genre5.data in genre:
                continue
            else:
                available.append(genre)
        CHOICES=[
            available
        ],
        validators=[
            Length(min=3, max=20),
            Optional()
        ]
    )

    genre3 = StringField("Genre #3",
        available=[]
        for genre in allgenres.Genre:
            if form.genre1.data in genre or form.genre2.data in genre or form.genre4.data in genre or form.genre5.data in genre:
                continue
            else:
                available.append(genre)
        CHOICES=[
            available
        ],
        validators=[
            Length(min=3, max=20),
            Optional()
        ]
    )

    genre4 = StringField("Genre #4",
        available=[]
        for genre in allgenres.Genre:
            if form.genre1.data in genre or form.genre2.data in genre or form.genre3.data in genre or form.genre5.data in genre:
                continue
            else:
                available.append(genre)
        CHOICES=[
            available
        ],
        validators=[
            Length(min=3, max=20),
            Optional()
        ]
    )

    genre5 = StringField("Genre #5",
        available=[]
        for genre in allgenres.Genre:
            if form.genre1.data in genre or form.genre2.data in genre or form.genre3.data in genre or form.genre4.data in genre:
                continue
            else:
                available.append(genre)
        CHOICES=[
            available
        ],
        validators=[
            Length(min=3, max=20),
            Optional()
        ]
    )

    allratings = Ratings.query.all()

    rating = StringField("Rating",
        CHOICES = [
            allratings
        ],
        validators=[
            DataRequired()
            Length(min=1, max=10)
        ]
    )

    description = StringField("Description",
        validators=[
            DataRequired().
            Length(min=1, max=999)
        ]
    )

class UserLoginForm(FlaskForms):

    email = StringField("Email",
        validators=[
            DataRequired().
            Email()
        ]
    )

    password = StringField("Password",
        validators=[
            DataRequired(),
            Length(min=8, max=50)
        ]
    )

    remember = BooleanFeild('Remember Me')

    submit = SubmitFeild('Login')

class UserRegisterForm(FlaskForms):

    email = StringField("Email",
        validators=[
            DataRequired().
            Email()
        ]
    )

    user_name = StringField("User Name",
        validators=[
            DataRequired().
            Length(min=5, max=50)
        ]
    )

    first_name = StringField("First Name",
        validators=[
            DataRequired().
            Length(min=2, max=50)
        ]
    )

    middle_names = StringField("Middle Name(s)",
        validators=[
            Length(min=2, max=50)
        ]
    )

    surname = StringField("Surname",
        validators=[
            DataRequired().
            Length(min=2, max=50)
        ]
    )

    sex = StringField("Sex",
        CHOICES=[
            "Prefure not to say",
            "Male",
            "Female"
        ]
        validators=[
            DataRequired().
            Length(min=2, max=10)
        ]
    )

    age = IntegerField("Age", CHOICES = [(i) for i in range(101)]
        validators=[
            DataRequired()
        ]
    )

    password = StringField("Password",
        validators=[
            DataRequired(),
            Length(min=8, max=50)
        ]
    )

    confirm_password = StringField("Confirm Password",
        validators=[
            DataRequired()
            EqualTo('password')
        ]
    )

    remember = BooleanFeild('Remember Me')

    submit = SubmitFeild('Register')

class UserUpdateForm(FlaskForms):

    first_name = StringField("First Name",
        validators=[
            DataRequired().
            Length(min=2, max=50)
        ]
    )

    middle_names = StringField("Middle Name(s)",
        validators=[
            Length(min=2, max=50)
        ]
    )

    surname = StringField("Surname",
        validators=[
            DataRequired().
            Length(min=2, max=50)
        ]
    )

    sex = StringField("Sex",
        CHOICES=[
            "Prefure not to say",
            "Male",
            "Female"
        ]
        validators=[
            DataRequired().
            Length(min=2, max=10)
        ]
    )

    submit = SubmitFeild('Submit Changes')