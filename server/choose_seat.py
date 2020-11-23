from dao.seat_inform import Seat
from dao.airline_inform import Airline
from dao.flight_inform import Flight
from dao.airplane_inform import Airplane
from dao.ticket_inform import Ticket
from tools.global_var import db
from dao.passenger_flight_table import passenger_flight
from dao.passenger_inform import Passenger
from typing import *


def get_seat_all(f_id):
    flight = Flight.query.filter_by(id=f_id).first()
    airplane = Airplane.query.filter_by(id=flight.Airplane_id).first()
    seats = Seat.query.filter_by(Airplane_id=airplane.id).all()
    result: List[Dict[str]] = [{
        'CLass': seat.CLASS,
        'seat_num': seat.seat_num,
    } for seat in seats]
    return result


def get_seat(f_id, id):
    flight = Flight.query.filter_by(id=f_id).first()
    airline = Airline.query.filter_by(id=flight.Airline_id).first()
    passenger = Passenger.query.filter_by(id=id).first()
    eco = airline.passenger_num_eco
    fir = airline.passenger_num_fir
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
    res = passenger_flight.query.filter_by(Passenger_id=id, Flight_id=f_id).first()
    passenger = Passenger.query.filter_by(id=id).first()
    airline = Airline.query.filter_by(id=flight.Airline_id).first()
    passenger.mile_score += int(airline.mileage)
    if not res:
        res = passenger_flight(
            Passenger_id=id,
            Flight_id=f_id
        )
        db.session.add(res)
    db.session.add(ticket)
    db.session.commit()
    return True
