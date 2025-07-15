from tkinter import *

from tkinter.filedialog import *

from tkinter import messagebox

groots=Tk()

infooooh={}

def small_window(event):
    global grooooot_junior,select,details,key,values
    grooooot_junior=Toplevel(groots)
    select=lllliiiiisssstttt.curselection()
    details=""
    if select:
        key=lllliiiiisssstttt.get(select)
        values=infooooh[key]
        details="Name:"+key+"\n"
        details+="Adress:"+values[0]+"\n"
        details+="Mobile:"+values[1]+"\n"
        details+="Email:"+values[2]+"\n"
        details+="Birthday"+values[3]+"\n"
    Lb=Label(grooooot_junior,text=details)
    Lb.pack()


def clear_everythinggggggg():
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
    entry4.delete(0,END)
    entry5.delete(0,END)
    

def add():
    nama=entry1.get()
    if nama=="":
        messagebox.showinfo("ERROR!!!","Name cannot be empty, please fill that in...")
    else:
        if nama not in infooooh.keys():
            lllliiiiisssstttt.insert(END,nama)
        infooooh[nama]=(entry2.get(),entry3.get(),entry4.get(),entry5.get())
    clear_everythinggggggg()

def edit():
    select=lllliiiiisssstttt.curselection()
    if select:
        entry1.insert(0,lllliiiiisssstttt.get(select))
        details=infooooh[entry1.get()] 
        entry2.insert(0,details[0])  
        entry3.insert(0,details[1])
        entry4.insert(0,details[2])
        entry5.insert(0,details[3])
    else:
        messagebox.showinfo("ERROR!!!","Please add your name first!")


def delete():
    selectt=lllliiiiisssstttt.curselection()
    if selectt:
        del infooooh[lllliiiiisssstttt.get(selectt)]
        lllliiiiisssstttt.delete(selectt)
    else:
        messagebox.showinfo("ERROR!","Please make a selection first!")

def saveee():
    file=asksaveasfile(defaultextension=".txt")
    if file:
        print(infooooh,file=file)
        lllliiiiisssstttt.delete(0,END)
        infooooh.clear()
    else:
        messagebox.showinfo("ERROR!","The file has not been saved.")

def open_file():
    global infooooh
    lllliiiiisssstttt.delete(0,END)
    infooooh.clear()
    file=askopenfile()
    if file:
        infooooh=eval(file.read())
        for i in infooooh:
            lllliiiiisssstttt.insert(END,i) 
    else:
        messagebox.showinfo("ERROR!","No file has been selected.")  

label=Label(groots,text="My Address Book")
label.grid(row=0,column=1,columnspan=3)

open_b=Button(groots,text="Open",bg="white",command=open_file)
open_b.grid(row=0,column=4)

lllliiiiisssstttt=Listbox(groots,height=15,width=30)
lllliiiiisssstttt.grid(row=1,column=0,columnspan=3,rowspan=5)
lllliiiiisssstttt.bind('<<ListboxSelect>>',small_window)

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

update_b=Button(groots,text="Update/Add",bg="white",command=add)
update_b.grid(row=7,column=4,pady=30)

edit_b=Button(groots,text="Edit",bg="white",command=edit)
edit_b.grid(row=0,column=0)

delete_b=Button(groots,text="Delete",bg="white",command=delete)
delete_b.grid(row=7,column=0)

save_b=Button(groots,text="Save!",width=35,bg="white",command=saveee)
save_b.grid(row=8,column=3)
mainloop()