from flask import Flask, request
import requests
# * are only if i wish to expand
# from flask_login import LoginManager

app = Flask(__name__)

# login_manager = LoginManager(app)
# login_manager.login_view = 'login'

from application import routes