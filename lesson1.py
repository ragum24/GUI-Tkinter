from tkinter import *
#creating a tkinter window
root=Tk()
#deciding the dimension of the window
root.geometry("200x200")
#creating a button
b=Button(root,text="Press Here",bd="10",background="purple",foreground="white",font=("Calibri",10),command=root.destroy)
#creating a label
label=Label(root,text="Username:")

entry1=Entry(root,width=10)
entry1.place(x=80,y=10)
label.place(x=10,y=10)
b.pack(pady=80)
mainloop()