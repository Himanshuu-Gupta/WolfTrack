from flask import Blueprint, make_response, session, request, jsonify, current_app
from datetime import timedelta, datetime
import jwt

auth_token = Blueprint('auth_token', __name__)

@auth_token.route('/', methods=['GET', 'POST'])
def home():
    return make_response('Go to login page /login')

@auth_token.before_app_request
def before_request():
    pass

def isValid():
    pass

"""Verifying user login against LDAP and token generation"""
@auth_token.route('/login', methods=['POST'])
def login():
    username = request.json.get('Username')
    password = request.json.get('Password')

    if not isValid():
        pass

    return jsonify({'token': 'This Is a Token'})
