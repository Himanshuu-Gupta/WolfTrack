from flask import Blueprint, session, request, redirect, render_template, current_app
from flask_login import LoginManager, login_user, UserMixin
from datetime import datetime, timedelta

login_route = Blueprint('admin', __name__)
login_manager = LoginManager()

@login_route.record_once
def on_load(state):
    login_manager.init_app(state.app)

@login_manager.user_loader
def load_user(userid):
    return session['userinfo'][userid]

@login_route.before_app_request
def before_request():
    session.modified = True
    current_app.permanent_session_lifetime = timedelta(minutes=30)
    if request.endpoint != 'login_manager.login':
        if 'userinfo' not in session:
            pass

class User(UserMixin):
    pass

#Validate the username and password with DB
def is_valid(username, password):
    pass


@login_route.route('', methods=["GET", "POST"])
def login():
    username = request.json['Username']
    password = request.json['Password']
    if is_valid(username, password):
        pass
    user = User()
    session['userinfo'] = {'userid': username}
    user.id = username
    if request.method == 'POST':
        login_user(user)
    return render_template('home.html')
















# from flask import Blueprint, make_response, session, request, jsonify, current_app, redirect, url_for, render_template
# from datetime import timedelta, datetime
# from flask_login import login_user, LoginManager
# from Login.User import User, user_blueprint
# import jwt
# from templates import *
#
# auth_token = Blueprint('auth_token', __name__)
# auth_token.register_blueprint(user_blueprint)
#
# @auth_token.route('/', methods=['GET', 'POST'])
# def home():
#     return make_response('Go to login page /login')
#
# @auth_token.before_app_request
# def before_request():
#     session.modified = True
#
#     # current_app.permanent_session_lifetime = timedelta(minutes=30)
#     # if request.endpoint != 'auth_token.login':
#     #     if 'user' not in session:
#     #         if 'db_con' in session:
#     #             session.pop('db_con').close()
#
# def isValid():
#     pass
#
#
#
# """Verifying user login against LDAP and token generation"""
# @auth_token.route('/login', methods=['GET','POST'])
# def login():
#     if request.method == 'GET':
#         print('OK')
#         return render_template('home.html')
#     username = request.json.get('Username')
#     password = request.json.get('Password')
#     # username = request.form['username']
#     # password = request.form['password']
#     if not isValid():
#         pass
#
#     session['user'] = username
#     token = jwt.encode({'_id': username, 'exp': datetime.utcnow() + timedelta(hours=720)},
#                        current_app.config['SECRET_KEY'], algorithm='HS256')
#
#     user = User()
#     user.id = token
#     session['token'] = token
#     login_user(username)
#
#     return redirect(url_for('auth_token.homepage'))
#
#
#
#
#
#
#
# @auth_token.route('/home', methods=['GET'])
# def homepage():
#     return render_template('home.html')
#
