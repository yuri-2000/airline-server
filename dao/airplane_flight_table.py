from tools.global_var import db


class airplane_flight(db.Model):
    __tablename__ = 'Airplane_flight'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Airplane_id = db.Column(db.Integer, db.ForeignKey('Airplane.id'))
    Flight_id = db.Column(db.Integer, db.ForeignKey('Flight.id'))