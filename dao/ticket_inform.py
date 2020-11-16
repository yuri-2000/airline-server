from tools.global_var import db


class Ticket(db.Model):
    __tablename__ = 'Ticket'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Airport_id = db.Column(db.Integer, db.ForeignKey('Airport.id'))  # 机票-机场 n:1 外键
    flight_id = db.Column(db.Integer, db.ForeignKey('Flight.id'))  # 机票-航班 n:1 外键
    Passenger_id = db.Column(db.Integer, db.ForeignKey('Passenger.id'))  # 机票-客户 n:1 外键
    Seat_id = db.Column(db.Integer, db.ForeignKey('Seat.id'))  # 机票-座位 1:1 外键
    start = db.Column(db.String(20))
    destination = db.Column(db.String(20))
    date = db.Column(db.DateTime)
