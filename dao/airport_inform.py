from tools.global_var import db


class Airport(db.Model):
    __tablename__ = 'Airport'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))