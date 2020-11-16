from dao.passenger_inform import Passenger


def passenger_login(username: str, password: str) -> bool:
    query_res: Passenger = Passenger.query.filter_by(username=username, password=password)
    res_manage: Passenger = query_res.first()
    return bool(res_manage)


def passenger_login_id(username: str, password: str):
    query_res: Passenger = Passenger.query.filter_by(username=username, password=password)
    res_manage: Passenger = query_res.first()
    return res_manage.id
