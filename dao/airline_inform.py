from tools.global_var import db


class Airline(db.Model):
    __tablename__ = 'Airline'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    airline_num = db.Column(db.String(20))
    Airline_company_id = db.Column(db.Integer, db.ForeignKey('Airline_company.id'))  # 航空公司-航线 1:n 外键
    start = db.Column(db.String(20))
    destination = db.Column(db.String(20))
    flight_num = db.Column(db.String(20))
    air_model = db.Column(db.String(20))
    start_time = db.Column(db.DateTime, default=db.datetime.datetime.now)
    arrive_time = db.Column(db.DateTime, default=db.datetime.datetime.now)
    passenger_num_eco = db.Column(db.Integer)
    passenger_num_fir = db.Column(db.Integer)
    mileage = db.Column(db.FLOAT)
    standard_price = db.Column(db.Integer)
