import requests, json
from flask import request, redirect, url_for, jsonify
from application import app, db, bcrypt
from application.models import Directors, Movies, Genres, GenreLink, Ratings, Users
from flask_login import login_user, current_user, logout_user, login_required
import requests

@app.route('/register/user/create', methods=['GET', 'POST'])
def register_user_create():
    data = request.get_json()
    with open('data') as f:
        user = json.load(f)
    dataStack =[]
    for field in user['userData']:
        for info in field:
            dataStack.append(field[info])
    print('made it', dataStack)
    register = Users(
            email = dataStack[0],
            user_name = dataStack[1],
            password = dataStack[7],
            first_name = dataStack[2],
            middle_names = dataStack[3],
            surname = dataStack[4],
            sex = dataStack[5],
            age = dataStack[6]
    )
    print('register: ', register)
    db.session.add(register)
    db.session.commit()
    return dataStack[8]

@app.route('/user/update/<userID>/commit', methods=['GET'])
def user_update_content_commit(userID, userData):
    change_attribute = Users.query.filter_by(id=userID).first()
    change_attribute.first_name = userData['first']
    change_attribute.middle_names = userData["middle"]
    change_attribute.surname = userData["last"]
    change_attribute.sex = userData["sex"]
    db.session.commit()
    return True

@app.route('/user/delete/<userID>/commit', methods=['GET'])
def user_delete_content_commit(userID, account):
    logout = logging_out_user_confirm()
    if logout == True:
        db.session.delete(account)
        db.session.commit()
        return True

@app.route('/login/user/varify', methods=['GET'])
def login_user_Varify():
    json_data = request.get_json()
    userData = Users.query.filter_by(email=json_data['email']).first()
    if userData and bycrpt.check_password_hash(userData.password, json_data['password']):

        {login_user:{account:account, remember:json_data['rememebr']}}

    return login_user

@app.route('/logout/user/confirm', methods=['GET'])
def logging_out_user_confirm():
    logout_user()
    return True



    