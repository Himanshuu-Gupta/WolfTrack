from flask import request
from flask_restful import Resource
from flask_login import login_required

class Activity(Resource):

    def __init__(self):
        self.headers = {'Content-Type': 'text/html'}

    @login_required
    def get(self):
        return {'about':"hello!"}

    @login_required
    def post(self):
        some_json=request.get_json()
        return {'you sent': some_json}, 201

    @login_required
    def put(self):
        some_json=request.get_json()
        return {'you sent': some_json}, 201

    @login_required
    def delete(self):
        some_json=request.get_json()
        return {'you sent': some_json}, 201