from tkinter import*
import random
from PIL import Image , ImageTk

window=Tk()
window.title("Rock , papers , Sissors")
window.geometry("400x400")
window.configure(bg="light blue")



choices=["rock" , "paper" , "sissor"] 
c=random.choice(choices)


frame=Frame(master=window , relief=RAISED , borderwidth=5)
label1=Label(master=frame , text="Welcome to rock paper sissors" , fg="green" , bg="blue")
label2=Label(master=frame , text="Choose weather you wanna do rock paper or sissors write r for rock p for paper and s for sissors")
frame.pack()
label1.pack()
label2.pack()


entry=Entry(fg="white" , bg="black" , width=50)
def play():
    global u
    u=entry.get()

btn2=Button(window , text="RESULT" , command=play , fg="yellow" , bg="orange")
entry.pack()

if c=="rock" and u=="p":
    upload=Image.open("w.webp")
    upload=upload.resize((300 , 300))
    image=ImageTk.PhotoImage(upload)
    label=Label(window , image=image)

elif c=="rock" and u=="s":
    upload=Image.open("l.png")
    upload=upload.resize((300 , 300))
    image=ImageTk.PhotoImage(upload)
        
elif c=="rock" and u=="r":
    upload=Image.open("t.png")
    upload=upload.resize((300 , 300))
    image=ImageTk.PhotoImage(upload)

