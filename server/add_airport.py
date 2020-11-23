from dao.airport_inform import Airport
from tools.global_var import db


def add_airport(
        name, address, telephone
) -> bool:
    query_res = Airport.query.filter_by(name=name)
    airport = query_res.first()
    if not airport:
        airport = Airport(
            name=name,
            address=address,
            telephone=telephone,
        )
        db.session.add(airport)
    else:
        return False
    db.session.commit()
    return True
