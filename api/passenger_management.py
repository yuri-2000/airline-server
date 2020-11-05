from flask.blueprints import Blueprint
from typing import *
from flask import request
from server.passenger_login import passenger_login
from server.add_passenger import add_passenger

passenger_management = Blueprint('passenger', __name__, url_prefix='/passenger')


@passenger_management.route('/login', methods=['POST'])
def login():
    data = request.get_json(silent=True)
    username: str = data['username']
    password: str = data['password']
    if passenger_login(username, password):
        return {'success': True}
    else:
        return {'success': False, 'info': 'username or password incorrect.'}


@passenger_management.route('/add_resident', methods=['POST'])
def add_passenger():
    data = request.get_json(silent=True)
    username = data['username']
    password = data['password']
    name = data['name']
    type = data['type']
    mile_score = data['mile_score']
    add_passenger(username, password, name, type, mile_score)
    return {'success': True}

