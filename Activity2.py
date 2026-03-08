from tkinter import*
from tkinter import messagebox

window=Tk()
window.geometry("200x200")
window.title("Messagebox")

def msg():
    messagebox.showwarning("Alert!! Stop clicking me")

btn=Button(window , text="Check for Virus" , command=msg)
btn.place(x=40 , y=80)

window.mainloop()