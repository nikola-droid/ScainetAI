import time
from tkinter import *
from PIL import Image, ImageTk
import os
from skills import MyGlobals


root = Tk()
root.title("Scainet")
root.configure(background="darkGrey")
root.minsize(1024, 540)  # width, height
root.maxsize(1024, 540)
root.geometry("480x480+450+170")



# TextBox Design
txtBox = Text(root, width=105, height=3, font='Tahoma')
txtBox.place(x=35, y=200)
sr = Scrollbar(root)
sr.config(command=txtBox.yview)
txtBox.config(yscrollcommand=sr.set)

txtBox.insert('1.0', MyGlobals.outfraze)


root.mainloop()







