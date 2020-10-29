from dao.base_element import *

Session = sessionmaker(bind=engine)
session = Session()


def show_airline(sta, des):
    airlines = session.query(Airline).filter(and_(Airline.start == sta, Airline.destination == des)).all()
    n = 1
    for airline in airlines:
        total = airline.passenger_num_fir + airline.passenger_num_eco
        flight = session.query(Flight).filter(Flight.Airline_id == airline.id).first()
        query = session.query(passenger_flight).filter(Flight.id == flight.id).all()
        rest = total - query
        print(f'{n}.航班号: {airline.flight_num},出发时间: {airline.start_time},预计抵达时间:{airline.arrive_time},'
              f'票价: {airline.standard_price}, 余票量: {rest}')
        n += 1


if __name__ == "__main__":
    print("欢迎使用航空订票系统！")
    print("输入你的出发地：")
    start = input()
    print("输入你的目的地：")
    destination = input()
    show_airline(start, destination)
    session.commit()
    session.close()
