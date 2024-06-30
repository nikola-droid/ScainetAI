from tkinter import *
from PIL import Image, ImageTk



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

# Define a function to play the animation
def play_animation(frame_idx):
    frame_label.config(image=frames[frame_idx])
    root.after(50, play_animation, (frame_idx+1) % len(frames))

#TextBox Design
txtBox = Text(root, width=80, height=3, font='Tahoma')
txtBox.place(x=225, y=600)
sr=Scrollbar(root)
sr.config(command=txtBox.yview)
txtBox.config(yscrollcommand=sr.set)

def searching():    #Функция записи в текстбокс
    key = txtBox.get("1.0",'end-1c')




#ButtonDesign
Button_img = PhotoImage(file = "GUI\Button.png")
btn1 = Button(root, text="Button_1", padx=50, pady=15, image=Button_img, command=searching)
btn1.place(x=40, y=600)



play_animation(0)
root.mainloop()







