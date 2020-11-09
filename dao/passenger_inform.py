from tools.global_var import db


class Passenger(db.Model):
    __tablename__ = 'Passenger'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(20))
    type = db.Column(db.String(20), default='普通旅客')
    mile_score = db.Column(db.String(20), default=0)
