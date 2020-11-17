from dao.seat_inform import Seat
from dao.airline_inform import Airline
from tools.global_var import db


def get_seat(a_id):
    airline = Airline.query.filter_by(id=a_id).first()
    result = airline.passenger_num_fir + airline.passenger_num_eco
    if result / 10 != 0:
        result -= result % 10
    return result


def choose_seat(Airplane_id, seat_num, CLASS):
    seat = Seat(
        Airplane_id=Airplane_id,
        seat_num=seat_num,
        CLASS=CLASS
    )
    db.session.add(seat)
    db.session.commit()
