from tkinter import*

window=Tk()
window.geometry("400x300")


def topwin():
    top=Toplevel()
    top.geometry("180x100")
    top.title("Top level")
    label1=Label(top , text="This is a top level window")
    label1.pack()

    top.mainloop()

label2=Label(window , text="This is a root window")
btn=Button(window , text="Click to open another window" , command=topwin)

label2.pack()
btn.pack()

window.mainloop()