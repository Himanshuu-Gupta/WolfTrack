from flask import Blueprint, flash, session
from flask import Flask, render_template, url_for, request
from flask_login import login_required, logout_user
from werkzeug.utils import redirect
from Controller.user_controller import User
from Controller.application_controller import Application
home_route = Blueprint('home_route', __name__)

user = User()
application = Application()

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
    session['email'] = request.form["username"]
    password = request.form["password"]
    result = user.get(session['email'],password)
    print(result)
    error = ""
    if(result == 0):
        error = "Email does not exits. Please enter a valid email."
        return render_template('login.html',loginError = error)
    elif(result == 2):
        error="Password incorrect."
        return render_template('login.html',loginError = error)
    else:
        return render_template('home.html', data=result, upcoming_events=upcoming_events)
    

@home_route.route('/signup', methods=['POST'])
def signup():
    name =  request.form["name"]
    session['email'] = request.form["email"]
    password = request.form["password"]
    result = user.post(name,session['email'],password)
    print(name)
    gender = request.form["gender"]
    location = request.form["location"]
    result = user.post(name,session['email'],password, gender, location)
    if(result == 0):
        error = "This email already exists. Please try with different email"
        return render_template('login.html', emailError=error)
    data["full_name"] = name
    return render_template('home.html', data=data, upcoming_events=upcoming_events)

@home_route.route('/view', methods=['GET'])
# @login_required
def view():
    application_category = request.args.get('show')
    

    result_data = application.get(session["email"], application_category)

    print(result_data)


    return render_template('view_list.html', data=result_data, upcoming_events=upcoming_events)

@home_route.route("/add_new_application", methods = ["GET","POST"])
# @login_required
def add_new_application():
    company_name = request.form["companyName"]
    location = request.form["location"]
    job_profile = request.form["jobProfile"]
    salary = request.form["salary"]
    username = request.form["username"]
    password = request.form["password"]
    security_question = request.form["securityQuestion"]
    security_answer = request.form["securityAnswer"]
    notes = request.form["notes"]
    date_applied = request.form["dateApplied"]
    result = application.post(session['email'], company_name, location, job_profile, salary, username, password, security_question, security_answer, notes,
    date_applied)
    if (result==0):
        error = "This job application could not be stored in the database. Please try again."
        return render_template('home.html', jobAddError=error)
    return render_template('home.html', data=data, upcoming_events=upcoming_events)


@home_route.route('/logout', methods=['GET'])
# @login_required
def logout():
    # logout_user()
    return redirect("/login")

# if __name__ == '__main__':
#     app.run(debug=True)