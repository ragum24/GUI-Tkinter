from tkinter import *
#creating a tkinter window
root=Tk()
root.title="Login"
#deciding the dimension of the window
root.geometry("200x200")
#creating a button
b=Button(root,text="Press Here",bd="10",background="purple",foreground="white",font=("Calibri",10),command=root.destroy)

s=Button(root,text="Save",bd="3",background="light gray")
#creating a label
label1=Label(root,text="Username:")
label2=Label(root,text="Password:")


entry1=Entry(root,width=15)
entry1.place(x=80,y=10)
entry2=Entry(root,show="*",width=15)
entry2.place(x=80,y=35)
label1.place(x=10,y=10)
label2.place(x=10,y=35)
b.pack(pady=80)
s.place(x=15,y=55)
mainloop()