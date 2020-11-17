from dao.airline_company_inform import Airline_company
from dao.airline_inform import Airline
from dao.airport_inform import Airport
from dao.flight_inform import Flight
from typing import *


def get_flight(start, des, date):
    flights = Flight.query.join(Airline, Flight.Airline_id == Airline.id). \
        filter(Airline.start == start, Airline.destination == des, Flight.date == date). \
        with_entities(Flight.id,
                      Flight.flight_num,
                      Flight.date,
                      Airline.start,
                      Airline.destination,
                      Airline.start_time,
                      Airline.arrive_time,
                      Airline.standard_price).all()
    result: List[Dict[str]] = [{
        'id': flight.id,
        'flight_num': flight.flight_num,
        'start': flight.start,
        'destination': flight.destination,
        'start_time': str(flight.start_time),
        'arrive_time': str(flight.arrive_time),
        'standard_price': flight.standard_price
    } for flight in flights]
    return result


def get_flight_all():
    flights = Flight.query.all()
    result: List[Dict[str]] = [{
        'id': flight.id,
        'flight_num': flight.flight_num,
        'date': str(flight.date)
    } for flight in flights]
    return result
