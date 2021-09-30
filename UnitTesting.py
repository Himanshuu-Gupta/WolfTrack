from flask.typing import StatusCode
from main import app
import unittest

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
        response = tester.get("/user")
        self.assertEqual(response.content_type, "application/json")

    #check data returned
    def test_index_data(self):
        tester = app.test_client(self)
        response = tester.get("/login")
        print(response.data)
        self.assertEqual(b'WolfTrack' in response.data, True)

 if __name__=="__main__":
     unittest.main()