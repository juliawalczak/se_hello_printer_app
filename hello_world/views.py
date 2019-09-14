from hello_world import app
from formater import get_formatted
from formater import SUPPORTED, PLAIN
from flask import request

moje_imie = "Pantera"
msg = "Hello World!"


@app.route('/')
def index():
    output = request.args.get('output')
    if not output:
        output = PLAIN
    imie = request.args.get('imie')
    if not imie:
        imie = moje_imie
    return get_formatted(msg, imie,
                         output.lower())


@app.route('/outputs')
def supported_output():
    return ", ".join(SUPPORTED)
