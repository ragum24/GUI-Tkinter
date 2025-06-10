from tkinter import *


grooooot_4_ever=Tk()

grooooot_4_ever.title("Multiplication")

grooooot_4_ever.geometry("200x300")

def something():
    table=""
    for i in range(rad_num.get()):
        table+=str(num.get())+"x"+ str(i)+"="+ str(num.get()*i)+"\n"
    label3.config(text=table)


button=Button(grooooot_4_ever,text="Generate",bd=10,background="light grey",foreground="black",font=("Calibri",10),command=something)
button.grid(row=3,column=0,columnspan=3)

num=IntVar()

rad_num=IntVar()

label1=Label(grooooot_4_ever,text="Mathematical Table")
label1.grid(row=0,column=0,columnspan=3,pady=20)

label2=Label(grooooot_4_ever,text="Number:")
label2.grid(row=1,column=0,padx=10,pady=25)

label3=Label(grooooot_4_ever,text="")
label3.grid(row=4,column=0)


from tkinter.ttk import *

drop=Combobox(grooooot_4_ever,textvariable=num,width=5)
drop["values"]=tuple(range(1,101))
drop.grid(row=1,column=1)

radio1=Radiobutton(grooooot_4_ever,text="10",variable=rad_num,value=10)
radio1.grid(row=2,column=0)

radio2=Radiobutton(grooooot_4_ever,text="20",variable=rad_num,value=20)
radio2.grid(row=2,column=1,padx=10)

radio3=Radiobutton(grooooot_4_ever,text="30",variable=rad_num,value=30)
radio3.grid(row=2,column=2,pady=10,padx=15)



import tkinter as tk
 


mainloop()