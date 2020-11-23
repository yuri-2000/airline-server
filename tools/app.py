from flask import Flask
from flask_cors import CORS
from tools.global_var import db
import config
from api.passenger_management import passenger_management
from api.admin_management import admin_management

app = Flask(__name__)
app.config.from_object(config)
CORS(app, resources=r'/*', supports_credentials=True)


def init():
    app.register_blueprint(passenger_management)
    app.register_blueprint(admin_management)


init()

with app.app_context():
    db.init_app(app=app)
    db.drop_all()
    db.create_all()

if __name__ == '__main__':
    app.run()
