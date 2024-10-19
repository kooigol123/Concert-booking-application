import tkinter as tk
import datetime
from tkinter import*
from tkinter import filedialog
from tkinter import ttk, messagebox, Toplevel, Text
from Random_seat import ticket,Show_seat_available
from PIL import ImageTk, Image,ImageGrab

x = 675
y = 150
Main_window = tk.Tk()
Main_window.resizable(False,False)
Main_window.title('🪗 : Music Festival Night in Bangkok')
Main_window.config(bg="#93BEB7",pady=20,padx=40)
title_bar = Frame(Main_window, bg='#93BEB7', relief='raised', bd=2)
Main_window.geometry(f"+{x}+{y}")

poster = Image.open("Image/Poster.png")
poster = poster.resize((430,594), Image.LANCZOS)
photo = ImageTk.PhotoImage(poster)
canvas = tk.Canvas(Main_window, width=430, height=590)
canvas.create_image(0, 0,anchor=tk.NW, image=photo)
canvas.grid(row=1,column=0,sticky=N,pady=(10))
canvas.image = photo

def second_window():
    global S_window
    Main_window.withdraw()
    S_window=tk.Tk()
    S_window.title("รายละเอียด")
    S_window.resizable(False,False)
    S_window.geometry(f"+{x}+{y}")
    S_window.config(padx=40,pady=10,background="#93BEB7")
    S_window.protocol("WM_DELETE_WINDOW", Main_window.quit)
    
    ttk.Label(S_window,text="รายระเอียดงานคอนเสิร์ต",font=("kanit",25,"bold"),foreground="#020507",background="#93BEB7",padding=0).grid(row=0,column=0,columnspan=2,pady=(0,10))

    ttk.Label(S_window,text="🪗 ชื่องานคอนเสิร์ต : ",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=0).grid(row=9, column=0, sticky=W)
    ttk.Label(S_window,text="Music Festival Night in Bangkok",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=0).grid(row=9, column=1, sticky=W)
    ttk.Label(S_window,text="🎸 วงในงานคอนเสิร์ต : ",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=0).grid(row=190, column=0, sticky=W)
    ttk.Label(S_window,text="Three Man Down, PiXXiE, Violette Wautier, Dept",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=0).grid(row=190, column=1, sticky=W)
    ttk.Label(S_window,text="Safeplanet, Jeff Satur, BIG ASS",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=0).grid(row=191, column=1, sticky=W)
    ttk.Label(S_window,text="📍สถานที่จัด : ",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=0).grid(row=200, column=0, sticky=W)
    ttk.Label(S_window,text="อิมแพ็ค อารีน่า เมืองทองธานี",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=0).grid(row=200, column=1, sticky=W)
    ttk.Label(S_window,text="🧸 วันที่จัดคอนเสิร์ต : ",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=0).grid(row=220, column=0, sticky=W) 
    ttk.Label(S_window,text="1 ธันวาคม 2567",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=0).grid(row=220, column=1, sticky=W) 
    ttk.Label(S_window,text="⏱️เวลาเริ่มงานคอนเสิร์ต : ",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=0).grid(row=230, column=0, sticky=W)
    ttk.Label(S_window,text="16:00 - 23:00",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=0).grid(row=230, column=1, sticky=W)
    ttk.Label(S_window,text="📅 จำหน่ายบัตรตั้งแต่วันที่ : ",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=0).grid(row=240, column=0, sticky=W)
    ttk.Label(S_window,text="21 ตุลาคม 2567",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=0).grid(row=240, column=1, sticky=W)
    ttk.Label(S_window,text="🎫 ราคาบัตร : ",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=0).grid(row=250, column=0, sticky=W)
    ttk.Label(S_window,text="Vip 4000,A 3000,B 2500,C 1500",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=0).grid(row=250, column=1, sticky=W)
    ttk.Label(S_window,text="💺 จำนวนที่นั่งทั้งหมด : ",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=0).grid(row=260, column=0, sticky=W)
    ttk.Label(S_window,text="100 ที่นั่ง",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=0).grid(row=260, column=1, sticky=W)
    ttk.Label(S_window,text="🔴 เงื่อนไขในการจำหน่ายบัตร 👉🏻",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=0).grid(row=270, column=0, sticky=W)
    ttk.Label(S_window,text="• จำกัดการซื้อ 4 ใบต่อ 1 ใบเสร็จ",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=0).grid(row=270, column=1, sticky=W)
    ttk.Label(S_window,text="• ถ้ามีเด็กจะนับเป็น 1 คนต่อที่นั่ง",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=0).grid(row=280, column=1, sticky=W)
    ttk.Label(S_window,text="• เมื่อซื้อครบ 4 ที่นั่งจะได้รับส่วนลด 5%",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=0).grid(row=290, column=1, sticky=W)

    ttk.Label(S_window,text="----------------------------------(Zone_Vip)-------------------------------------",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=-5).grid(row=300,columnspan=2,sticky='N')
    ttk.Label(S_window,text="โซน : ",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=-2).grid(row=310, column=0,columnspan=2,sticky=W)
    ttk.Label(S_window,text="Vip",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=-2).grid(row=310,column=1,sticky=W)
    ttk.Label(S_window,text="ราคาตั๋ว : ",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=-2).grid(row=320, column=0, sticky=W)
    ttk.Label(S_window,text="4000",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=-2).grid(row=320, column=1, sticky=W)
    ttk.Label(S_window,text="จำนวนที่นั่ง : ",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=-2).grid(row=330, column=0, sticky=W)
    ttk.Label(S_window,text="10",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=-2).grid(row=330, column=1, sticky=W)
    ttk.Label(S_window,text="ของแจก : ",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=-2).grid(row=340, column=0, sticky=W)
    ttk.Label(S_window,text="เสื้อวง(สุ่ม) + พวงกุญแจ + ปิ๊กกีตาร์",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=-2).grid(row=340, column=1, sticky=W)

    ttk.Label(S_window,text="----------------------------------(Zone_A)--------------------------------------",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=-5).grid(row=350, column=0,columnspan=2, sticky='N')
    ttk.Label(S_window,text="โซน : ",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=-2).grid(row=360, column=0, sticky=W)
    ttk.Label(S_window,text="A",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=-2).grid(row=360, column=1, sticky=W)
    ttk.Label(S_window,text="ราคาตั๋ว : ",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=-2).grid(row=370, column=0, sticky=W)
    ttk.Label(S_window,text="3000 ",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=-2).grid(row=370, column=1, sticky=W)
    ttk.Label(S_window,text="จำนวนที่นั่ง : ",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=-2).grid(row=380, column=0, sticky=W)
    ttk.Label(S_window,text="20",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=-2).grid(row=380, column=1, sticky=W)
    ttk.Label(S_window,text="ของแจก : ",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=-2).grid(row=390, column=0, sticky=W)
    ttk.Label(S_window,text="พวงกุญแจ+ปิ๊กกีตาร์",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=-2).grid(row=390, column=1, sticky=W)

    ttk.Label(S_window,text="----------------------------------(Zone_B)-------------------------------------",font=("kanit",9,),foreground="#020507",background="#93BEB7",padding=-5).grid(row=400, column=0,columnspan=2, sticky='N')
    ttk.Label(S_window,text="โซน : ",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=-2).grid(row=410, column=0, sticky=W)
    ttk.Label(S_window,text="B",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=-2).grid(row=410, column=1, sticky=W)
    ttk.Label(S_window,text="ราคาตั๋ว : ",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=-2).grid(row=420, column=0, sticky=W)
    ttk.Label(S_window,text="2500 ",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=-2).grid(row=420, column=1, sticky=W)
    ttk.Label(S_window,text="จำนวนที่นั่ง : ",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=-2).grid(row=430, column=0, sticky=W)
    ttk.Label(S_window,text="30",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=-2).grid(row=430, column=1, sticky=W)
    ttk.Label(S_window,text="ของแจก : ",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=-2).grid(row=440, column=0, sticky=W)
    ttk.Label(S_window,text="พวงกุญแจ",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=-2).grid(row=440, column=1, sticky=W)

    ttk.Label(S_window,text="----------------------------------(Zone_C)-------------------------------------",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=-5).grid(row=450, column=0,columnspan=2, sticky='N')
    ttk.Label(S_window,text="โซน : ",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=-2).grid(row=460, column=0, sticky=W)
    ttk.Label(S_window,text="C",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=-2).grid(row=460, column=1, sticky=W)
    ttk.Label(S_window,text="ราคาตั๋ว : ",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=-2).grid(row=470, column=0, sticky=W)
    ttk.Label(S_window,text="1500 ",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=-2).grid(row=470, column=1, sticky=W)
    ttk.Label(S_window,text="จำนวนที่นั่ง : ",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=-2).grid(row=480, column=0, sticky=W)
    ttk.Label(S_window,text="40",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=-2).grid(row=480, column=1, sticky=W)
    ttk.Label(S_window,text="ของแจก : ",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=-2).grid(row=490, column=0, sticky=W)
    ttk.Label(S_window,text="เข็มกลัด",font=("kanit",9),foreground="#020507",background="#93BEB7",padding=-2).grid(row=490, column=1, sticky=W)

    tk.Button(S_window,text="ย้อนกลับ",command=lambda: [S_window.withdraw(), Main_window.deiconify()],width=15,font=("kanit",10),foreground="white",background="#2A454E").grid(row=660, column=0, sticky='W',padx=(30,0))
    tk.Button(S_window,text="ถัดไป",command=lambda:[S_window.withdraw(),Booking_seat_selection()],width=15,font=("kanit",10),foreground="white",background="#2A454E").grid(row=660, column=1,sticky='E',padx=(0,30),pady=(20))
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Booking_seat_selection():
    global top,seat_result,Show_limit,index_seat,Check_delete
    seat_result = Show_seat_available()
    Time = datetime.datetime.now()
    index_seat = 0
    Show_limit = 4
    User_selection={}

    Check_delete = False
    def booking_seat():
        global Show_limit,index_seat,zonelist,seatlist
        if Show_limit == 0:
            messagebox.showinfo("","คุณได้ซื้อเต็มจำนวนแล้ว")
        else:
            zonelist = cmdzonelist.get()
            seatlist = cmdseatlist.get()
            print(zonelist)
            print(seatlist)
            if zonelist == "โปรดเลือกโซน":
                messagebox.showwarning("Warning","โปรดเลือกโซน")
            elif seatlist == "โปรดเลือกที่นั่ง":
                messagebox.showinfo("Warning","โปรดเลือกที่นั่ง")
            elif seatlist == "ที่นั่งหมดแล้ว":
                pass
            else:
                try:
                    if seatlist:
                        if zonelist not in User_selection:
                            User_selection[zonelist] = []
                        index_seat += 1
                        User_selection[zonelist].append(seatlist)
                        seat_result[zonelist].remove(seatlist)
                        Show_selseat.configure(state="normal",selectmode="single")
                        Show_selseat.insert("end",f"{index_seat}){seatlist}")

                        Show_gift_zone.configure(state="normal")
                        Show_gift_zone.insert("end",f"{index_seat}){zonelist} ({seatlist}) {ticket[zonelist]['gift']}")


                        Show_limit -= 1
                        Limit.config(text=f"เลือกซื้อได้อีก {Show_limit} บัตร")
                        if not Show_limit:
                            Limit.config(text=f"คุณได้ซื้อเต็มจำนวนแล้ว")
                except:
                    print("เกิดข้อผิดพลาด")
                finally:
                    update_seat_list()
                    Show_seat_amount()

    
    def User_delete_seat():
        global Show_limit,index_seat,Check_delete
        try:
            if not Check_delete:
                if not Show_selseat.size():
                    messagebox.showwarning("Warning","ไม่พบที่นั่งที่จะลบ")
                elif zonelist == "โปรดเลือกโซน":
                    messagebox.showwarning("Warning","โปรดเลือกโซน")
                    return
                elif seatlist == "โปรดเลือกที่นั่ง":
                    messagebox.showinfo("Warning","โปรดเลือกที่นั่ง")
                    return
                else:
                    #ลบที่นั่ง และเพิ่มที่นั่งกลับเข้าไป
                    selection = Show_selseat.curselection()
                    if selection:
                        for index in selection:
                            seat = Show_selseat.get(index)
                            new_text = seat.split(')')[-1]
                            Show_selseat.delete(selection[0])
                            for zone,seat in User_selection.items():
                                if new_text in seat:
                                    seat.remove(new_text)
                                    seat_result[zone].append(new_text)
                                    seat_result[zone] = sorted(seat_result[zone], key=lambda x: (x[0], int(''.join(filter(str.isdigit, x)))))

                        Show_selseat.delete(0, END)
                        Show_gift_zone.delete(0, END)
                        
                        Display_index = 1
                        for zone, seat in User_selection.items():
                            for x in seat:
                                Show_selseat.insert("end", f"{Display_index }){x}")
                                Show_gift_zone.insert("end", f"{Display_index }){zone} ({x}) {ticket[zone]['gift']}")
                                Display_index  += 1
                                

                        index_seat -= 1
                                
                        update_seat_list()
                        Show_limit +=1
                        if not Show_limit :
                            Limit.config(text=f"คุณได้ซื้อเต็มจำนวนแล้ว")
                        else:
                            Limit.config(text=f"เลือกซื้อได้อีก {Show_limit} บัตร")
                        for User_delete_zone in list(User_selection.keys()):
                            User_delete_seat = User_selection[User_delete_zone]
                            if not User_delete_seat:
                                del User_selection[User_delete_zone]
                Check_delete = False
        except:
            print("เกิดข้อผิดพลาด")
        finally:
            Show_seat_amount()

    def update_seat_list(event=None):
        
        cmdseatlist.set("โปรดเลือกที่นั่ง")
        zone = cmdzonelist.get()
        seats = seat_result.get(zone,"")
        if not seats:
            cmdseatlist.set("ที่นั่งหมดแล้ว")
            cmdseatlist['values']=[]
        else:
            cmdseatlist['values'] = seats
    #Receipt
    def Screenshot():
            Button_capture.grid_forget()
            info_frame.after(100,Capture_sceen)
    def Capture_sceen():
        global Button_capture

        x = info_frame.winfo_rootx()
        y = info_frame.winfo_rooty()
        width = info_frame.winfo_width()
        height = info_frame.winfo_height()
        
        default_filename = "Concert_receipt.png"
        screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))
        file_path = filedialog.asksaveasfilename(
            filetypes=[("PNG files", "*.png"),("All files", "*.*")],
            initialfile=default_filename,
            title="Save screenshot as")
        if file_path:
            if not file_path.endswith(".png"):
                file_path += ".png"
            screenshot.save(file_path)
            print(f"คุณทำการบันทึกรูปภาพ {file_path}")
        Button_capture.grid(row=0,column=0,columnspan=5,sticky=NE)
        

    def update_time():
        global current_date,current_time
        now = datetime.datetime.now()
        current_date = now.strftime('%x')
        current_time = now.strftime('%X')
        
    def receipt():
        global top,photoQR
        if not User_selection:
            messagebox.showinfo("Warning","โปรดจองที่นั่งก่อนทำการชำระเงิน")
        if top is None or not top.winfo_exists():
            if User_selection :
                    Check_pay = messagebox.askyesno("Confirm","คุณต้องการจ่ายตังใช่หรือไม่")
                    if Check_pay:
                        top = Toplevel()
                        top.resizable(False,False)
                        def Create_info(Containter):
                            global info_frame,Button_capture
                            update_time()
                            info_frame = ttk.Frame(Containter,padding=15)

                            Button_capture = tk.Button(info_frame,text="บันทึกรูปภาพ",command=Screenshot,font=("kanit",7))
                            Button_capture.grid(row=0,column=0,columnspan=5,sticky=NE)
                            ttk.Label(info_frame,text=f"Recepit",font=("kanit","25"),padding=-2).grid(row=0,column=0,columnspan=5,sticky=N)
                            ttk.Label(info_frame,text=f"{"-----------------------------------------------------------------------"+("--"*index_seat)}").grid(row=1,columnspan=5,sticky=N)
                            ttk.Label(info_frame,text=f"ชื่อคอนเสิร์ต").grid(row=2,column=0,sticky=W,padx=(0,30))
                            ttk.Label(info_frame,text=f"Music Festival Night in Bangkok").grid(row=2,column=1,sticky=W)
                            ttk.Label(info_frame,text=f"จำนวนบัตร").grid(row=3,column=0,sticky=W)
                            ttk.Label(info_frame,text=f"{index_seat}").grid(row=3,column=1,sticky=W)

                            ttk.Label(info_frame,text=f"สถานที่จัด").grid(row=4,column=0,sticky=W)
                            ttk.Label(info_frame,text=f"อิมแพ็ค อารีน่า เมืองทองธานี").grid(row=4,column=1,sticky=W)
                            ttk.Label(info_frame,text=f"วันที่จัดคอนเสิร์ต").grid(row=5,column=0,sticky=W)
                            ttk.Label(info_frame,text=f"1 ธันวาคม 2567").grid(row=5,column=1,sticky=W)
                            ttk.Label(info_frame,text=f"เวลา").grid(row=6,column=0,sticky=W)
                            ttk.Label(info_frame,text=f"16:00 - 23:00").grid(row=6,column=1,sticky=W)
                            ttk.Label(info_frame,text=f"").grid(row=7,column=0,sticky=W)

                            ttk.Label(info_frame,text=f"{current_date}").grid(row=11,column=0,sticky=W)
                            ttk.Label(info_frame,text=f"{current_time}").grid(row=11,column=4,sticky=E)

                            ttk.Label(info_frame,text=f"{"-----------------------------------------------------------------------"+("--"*index_seat)}").grid(row=12,columnspan=5,sticky=N)
                            ttk.Label(info_frame,text=f"ลำดับ").grid(row=13,column=0,sticky=N)
                            ttk.Label(info_frame,text=f"โซน/หมายเลขที่นั่ง",anchor="center").grid(row=13,column=1,sticky=N,ipadx=10+(12*len(User_selection)))
                            ttk.Label(info_frame,text=f"จำนวน").grid(row=13,column=2,sticky=N)
                            ttk.Label(info_frame,text=f"ราคาบัตร").grid(row=13,column=3,sticky=N)
                            ttk.Label(info_frame,text=f"จำนวนเงิน").grid(row=13,column=4,sticky=N)

                            Sum_price = 0
                            for i,(Order_zone,Order_seat) in enumerate(User_selection.items(),start=1):
                                if not Order_seat:
                                    return
                                else:
                                    ttk.Label(info_frame,text=f"{i}").grid(row=i+13,column=0,sticky=N)
                                    ttk.Label(info_frame,text=f"{Order_zone} • {Order_seat}").grid(row=i+13,column=1,sticky=W)
                                    ttk.Label(info_frame,text=f"{len(Order_seat)}").grid(row=i+13,column=2,sticky=N)
                                    ttk.Label(info_frame,text=f"{ticket[Order_zone]["price"]}").grid(row=i+13,column=3,sticky=N)
                                    ttk.Label(info_frame,text=f"{len(Order_seat)*ticket[Order_zone]["price"]}").grid(row=i+13,column=4,sticky=N)
                                    Sum_price += len(Order_seat)*ticket[Order_zone]["price"]

                            ttk.Label(info_frame,text=f"รวมเป็นเงินทั้งสิ้น").grid(row=18,column=1,columnspan=2,sticky=E,pady=(30,0))
                            ttk.Label(info_frame,text=f"{Sum_price}").grid(row=18,column=3,sticky=E,pady=(30,0))
                            ttk.Label(info_frame,text=f"บาท").grid(row=18,column=4,sticky=E,pady=(30,0),padx=(5))
                            ttk.Label(info_frame,text=f"ส่วนลด 5%").grid(row=19,column=1,columnspan=2,sticky=E)
                            Discount = 0
                            if index_seat == 4:
                                Discount = (Sum_price*5)/100
                                ttk.Label(info_frame,text=f"{Discount}").grid(row=19,column=3,sticky=E)
                                    
                            else:
                                ttk.Label(info_frame,text=f"-").grid(row=19,column=3,sticky=E)
                            ttk.Label(info_frame,text=f"บาท").grid(row=19,column=4,padx=(5),sticky=E)

                            ttk.Label(info_frame,text=f"ยอดหลังจากหักส่วนลด").grid(row=20,column=1,columnspan=2,sticky=E)
                            ttk.Label(info_frame,text=f"{Sum_price-Discount}").grid(row=20,column=3,sticky=E)
                            ttk.Label(info_frame,text=f"บาท").grid(row=20,column=4,padx=(5),sticky=E)

                            ttk.Label(info_frame,text=f"ยอดรวมสุทธิ").grid(row=21,column=1,columnspan=2,sticky=E)
                            ttk.Label(info_frame,text=f"{(Sum_price-Discount):.2f}").grid(row=21,column=3,sticky=E)
                            ttk.Label(info_frame,text=f"บาท").grid(row=21,column=4,padx=(5),sticky=E)

                            ttk.Label(info_frame,text=f"{"-----------------------------------------------------------------------"+("--"*index_seat)}").grid(row=22,columnspan=5,sticky=N)
                            ttk.Label(info_frame,text=f"ของแจกที่คุณได้รับ",font=("kanit",15),padding=-2).grid(row=23,columnspan=5,sticky=N)
                            ttk.Label(info_frame,text=f"โปรดนำใบเสร็จมาแสดงเพื่อรับของ",font=("kanit",10),padding=-2).grid(row=24,columnspan=5,sticky=N)

                            for i,(Zone,seat) in enumerate(User_selection.items(),start=1):
                                ttk.Label(info_frame,text=f"{Zone} {seat} : {ticket[Zone]['gift']} x{len(seat)}").grid(row=30+i,columnspan=5,sticky=N)
                                
                            image = Image.open('Image/QR.png')
                            new_size = (200, 200)
                            image = image.resize(new_size, Image.LANCZOS)
                            photo = ImageTk.PhotoImage(image)
                            canvas = tk.Canvas(info_frame, width=200, height=200)
                            canvas.grid(row=100, columnspan=5,pady=(10,0))
                            canvas.image = photo  # Keep a reference
                            canvas.create_image(0, 0, anchor=tk.NW, image=photo)


                            return info_frame

                        receipt_info = Create_info(top)
                        receipt_info.grid(row=0,column=0)
        else:
            top.lift()
    def Show_seat_amount(event=None):
        
        style = ttk.Style()
        style.configure("WhiteBorder.TFrame", borderwidth=0, background="#f0f0f0")
        bb = ttk.Frame(app3, borderwidth=0, relief="flat", padding=10,style="WhiteBorder.TFrame")
        bb.place(x=30, y=95, width=120, height=100)
        
        for i,(zone,amount) in enumerate(seat_result.items(),start=1):
            if not amount:
                ttk.Label(app3,text=f"{zone}",font=("kanit","10"),padding=-2,).place(x=35,y=75+(20*i))
                ttk.Label(app3,text=f":",font=("kanit","10"),padding=-2,).place(x=98,y=75+(20*i))
                ttk.Label(app3,text=f"หมด",font=("kanit","10"),padding=(2,-2),).place(x=105,y=75+(20*i))
            else:
                ttk.Label(app3,text=f"{zone}",font=("kanit","10"),padding=-2,).place(x=35,y=75+(20*i))
                ttk.Label(app3,text=f":",font=("kanit","10"),padding=-2,).place(x=98,y=75+(20*i))
                ttk.Label(app3,text=f"{len(amount)}",font=("kanit","10"),padding=(3,-2)).place(x=105,y=75+(20*i))


    def Create_zone_selection(container):
        frame = ttk.Frame(container)

        ttk.Label(frame,text="เลือกจองที่นั่งของคุณ",font=("kanit",20),padding=-2,).grid(row=0,column=0,columnspan=3,sticky=tk.N,pady=15)

        ttk.Label(frame, text="เหลือที่นั่งจำนวน", font=("kanit", 12),padding=-2,anchor="nw",).grid(row=1, column=0, sticky=tk.N,padx=20,ipadx=10)
        Show_seat_amount()
        cmdzonelist = ttk.Combobox(frame,state="readonly",textvariable=select_zone)
        cmdzonelist.configure(width=20)
        cmdzonelist['value']=list(ticket.keys())
        cmdzonelist.set("โปรดเลือกโซน")
        cmdzonelist.bind("<<ComboboxSelected>>",update_seat_list)
        cmdzonelist.grid(row=1,column=1,padx=10,sticky=tk.N)
        
        cmdseatlist = ttk.Combobox(frame,state="readonly",textvariable=select_seat)
        cmdseatlist.configure(width=20,height=10)
        cmdseatlist.set("โปรดเลือกที่นั่ง")
        cmdseatlist.grid(row=2,column=1,padx=10,pady=20,sticky=tk.N)

        Show_selseat = Listbox(frame,font=("kanit",10),background="#F5DEB3",state="disabled",highlightbackground="Black",selectbackground="#926500",activestyle=tk.NONE,foreground="Black")
        Show_selseat.configure(width=7,height=10)
        Show_selseat.grid(row=1,rowspan=2,column=2,padx=20,sticky=tk.NSEW,ipadx=30)
        
        Limit = ttk.Label(frame,text=f"เลือกซื้อได้อีก {Show_limit} บัตร", font=("kanit",11),padding=-2,anchor=W,)
        Limit.grid(row=10,column=0)

        tk.Button(frame,text="DELETE", command=User_delete_seat,width=10,pady=0,font=("kanit",8),foreground="White",background="#E03423",activebackground="#CED1E3").grid(row=10,column=1,sticky=tk.W)
        tk.Button(frame,text="ADD", command=booking_seat,width=10,pady=0,font=("kanit",8),foreground="White",background="#47DB3D",activebackground="#CED1E3").grid(row=10,column=1,sticky=tk.E)
        tk.Button(frame,text="PAY",command=receipt,width=10,pady=0,font=("kanit",8),foreground="White",background="#347BE0",activebackground="#CED1E3").grid(row=10,column=2,sticky=tk.N,padx=20,pady=10)

        ttk.Label(frame,text="--------------------------------------------",font=("kanit",15),padding=-2,).grid(row=11,columnspan=3)
        ttk.Label(frame,text=f"สิ่งที่คุณจะได้รับ",font=("kanit",15),padding=-2,).grid(row=12,columnspan=3,sticky=tk.N)
        Show_gift_zone = Listbox(frame, font=("kanit", 10),background="#F5DEB3",highlightbackground="Black",selectbackground="#F5DEB3",selectforeground="Black",activestyle=tk.NONE,foreground="Black")
        Show_gift_zone.configure(width=45, height=6)
        Show_gift_zone.grid(row=13, sticky=tk.N, columnspan=3, pady=(10, 30))


        return frame,cmdzonelist,cmdseatlist,Show_selseat,booking_seat,receipt,Show_gift_zone,Limit

    app3 = tk.Tk()
    app3.title('Music Festival Night in Bangkok')
    app3.resizable(False,False)
    x = 675
    y = 150
    app3.geometry(f"+{x}+{y}")
    top = None
    select_zone = tk.StringVar()
    select_seat = tk.StringVar()
    Zone_selection,cmdzonelist,cmdseatlist,Show_selseat,booking_seat,receipt,Show_gift_zone,Limit = Create_zone_selection(app3)
    Zone_selection.grid(row=0,column=0)

    #ตรวจสอบว่าผูัใช้ต้องการออกจากระบบหรือไม่
    def window_quit():
        if messagebox.askyesno("Confirm","คุณต้องการออกจากระบบใช่หรือไม่"):
            app3.quit()
            app3.destroy()

    app3.protocol("WM_DELETE_WINDOW", window_quit)

btn1=tk.Button(Main_window,text="รายละเอียด",command=second_window,fg="Black",bg="White",width=14,font=("kanit",11),foreground="white",background="#2A454E").grid(row=2,column=0,sticky=N,pady=(30,10))
Main_window.mainloop()