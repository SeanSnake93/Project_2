from application import app
from random import randrange
import requests

@app.route('/register/user/create', methods=['GET'])
def register_user_create(account, hashed):
    userData = Users(
            email = userData[0]
            user_name = userData[1]
            password = hashed
            first_name = userData[2]
            middle_names = userData[3]
            surname = userData[4]
            sex = userData[5]
            age = int(userData[6])
        )
        db.session.add(userData)
        bd.seesion.commit()
    return True

@app.route('/user/update/<userID>/commit', methods=['GET'])
@login_required
def user_update_content_commit(userID, first, middle, last, sex):
    change_attribute = Users.query.filter_by(id=userID).first()
    change_attribute.first_name = first
    change_attribute.middle_names = middle
    change_attribute.surname = last
    change_attribute.sex = sex
    db.session.commit()
    return True

@app.route('/user/delete/<userID>/commit', methods=['GET'])
@login_required
def user_delete_content_commit(userID, account):
    logout = logging_out_user_confirm()
    if logout = True:
        db.session.delete(account)
        db.session.commit()
        return True

@app.route('/login/user/varify', methods=['GET'])
def login_user_Varify(account, hashed, pin):
    if account and bycrpt.check_password_hash(account.password, hashed):
        login_user(
            account,
            remember=pin
        )
    return login_user

@app.route('/logout/user/confirm', methods=['GET'])
@login_required
def logging_out_user_confirm():
    logout_user()
    return True