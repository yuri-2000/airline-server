from dao.passenger_inform import Passenger
from typing import *


def get_passenger(username: str):
    query_res = Passenger.query.filter_by(username=username)
    passenger = query_res.first()
    result: Dict[str] = {
        'id': passenger.id,
        'username': passenger.username,
        'name': passenger.name,
        'gender': passenger.gender,
        'type': passenger.type,
        'mile_score': passenger.mile_score,
    }
    return result
