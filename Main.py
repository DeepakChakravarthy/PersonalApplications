import sys
from tkinter import *
import tkinter as tk
def box():
    from tkinter import messagebox
    UName = var1.get()
    PWD = var2.get()
    USERNAME = "DeepakChakravarthy"
    PASSWORD = "test@123"
    if UName!=USERNAME:
        messagebox.showwarning("LOGIN FAIL","USERNAME IS INCORRECT")
    if PWD!=PASSWORD:
        messagebox.showwarning("LOGIN FAIL","PASSWORD IS INCORRECT")
    else:
        messagebox.showinfo("WELCOME","WELCOME")
        import menu1
def clear():
    var11 = StringVar()#declaring the variable to store the text
    var22 = StringVar()
    e1 = Entry(top,textvariable= var11,font = large_font).place(x = 550, y = 250)
    e2 = Entry(top,textvariable = var22,show="*",font = large_font).place(x = 550, y = 320)
top= Tk()
var1 = StringVar()#declaring the variable to store the text
var2 = StringVar()#.....\....\...
top.title("LOGIN TO PERSONAL APP")
image1 = tk.PhotoImage(file='main.PNG')
w = image1.width()
h = image1.height()
top.geometry("%dx%d+0+0" % (w, h))
panel1 = tk.Label(top, image=image1)
panel1.pack(side='top', fill='both', expand='yes')
panel1.image = image1

name = Label(top, text = "Login",font = 'Algerian 40 bold italic underline',background = "white",fg = "blue").place(x = 500,y = 150)
name = Label(top, text = "Login User Name:",font = 'Algerian 15 bold',background = "black",fg = "white").place(x = 330,y = 250)
nick = Label(top, text = "Password:",font = 'Algerian 15 bold',background = "black",fg = "white").place(x = 370,y = 320)
resetbtn = Button(top, text = "   Reset   ",command =clear ,font = 'HarlowSolidItalic 14 bold italic',background = "dark blue",foreground = "white").place(x = 550, y = 400)
sbmitbtn = Button(top, text = " Continue ",command = box,font = 'HarlowSolidItalic 14 bold italic',background = "dark blue",foreground = "white").place(x = 680, y = 400)
large_font = ('Algerian 16')
e1 = Entry(top,textvariable= var1,font = large_font).place(x = 550, y = 250)
e2 = Entry(top,textvariable = var2,show="*",font = large_font).place(x = 550, y = 320)
top.mainloop()
