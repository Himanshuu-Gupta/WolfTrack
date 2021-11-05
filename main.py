from flask import Flask, request, render_template, make_response
from flask_restful import Resource, Api
# from Login.login import login_route
from Controller.activity_controller import Activity
from Controller.application_controller import Application
from Controller.profile_controller import Profile
from Controller.user_controller import User
from Controller.home import home_route

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'Sample' #os.environ.get('SECRET_KEY')
api.add_resource(User, '/user')
api.add_resource(Activity, '/activity')
api.add_resource(Profile, '/profile')
api.add_resource(Application, '/application')
app.register_blueprint(home_route, url_prefix='/login')
app.register_blueprint(home_route, url_prefix='/')
app.app_context().push()


if __name__ == '__main__':

    app.run(debug=True)
