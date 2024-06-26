from tkinter import *
from PIL import Image, ImageTk
import sys




root = Tk()
root.title("Scainet")
root.configure(background="darkGrey")
root.minsize(1280, 720)  # width, height
root.maxsize(1280, 720)
root.geometry("480x480+320+150")

gif = Image.open("GUI\ScainetHUD.gif")


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

# Start playing the animation
play_animation(0)
root.mainloop()








