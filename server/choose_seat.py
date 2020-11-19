from dao.seat_inform import Seat
from dao.airline_inform import Airline
from dao.flight_inform import Flight
from dao.airplane_inform import Airplane
from dao.ticket_inform import Ticket
from tools.global_var import db
from dao.passenger_flight_table import passenger_flight


def get_seat(a_id):
    airline = Airline.query.filter_by(id=a_id).first()
    result = airline.passenger_num_fir + airline.passenger_num_eco
    if result / 10 != 0:
        result -= result % 10
    return result


def add_ticket(id, f_id, seat_num, CLass, start, destination):
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
    if not res:
        res = passenger_flight(
            Passenger_id=id,
            Flight_id=f_id
        )
        db.session.add(res)
    else:
        return False
    db.session.add(ticket)
    db.session.commit()
