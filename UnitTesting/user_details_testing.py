from flask.typing import StatusCode

import unittest
import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from main import app

# Testing template
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