from dao.base_element import *


def add_Airline_company(name):
    airline_company = Airline_company(name=name)
    session.add(airline_company)
    session.commit()


def add_Airline(a_n, a_c_id, sta, des, f_n, a_m, s_t, a_t, p_n_e, p_n_f, mil, s_p):
    airline = Airline(airline_num=a_n, Airline_company_id=a_c_id, start=sta, destination=des, flight_num=f_n,
                      air_model=a_m, start_time=s_t, arrive_time=a_t,
                      passenger_num_eco=p_n_e, passenger_num_fir=p_n_f, mileage=mil, standard_price=s_p)
    session.add(airline)
    session.commit()


def add_Flight(airline_i: int, airport_i: int, f_n, date):
    flight = Flight(Airline_id=airline_i, Airport_id=airport_i, flight_num=f_n, date=date)
    session.add(flight)
    session.commit()


def add_Airport(name):
    airport = Airport(name=name)
    session.add(airport)
    session.commit()


def add_Ticket(airport_i: int, flight_i: int, pas_i: int, seat_i: int, sta, des, date, price: int):
    ticket = Ticket(Airport_id=airport_i, flight_id=flight_i, Passenger_id=pas_i, Seat_id=seat_i, start=sta,
                    destination=des, date=date, price=price)
    session.add(ticket)
    session.commit()


def add_Passenger(name, sex, typ, mile_score: int):
    passenger = Passenger(name=name, sex=sex, type=typ, mile_score=mile_score)
    session.add(passenger)
    session.commit()


def add_Airplane(a_c_i: int, a_m):
    airplane = Airplane(Airline_company_id=a_c_i, air_model=a_m)
    session.add(airplane)
    session.commit()


def add_Seat(airplane_i: int, seat_num, Type):
    seat = Seat(Airplane_id=airplane_i, seat_num=seat_num, CLASS=Type)
    session.add(seat)
    session.commit()


def add_airplane_flight(airplane_id, flight_id):
    a_f = airplane_flight(Airplane_id=airplane_id, Flight_id=flight_id)
    session.add(a_f)
    session.commit()


def add_passenger_flight(passenger_id, flight_id):
    p_f = passenger_flight(Passenger_id=passenger_id, Flight_id=flight_id)
    session.add(p_f)
    session.commit()


Session = sessionmaker(bind=engine)
session = Session()

"""还原数据库入口"""
"""测试用数据入口（添加） 3*10"""
# add_Airline_company('南方航空')
# add_Airline('A0001', 1, '上海', '广州', 'A1024', '波音747', datetime.datetime(2020, 10, 25, 10, 30),
#             datetime.datetime(2020, 10, 27, 11), 20, 30, 800, 520)
# add_Airport('虹桥国际机场')
# add_Flight(1, 1, 'A1024', datetime.datetime(2020, 10, 25, 10, 30))
# add_Airplane(1, '空客330')
# add_Passenger('zsc', 'male', 'vip', 20)
# add_Seat(1, 'A01', 'eco')
# add_Ticket(1, 1, 1, 1, '上海', '广州', datetime.datetime(2020, 10, 25, 10, 30), 520)
# add_airplane_flight(1, 1)
# add_passenger_flight(1, 1)
# add_Airline_company('九元航空')
# add_Airline_company('东方航空')
# add_Airplane(2, '空客320')
# add_Airplane(3, '空客330')
# add_Airport('浦东国际机场')
# add_Airport('白云国际机场')
# add_Passenger('ame', 'male', 'normal', 0)
# add_Passenger('ams', 'female', 'normal', 0)
# add_Airline('B0002', 2, '上海', '广州', 'B2048', '空客320', datetime.datetime(2020, 10, 24, 11, 30),
#             datetime.datetime(2020, 10, 28, 13), 30, 20, 800, 521)
# add_Airline('C0003', 3, '上海', '广州', 'C4096', '空客330', datetime.datetime(2020, 10, 26, 7, 30),
#             datetime.datetime(2020, 10, 26, 15), 30, 30, 800, 1001)
# add_Flight(2, 2, 'B2048', datetime.datetime(2020, 10, 24, 11, 30))
# add_Flight(3, 3, 'C4096', datetime.datetime(2020, 10, 26, 7, 30))
# add_Seat(2, 'B02', 'eco')
# add_Seat(3, 'C33', 'fir')
# add_Ticket(2, 2, 2, 2, '上海', '广州', datetime.datetime(2020, 10, 24, 11, 30), 521)
# add_Ticket(3, 3, 3, 3, '上海', '广州', datetime.datetime(2020, 10, 26, 15), 1000)
# add_airplane_flight(2, 2)
# add_passenger_flight(2, 2)
# add_airplane_flight(3, 3)
# add_passenger_flight(3, 3)
