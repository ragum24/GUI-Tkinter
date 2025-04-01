from tkinter import *
import calendar
root=Tk()

root.title("calendar")

root.geometry("200x250")
def show_cal():
    window=Tk()
    window.config(bg="White")
    window.title("calendar")
    window.geometry("550x600")
    year=int(enrty1.get())
    cal_content=calendar.calendar(year)
    tttttttttteeeeeeeeeeeeexxxxxxxxxxxxttttttttttt=Text(window,font="Consolas 10",wrap="none",height=80,width=80)
    tttttttttteeeeeeeeeeeeexxxxxxxxxxxxttttttttttt.insert("1.0",cal_content)
    tttttttttteeeeeeeeeeeeexxxxxxxxxxxxttttttttttt.pack(padx=20)

    window.mainloop()
label1=Label(root,text="Calendar-",font="Calibri") 
label1.pack(pady=20)
lllllllaaaaaaaaaaaabbbbbbbeeeeeeeeelllllllll=Label(root,text="Year:",fg="royal blue",font="Calibri")
lllllllaaaaaaaaaaaabbbbbbbeeeeeeeeelllllllll.pack(pady=10)

enrty1=Entry(root)
enrty1.pack(pady=5)

button=Button(root,text="Show calendar",bg="medium violet red",fg="white",font=("Calibri",10),command=show_cal)
button.pack(pady=5)
button2=Button(root,text="Exit",bg="medium orchid",fg="white",font=("Calibri",10),command=root.destroy)
button2.pack(pady=5)





mainloop()