# from flask import Blueprint, session, request, redirect, render_template, current_app, make_response, url_for
# from flask_login import LoginManager, login_user, UserMixin
# from datetime import datetime, timedelta

# login_route = Blueprint('admin', __name__)
# login_manager = LoginManager()
# headers = {'Content-Type': 'text/html'}

# data = {
#     "wishlist": ["Microsoft", "Google", "Uber"],
#     "inprogress": ["Twitter", "Pearson"],
#     "applied": ["Amazon", "NetApp"],
#     "offers": ["Perfios"]
# }

# upcoming_events = [
#     {"duedate": "28th Sept, 2021",
#      "company": "Apple"
#      },
#     {"duedate": "19th Dec, 2021",
#      "company": "Microsoft"
#      },
#     {"duedate": "21st Dec, 2021",
#      "company": "Amazon"
#      },
#     {"duedate": "21st Dec, 2021",
#      "company": "Amazon"
#      },
#     {"duedate": "21st Dec, 2021",
#      "company": "Amazon"
#      }
# ]


# @login_route.record_once
# def on_load(state):
#     login_manager.init_app(state.app)

# @login_manager.user_loader
# def load_user(userid):
#     return User(session['userinfo']['userid'])

# @login_route.before_app_request
# def before_request():
#     session.modified = True
#     current_app.permanent_session_lifetime = timedelta(minutes=30)
#     if request.endpoint != 'login_manager.login':
#         if 'userinfo' not in session:
#             pass

# class User(UserMixin):
#     def __init__(self, username) -> None:
#         self.username = username

#     def is_active(self):
#         return self.active

#     def is_anonymous(self):
#         return False

#     def is_authenticated(self):
#         return True


# def is_valid(username, password):
#     ''' Validate the username and password with DB '''
#     return True


# @login_route.route('', methods=["GET", "POST"])
# def login():
#     if request.method == 'GET':
#         return make_response(render_template('login.html'), 200, headers)
#     username = request.form['username']
#     password = request.form['password']
#     if not is_valid(username, password):
#         pass
#     user = User(username)
#     session['userinfo'] = {'userid': username}
#     user.id = username
#     if request.method == 'POST':
#         login_user(user)

#     return redirect(url_for('home_route.home'))