from flask.blueprints import Blueprint
from typing import *
import datetime
from flask import request
from server.passenger_login import *
from server.add_passenger import add_passenger as add_passenger_api
from server.get_passenger import get_passenger
from server.add_passenger import add_passenger_info
from server.get_flight import *
from server.get_ticket import *
from server.choose_seat import *


passenger_management = Blueprint('passenger', __name__, url_prefix='/passenger')


@passenger_management.route('/login', methods=['POST'])
def login():
    data = request.get_json(silent=True)
    username: str = data['username']
    password: str = data['password']
    if passenger_login(username, password):
        passenger_id = passenger_login_id(username, password)
        return {'success': True, 'id': passenger_id}
    else:
        return {'success': False, 'info': 'username or password incorrect.'}


@passenger_management.route('/add_passenger', methods=['POST'])
def add_passenger():
    data = request.get_json(silent=True)
    username = data['username']
    password = data['password']
    if add_passenger_api(username, password):
        passenger_id = passenger_login_id(username, password)
        return {'success': True, 'id': passenger_id}
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
        data['gender'],
        data['type'],
        data['mile_score']
    )
    return {'success': True}


@passenger_management.route('/get_flight', methods=['POST'])
def get_airline_info():
    data = request.get_json(silent=True)
    flight_info = get_flight(data['start'], data['destination'], data['start_date'])
    return {'success': True, 'flight_info': flight_info}


@passenger_management.route('/get_ticket', methods=['POST'])
def get_ticket_info():
    data = request.get_json(silent=True)
    ticket_info = get_ticket(data['id'])
    return {'success': True, 'ticket_info': ticket_info}


@passenger_management.route('/filter_ticket', methods=['POST'])
def filter_ticket_info():
    data = request.get_json(silent=True)
    ticket_info = filter_ticket(data['id'], data['start_date'], data['flight_num'])
    return {'success': True, 'ticket_info': ticket_info}


@passenger_management.route('/get_seat', methods=['POST'])
def get_seat_info():
    data = request.get_json(silent=True)
    eco, fir, standard_price, type = get_seat(data['f_id'], data['id'])
    return {'success': True, 'eco': eco, 'fir': fir, 'standard_price': standard_price, 'type': type}


@passenger_management.route('/add_ticket', methods=['POST'])
def add_ticket_info():
    data = request.get_json(silent=True)
    if add_ticket(
            data['id'],
            data['f_id'],
            data['seat_num'],
            data['CLass'],
            data['start'],
            data['destination'],
            ):
        return {'success': True}
    else:
        return {'success': False, 'info': 'error.'}


@passenger_management.route('/get_seat_all', methods=['POST'])
def get_all_seat():
    data = request.get_json(silent=True)
    e_info, f_info = get_seat_all(data['f_id'])
    return {'success': True, 'e_info': e_info, 'f_info': f_info}


@passenger_management.route('/delete_ticket', methods=['POST'])
def delete_ticket_info():
    data = request.get_json(silent=True)
    if delete_ticket(data['checked']):
        return {'success': True}
    else:
        return False


@passenger_management.route('/is_empty', methods=['POST'])
def is_empty():
    data = request.get_json(silent=True)
    if isempty(data['id']):
        return {'success': True, 'result': 1}
    else:
        return {'success': False, 'result': 0}
