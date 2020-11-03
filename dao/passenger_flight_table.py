from tools.global_var import db


class passenger_flight(db.Model):
    __tablename__ = 'Passenger_flight'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Passenger_id = db.Column(db.Integer, db.ForeignKey('Passenger.id'))
    Flight_id = db.Column(db.Integer, db.ForeignKey('Flight.id'))
