import unittest
import json
from app import *
from create_test_mongodb import*

class ToDoList(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()
        self.SOMETHING = [
            {
                'id': uuid.uuid4().hex,
                'title': 'Kai',
                'comment': 'a handsome boy',
                'check': True
            },
            {
                'id': uuid.uuid4().hex,
                'title': 'Mi',
                'comment': 'a little girl',
                'check': False
            }
        ]

    def tearDown(self):
        self.client = None

    @unittest.skip("demonstrating skipping")
    def test_api_home(self):
        res = self.client.get("/")
        print(res.data)
        # assert b'<h1>Hello Flask!</h1>' in res.data
        self.assertEqual(res.data, b'<h1>Hello Flask!</h1>')

    @unittest.skip("demonstrating skipping")
    def test_db_remove(self):
        res = remove_sth("Mi")
        print('res:', res)
        self.assertEqual(res, True)

    @unittest.skip("demonstrating skipping")
    def test_db_insertMany(self):
        res = insertMany(self.SOMETHING)
        self.assertEqual(res, 'DOWN')

    @unittest.skip("demonstrating skipping")
    def test_db_updateOne(self):
        myquery = { "title": "Kai" }
        newvalues = { "$set": { "title": "KAKA" } }
        res = updateOne(myquery, newvalues)
        self.assertEqual(res, 'DOWN')

    # @unittest.skip("demonstrating skipping")
    def test_db_queryAll(self):
        res = queryAll()
        self.assertEqual(res, 'DOWN')

    @unittest.skip("demonstrating skipping")
    def test_db_clear(self):
        res = clear()
        self.assertEqual(res, 'DOWN')

if __name__ == '__main__':
    unittest.main()
