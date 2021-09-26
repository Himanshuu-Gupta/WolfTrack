from flask import Blueprint
from Controller.add_user import add_user

route = Blueprint('', __name__, url_prefix='')

route.register_blueprint(add_user, url_prefix='/user')