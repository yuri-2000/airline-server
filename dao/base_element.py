from pymysql import NULL
from sqlalchemy import Column, String, create_engine, Integer, DateTime, FLOAT, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from sqlalchemy.sql.elements import and_
from flask_sqlalchemy import SQLAlchemy
import datetime

Base = declarative_base()
engine = create_engine('mysql+pymysql://root:daiski@127.0.0.1:3306/Airline?charset=utf8', echo=True)


class airplane_flight(Base):
    __tablename__ = 'Airplane_flight'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Airplane_id = Column(Integer, ForeignKey('Airplane.id'))
    Flight_id = Column(Integer, ForeignKey('Flight.id'))


class passenger_flight(Base):
    __tablename__ = 'Passenger_flight'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Passenger_id = Column(Integer, ForeignKey('Passenger.id'))
    Flight_id = Column(Integer, ForeignKey('Flight.id'))


class Airline_company(Base):
    __tablename__ = 'Airline_company'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)


class Airline(Base):
    __tablename__ = 'Airline'
    id = Column(Integer, primary_key=True, autoincrement=True)
    airline_num = Column(String(20))
    Airline_company_id = Column(Integer, ForeignKey('Airline_company.id'))  # 航空公司-航线 1:n 外键
    start = Column(String(20))
    destination = Column(String(20))
    flight_num = Column(String(20))
    air_model = Column(String(20))
    start_time = Column(DateTime, default=datetime.datetime.now)
    arrive_time = Column(DateTime, default=datetime.datetime.now)
    passenger_num_eco = Column(Integer)
    passenger_num_fir = Column(Integer)
    mileage = Column(FLOAT)
    standard_price = Column(Integer)


class Flight(Base):
    __tablename__ = 'Flight'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Airline_id = Column(Integer, ForeignKey('Airline.id'))  # 航线-航班 1:n 外键
    Airport_id = Column(Integer, ForeignKey("Airport.id"))  # 机场-航班 1:n 外键
    flight_num = Column(String(20))
    date = Column(DateTime, default=datetime.datetime.now)


class Airport(Base):
    __tablename__ = 'Airport'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))


class Ticket(Base):
    __tablename__ = 'Ticket'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Airport_id = Column(Integer, ForeignKey('Airport.id'))  # 机票-机场 n:1 外键
    flight_id = Column(Integer, ForeignKey('Flight.id'))  # 机票-航班 n:1 外键
    Passenger_id = Column(Integer, ForeignKey('Passenger.id'))  # 机票-客户 n:1 外键
    Seat_id = Column(Integer, ForeignKey('Seat.id'))  # 机票-座位 1:1 外键
    start = Column(String(20))
    destination = Column(String(20))
    date = Column(DateTime)
    price = Column(Integer)


class Passenger(Base):
    __tablename__ = 'Passenger'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    sex = Column(String(20), default='M')
    type = Column(String(20), default='普通旅客')
    mile_score = Column(Integer, default=0)


class Airplane(Base):
    __tablename__ = 'Airplane'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Airline_company_id = Column(Integer, ForeignKey('Airline_company.id'))  # 航空公司-飞机 1:n 外键
    air_model = Column(String(20))


class Seat(Base):
    __tablename__ = 'Seat'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Airplane_id = Column(Integer, ForeignKey('Airplane.id'))  # 飞机-座位 1:n 外键
    seat_num = Column(String(20))
    CLASS = (String(20))


def init_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)


'''建表更新入口'''
# drop_db()
# init_db()

