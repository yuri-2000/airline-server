from tools.global_var import db


class Airline_company(db.Model):
    __tablename__ = 'Airline_company'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
