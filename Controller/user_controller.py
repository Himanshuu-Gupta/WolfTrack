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
    def get(self,email,password):
        return self.user.get_user(email,password)

    #@login_required
    def post(self, name, email,password):
        return self.user.create_user(name,email,password)
        

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






