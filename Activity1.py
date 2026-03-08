from tkinter import*
from PIL import Image,ImageTk

window=Tk()
window.geometry("400x400")
window.title("Image")

upload=Image.open("fruit.avif")
image=ImageTk.PhotoImage(upload)

label=Label(window , image=image , height=350 , width=300)
label.place(x=50 , y=0)

window.mainloop()
