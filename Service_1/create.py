#!/usr/bin/env python3

from application import db
from application.models import Genres, Movies

db.drop_all()
db.create_all()