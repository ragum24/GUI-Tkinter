from tkinter import *

root=Tk()

root.title("Rock Paper Sissors Game!")

label1=Label(root,text="Rock Paper Sissors")
label1.pack(pady=10)
label2=Label(root,text="Start The Game Noaw!",fg="midnight blue")
label2.pack(pady=10)

frame=Frame(root)
frame.pack(pady=10)
label3=Label(frame,text="Options:")
label3.grid(row=0,column=0)
button1=Button(frame,text="Rock",bg="hot pink")
button1.grid(row=1,column=1,padx=10)
button2=Button(frame,text="Paper",bg="royal blue")
button2.grid(row=1,column=2,padx=10)
button3=Button(frame,text="Sissors",bg="medium orchid")
button3.grid(row=1,column=3,padx=10)


frames=Frame(root)
frames.pack(pady=10)
label4=Label(frames,text="Scores:")
label4.grid(row=0,column=0)
label5=Label(frames,text="You Selected:")
label5.grid(row=1,column=0)
label6=Label(frames,text="Your Wins:")
label6.grid(row=1,column=1)
label7=Label(frames,text="Computer Selected:")
label7.grid(row=2,column=0)
COOKIE=Label(frames,text="Computer Wins:")
COOKIE.grid(row=2,column=1)

mainloop()