from unittest.main import main
from flask import app
from flask.typing import StatusCode
import unittest
import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from main import app

class FlaskTest(unittest.TestCase):

    #check if response is 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/login")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    #check if content returned is application/json
    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get("/login")
        self.assertEqual(response.content_type, "text/html; charset=utf-8")

    #check data returned
    def test_valid_email(self):
        tester = app.test_client(self)
        response = tester.post("/loginUser",data = {"username":"wrongformat.com","password":"password"})
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_validate_credentials(self):
        tester = app.test_client(self)
        response = tester.post("/loginUser",data = {"username":"test@gmail.com","password":"pasword"})
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_validate_credentials(self):
        tester = app.test_client(self)
        response = tester.post("/loginUser", data={"username": "test@gmail.com", "password": "password"})
        self.assertEqual(response.status_code, 200)

    def test_repeated_signup(self):
        tester = app.test_client(self)
        response = tester.post("/signup", data={"username": "test@gmail.com", "password": "password", "name": "test", "gender": "Female", "location":"Raleigh"})
        self.assertEqual(response.status_code, 400)

    def test_new_application(self):
        with app.test_client(self) as c:
            with c.session_transaction() as sess:
                sess["email"] = "test@gmail.com"
                sess["password"] = "password"
        response = c.post("/add_new_application", data={"companyName" : "ANB", "location":"Seattle", "jobProfile": "Software Engineer", "salary":80000, "securityQuestion":"What is the name of your first dog?", "securityAnswer":"Tommy", "dateApplied" : "2021-02-01", "notes":"Check back in 2 weeks", "username": "abc@adobe.com", "password": "password1"})
        self.assertEqual(response.status_code, 200)

if __name__=="__main__":
     unittest.main()