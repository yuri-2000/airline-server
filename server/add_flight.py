from dao.flight_inform import Flight
from tools.global_var import db


def add_flight(
        airport_id: int,
        airline_id: int,
        flight_num: str,
        start_date: str,
) -> bool:
    query_res = Flight.query.filter_by(Airport_id=airport_id,
                                       Airline_id=airline_id,
                                       flight_num=flight_num,
                                       date=start_date
                                       )
    flight = query_res.first()
    if not flight:
        flight = Flight(
            Airport_id=airport_id,
            Airline_id=airline_id,
            flight_num=flight_num,
            date=start_date
        )
        db.session.add(flight)
    else:
        return False
    db.session.commit()
    return True
