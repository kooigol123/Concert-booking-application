import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk

#Infomation about the program

#root 
root = ctk.CTk()
root.geometry("1200x680")
ctk.set_appearance_mode("dark")  
root.title("Music Festival  Night in Bangkok")
root.grid_columnconfigure(1, weight=1)
Poster_Frame = ctk.CTkFrame(root)
Poster_Frame.grid(row=0, column=0, sticky="nsew")

image = Image.open("Image\Poster.png")
resized = image.resize((479, 680))  
photo = ImageTk.PhotoImage(resized)
label = ctk.CTkLabel(Poster_Frame, image=photo, text="")  
label.pack(side="left")


SignIn_Frame = ctk.CTkFrame(root,fg_color="#fdf1d9")
SignIn_Frame.grid(row=0, column=1,sticky="nsew")
ctk.CTkLabel(SignIn_Frame,text="Sign In",text_color="black",font=("Mitr",65)).grid()

ctk.CTkLabel(SignIn_Frame,text="Username",text_color="black",font=("Mitr",18)).grid()
Username = ctk.CTkEntry(SignIn_Frame,placeholder_text="Username",width=600,height=82)
Username.grid()
ctk.CTkLabel(SignIn_Frame,text="Password",text_color="black",font=("Mitr",18)).grid()
Password = ctk.CTkEntry(SignIn_Frame,placeholder_text="Password",width=600,height=82)
Password.grid()
Forget_Password = ctk.CTkButton(SignIn_Frame,text="Forget Password?")
Forget_Password.grid() 
SignIn_btn = ctk.CTkButton(SignIn_Frame,text="Sign In",width=600,height=82)
SignIn_btn.grid()

ctk.CTkLabel(SignIn_Frame,text="Don't have a acount?").grid()
Register_btn = ctk.CTkButton(SignIn_Frame,text="Register" ,text_color="red")
Register_btn.grid()
root.mainloop()