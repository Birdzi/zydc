from flask import Flask
import json


app = Flask(__name__)


@app.route('/')
def index():
    return "hello world!"


@app.route('/error')
def error():
    info = dict(success=False, error_info="Not Permitted!")
    return json.dumps(info), 403
