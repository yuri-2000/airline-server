from tools.global_var import db


class Airline_company(db.Model):
    __tablename__ = 'Airline_company'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(20))
    total = db.Column(db.Integer, default='0')
