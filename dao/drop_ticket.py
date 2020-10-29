from dao.base_element import *


def deter_pi(p_name):
    passenger = session.query(Passenger).filter(Passenger.name == p_name).first()
    print(f'你的乘客id是： {passenger.id}')
    ticket = session.query(Ticket).filter(Ticket.Passenger_id == passenger.id).first()
    flight = session.query(Flight).filter(Flight.id == ticket.flight_id).first()
    print(f'你的所有订票信息如下：\n航班号： {flight.flight_num}\n出发地： {ticket.start}\n目的地： {ticket.destination}')
    return passenger.id


def deter_fi(f_num):
    flight = session.query(Flight).filter(Flight.flight_num == f_num).first()
    print(f'航班id是: {flight.id}')
    return flight.id


def refund_ticket(pass_id, flight_id):
    session.query(Ticket).filter(Ticket.flight_id == flight_id).delete()
    session.query(passenger_flight).filter(and_(passenger_flight.Flight_id == flight_id,
                                                passenger_flight.Passenger_id == pass_id)).delete()
    print("退票成功！")
    pass


Session = sessionmaker(bind=engine)
session = Session()


if __name__ == "__main__":
    print("输入你的姓名")
    passenger_name = input()
    deter_pi(passenger_name)
    print("输入要退票的航班号")
    flight_num = input()
    deter_fi(flight_num)
    f_id = deter_fi(flight_num)
    p_id = deter_pi(passenger_name)
    refund_ticket(p_id, f_id)
    session.commit()
    session.close()
