import tkinter as tk
from tkinter import ttk
import random

# ข้อมูลของโซนและที่นั่ง
ticket = {
    "Zone_Vip": {"price": 4000, "seat_available": 10, "gift": "เสื้อวง(สุ่ม) + พวงกุญแจ + ปิ๊กกีตาร์"},
    "Zone_A": {"price": 3000, "seat_available": 20, "gift": "พวงกุญแจ + ปิ๊กกีตาร์"},
    "Zone_B": {"price": 2500, "seat_available": 30, "gift": "พวงกุญแจ"},
    "Zone_C": {"price": 1500, "seat_available": 40, "gift": "เข็มกลัด"},
}

# สุ่มที่นั่งที่ถูกจองแล้ว
def Random_seat_booked():
    seat_booked = {}
    for Zone, Info in ticket.items():
        booked = random.randint(0, Info['seat_available'])
        seat_booked[Zone] = booked
    return seat_booked

# แสดงที่นั่งที่ไม่ว่าง
def Show_seat_unavailable():
    seat_booked = Random_seat_booked()
    seat_unavailable = {}
    for Zone, Info in ticket.items():
        if not seat_booked[Zone]:
            seat_unavailable[Zone] = []
        else:
            unavailable = random.sample(range(1, Info['seat_available'] + 1), seat_booked[Zone])
            unavailable = sorted(unavailable)
            seat_name = []
            for i in unavailable:
                seat_name.append(f"{Zone.removeprefix('Zone_')}{i}")
            seat_unavailable[Zone] = seat_name
    return seat_unavailable

# แสดงที่นั่งที่ว่างอยู่
def Show_seat_available():
    seat_unavailable = Show_seat_unavailable()
    seat_result = {}
    for Zone, Info in ticket.items():
        seat = Info['seat_available']
        seat_position = [f"{Zone.removeprefix('Zone_')}{i}" for i in range(1, seat + 1)]
        difference = set(seat_position).difference(set(seat_unavailable[Zone]))
        sort = sorted(difference, key=lambda x: (x[0], int(''.join(filter(str.isdigit, x)))))
        seat_result[Zone] = sort
    return seat_result


