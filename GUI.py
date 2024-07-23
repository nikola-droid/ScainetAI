from tkinter import *
import time
from PIL import Image, ImageTk
from tkinter.ttk import *
from threading import Thread
from tkinter import messagebox

root = Tk()
root.title("Scainet_lock")
root.configure(background="darkGrey")
root.minsize(480, 640)  # width, height
root.maxsize(480, 640)
root.geometry("480x488+760+180")


#TextBox Design
txtBox = Text(root, width=45, height=3, font='Tahoma')
txtBox.place(x=35, y=200)
sr=Scrollbar(root)
sr.config(command=txtBox.yview)
txtBox.config(yscrollcommand=sr.set)

def preventClose():
    pass
root.protocol("WM_DELETE_WINDOW", preventClose)

def new_thread():
    t1 = Thread(target=searching())
    t1.start()
red= "\x1b[32m"
def searching():
    key = txtBox.get("1.0",'end-1c')
    if key =="1234":
        print("\x1b[32m", "Good")
        Slide()
        quit()
    else:
        txtBox.delete(1.0,END)
        messagebox.showerror("УПС", "Пароль не верный")
        txtBox.delete(1.0, END)
        key = txtBox.get("1.0", 'end-1c')



#ButtonDesign
Button_img = ImageTk.PhotoImage(file = "GUI\Button.png")
btn1 = Button(root, text="Button_1",  image=Button_img, command=searching)
btn1.place(x=115, y=300)


PB = Progressbar(root,orient=HORIZONTAL,length=250, mode='determinate')

def Slide():
    import time
    PB['value']=20
    root.update_idletasks()
    time.sleep(1)
    PB['value']=50
    root.update_idletasks()
    time.sleep(1)
    PB['value']=80
    root.update_idletasks()
    time.sleep(1)
    PB['value']=100
PB.pack(side = BOTTOM, pady = 200, ipadx=50, ipady= 5)


root.mainloop()







