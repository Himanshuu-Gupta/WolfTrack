from flask import render_template, request
from flask_restful import Resource
from flask_login import login_required
from DAO.application_dao import Application as application_dao



class Application(Resource):
    def __init__(self):
        self.headers = {'Content-Type': 'text/html'}

    @login_required
    def get(self):
        return {'about':"hello!"}

    @login_required
    def post(self):
        some_json=request.get_json()
        application_dao.add_new_application(request)
        print(some_json)

    @login_required
    def put(self):
        some_json=request.get_json()
        return {'you sent': some_json}, 201

    @login_required
    def delete(self):
        some_json=request.get_json()
        return {'you sent': some_json}, 201