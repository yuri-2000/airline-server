from dao.airline_company_inform import Airline_company
from typing import *


def get_admin(username: str):
    query_res = Airline_company.query.filter_by(username=username)
    admin = query_res.first()
    result: Dict[str] = {
        'id': admin.id,
        'username': admin.username,
        'name': admin.name,
    }
    return result
