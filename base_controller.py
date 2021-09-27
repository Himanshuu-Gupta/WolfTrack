'''from flask import Blueprint, make_response, session, request, jsonify, current_app
from datetime import timedelta, datetime
#import jwt

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
'''

from re import DEBUG
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class User(Resource):
    def get(self):
        return {'about':"hello!"}
    def post(self):
        some_json=request.get_json()
        return {'you sent': some_json}, 200
    def put(self):
        some_json=request.get_json()
        return {'you sent': some_json}, 200
    def delete(self):
        some_json=request.get_json()
        return {'you sent': some_json}, 200

class Application(Resource):
    def get(self):
        return {'about':"hello!"}
    def post(self):
        some_json=request.get_json()
        return {'you sent': some_json}, 201
    def put(self):
        some_json=request.get_json()
        return {'you sent': some_json}, 201
    def delete(self):
        some_json=request.get_json()
        return {'you sent': some_json}, 201

class Profile(Resource):
    def get(self):
        return {'about':"hello!"}
    def post(self):
        some_json=request.get_json()
        return {'you sent': some_json}, 201
    def put(self):
        some_json=request.get_json()
        return {'you sent': some_json}, 201
    def delete(self):
        some_json=request.get_json()
        return {'you sent': some_json}, 201

class Activity(Resource):
    def get(self):
        return {'about':"hello!"}
    def post(self):
        some_json=request.get_json()
        return {'you sent': some_json}, 201
    def put(self):
        some_json=request.get_json()
        return {'you sent': some_json}, 201
    def delete(self):
        some_json=request.get_json()
        return {'you sent': some_json}, 201

#api.add_resource(HelloWorld, '/HelloWorld')
api.add_resource(User, '/user')
api.add_resource(Activity, '/activity')
api.add_resource(Profile, '/profile')
api.add_resource(Application, '/application')

if __name__ == '__main__':
    app.run(debug=True)