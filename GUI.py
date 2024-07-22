import time
from tkinter import *
from PIL import Image, ImageTk
import os
from skills import MyGlobals


root = Tk()
root.title("Scainet")
root.configure(background="darkGrey")
root.minsize(1280, 720)  # width, height
root.maxsize(1280, 720)
root.geometry("480x480+300+150")

gif = Image.open("GUI\HUD-Interface-NEW.gif")


# Create a list of frames
frames = []
for i in range(gif.n_frames):
    gif.seek(i)
    frames.append(ImageTk.PhotoImage(gif))

# Create a label widget to display the frames
frame_label = Label(root)
frame_label.pack()



#TextBox Design
txtBox = Text(root, width=80, height=3, font='Tahoma')
txtBox.place(x=225, y=600)
sr=Scrollbar(root)
sr.config(command=txtBox.yview)
txtBox.config(yscrollcommand=sr.set)

def searching():
    key = txtBox.get("1.0",'end-1c')
    if key == "1234":
        print("\x1b[32m","Good")
        os.system('start python %USERPROFILE%\Documents\GitHub\ScainetAI\main.py')
        print(MyGlobals.outfraze)


        
    else:
        print("\x1b[31m","EROR")

def load():
    print("\x1b[0m","...Начало загрузки...")
    s="█"
    for i in range (101):
        time.sleep(0.05)
        print('\r', 'Запуск', i*s, str(i), '%', end='')
    print("\x1b[32m","\nЗагрузка завершена")


#ButtonDesign
Button_img = PhotoImage(file = "GUI\Button.png")
btn1 = Button(root, text="Button_1", padx=50, pady=15, image=Button_img, command=searching)
btn1.place(x=40, y=600)



root.mainloop()







