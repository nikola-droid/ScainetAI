from tkinter import *
import time
from PIL import ImageTk
from tkinter.ttk import *
import tkinter as tk
from tkinter import messagebox
import hashlib
import sys




root = Tk()
root.title("Scainet_lock")
root.configure(background="darkGrey")
root.minsize(480, 640)  # width, height
root.maxsize(480, 640)
root.geometry("480x488+760+180")
label =Label(root)
label.pack(pady=10)


#TextBox Design
txtBox = Text(root, width=45, height=3, font='Tahoma')
txtBox.place(x=35, y=200)
sr=Scrollbar(root)
sr.config(command=txtBox.yview)
txtBox.config(yscrollcommand=sr.set)

def preventClose():
    pass
root.protocol("WM_DELETE_WINDOW", preventClose)


red= "\x1b[32m"

def hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

def searching():
    key = txtBox.get("1.0",'end-1c')
    hash_input = hash(key)
    hash_password="03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4"
    if hash_input == hash_password:
        print("\x1b[32m", "Good")
        print(hash(key))
        Slide()
        check_status()
        sys.exit(0)
    else:
        txtBox.delete(1.0,END)
        messagebox.showerror("УПС", "Пароль не верный")
        time.sleep(10)
        txtBox.delete(1.0, END)
        key = txtBox.get("1.0", 'end-1c')


#pass 1234#

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








def check_status():
    print(f"Чекбокс выбран: {var.get()}")


# Переменная для хранения состояния чекбокса
var = tk.BooleanVar()

# Создаем Checkbutton
checkbox = tk.Checkbutton(root, text="Dialog", variable=var, command=check_status)
checkbox.pack()

def blocking():
    # Возвращаем состояние чекбокса для использования в других функциях
    return var.get()




root.mainloop()







