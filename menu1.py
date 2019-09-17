#import statements
import tkinter as tk
from tkinter import *
import PIL
import subprocess
top= Tk()
top.title('PERSONAL-APPS')
image1 = tk.PhotoImage(file='bg1.PNG')
w = image1.width()
h = image1.height()
top.geometry("%dx%d+0+0" % (w, h))
panel1 = tk.Label(top, image=image1)
panel1.pack(side='top', fill='both', expand='yes')
panel1.image = image1
def word():
    import os
    os.startfile('C:\Program Files\Microsoft Office\Office12\WINWORD.EXE')
def powerpoint():
    import os
    os.startfile('C:\Program Files\Microsoft Office\Office12\POWERPNT.EXE')
def excel():
    import os
    os.startfile('C:\Program Files\Microsoft Office\Office12\EXCEL.EXE')
def browser():
    subprocess.call([r'C:\Users\DEEPAK\mu_code\browser.bat'])
def music():
    import Music
def calc():
    subprocess.call([r'C:\Users\DEEPAK\mu_code\calc.bat'])
def contact():
    import file
def systemcleaner():
    subprocess.call([r'C:\Users\DEEPAK\mu_code\SYSTEM CLEANER.bat'])
def sticky():
    import stickynote
Musicbt = Button(top, text = "Music Player",command = music,font = 'HarlowSolidItalic 14 bold italic',background = "dark blue",foreground = "white").place(x = 150, y = 200)
calcbt = Button(top, text = "Calculator",command = calc,font = 'HarlowSolidItalic 14 bold italic',background = "dark blue",foreground = "white").place(x = 170, y = 400)
wordbt = Button(top, text = "MS-WORD",command = word,font = 'HarlowSolidItalic 14 bold italic',background = "dark blue",foreground = "white").place(x = 170, y = 630)
excelbt = Button(top, text = "MS-EXCEL",command = excel,font = 'HarlowSolidItalic 14 bold italic',background = "dark blue",foreground = "white").place(x = 550, y = 200)
stickybt = Button(top, text = "StickyNote",command = sticky,font = 'HarlowSolidItalic 14 bold italic',background = "dark blue",foreground = "white").place(x = 550, y = 400)
powerbt = Button(top, text = "MS-POWER",command = powerpoint,font = 'HarlowSolidItalic 14 bold italic',background = "dark blue",foreground = "white").place(x = 550, y = 630)
chromebt = Button(top, text = "Chrome",command = browser,font = 'HarlowSolidItalic 14 bold italic',background = "dark blue",foreground = "white").place(x = 980, y = 200)
sysbt = Button(top, text = "System-Cleaner",command = systemcleaner,font = 'HarlowSolidItalic 14 bold italic',background = "dark blue",foreground = "white").place(x = 980, y = 400)
contactbt = Button(top, text = "Contacts",command = contact,font = 'HarlowSolidItalic 14 bold italic',background = "dark blue",foreground = "white").place(x = 980, y = 640)
top.mainloop()
