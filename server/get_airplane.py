from dao.airplane_inform import Airplane
from typing import *


def get_airplane_all():
    airplanes = Airplane.query.all()
    result: List[Dict[str]] = [{
        'airplane_id': airplane.id,
        'air_model': airplane.air_model,
        'total': airplane.passenger_num_eco + airplane.passenger_num_fir
    } for airplane in airplanes]
    return result
