from flask.blueprints import Blueprint
from tools.global_var import s
from flask import request
from service.passenger_login import passenger_login


passenger_management = Blueprint('passenger', __name__, url_prefix='/passenger')


@passenger_management.route('/login', methods=['POST'])
def login():
    data = request.get_json(silent=True)
    username: str = data['username']
    password: str = data['password']
    if passenger_login(username, password):
        token = s.dumps({'username': username, 'role': 'passenger'}).decode("ascii")
        return {'success': True, 'token': token}
    else:
        return {'success': False, 'info': 'username or password incorrect.'}
