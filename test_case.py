import unittest
import json
from app import app

class ToDoList(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()
        
    def tearDown(self):
        self.client = None
        
    def test_home(self):
        res = self.client.get("/")
        print(res.data)
        # assert b'<h1>Hello Flask!</h1>' in res.data
        self.assertEqual(res.data, b'<h1>Hello Flask!</h1>')

    def test_api_sth(self):
        res = self.client.get("/Sth")
        print(res.data)

if __name__ == '__main__':
    unittest.main()
