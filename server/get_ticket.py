from dao.ticket_inform import Ticket
from dao.seat_inform import Seat
from dao.passenger_inform import Passenger
from dao.flight_inform import Flight
from typing import *
from dao.airline_inform import Airline
from tools.global_var import db


def get_ticket(p_id):
    tickets = Ticket.query.join(Flight, Ticket.flight_id == Flight.id). \
        filter(Ticket.Passenger_id == p_id). \
        join(Seat, Seat.id == Ticket.Seat_id). \
        join(Airline, Airline.id == Flight.Airline_id). \
        with_entities(Ticket.id, Flight.flight_num, Seat.seat_num, Ticket.start, Ticket.destination,
                      Airline.start_time, Airline.arrive_time, Flight.date, Seat.CLASS).all()
    result: List[Dict[str]] = [{
        't_id': ticket.id,
        'flight_num': ticket.flight_num,
        'start': ticket.start,
        'destination': ticket.destination,
        'seat_num': ticket.seat_num,
        'CLass': ticket.CLASS,
        'start_date': str(ticket.date),
        'start_time': str(ticket.start_time),
        'arrive_time': str(ticket.arrive_time)
    } for ticket in tickets]
    return result


def filter_ticket(p_id, date, flight_num):
    tickets = Ticket.query.join(Flight, Ticket.flight_id == Flight.id). \
        filter(Ticket.Passenger_id == p_id, Flight.flight_num.like("%" + flight_num + "%"),
               Flight.date.like("%" + date + "%")). \
        join(Seat, Seat.id == Ticket.Seat_id). \
        join(Airline, Airline.id == Flight.Airline_id). \
        with_entities(Ticket.id, Flight.flight_num, Seat.seat_num, Ticket.start, Ticket.destination,
                      Airline.start_time, Airline.arrive_time, Flight.date, Seat.CLASS).all()
    result: List[Dict[str]] = [{
        't_id': ticket.id,
        'flight_num': ticket.flight_num,
        'start': ticket.start,
        'destination': ticket.destination,
        'seat_num': ticket.seat_num,
        'CLass': ticket.CLASS,
        'start_date': str(ticket.date),
        'start_time': str(ticket.start_time),
        'arrive_time': str(ticket.arrive_time)
    } for ticket in tickets]
    return result


def delete_ticket(checked):
    for value in checked:
        ticket = Ticket.query.filter_by(id=value).first()
        seat = Seat.query.filter_by(id=ticket.Seat_id).first()
        flight = Flight.query.filter_by(id=ticket.flight_id).first()
        airline = Airline.query.filter_by(id=flight.Airline_id).first()
        passenger = Passenger.query.filter_by(id=ticket.Passenger_id).first()
        db.session.delete(ticket)
        db.session.commit()
        db.session.delete(seat)
        passenger.mile_score -= int(airline.mileage)
        db.session.commit()
    return True
