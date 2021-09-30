from flask import Blueprint, session, request, redirect, render_template, current_app, make_response
from flask_login import LoginManager, login_user, UserMixin
from datetime import datetime, timedelta

login_route = Blueprint('admin', __name__)
login_manager = LoginManager()
headers = {'Content-Type': 'text/html'}
from DAO.sql_helper import sql_helper
db = sql_helper()

data = {
    "wishlist": ["Microsoft", "Google", "Uber"],
    "inprogress": ["Twitter", "Pearson"],
    "applied": ["Amazon", "NetApp"],
    "offers": ["Perfios"]
}

upcoming_events = [
    {"duedate": "28th Sept, 2021",
     "company": "Apple"
     },
    {"duedate": "19th Dec, 2021",
     "company": "Microsoft"
     },
    {"duedate": "21st Dec, 2021",
     "company": "Amazon"
     },
    {"duedate": "21st Dec, 2021",
     "company": "Amazon"
     },
    {"duedate": "21st Dec, 2021",
     "company": "Amazon"
     }
]


@login_route.record_once
def on_load(state):
    login_manager.init_app(state.app)

@login_manager.user_loader
def load_user(id):
    return User(session['userinfo']['user_name'])

@login_route.before_app_request
def before_request():
    session.modified = True
    current_app.permanent_session_lifetime = timedelta(minutes=30)
    if request.endpoint != 'login_manager.login':
        if 'userinfo' not in session:
            pass

class User(UserMixin):
    def __init__(self, username) -> None:
        self.username = username

    def is_active(self):
        return self.active

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True


def is_valid(username, password):
    ''' Validate the username and password with DB '''
    query = None
    query = 'SELECT id FROM user_login as u INNER JOIN user ON u.user_id=user.user_id WHERE user.email ' \
            '='+username+'and user.password='+password
    result = db.run_query(query)
    if not result:
        return False
    session['userinfo'] = {'email_id': username, 'user_id': result}
    return True

@login_route.route('', methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return make_response(render_template('login.html'), 200, headers)
    username = request.form['username']
    password = request.form['password']
    if not is_valid(username, password):
        raise 401
    user = User(username)
    user.id = username
    if request.method == 'POST':
        login_user(user)
    return make_response(render_template('home.html', data=data, upcoming_events=upcoming_events), 301, headers)