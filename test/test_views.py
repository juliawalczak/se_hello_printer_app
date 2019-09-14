import unittest
import json
from hello_world import app
from hello_world.formater import SUPPORTED
from hello_world.formater import format_to_json


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        ','.join(SUPPORTED) in rv.data

    def test_msg_with_output(self):
        imie = "Apolonia"
        expected = {"imie": imie, "msg": "Hello World!"}

        rv = self.app.get('/?output=json&imie=' + imie)

        js = json.loads(rv.data)
        self.assertEqual(expected["imie"], js["imie"])
        self.assertEqual(expected["msg"], js["msg"])
