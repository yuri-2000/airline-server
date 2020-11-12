from dao.passenger_inform import Passenger
from tools.global_var import db


def add_passenger(
        username: str,
        password: str,
) -> bool:
    query_res = Passenger.query.filter_by(username=username)
    passenger = query_res.first()
    if not passenger:
        passenger = Passenger(
            username=username,
            password=password,
        )
        db.session.add(passenger)
    else:
        return False
    db.session.commit()
    return True


def add_passenger_info(
        username: str,
        password: str,
        name: str,
        type: str,
        mile_score: str
):
    query_res = Passenger.query.filter_by(username=username)
    passenger = query_res.first()
    if not passenger:
        passenger = Passenger(
            username=username,
            password=password,
            name=name,
            type=type,
            mile_score=mile_score
        )
        db.session.add(passenger)
    else:
        if password != 'do_not_change':
            passenger.password = password
        passenger.username = username
        passenger.name = name
        passenger.type = type
        passenger.mile_score = mile_score
    db.session.commit()
