from tools.global_var import db
from datetime import date


class Airline(db.Model):
    __tablename__ = 'Airline'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Airline_company_id = db.Column(db.Integer, db.ForeignKey('Airline_company.id'))  # 航空公司-航线 1:n 外键
    start = db.Column(db.String(20))
    destination = db.Column(db.String(20))
    flight_num = db.Column(db.String(20))
    air_model = db.Column(db.String(20))
    start_time = db.Column(db.TIME)
    arrive_time = db.Column(db.TIME)
    passenger_quota = db.Column(db.Integer)
    mileage = db.Column(db.Integer)
    standard_price = db.Column(db.Integer)
