from flask.blueprints import Blueprint
from typing import *
import datetime
from flask import request
from server.admin_login import *
from server.add_admin import *
from server.get_admin import get_admin
from server.airline_management import *
from server.add_airline import add_airline
from server.add_airport import add_airport
from server.add_flight import add_flight
from server.get_flight import get_flight_all


admin_management = Blueprint('admin', __name__, url_prefix='/admin')


@admin_management.route('/login', methods=['POST'])
def login():
    data = request.get_json(silent=True)
    username: str = data['username']
    password: str = data['password']
    if admin_login(username, password):
        admin_id = admin_login_id(username, password)
        return {'success': True, 'id': admin_id}
    else:
        return {'success': False, 'info': 'username or password incorrect.'}


@admin_management.route('/register', methods=['POST'])
def register_admin():
    data = request.get_json(silent=True)
    username = data['username']
    password = data['password']
    if add_admin(username, password):
        admin_id = admin_login_id(username, password)
        return {'success': True, 'id': admin_id}
    else:
        return {'success': False, 'info': "user exist"}


@admin_management.route('/get_admin_info', methods=['POST'])
def get_admin_info():
    data = request.get_json(silent=True)
    a_info: Dict[str, str] = get_admin(data['username'])
    return {'success': True, 'a_info': a_info}


@admin_management.route('/update_admin_info', methods=['POST'])
def update_admin_info():
    data = request.get_json(silent=True)
    add_admin_info(
        data['username'],
        data['password'],
        data['name']
    )
    return {'success': True}


@admin_management.route('/get_airline', methods=['POST'])
def get_airline_info():
    data = request.get_json(silent=True)
    airline_info = get_airline(data['id'])
    return {'success': True, 'airline_info': airline_info}


@admin_management.route('/update_airline', methods=['POST'])
def update_airline_info():
    data = request.get_json(silent=True)
    if add_airline(
            data['a_id'],
            data['a_c_id'],
            data['start'],
            data['destination'],
            data['air_model'],
            data['flight_num'],
            data['start_time'],
            data['arrive_time'],
            data['eco'],
            data['fir'],
            data['mileage'],
            data['standard_price']
    ):
        return {'success': True}
    else:
        return {'success': False, 'info': "airline exist"}


@admin_management.route('/get_airline_info', methods=['POST'])
def init_airline():
    data = request.get_json(silent=True)
    a_info: Dict[str, str] = get_airline_id(data['a_id'])
    return {'success': True, 'a_info': a_info}


@admin_management.route('/add_airport', methods=['POST'])
def add_airport_info():
    data = request.get_json(silent=True)
    if add_airport(
            data['name'],
            data['address'],
            data['telephone'],
    ):
        return {'success': True}
    else:
        return {'success': False, 'info': "airport exist"}


@admin_management.route('/add_flight', methods=['POST'])
def add_flight_info():
    data = request.get_json(silent=True)
    if add_flight(
            data['airport_id'],
            data['airline_id'],
            data['flight_num'],
            data['start_date']
    ):
        return {'success': True}
    else:
        return {'success': False, 'info': "flight exist"}


@admin_management.route('/get_flight_all', methods=['POST'])
def get_all_flight():
    flight_info = get_flight_all()
    return {'success': True, 'flight_info': flight_info}
