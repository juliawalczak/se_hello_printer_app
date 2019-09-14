import unittest
import json
from lxml import etree
from xml.etree import ElementTree
import xml.etree.ElementTree as ET
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

    def test_json(self):
        imie = "Apolonia"
        expected = {"imie": imie, "msg": "Hello World!"}

        rv = self.app.get('/?output=json&imie=' + imie)

        js = json.loads(rv.data)
        self.assertEqual(expected["imie"], js["imie"])
        self.assertEqual(expected["msg"], js["msg"])

    def test_xml(self):
        xmlElem = """
        <greetings>
            <imie>{0}</imie>
            <msg>Hello World!</msg>
        </greetings>
        """
        expected = xmlElem.format("maria")
        expectedXML = etree.fromstring(expected)
        rv = self.app.get('?output=xml&imie=maria')

        self.assertEquals(expectedXML.findtext("imie"), rv.data)
