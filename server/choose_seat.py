from dao.seat_inform import Seat
from dao.airline_inform import Airline
from dao.flight_inform import Flight
from dao.airplane_inform import Airplane
from dao.ticket_inform import Ticket
from tools.global_var import db
from dao.passenger_inform import Passenger
from typing import *


def get_seat_all(f_id):
    flight = Flight.query.filter_by(id=f_id).first()
    airplane = Airplane.query.filter_by(id=flight.Airplane_id).first()
    ecos = Seat.query.filter_by(Airplane_id=airplane.id, CLASS='eco').all()
    firs = Seat.query.filter_by(Airplane_id=airplane.id, CLASS='fir').all()
    eco_result: List[Dict[str]] = [{
        'seat_num': eco.seat_num,
    } for eco in ecos]
    fir_result: List[Dict[str]] = [{
        'seat_num': fir.seat_num,
    } for fir in firs]
    return eco_result, fir_result


def get_seat(f_id, id):
    flight = Flight.query.filter_by(id=f_id).first()
    airplane = Airplane.query.filter_by(id=flight.Airplane_id).first()
    airline = Airline.query.filter_by(id=flight.Airline_id).first()
    passenger = Passenger.query.filter_by(id=id).first()
    eco = airplane.passenger_num_eco
    fir = airplane.passenger_num_fir
    standard_price = airline.standard_price
    type = passenger.type
    return eco, fir, standard_price, type


def add_ticket(id, f_id, seat_num, CLass, start, destination) -> bool:
    flight = Flight.query.filter_by(id=f_id).first()
    seat = Seat(
        Airplane_id=flight.Airplane_id,
        seat_num=seat_num,
        CLASS=CLass
    )
    db.session.add(seat)
    s = Seat.query.filter_by(Airplane_id=flight.Airplane_id,
                             seat_num=seat_num,
                             CLASS=CLass).first()
    ticket = Ticket(Airport_id=flight.Airport_id, flight_id=f_id, Passenger_id=id, Seat_id=s.id,
                    start=start, destination=destination, date=flight.date)
    passenger = Passenger.query.filter_by(id=id).first()
    airline = Airline.query.filter_by(id=flight.Airline_id).first()
    passenger.mile_score += int(airline.mileage)
    if 100 <= passenger.mile_score < 300:
        passenger.type = 0.9
    elif 300 <= passenger.mile_score < 500:
        passenger.type = 0.7
    elif passenger.mile_score >= 500:
        passenger.type = 0.5
    db.session.add(ticket)
    db.session.commit()
    return True
