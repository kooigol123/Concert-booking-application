import random
Ticket = {
    "Zone_Vip" : {"price" : 4000, "seat_available" : 10, "gift":"เสื้อวง(สุ่ม),พวงกุญแจ,ปิ๊กกีตาร์"},
    "Zone_A" : {"price" : 3000, "seat_available" : 20, "gift":"พวงกุญแจ+ปิ๊กกีตาร์" },
    "Zone_B" : {"price" : 2500, "seat_available" : 30, "gift":"พวงกุญแจ" },
    "Zone_C" : {"price" : 1500, "seat_available" : 40, "gift":"เข็มกลัด" },
}

#สุ่มจำนวนที่มีคนจองที่นั่งแล้ว
seat_booked={}
for Zone,Info in Ticket.items():
    booked = random.randint(1,Info['seat_available'])
    seat_booked[Zone]=booked
    print(booked)
print(seat_booked)
print("--------------------------------------------")
# ผลลัพธ์คือ Vip1 Vip4 Vip5 Vip6
print("--------------------------------------------")
print(f"มีคนจองตั๋วไปแล้ว {seat_booked}")
print("--------------------------------------------")
# โชว์ที่นั่งทั้งหมดในแต่ละโซน
seat_available={}
for Zone,Info in Ticket.items():
    seat = int(Info['seat_available'])
    seat_position=[]
    for i in range(1,seat+1):
        Position = f"{Zone.removeprefix("Zone_")}{i}"
        seat_position.append(Position)
    seat_available[Zone]=seat_position
print(seat_available)
print("----------Error-----------")
# Zone Vip = {Vip1,Vip2,Vip3,Vip4,...,Vip10}
# ลบที่นั่งที่มีคนจอง
# A.difference()

def Main_menu():
    print("------------------(MENU)------------------")
    print("1.รายระเอียดงานคอนเสิร์ต ")
    print("2.ซื้อบัตรงานคอนเสิร์ต")
    print("3.แลกของรางวัล ")
    print("------------------------------------------")
    Menu = int(input("กรุณากรอกหมายเลขที่ต้องการดำเนินการ : "))
    if Menu == 1:
        print("-------------รายระเอียดงานคอนเสิร์ต-------------")
        print("🪗  ชื่องานคอนเสิร์ต : Music Festival Night in Bangkok")
        print("🎸 วงในงานคอนเสิร์ต : Three Man Down, PiXXiE, Violette Wautier, Dept, 25hours, Jeff Satur, BIG ASS")
        print("📍 สถานที่จัด : อิมแพ็ค อารีน่า เมืองทองธานี")
        print("🧸 วันที่จัดคอนเสิร์ต : 1 ธันวาคม 2567")
        print("⏱️  เวลาเริ่มงานคอนเสิร์ต : 16:00 - 23:00")
        print("🎟️  จำหน่ายบัตรตั้งแต่วันที่ : 21 ตุลาคม 2567")
        print("🎫 ราคาบัตร Vip 4000,A 3000,B 2500,C 1500")
        print("💺 จำนวนที่นั่งทั้งหมด : 100 ที่นั่ง")
        print("🔴 เงื่อนไขในการจำหน่ายบัตร :")
        print(" -จำกัดการซื้อ 10 ใบต่อ 1 รายการสั่งซื้อ")
        for Zone,Info in Ticket.items():
            print(f"-------------------(ZONE)-------------------")
            print(f"• โซน : {Zone.removeprefix('Zone_')}") 
            print(f"• ราคาตั๋ว : {Info['price']}")
            print(f"• จำนวนที่นั่ง : {Info['seat_available']}")
            print(f"• ของแจก : {Info['gift']}")
        print("--------------------------------------------")
        Back_menu()
        Choice = int(input("กรุณากรอกหมายเลขที่ต้องการดำเนินการ : "))
        if Choice == 1:
            Main_menu()
    elif Menu == 2:
            print("-------------ซื้อบัตรงานคอนเสิร์ต-------------")
            print("1.ซื้อบัตรงานคอนเสิร์ต \n")
            print("------------------------------------------")
            # Choice = int(input("กรุณากรอกหมายเลขที่ต้องการดำเนินการ : "))
            # สุ่มที่นั่งที่มีคนจองแล้ว
                
            # if Choice == 1:
            # โชว์ที่นั่งว่างของแต่ละโซน
    else:
        pass

def Back_menu():
    print("(MENU)")
    print("1.ออก")
    print("--------------------------------------------")
# โชว์งาน
# Menu = Main_menu()

# if Menu == 1:
#     print("-------------รายระเอียดงานคอนเสิร์ต-------------")
#     print("🪗  ชื่องานคอนเสิร์ต : Music Festival Night in Bangkok")
#     print("🎸 วงในงานคอนเสิร์ต : Three Man Down, PiXXiE, Violette Wautier, Dept, 25hours, Jeff Satur, BIG ASS")
#     print("📍 สถานที่จัด : อิมแพ็ค อารีน่า เมืองทองธานี")
#     print("🧸 วันที่จัดคอนเสิร์ต : 1 ธันวาคม 2567")
#     print("⏱️  เวลาเริ่มงานคอนเสิร์ต : 16:00 - 23:00")
#     print("🎟️  จำหน่ายบัตรตั้งแต่วันที่ : 21 ตุลาคม 2567")
#     print("🎫 ราคาบัตร Vip 4000,A 3000,B 2500,C 1500")
#     print("💺 จำนวนที่นั่งทั้งหมด : 100 ที่นั่ง")
#     print("🔴 เงื่อนไขในการจำหน่ายบัตร :")
#     print(" -จำกัดการซื้อ 10 ใบต่อ 1 รายการสั่งซื้อ")
#     for Zone,Info in Ticket.items():
#         print(f"-------------------(ZONE)-------------------")
#         print(f"• โซน : {Zone.removeprefix('Zone_')}") 
#         print(f"• ราคาตั๋ว : {Info['price']}")
#         print(f"• จำนวนที่นั่ง : {Info['seat_available']}")
#         print(f"• ของแจก : {Info['gift']}")
#     print("--------------------------------------------")
#     Back_menu()
#     Choice = int(input("กรุณากรอกหมายเลขที่ต้องการดำเนินการ : "))
#     if Choice == 1:
#         Main_menu()




# elif Menu == 2:
