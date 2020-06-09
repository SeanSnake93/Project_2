from datetime import date, time, datetime, timedelta
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, PasswordField, BooleanField, TextAreaField, Form, FormField
from flask_sqlalchemy import SQLAlchemy
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Optional
from application import app, db
from application.models import Directors, Genres, GenreLink, Movies, Ratings, Users
from flask_login import current_user

def genres_options():
    return Genres.query

def ratings_options():
    return Ratings.query

class GenreForm(Form):
    genre1 = QuerySelectField(query_factory=genres_options, allow_blank=True, get_lable='genre')
    genre2 = QuerySelectField(query_factory=genres_options, allow_blank=True, get_lable='genre')
    genre3 = QuerySelectField(query_factory=genres_options, allow_blank=True, get_lable='genre')
    genre4 = QuerySelectField(query_factory=genres_options, allow_blank=True, get_lable='genre')
    genre5 = QuerySelectField(query_factory=genres_options, allow_blank=True, get_lable='genre')

class MovieForm(FlaskForm):

    movie_title = StringField("Title", validators=[DataRequired(), Length(min=1, max=100)])
    year = IntegerField("Year", validators=[DataRequired()])
    genre = FormField(GenreForm)
    director = StringField("Title", validators=[DataRequired(), Length(min=1, max=100)])
    rating = QuerySelectField(query_factory=ratings_options, allow_blank=True, get_lable='rating')
    description = TextAreaField("Description", validators=[DataRequired(), Length(min=1, max=999)])
    submit = SubmitField('Varify')

class UserLoginForm(FlaskForm):

    email = StringField("Email", validators=[DataRequired(), Email()])
    password = StringField("Password", validators=[DataRequired(), Length(min=8, max=50)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UserRegisterForm(FlaskForm):

    email = StringField("Email", validators=[DataRequired(), Email()])
    user_name = StringField("User Name", validators=[DataRequired(), Length(min=5, max=50)])
    first_name = StringField("First Name", validators=[DataRequired(), Length(min=1, max=50)])
    middle_names = StringField("Middle Name(s)", validators=[Length(min=1, max=50)])
    surname = StringField("Surname", validators=[DataRequired(), Length(min=1, max=50)])
    sex = StringField("Sex", validators=[DataRequired(), Length(min=2, max=10)])
    age = IntegerField("Age", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired(), Length(min=8, max=50)])
    confirm_password = StringField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Register')

class UserUpdateForm(FlaskForm):

    first_name = StringField("First Name", validators=[DataRequired(), Length(min=2, max=50)])
    middle_names = StringField("Middle Name(s)", validators=[Length(min=2, max=50)])
    surname = StringField("Surname", validators=[DataRequired(), Length(min=2, max=50)])
    sex = StringField("Sex", validators=[DataRequired(), Length(min=2, max=10)])
    submit = SubmitField('Confirm')