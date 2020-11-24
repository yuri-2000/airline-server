from flask.blueprints import Blueprint
from typing import *
import datetime
from flask import request
from server.admin_login import *
from server.add_admin import *
from server.get_admin import get_admin
from server.airline_management import *
from server.add_airline import *
from server.add_airport import add_airport
from server.add_flight import *
from server.get_flight import *
from server.add_airplane import add_airplane
from server.get_airplane import get_airplane_all

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
    if update_airline(
            data['a_id'],
            data['a_c_id'],
            data['start'],
            data['destination'],
            data['air_model'],
            data['flight_num'],
            data['start_time'],
            data['arrive_time'],
            data['quota'],
            data['mileage'],
            data['standard_price']
    ):
        return {'success': True}
    else:
        return {'success': False, 'info': "airline exist"}


@admin_management.route('/add_airline', methods=['POST'])
def add_airline_info():
    data = request.get_json(silent=True)
    if add_airline(
            data['a_c_id'],
            data['start'],
            data['destination'],
            data['air_model'],
            data['flight_num'],
            data['start_time'],
            data['arrive_time'],
            data['quota'],
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


@admin_management.route('/get_flight_info', methods=['POST'])
def init_flight():
    data = request.get_json(silent=True)
    f_info: Dict[str, str] = get_flight_id(data['f_id'])
    return {'success': True, 'f_info': f_info}


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
            data['airplane_id'],
            data['flight_num'],
            data['start_date']
    ):
        return {'success': True}
    else:
        return {'success': False, 'info': "flight exist"}


@admin_management.route('/get_flight_all', methods=['POST'])
def get_all_flight():
    data = request.get_json(silent=True)
    flight_info = get_flight_all(data['id'])
    return {'success': True, 'flight_info': flight_info}


@admin_management.route('/get_airline_all', methods=['POST'])
def get_all_airline():
    airline_info = get_airline_all()
    return {'success': True, 'airline_info': airline_info}


@admin_management.route('/get_airplane_all', methods=['POST'])
def get_all_airplane():
    airplane_info = get_airplane_all()
    return {'success': True, 'airplane_info': airplane_info}


@admin_management.route('/add_airplane', methods=['POST'])
def add_airplane_info():
    data = request.get_json(silent=True)
    if add_airplane(data['id'], data['air_model'], data['eco'], data['fir']):
        return {'success': True}
    else:
        return {'success': False, 'info': "error"}


@admin_management.route('/update_flight', methods=['POST'])
def update_flight_info():
    data = request.get_json(silent=True)
    if update_flight(
            data['f_id'],
            data['airport_id'],
            data['airline_id'],
            data['airplane_id'],
            data['flight_num'],
            data['start_date'],
    ):
        return {'success': True}
    else:
        return {'success': False, 'info': "flight exist"}


@admin_management.route('/get_name', methods=['POST'])
def get_company_name():
    data = request.get_json(silent=True)
    a_c_name = get_name(
        data['id'],
    )
    return {'success': True, 'a_c_name': a_c_name}


@admin_management.route('/delete_flight', methods=['POST'])
def delete_flight_info():
    data = request.get_json(silent=True)
    if delete_flight(
        data['f_id'],
    ):
        return {'success': True, 'info': 'success'}
    else:
        return {'success': False, 'info': 'false'}

