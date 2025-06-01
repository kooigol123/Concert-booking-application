#!Learn Python!#

#! Comments
# #! 
# #*
# #? 
# #Todo:
#*Python Basics
# x  = 10 #bool
# name = "Titan" #str
# is_value = True #bool
# list_number = [1, 2, 3, 4, 5] #list
# dict = {"key": "value"} #dict
# ticket = {
#     "Zone_Vip": {"price": 4000, "seat_available": 10, "gift": "เสื้อวง(สุ่ม) + พวงกุญแจ + ปิ๊กกีตาร์"},
#     "Zone_A": {"price": 3000, "seat_available": 20, "gift": "พวงกุญแจ + ปิ๊กกีตาร์"},
#     "Zone_B": {"price": 2500, "seat_available": 30, "gift": "พวงกุญแจ"},
#     "Zone_C": {"price": 1500, "seat_available": 40, "gift": "เข็มกลัด"},
# }


#*Functions
# def():
# example 1

# def Page_Promotion():
#     print("Promotion")

# example 2
# def Greeting(name):
    # printf("Hello {name}")



#*if else statement
# if x > y
#     print(x)
# else
#     print(y)

# for x,y in ____:


#*Exception Handling
#try:
#except:
#except ZeroDivisionError:
#except Exception as e:
#except ValueError:
#except TypeError:
#finally:

#*File 
# with open("file.txt", "r") as file:
#file.write("Hello World")
#file.read()
#file.close()


#*Tkinter
# import tkinter as tk
# from Name_module import Name_class or Function
# from ui.Promotion import Promotion_page
# Example 1 
#def add(a, b):
#    return a + b
#from math import add
#import customtkinter as ctk คือการ Import customtkinter แล้วเรียกใช้โดย ctk เช่น ctk.CTkLabel()
#from customtkinter import ctkLabel คือการนำเอา ctkLabel จาก customtkinter มาใช้อันเดียว

#* CustomTkinter
# import customtkinter as ctk
# ctk.set_appearance_mode("dark")
# ctk.set_default_color_theme("blue")
# ctk.set_ti
# root = ctk.CTk()
# root.geometry("400x300")
# root.title("CustomTkinter Example")
# label = ctk.CTkLabel(root, text="Hello World")
# label.pack(pady=20)
# button = ctk.CTkButton(root, text="Click Me", command=lambda: print("Button Clicked"))
# button.pack(pady=20)
# root.mainloop()
# root = ctk.CTk()
# root.geometry("400x300")
# root.title("CustomTkinter Example")
# label = ctk.CTkLabel(root, text="Hello World")
# label.pack(pady=20)
# button = ctk.CTkButton(root, text="Click Me", command=lambda: print("Button Clicked"))
# button.pack(pady=20)

#! Button
# ctk.CTkButton(root, text="Click Me", command=lambda: print("Button Clicked"))
#customtkinter.set_appearance_mode("dark") # dark, light, system
#fgcolor() สีด้านใน
#bgcolor() สีด้านนอก
#hover_color() เมือเมาส์อยู่เหนือปุ่ม
#text_color() สีอักษร
#text_color_disabled()
#text_color()
#border_color()
#button = tk.Button(root, 
#                    text="Click Me", 
#                    command=button_clicked,
#                    activebackground="blue", 
#                    activeforeground="white",
#                    anchor="center",
#                    bd=3,
#                    bg="lightgray",
#                    cursor="hand2",
#                    disabledforeground="gray",
#                    fg="black",
#                    font=("Arial", 12),
#                    height=2,
#                    highlightbackground="black",
#                    highlightcolor="green",
#                    highlightthickness=2,
#                    justify="center",
#                    overrelief="raised",
#                    padx=10,
#                    pady=5,
#                    width=15,
#                    wraplength=100)
# btn = Button(root, text = 'Click me !', command = root.destroy) 
