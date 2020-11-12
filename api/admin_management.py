from flask.blueprints import Blueprint
from typing import *
import datetime
from flask import request
from server.admin_login import admin_login
from server.add_admin import *
from server.get_admin import get_admin
from server.airline_management import get_airline

admin_management = Blueprint('admin', __name__, url_prefix='/admin')


@admin_management.route('/login', methods=['POST'])
def login():
    data = request.get_json(silent=True)
    username: str = data['username']
    password: str = data['password']
    if admin_login(username, password):
        admin_id = admin_login(username, password)
        return {'success': True, 'id': admin_id}
    else:
        return {'success': False, 'info': 'username or password incorrect.'}


@admin_management.route('/register', methods=['POST'])
def register_admin():
    data = request.get_json(silent=True)
    username = data['username']
    password = data['password']
    if add_admin(username, password):
        admin_id = admin_login(username, password)
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

