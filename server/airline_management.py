from dao.airline_company_inform import Airline_company
from dao.airline_inform import Airline
from dao.airport_inform import Airport
from dao.flight_inform import Flight
from typing import *


def get_airline(a_id):
    query_res = Airline.query.filter_by(Airline_company_id=a_id)
    airlines = query_res.all()
    result: List[Dict[str]] = [{
        'flight_num': airline.flight_num,
        'start': airline.start,
        'destination': airline.destination,
        'start_date': airline.start_time,
        'standard_price': airline.standard_price
    } for airline in airlines]
    return result
