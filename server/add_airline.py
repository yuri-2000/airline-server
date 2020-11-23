from dao.airline_inform import Airline
from dao.flight_inform import Flight
from tools.global_var import db


def add_airline(
        airline_company_id: int,
        start: str,
        destination: str,
        air_model: str,
        flight_num: str,
        start_time: str,
        arrive_time: str,
        quota: int,
        mileage: int,
        standard_price: int
) -> bool:
    airline = Airline.query.filter_by(
        Airline_company_id=airline_company_id,
        start=start,
        destination=destination,
        air_model=air_model,
        flight_num=flight_num,
        start_time=start_time,
        arrive_time=arrive_time,
        passenger_quota=quota,
        mileage=mileage,
        standard_price=standard_price
    ).first()
    if not airline:
        airline = Airline(
            Airline_company_id=airline_company_id,
            start=start,
            destination=destination,
            air_model=air_model,
            flight_num=flight_num,
            start_time=start_time,
            arrive_time=arrive_time,
            passenger_quota=quota,
            mileage=mileage,
            standard_price=standard_price
        )
        db.session.add(airline)
    else:
        return False
    db.session.commit()
    return True


def update_airline(
        a_id: int,
        airline_company_id: int,
        start: str,
        destination: str,
        air_model: str,
        flight_num: str,
        start_time: str,
        arrive_time: str,
        quota: int,
        mileage: int,
        standard_price: int
) -> bool:
    query_res = Airline.query.filter_by(id=a_id)
    airline = query_res.first()
    if not airline:
        airline = Airline(
            Airline_company_id=airline_company_id,
            start=start,
            destination=destination,
            air_model=air_model,
            flight_num=flight_num,
            start_time=start_time,
            arrive_time=arrive_time,
            passenger_quota=quota,
            mileage=mileage,
            standard_price=standard_price
        )
        db.session.add(airline)
    else:
        airline.airline_company_id = airline_company_id
        airline.start = start
        airline.destination = destination
        airline.air_model = air_model
        airline.flight_num = flight_num
        airline.arrive_time = arrive_time
        airline.passenger_quota = quota
        airline.mileage = mileage
        airline.standard_price = standard_price
    db.session.commit()
    return True



