from dao.airline_inform import Airline
from tools.global_var import db


def add_airline(
        airline_company_id: int,
        start: str,
        destination: str,
        air_model: str,
        flight_num: str,
        start_date: str,
        arrive_date: str,
        eco: int,
        fir: int,
        mileage: int,
        standard_price: int
) -> bool:
    query_res = Airline.query.filter_by(Airline_company_id=airline_company_id,
                                        start=start,
                                        destination=destination,
                                        air_model=air_model,
                                        flight_num=flight_num,
                                        start_time=start_date,
                                        arrive_time=arrive_date,
                                        passenger_num_eco=eco,
                                        passenger_num_fir=fir,
                                        mileage=mileage,
                                        standard_price=standard_price)
    airline = query_res.first()
    if not airline:
        airline = Airline(
            Airline_company_id=airline_company_id,
            start=start,
            destination=destination,
            air_model=air_model,
            flight_num=flight_num,
            start_time=start_date,
            arrive_time=arrive_date,
            passenger_num_eco=eco,
            passenger_num_fir=fir,
            mileage=mileage,
            standard_price=standard_price
        )
        db.session.add(airline)
    else:
        return False
    db.session.commit()
    return True
