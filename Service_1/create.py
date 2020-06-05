#!/usr/bin/env python3

from application import db
from application.models import Directors, Genres, GenreLink, Movies, Ratings, Users

db.drop_all()
db.create_all()