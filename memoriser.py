from tkinter import *

from tkinter.filedialog import *

roooooooootttttttuuuhhh=Tk()

roooooooootttttttuuuhhh.title("Memoriser-")

def opennnn():
    file=askopenfile(title="Open File")
    if file is not None:
        list.delete(0,END)
        read=file.readlines()
        for i in read:
            list.insert(END,i) 

def save_me_plsss_just_kidding():
    file=asksaveasfile(title="Save File")
    if file is not None:
        for i in list.get(0,END):
            print(i,file=file)
        list.delete(0,END)

def add_cookies():
    list.insert(END,entry1.get())
    entry1.delete(0,END)
    

button1=Button(roooooooootttttttuuuhhh,text="SAVE",command=save_me_plsss_just_kidding)
button1.pack(pady=20)

entry1=Entry(roooooooootttttttuuuhhh)
entry1.pack()

button2=Button(roooooooootttttttuuuhhh,text="ADD",command=add_cookies)
button2.pack(pady=20)

button3=Button(roooooooootttttttuuuhhh,text="OPEN",command=opennnn)
button3.pack(side=LEFT,padx=20)

button4=Button(roooooooootttttttuuuhhh,text="DELETE")
button4.pack(side=RIGHT,padx=20)

list=Listbox(roooooooootttttttuuuhhh,width=40,bg="light grey")
list.pack(pady=20)


mainloop()