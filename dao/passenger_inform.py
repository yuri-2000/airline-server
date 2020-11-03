from tools.global_var import db


class Passenger(db.Model):
    __tablename__ = 'Passenger'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    password = db.Column(db.String(128), nullable=False)
    sex = db.Column(db.String(20), default='M')
    type = db.Column(db.String(20), default='普通旅客')
    mile_score = db.Column(db.Integer, default=0)
