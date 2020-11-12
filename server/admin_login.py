from dao.airline_company_inform import Airline_company


def admin_login(username: str, password: str) -> bool:
    query_res = Airline_company.query.filter_by(username=username, password=password)
    admin = query_res.first()
    return bool(admin)
