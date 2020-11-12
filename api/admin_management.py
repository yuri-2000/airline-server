from flask.blueprints import Blueprint
from typing import *
import datetime
from flask import request
from server.admin_login import admin_login
from server.add_admin import *

admin_management = Blueprint('admin', __name__, url_prefix='/admin')


@admin_management.route('/login', methods=['POST'])
def login():
    data = request.get_json(silent=True)
    username: str = data['username']
    password: str = data['password']
    if admin_login(username, password):
        return {'success': True}
    else:
        return {'success': False, 'info': 'username or password incorrect.'}


@admin_management.route('/register', methods=['POST'])
def register_admin():
    data = request.get_json(silent=True)
    username = data['username']
    password = data['password']
    if add_admin(username, password):
        return {'success': True}
    else:
        return {'success': False, 'info': "user exist"}

