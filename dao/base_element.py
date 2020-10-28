from pymysql import NULL
from sqlalchemy import Column, String, create_engine, Integer, DateTime, FLOAT, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()
engine = create_engine('mysql+pymysql://root:@127.0.0.1:3306/test', echo=True)

airplane_flight = Table('airplane_flight', Base.metadata,  # 飞机-航班 m:n
                        Column('Airplane_id', Integer, ForeignKey('Airplane.id'), primary_key=True),  #
                        Column('Flight_id', Integer, ForeignKey('Flight.id'), primary_key=True),  #
                        )

passenger_flight = Table('passenger_flight', Base.metadata,
                         Column('Passenger_id', Integer, ForeignKey('Passenger.id'), primary_key=True),  #
                         Column('Flight_id', Integer, ForeignKey('Flight.id'), primary_key=True),  #

                         )


class Airline_company(Base):
    __tablename__ = 'Airline_company'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)

    def __repr__(self):
        tql = "Airline_company(id={}, name={}, airlines={}, flights={})"
        return tql.format(self.id, self.name)


class Airline(Base):
    __tablename__ = 'Airline'
    id = Column(Integer, primary_key=True, autoincrement=True)
    airline_num = Column(String(20))
    Airline_company_id = Column(Integer, ForeignKey('Airline_company.id'), default=NULL)  # 航空公司-航线 1:n 外键
    airline_company = relationship("Airline_company", backref="Airline_of_Airline_company")
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

    def __repr__(self):
        tql = "Airline(id={}, Airline_num={}, Airline_company_id={}, start={}, destination={}, flight_num={}, " \
              "air_model={}, start_time={}, arrive_time={}, passenger_num_eco={}, passenger_num_fir={}, mileage={}, " \
              "standard_price={})"
        return tql.format(self.id, self.airline_num, self.Airline_company_id, self.start, self.destination,
                          self.flight_num, self.air_model, self.start_time, self.arrive_time, self.passenger_num_eco,
                          self.passenger_num_fir, self.mileage, self.standard_price)


class Flight(Base):
    __tablename__ = 'Flight'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Airline_id = Column(Integer, ForeignKey('Airline.id'), default=NULL)  # 航线-航班 1:n 外键
    airline = relationship("Airline_company", backref="Flight_of_Airline")
    Airport_id = Column(Integer, ForeignKey("Airport.id"), default=NULL)  # 机场-航班 1:n 外键
    airport = relationship("Airport", backref="Flight_of_Airport")
    flight_num = Column(String(20))
    date = Column(DateTime, default=datetime.datetime.now)
    airplanes = relationship("Airplane", secondary=airplane_flight, backref='Flight')
    passengers = relationship("Passenger", secondary=passenger_flight, backref='Flight')

    def __repr__(self):
        tql = "Flight(id={}, Airline_id={}, Airport_id={}, flight_num={}, date={})"
        return tql.format(self.id, self.Airline_id, self.Airport_id, self.flight_num, self.date)


class Airport(Base):
    __tablename__ = 'Airport'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))


class Ticket(Base):
    __tablename__ = 'Ticket'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Airport_id = Column(Integer, ForeignKey('Airport.id'), default=NULL)  # 机票-机场 n:1 外键
    airport = relationship("Airport", backref="Ticket_of_Airport")
    flight_id = Column(Integer, ForeignKey('Flight.id'), default=NULL)  # 机票-航班 n:1 外键
    flight = relationship("Flight", backref="Ticket_of_Flight")
    Passenger_id = Column(Integer, ForeignKey('Passenger.id'), default=NULL)  # 机票-客户 n:1 外键
    passenger = relationship("Passenger", backref="Ticket_of_Passenger")
    Seat_id = Column(Integer, ForeignKey('Seat.id'), default=NULL)  # 机票-座位 1:1 外键
    seat = relationship("Seat", backref="Ticket_of_Seat")
    start = Column(String(20))
    destination = Column(String(20))
    date = Column(DateTime)
    price = Column(Integer)


class Passenger(Base):
    __tablename__ = 'Passenger'
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(20), default='普通旅客')
    mile_score = Column(Integer, default=0)


class Airplane(Base):
    __tablename__ = 'Airplane'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Airline_company_id = Column(Integer, ForeignKey('Airline_company.id'), default=NULL)  # 航空公司-飞机 1:n 外键
    airline_company = relationship("Airline_company", backref="Airplane_of_Airline_company")
    air_model = Column(String(20))


class Seat(Base):
    __tablename__ = 'Seat'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Airplane_id = Column(Integer, ForeignKey('Airplane.id'), default=NULL)  # 飞机-座位 1:n 外键
    airplane = relationship("Airplane", backref="Ticket_of_Airplane")
    seat_num = Column(String(20))
    CLASS = (String(20))


def init_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)


'''更新入口'''
# drop_db()
# init_db()


Session = sessionmaker(bind=engine)
session = Session

# session.add_all((
#     Airline_company(name='九元航空'),
# ))
#
# session.add_all([
#     Airline(Airline_company_id=1, airline_num='C346', start='宁波', destination='广州', flight_num='C789',
#             air_model='B820', start_time=datetime.datetime(2020, 10, 23), arrive_time=datetime.datetime(2020, 10, 24),
#             passenger_num_eco=30, passenger_num_fir=20, mileage=50, standard_price=838),
# ])
#
# session.add_all([
#     Flight(Airline_company_id=1, flight_num='C789', date=datetime.datetime(2020, 10, 23), passenger_list='1',
#            position='2')
# ])
