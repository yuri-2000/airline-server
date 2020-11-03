from flask import Flask, views, request
from flask_cors import CORS
from api import passenger_management
from dao.base_element import *

app = Flask(__name__)
CORS(app, resources=r'/*', supports_credentials=True)


def init():
    app.register_blueprint(passenger_management)


init()


if __name__ == '__main__':
    app.run()
