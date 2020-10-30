from dao.base_element import *
from dao.session_add import add_Ticket, add_passenger_flight

Session = sessionmaker(bind=engine)
session = Session()


def show_airline(sta, des):
    airlines = session.query(Airline).filter(and_(Airline.start == sta, Airline.destination == des)).all()
    n = 1
    for airline in airlines:
        total = airline.passenger_num_fir + airline.passenger_num_eco
        flight = session.query(Flight).filter(Flight.Airline_id == airline.id).first()
        ticket_count = session.query(func.count(passenger_flight.Passenger_id)).\
            filter(passenger_flight.Flight_id == flight.id).scalar()
        rest = total - ticket_count
        print(f'{n}.航班号: {airline.flight_num},出发时间: {airline.start_time},预计抵达时间:{airline.arrive_time},'
              f'票价: {airline.standard_price}, 余票量: {rest} ')
        n += 1


def buy_ticket(pas_id, fli_id, seat_id, sta, des):
    flight = session.query(Flight).filter(Flight.id == fli_id).first()
    airline = session.query(Airline).filter(Airline.flight_num == flight.flight_num).first()
    add_Ticket(flight.Airport_id, fli_id, pas_id, seat_id, sta, des, flight.date, airline.standard_price)
    print(f"购票成功！您的机票信息如下：\n航班号: {flight.flight_num} 姓名：")


if __name__ == "__main__":
    print("欢迎使用航空订票系统！")
    print("输入你的出发地：")
    start = input()
    print("输入你的目的地：")
    destination = input()
    show_airline(start, destination)
    print("输入购票的航班号")
    flight_id = input()
    buy_ticket(1, flight_id, 1, start, destination)
    session.commit()
    session.close()
