from dao.airline_company_inform import Airline_company
from dao.airline_inform import Airline
from dao.airport_inform import Airport
from dao.flight_inform import Flight
from typing import *


def get_airline(a_id):
    query_res = Airline.query.filter_by(Airline_company_id=a_id)
    airlines = query_res.all()
    result: List[Dict[str]] = [{
        'a_id': airline.id,
        'flight_num': airline.flight_num,
        'start': airline.start,
        'destination': airline.destination,
        'start_time': str(airline.start_time),
        'standard_price': airline.standard_price,
        'mileage': airline.mileage,
        'quota': airline.passenger_quota
    } for airline in airlines]
    return result


def get_airline_id(a_id):
    airline = Airline.query.filter_by(id=a_id).first()
    airline_company = Airline_company.query.filter_by(id=airline.Airline_company_id).first()
    result: Dict[str] = {
        'a_id': airline.id,
        'a_c_id': airline.Airline_company_id,
        'a_c_name': airline_company.name,
        'start': airline.start,
        'destination': airline.destination,
        'air_model': airline.air_model,
        'flight_num': airline.flight_num,
        'start_time': str(airline.start_time),
        'arrive_time': str(airline.arrive_time),
        'quota': airline.passenger_quota,
        'mileage': airline.mileage,
        'standard_price': airline.standard_price
    }
    return result


def get_airline_all():
    airlines = Airline.query.all()
    result: List[Dict[str]] = [{
        'airline_id': airline.id,
        'start': airline.start,
        'destination': airline.destination,
        'start_time': str(airline.start_time),
        'mileage': airline.mileage,
        'quota': airline.passenger_quota
    } for airline in airlines]
    return result
