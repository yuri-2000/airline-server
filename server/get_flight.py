from pymysql.constants.FIELD_TYPE import NULL

from dao.airline_company_inform import Airline_company
from dao.airline_inform import Airline
from dao.airport_inform import Airport
from dao.seat_inform import Seat
from dao.flight_inform import Flight
from dao.airplane_inform import Airplane
from dao.passenger_inform import Passenger
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


def get_flight_id(f_id):
    flight = Flight.query.filter_by(id=f_id).first()
    airport = Airport.query.filter_by(id=flight.Airport_id).first()
    result: Dict[str] = {
        'a_id': flight.Airline_id,
        'airport_id': flight.Airport_id,
        'airport_name': airport.name,
        'airplane_id': flight.Airplane_id,
        'flight_num': flight.flight_num,
        'date': str(flight.date),
    }
    return result


def get_flight_all(id):
    flights = Flight.query.join(Airline, Airline.id == Flight.Airline_id). \
        join(Airline_company, Airline_company.id == Airline.Airline_company_id). \
        join(Airplane, Airplane.id == Flight.Airplane_id). \
        filter(Airline_company.id == id). \
        with_entities(Flight.id, Flight.flight_num, Airplane.passenger_num_eco, Airplane.passenger_num_fir,
                      Flight.date, Airplane.air_model).all()
    result: List[Dict[str]] = [{
        'f_id': flight.id,
        'air_model': flight.air_model,
        'flight_num': flight.flight_num,
        'eco': flight.passenger_num_eco,
        'fir': flight.passenger_num_fir,
        'date': str(flight.date),
    } for flight in flights]
    return result


def isempty(id) -> bool:
    passenger = Passenger.query.filter_by(id=id).first()
    if passenger.name != 'need to change':
        return True
    else:
        return False
