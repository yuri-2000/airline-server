from tools.global_var import db


class Flight(db.Model):
    __tablename__ = 'Flight'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Airline_id = db.Column(db.Integer, db.ForeignKey('Airline.id'))  # 航线-航班 1:n 外键
    Airport_id = db.Column(db.Integer, db.ForeignKey("Airport.id"))  # 机场-航班 1:n 外键
    flight_num = db.Column(db.String(20))
    date = db.Column(db.DateTime, default=db.datetime.datetime.now)
