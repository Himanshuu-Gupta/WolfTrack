from flask import Flask
from flask_cors import CORS
import os
from ErrorHandler.error import handle_err
from login import auth_token


def create_app():
    app_p = Flask(__name__)
    # CORS(app_p)
    app_p.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app_p.app_context().push()
    print(app_p.url_map)
    return app_p

def link_blueprints(app):
    # app.register_blueprint(report_api, url_prefix='/reports')
    app.register_blueprint(handle_err)
    app.register_blueprint(auth_token, url_prefix='')
    return app

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = create_app()
    app = link_blueprints(app)
    print(app.url_map)
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
