from dao.airline_company_inform import Airline_company
from tools.global_var import db


def add_admin(username: str, password: str) -> bool:
    query_res = Airline_company.query.filter_by(username=username)
    admin = query_res.first()
    if not admin:
        admin = Airline_company(
            username=username,
            password=password
        )
        db.session.add(admin)
    else:
        return False
    db.session.commit()
    return True


def add_admin_info(
        username: str,
        password: str,
        name: str
):
    query_res = Airline_company.query.filter_by(username=username)
    admin = query_res.first()
    if not admin:
        admin = admin(
            username=username,
            password=password,
            name=name,
        )
        db.session.add(admin)
    else:
        if password != 'do_not_change':
            admin.password = password
        admin.username = username
        admin.name = name
    db.session.commit()
