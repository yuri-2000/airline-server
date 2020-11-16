from dao.ticket_inform import Ticket
from dao.seat_inform import Seat
from dao.airplane_inform import Airplane
from dao.flight_inform import Flight
from typing import *


def get_ticket(p_id):
    tickets = Ticket.query.join(Flight, Ticket.flight_id == Flight.id). \
        filter(Ticket.Passenger_id == p_id). \
        join(Seat, Seat.id == Ticket.Seat_id). \
        with_entities(Ticket.id, Flight.flight_num, Seat.seat_num, Ticket.start, Ticket.destination, Ticket.date).all()
    result: List[Dict[str]] = [{
        'flight_num': ticket.flight_num,
        'start': ticket.start,
        'destination': ticket.destination,
        'seat_num': ticket.seat_num,
        'start_time': str(ticket.date)
    } for ticket in tickets]
    return result

