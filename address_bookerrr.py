from tkinter import *

groots=Tk()

label=Label(groots,text="My Address Book")
label.grid(row=0,column=1,columnspan=3)

open_b=Button(groots,text="Open",bg="white")
open_b.grid(row=0,column=4)

lllliiiiisssstttt=Listbox(groots,height=15,width=30)
lllliiiiisssstttt.grid(row=1,column=0,columnspan=3,rowspan=5)

name=Label(groots,text="Name:")
name.grid(row=2,column=3)

entry1=Entry(groots)
entry1.grid(row=2,column=4)

address=Label(groots,text="Address:")
address.grid(row=3,column=3)

entry2=Entry(groots)
entry2.grid(row=3,column=4)

phone_num=Label(groots,text="Mobile:")
phone_num.grid(row=4,column=3)

entry3=Entry(groots)
entry3.grid(row=4,column=4)

email=Label(groots,text="Email:")
email.grid(row=5,column=3)

entry4=Entry(groots)
entry4.grid(row=5,column=4)

birthdayyyy=Label(groots,text="Birthday:")
birthdayyyy.grid(row=6,column=3)

entry5=Entry(groots)
entry5.grid(row=6,column=4)

update_b=Button(groots,text="Update/Add",bg="white")
update_b.grid(row=7,column=4,pady=30)

edit_b=Button(groots,text="Edit",bg="white")
edit_b.grid(row=0,column=0)

delete_b=Button(groots,text="Delete",bg="white")
delete_b.grid(row=7,column=0)

save_b=Button(groots,text="Save!",width=35,bg="white")
save_b.grid(row=8,column=3)
mainloop()