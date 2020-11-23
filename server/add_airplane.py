from dao.airplane_inform import Airplane
from tools.global_var import db


def add_airplane(
        id,
        air_model,
        eco,
        fir
) -> bool:
    airplane = Airplane(Airline_company_id=id, air_model=air_model, passenger_num_eco=eco, passenger_num_fir=fir)
    db.session.add(airplane)
    db.session.commit()
    return True
