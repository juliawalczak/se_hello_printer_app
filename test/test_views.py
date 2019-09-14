import unittest
import jmespath
import json
from hello_world import app
from hello_world.formater import SUPPORTED


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        ','.join(SUPPORTED) in rv.data

    def test_msg_with_output(self):
        rv = self.app.get('/?output=json')
        self.assertEquals('{ "imie":"Pantera", "mgs":"Hello World!"}', rv.data)

    def test_msg_with_json_2(self):
        imie = "Pantera"
        rv = self.app.get('/?output=json&imie=' + imie)
        rj = json.loads(rv.data)
        actual = jmespath.search('imie', rj)
        expected = "Pantera"
        self.assertEquals(expected, actual)
