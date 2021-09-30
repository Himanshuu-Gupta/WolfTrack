from flask import make_response, Blueprint, request, jsonify, render_template
from flask_restful import Resource
from DAO.user_dao import user_dao
from flask_login import login_required

# add_user = Blueprint('add_user', )

# Specify the url end point for the function
class User(Resource):
    def __init__(self):
        self.headers = {'Content-Type': 'text/html'}
        self.user = user_dao()

    #@login_required
    def get(self):
        self.user.get_user()
        return make_response('Coming Soon!!')
        # return make_response(render_template('home.html', data=data, upcoming_events=upcoming_events), 200, headers)

    #@login_required
    def post(self):
        self.user.create_user()
        some_json=request.get_json()
        return {'you sent': some_json}, 200

    #@login_required
    def put(self):
        self.user.update_details()
        some_json=request.get_json()
        return {'you sent': some_json}, 200

    #@login_required
    def delete(self):
        self.user.delete_user()
        some_json=request.get_json()
        return {'you sent': some_json}, 200






