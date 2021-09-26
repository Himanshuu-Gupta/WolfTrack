from flask import jsonify, Blueprint, make_response, g, current_app
import jwt

handle_err = Blueprint('errors', __name__)

@handle_err.app_errorhandler(jwt.ExpiredSignatureError)
def signature_failed(e):
    return make_response('Signature expired. Please log in again!', 401)

@handle_err.app_errorhandler(jwt.InvalidTokenError)
def token_decode_failed(e):
    return make_response("Invalid token. Please log in again.", 401)