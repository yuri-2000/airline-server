from dao.passenger_inform import Passenger
import hashlib


# def admin_login(username: str, password: str) -> bool:
#     password_m = hashlib.md5(password.encode())
#     password_hash = password_m.hexdigest()
#     query_res: PropertyManagementInformation = PropertyManagementInformation.query.filter_by(username=username,
#                                                                                              password=password_hash)
#     prop_manage: PropertyManagementInformation = query_res.first()
#     return bool(prop_manage)


def passenger_login(username: str, password: str) -> bool:
    query_res: Passenger = Passenger.query.filter_by(username=username, password=password)
    res_manage: Passenger = query_res.first()
    return bool(res_manage)
