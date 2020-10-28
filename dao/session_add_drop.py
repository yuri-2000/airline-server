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


def add_Passenger(typ, mile_score: int):
    passenger = Passenger(type=typ, mile_score=mile_score)
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


def add_table_a_f(airplane_id: int):
    Flight.airplanes = [airplane_id]
    session.add(Flight.airplanes)
    session.commit()


def add_table_p_f(passenger_id: int):
    Flight.passengers = [passenger_id]
    session.add(Flight)
    session.commit()


Session = sessionmaker(bind=engine)
session = Session()


add_Airline_company('九元航空')
add_Airline('airline_num', 1, 'SHA', 'GUA', 'flight_num', 'TYPE', datetime.datetime(2020, 10, 25, 10, 30),
            datetime.datetime(2020, 10, 27, 11), 20, 30, 800, 520)
add_Airport('Airport')
add_Flight(1, 1, 'flight_num', datetime.datetime(2020, 10, 25, 10, 30))
add_Airplane(1, 'TYPE')
add_Passenger('normal', 0)
add_Seat(1, 'seat_num', 'eco')
add_Ticket(1, 1, 1, 1, 'SHA', 'GUA', datetime.datetime(2020, 10, 25, 10, 30), 520)
# add_table_a_f(1, 1)
# add_table_p_f(1, 1)
# Flight.airplanes = [1]
# session.commit()

