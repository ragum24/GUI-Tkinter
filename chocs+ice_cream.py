from tkinter import *

root=Tk()

root.geometry("500x500")

label=Label(root,text="Yummeh Chocolates & Ice_cream!",font=("Calibri",20))
label.pack()
# top frame 

frame=Frame(root)
frame.pack()
b1=Button(frame,text="Chocolate",font="Calibri",fg="brown",bg="sandy brown")
b1.pack(pady=20)
b2=Button(frame,text="Strawberry",font="Calibri",fg="pink",bg="salmon")
b2.pack(pady=20)
b3=Button(frame,text="Bubble Gum",font="Calibri",fg="teal",bg="medium aquamarine")
b3.pack(pady=20)

framed=Frame(root)
framed.pack(pady=50)
b4=Button(frame,text="Tiramasu",font="Calibri",fg="saddle brown",bg="sandy brown")
b4.pack(side=LEFT)
b5=Button(frame,text="Cake",font="Calibri",fg="salmon",bg="crimson")
b5.pack(side=LEFT)
b6=Button(frame,text="Hot Pastries",font="Calibri",fg="saddle brown",bg="sandy brown")
b6.pack(side=LEFT)
mainloop()