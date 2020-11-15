from tools.global_var import db


class Seat(db.Model):
    __tablename__ = 'Seat'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Airplane_id = db.Column(db.Integer, db.ForeignKey('Airplane.id'))  # 飞机-座位 1:n 外键
    seat_num = db.Column(db.String(20))
    CLASS = db.Column(db.String(20))
