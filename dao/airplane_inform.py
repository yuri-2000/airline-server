from tools.global_var import db


class Airplane(db.Model):
    __tablename__ = 'Airplane'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Airline_company_id = db.Column(db.Integer, db.ForeignKey('Airline_company.id'))  # 航空公司-飞机 1:n 外键
    air_model = db.Column(db.String(20))
