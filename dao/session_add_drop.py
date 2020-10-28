from dao.base_element import *


def add_Airline_company(name):
    airline_company = Airline_company(name=name)
    session.add(airline_company)
    session.commit()


def add_Airline(a_n, a_c_id: int, sta, des, f_n, a_m, s_t, a_t, p_n_e: int, p_n_f: int, mil: float, s_p):
    airline = Airline(airline_num=a_n, Airline_company_id=a_c_id, start=sta, destination=des, flight_num=f_n,
                      air_model=a_m, start_time=datetime.datetime(s_t), arrive_time=datetime.datetime(a_t),
                      passenger_num_eco=p_n_e, passenger_num_fir=p_n_f, mileage=mil, standard_price=s_p)
    session.add(airline)
    session.commit()


def add_Flight(airline_i: int, airport_i: int, f_n, date):
    flight = Flight(Airline_id=airline_i, Airport_id=airport_i, flight_num=f_n, date=datetime.datetime(date))
    session.add(flight)
    session.commit()


def add_Airport(name):
    airport = Airport(name=name)
    session.add(airport)
    session.commit()


def add_Ticket(airport_i: int, flight_i: int, pas_i: int, seat_i: int, sta, des, date, price: int):
    ticket = Ticket(Airport_id=airport_i, flight_id=flight_i, Passenger_id=pas_i, Seat_id=seat_i, start=sta,
                    destination=des, date=datetime.datetime(date), price=price)
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


def add_table_a_f(airplane_id: int, flight_id: int):
    a_f = airplane_flight(Airplane_id=airplane_id, Flight_id=flight_id)
    session.add(a_f)
    session.commit()


def add_table_p_f(passenger_id: int, flight_id: int):
    p_f = passenger_flight(Passenger_id=passenger_id, Flight_id=flight_id)
    session.add(p_f)
    session.commit()


add_Airline_company("九元航空")
add_Airline('airline_num', 1, 'SHA', 'GUA', 'flight_num', 'TYPE', '2020, 10, 25', '2020, 10, 27',
            20, 30, 800, 520)
add_Flight(1, 1, 'flight_num', '2020, 10, 25')
add_Airport('Airport')
add_Ticket(1, 1, 1, 1, 'SHA', 'GUA', '2020, 10, 25', 520)
add_Passenger('normal', 0)
add_Airplane(1, 'TYPE')
add_Seat(1, 'seat_num', 'eco')
add_table_a_f(1, 1)
add_table_p_f(1, 1)
