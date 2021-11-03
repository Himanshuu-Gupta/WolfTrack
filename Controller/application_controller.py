from flask import render_template, request
from flask_restful import Resource
from flask_login import login_required
from DAO.application_dao import application_dao

class Application(Resource):
    def __init__(self):
        self.headers = {'Content-Type': 'text/html'}
        self.application = application_dao()

    # @login_required
    def get(self):
        return {'about':"hello!"}

    # @login_required
    def post(self, email, company_name, location, job_profile, salary, username, password, security_question, security_answer, notes,
    date_applied):
        return self.application.add_application(email, company_name, location, job_profile, salary, username, password, security_question, security_answer, notes,
    date_applied)

    # @login_required
    def put(self):
        some_json=request.get_json()
        return {'you sent': some_json}, 201

    # @login_required
    def delete(self):
        some_json=request.get_json()
        return {'you sent': some_json}, 201