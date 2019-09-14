import json
from lxml import etree
from xml.etree import ElementTree


PLAIN = "plain"
PLAIN_UP = "plain_uppercase"
PLAIN_LO = "plain_lowercase"
JSON = "json"
XML = "xml"

SUPPORTED = [PLAIN, PLAIN_UP, PLAIN_LO, JSON, XML]


def get_formatted(msg, imie, format):
    result = ""
    if format == PLAIN:
        result = plain_text(msg, imie)
    elif format == PLAIN_UP:
        result = plain_text_upper_case(msg, imie)
    elif format == PLAIN_LO:
        result = plain_text_lower_case(msg, imie)
    elif format == JSON:
        result = format_to_json(msg, imie)
    elif format == XML:
        result == format_to_xml(msg, imie)
    return result


def format_to_json(msg, imie):
    data = {"imie":imie, "msg":msg}
    y = json.dumps(data)
    return y



def format_to_xml(msg, imie):
    root = etree.Element('greetings')
    elem_name = etree.SubElement(root, 'name')
    elem_name.text = imie

    elem_msg = etree.SubElement(root, 'msg')
    elem_msg.text = msg

    r = ElementTree.dump(root)
    return r


def plain_text(msg, imie):
    return imie + ' ' + msg


def plain_text_upper_case(msg, imie):
    return plain_text(msg.upper(), imie.upper())


def plain_text_lower_case(msg, imie):
    return plain_text(msg.lower(), imie.lower())
