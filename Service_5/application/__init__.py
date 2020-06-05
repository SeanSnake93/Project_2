from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import requests
from os import getenv
from flask_bycrypt import Bycrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SQLACHEMY_DATABASE_URI'] = str(getenv( 'PROJECT_URI' ))
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = str(getenv( 'MY_SECRET_KEY' ))
db = SQLAlchemy(app)
bycrypt = Bycrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from application import routes