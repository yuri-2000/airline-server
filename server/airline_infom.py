from dao.airline_inform import Airline
from dao.flight_inform import Flight
from typing import *


def airline_inform(start, des, date):
    query_res = Airline.query.filter_by(start=start, destination=des, start_time=date)
    airlines = query_res.all()
    result: List[Dict[str]] = [{
        'id': airlines.id,
        'start': airlines.start,
        'destination': airlines.destination,

    }]