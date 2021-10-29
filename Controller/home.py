from flask import Blueprint, flash
from flask import Flask, render_template, url_for, request
from flask_login import login_required, logout_user
from werkzeug.utils import redirect
from Controller.user_controller import User
home_route = Blueprint('home_route', __name__)

user = User()

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

profile = {
    "name": "Jessica Holds",
    "Location": "Raleigh, NC",
    "phone_number": "",
    "social": {
            "linkedin": "www.linkedin.com/in/surajdm",

    }
}


# @home_route.route('', methods=['GET'])
# @login_required
# def home():
#     return render_template('home.html', data=data, upcoming_events=upcoming_events)

@home_route.route('/', methods=['GET', 'POST'])
@home_route.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html',loginError = "")

@home_route.route('/loginUser', methods=['GET', 'POST'])
def loginUser():
    email = request.form["username"]
    password = request.form["password"]
    result = user.get(email,password)
    error = ""
    if(result == 0):
        error = "Email does not exits. Please enter a valid email."
        return render_template('login.html',loginError = error)
    elif(result == 1):
        return render_template('home.html', data=data, upcoming_events=upcoming_events)
    elif(result == 2):
        error="Password incorrect."
        return render_template('login.html',loginError = error)
    

@home_route.route('/signup', methods=['POST'])
def signup():
    name =  request.form["name"]
    email = request.form["email"]
    password = request.form["password"]
    result = user.post(name,email,password)
    if(result ==0):
        error = "This email already exists. Please try with different email"
        return render_template('login.html/signup', emailError=error)
    return render_template('home.html', data=data, upcoming_events=upcoming_events)

@home_route.route('/view', methods=['GET'])
@login_required
def view():
    card_selected = request.args.get('user')
    return render_template('view_list.html', data=data, upcoming_events=upcoming_events)

@home_route.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect("/login")

if __name__ == '__main__':
    app.run(debug=True)