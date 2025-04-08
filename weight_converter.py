from tkinter import *

root=Tk()

root.title("Weight Converter")

def convert_maths():
    milli=float(eeeeeeeeeeeeeeeeeeeentry.get())*1000000
    gram=float(eeeeeeeeeeeeeeeeeeeentry.get())*1000
    tonne=float(eeeeeeeeeeeeeeeeeeeentry.get())/1000
    
    text1.delete("1.0",END)
    text1.insert(END,milli)
    text2.delete("1.1",END)
    text2.insert(END,gram)
    text3.delete("1.2",END)
    text3.insert(END,tonne)


lllllllllllllabbbbbbbbbbbbbellllllllllllll=Label(root,text="Enter Weight In Kg-")
eeeeeeeeeeeeeeeeeeeentry=Entry(root,bg="thistle")
bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbuuuuuuuuuuuttttttttttttttttttton=Button(root,text="Convert",bg="thistle",fg="dark slate blue",command=convert_maths)
llllllllllllllabel=Label(root,text="Milligram:")
labellllllllllllllll=Label(root,text="Gram")
labeeeeeeeeeel=Label(root,text="Tonne")
text1=Text(root,fg="purple",height=1,width=20)
text2=Text(root,fg="blue",height=1,width=20)
text3=Text(root,fg="deep pink",height=1,width=20)

lllllllllllllabbbbbbbbbbbbbellllllllllllll.grid(row=0,column=0)
eeeeeeeeeeeeeeeeeeeentry.grid(row=0,column=1)
bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbuuuuuuuuuuuttttttttttttttttttton.grid(row=0,column=2)
llllllllllllllabel.grid(row=1,column=0)
labellllllllllllllll.grid(row=1,column=1)
labeeeeeeeeeel.grid(row=1,column=2)
text1.grid(row=2,column=0)
text2.grid(row=2,column=1)
text3.grid(row=2,column=2)
mainloop()