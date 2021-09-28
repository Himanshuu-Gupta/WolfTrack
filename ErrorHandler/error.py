from flask import jsonify, Blueprint, make_response, g, current_app
from custom_error_function import *
handle_err = Blueprint('errors', __name__)

@handle_err.app_errorhandler(db_connection_issue)
def db_connection_failed(e):
    return make_response('Not able to connect to the database, check you connection!', 500)

@handle_err.app_errorhandler(401)
def unauthorized_request(e):
    return make_response("Ohh! looks like you missed to sign in. Please log in!.", 401)