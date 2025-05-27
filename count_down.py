from tkinter import *
import time
from tkinter import messagebox

i_am_groooooot=Tk()

i_am_groooooot.geometry("250x250")

#Declaration of Variables

sec=StringVar()
min=StringVar()
hrs=StringVar()
sec.set("00")
min.set("00")
hrs.set("00")

def down():
    temp=int(hrs.get())*3600+int(min.get())*60+int(sec.get())
    while temp>=0:
        minute,second=divmod(temp,60)
        hours=0
        if minute>60:
            hours,minute=divmod(minute,60)
        hrs.set(hours)
        min.set(minute)
        sec.set(second)
        i_am_groooooot.update()
        time.sleep(1)
        if temp==0:
            messagebox.showinfo(message="Time's Up!!")
        temp-=1

entry1=Entry(i_am_groooooot,width=3,textvariable=hrs)
entry1.place(x=80,y=30)

entry2=Entry(i_am_groooooot,width=3,textvariable=min)
entry2.place(x=110,y=30)

entry3=Entry(i_am_groooooot,width=3,textvariable=sec)
entry3.place(x=140,y=30)

button1=Button(i_am_groooooot,text="Start the Countdown!",command=down)
button1.place(x=60,y=80)

mainloop()