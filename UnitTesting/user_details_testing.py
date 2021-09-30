from flask.typing import StatusCode
from main import app
import unittest

class FlaskTest(unittest.TestCase):

    #check if response is 200
    def test_index(self):
        pass
    
    #check if content returned is application/json
    def test_index_content(self):
        pass

    #check data returned
    def test_index_data(self):
        pass
if __name__=="__main__":
    unittest.main()