from tkinter import *
from PIL import Image, ImageTk
from tkinter.ttk import *
from threading import Thread


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
        txtBox.insert(1.0,"ERROR")
        key = txtBox.get("1.0", 'end-1c')
        txtBox.delete(1.0, END)




#def load():
#    print("\x1b[0m","...Начало загрузки...")
#    s="█"
#    for i in range (101):
#        time.sleep(0.05)
#        print('\r', 'Запуск', i*s, str(i), '%', end='')
#    print("\x1b[32m","\nЗагрузка завершена")


#ButtonDesign
Button_img = ImageTk.PhotoImage(file = "GUI\Button.png")
btn1 = Button(root, text="Button_1",  image=Button_img, command=searching)
btn1.place(x=115, y=300)


PB = Progressbar(root,orient=HORIZONTAL,length=250, mode='determinate')

def Slide():
    import time
    PB['value']=20
    root.update_idletasks()
    time.sleep(2)
    PB['value']=50
    root.update_idletasks()
    time.sleep(2)
    PB['value']=80
    root.update_idletasks()
    time.sleep(2)
    PB['value']=100
PB.pack(side = BOTTOM, pady = 200, ipadx=50, ipady= 5)


root.mainloop()







