from flask import make_response, Blueprint, request, jsonify

add_user = Blueprint('add_user', url_prefix='user')

# Specify the url end point for the function
@add_user.route('',methods=['POST'])
def add_user():
    pass


