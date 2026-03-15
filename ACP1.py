
from tkinter import *
import random
from PIL import Image, ImageTk

window = Tk()
window.title("Rock Paper Scissors")
window.geometry("400x500")
window.configure(bg="lightblue")

choices = ["rock", "paper", "scissors"]

label = Label(window, text="Enter r for rock, p for paper, s for scissors", bg="lightblue")
label.pack()

entry = Entry(window)
entry.pack()

result_label = Label(window, text="", bg="lightblue")
result_label.pack()

image_label = Label(window, bg="lightblue")
image_label.pack()

def play():
    u = entry.get().lower()
    c = random.choice(choices)

    # ROCK CONDITIONS
    if c=="rock" and u=="p":
        upload = Image.open("w.webp")
        upload = upload.resize((250,250))
        image = ImageTk.PhotoImage(upload)
        image_label.config(image=image)
        image_label.image=image
        result_label.config(text="You Win!")

    elif c=="rock" and u=="s":
        upload = Image.open("l.png")
        upload = upload.resize((250,250))
        image = ImageTk.PhotoImage(upload)
        image_label.config(image=image)
        image_label.image=image
        result_label.config(text="You Lose!")

    elif c=="rock" and u=="r":
        upload = Image.open("t.png")
        upload = upload.resize((250,250))
        image = ImageTk.PhotoImage(upload)
        image_label.config(image=image)
        image_label.image=image
        result_label.config(text="Tie!")

    # PAPER CONDITIONS
    elif c=="paper" and u=="r":
        upload = Image.open("l.png")
        upload = upload.resize((250,250))
        image = ImageTk.PhotoImage(upload)
        image_label.config(image=image)
        image_label.image=image
        result_label.config(text="You Lose!")

    elif c=="paper" and u=="s":
        upload = Image.open("w.webp")
        upload = upload.resize((250,250))
        image = ImageTk.PhotoImage(upload)
        image_label.config(image=image)
        image_label.image=image
        result_label.config(text="You Win!")

    elif c=="paper" and u=="p":
        upload = Image.open("t.png")
        upload = upload.resize((250,250))
        image = ImageTk.PhotoImage(upload)
        image_label.config(image=image)
        image_label.image=image
        result_label.config(text="Tie!")

    # SCISSORS CONDITIONS
    elif c=="scissors" and u=="p":
        upload = Image.open("l.png")
        upload = upload.resize((250,250))
        image = ImageTk.PhotoImage(upload)
        image_label.config(image=image)
        image_label.image=image
        result_label.config(text="You Lose!")

    elif c=="scissors" and u=="r":
        upload = Image.open("w.webp")
        upload = upload.resize((250,250))
        image = ImageTk.PhotoImage(upload)
        image_label.config(image=image)
        image_label.image=image
        result_label.config(text="You Win!")

    elif c=="scissors" and u=="s":
        upload = Image.open("t.png")
        upload = upload.resize((250,250))
        image = ImageTk.PhotoImage(upload)
        image_label.config(image=image)
        image_label.image=image
        result_label.config(text="Tie!")

    else:
        result_label.config(text="Invalid Input")

btn = Button(window, text="RESULT", command=play)
btn.pack()

window.mainloop()

