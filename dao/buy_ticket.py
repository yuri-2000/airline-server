import string

from dao.base_element import *
from dao.session_add import add_Ticket, add_passenger_flight, add_Passenger, add_Seat
import random

Session = sessionmaker(bind=engine)
session = Session()


def deter_seat(n):
    li = [word for word in string.ascii_uppercase]
    seat = ''.join(random.sample(li[0: n], 1))
    seat = seat + (str(random.randint(1, 10)))
    return seat


def show_airline(sta, des):
    airlines = session.query(Airline).filter(and_(Airline.start == sta, Airline.destination == des)).all()
    n = 1
    for airline in airlines:
        total = airline.passenger_num_fir + airline.passenger_num_eco
        flight = session.query(Flight).filter(Flight.Airline_id == airline.id).first()
        ticket_count = session.query(func.count(passenger_flight.Passenger_id)). \
            filter(passenger_flight.Flight_id == flight.id).scalar()
        rest = total - ticket_count  # 余票量
        print(f'{n}.航班号: {airline.flight_num},出发时间: {airline.start_time},预计抵达时间:{airline.arrive_time},'
              f'票价: {airline.standard_price}, 余票量: {rest} ')
        n += 1


def buy_ticket(p_name, pas_id, fli_num, sta, des):  # 仓位等级，座位分配未完成
    flight = session.query(Flight).filter(Flight.flight_num == fli_num).first()
    airline = session.query(Airline).filter(Airline.id == flight.Airline_id).first()
    n = int(airline.passenger_num_eco/10)
    seat_t = deter_seat(n)
    a_f = session.query(airplane_flight).filter(airplane_flight.Flight_id == flight.id).first()
    res = session.query(exists().where(and_(Seat.Airplane_id == a_f.Airplane_id, Seat.seat_num == seat_t))).scalar()
    while res:
        seat_t = deter_seat(n)
        res = session.query(exists().where(and_(Seat.Airplane_id == a_f.Airplane_id, Seat.seat_num == seat_t))).scalar()
        print(seat_t)
    add_Seat(a_f.Airplane_id, seat_t, 'eco')
    seat = session.query(Seat).filter(Seat.Airplane_id == a_f.Airplane_id).first()
    add_Ticket(flight.Airport_id, flight.id, pas_id, seat.id, sta, des, flight.date, airline.standard_price)
    add_passenger_flight(pas_id, flight.id)
    print(f"购票成功！您的机票信息如下：\n航班号: {flight.flight_num} 姓名： {p_name} 登机时间: {flight.date}\n"
          f"目的地: {sta} 座位号: {seat_t}")


def Is_exist(p_name, p_sex):
    res = session.query(exists().where(and_(Passenger.name == p_name, Passenger.sex == p_sex))).scalar()
    if res:
        passenger = session.query(Passenger).filter(Passenger.name == p_name, Passenger.sex == p_sex).first()
        print(f"**********登录成功！**********\n乘客信息如下:\n姓名: {passenger.name}\n性别:{passenger.sex}\n"
              f"类别: {passenger.type}\n里程积分: {passenger.mile_score}")
        if passenger.type == 'normal':
            print("检测到您是普通乘客，加入会员即可优享里程积分满减票价，是否即可办理会员？\n1.太好了，这个会员我办定了！\n2.滚")
            temp = input()
            if temp == '1':
                print("这个功能王诗剑这个懒B还没写呢")
            else:
                pass
    else:
        add_Passenger(p_name, p_sex, 'normal', 0)
        passenger = session.query(Passenger).filter(Passenger.name == p_name, Passenger.sex == p_sex).first()
        print("尚不存在该乘客，已为您注册")
    return passenger.id


if __name__ == "__main__":
    print("欢迎使用航空订票系统！")
    print('输入姓名和性别：')
    name = 'zsc'
    sex = 'male'
    p_id = Is_exist(name, sex)
    print("输入你的出发地：")
    start = '上海'
    print("输入你的目的地：")
    destination = '广州'
    show_airline(start, destination)
    print("输入购票的航班号")
    flight_id = 'c4096'
    buy_ticket(name, p_id, flight_id, start, destination)
    session.commit()
    session.close()
