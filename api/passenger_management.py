from flask.blueprints import Blueprint
from typing import *
from flask import request
from server.passenger_login import passenger_login
from server.add_passenger import add_passenger as add_passenger_api
from server.get_passenger import get_passenger
from server.add_passenger import add_passenger_info

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


@passenger_management.route('/add_passenger', methods=['POST'])
def add_passenger():
    data = request.get_json(silent=True)
    username = data['username']
    password = data['password']
    if add_passenger_api(username, password):
        return {'success': True}
    else:
        return {'success': False, 'info': "user exist"}


@passenger_management.route('/get_passenger_info', methods=['POST'])
def get_resident_info():
    data = request.get_json(silent=True)
    u_info: Dict[str, str] = get_passenger(data['username'])
    return {'success': True, 'u_info': u_info}


@passenger_management.route('/update_passenger_info', methods=['POST'])
def update_passenger_info():
    data = request.get_json(silent=True)
    add_passenger_info(
        data['username'],
        data['password'],
        data['name'],
        data['type'],
        data['mile_score']
    )
    return {'success': True}
