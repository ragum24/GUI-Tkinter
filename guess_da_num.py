from tkinter import *
from tkinter import messagebox
import random

grooooooot=Tk()

grooooooot.title("Guess The Number Game")

grooooooot.geometry("400x100")

secret_num=random.randint(1,20)

count=0

def OK():
    name=entry.get()
    messagebox.showinfo(message=f"Hey {name}!\nTake a Guess: 1-20")

def Guess():
    global count
    name=entry.get()
    guess=int(entry1.get())
    if guess==secret_num:
        messagebox.showinfo(message=f"{name}, you are correct!\n You took...{count} tries!👌👍😊")
    elif guess>secret_num:
        messagebox.showinfo(message=f"Your guess, {guess} is too high...😒")
        count+=1
    elif guess<secret_num:
        messagebox.showinfo(message=f"Your guess, {guess} is too low...😒😂🤣")
        count+=1
    
       

label=Label(grooooooot,text="Welcome to our game!!!",font=("Times New Roman",15,"normal"))
label.grid(row=0,column=1)

label1=Label(grooooooot,text="Siapa nama kamu?")
label1.grid(row=1,column=0)

button=Button(grooooooot,text="OK",command=OK)
button.grid(row=1,column=2)

label2=Label(grooooooot,text="Take a guess-")
label2.grid(row=2,column=0)

button1=Button(grooooooot,text="Guess",command=Guess)
button1.grid(row=2,column=2)

entry=Entry(grooooooot)
entry.grid(row=1,column=1)

entry1=Entry(grooooooot)
entry1.grid(row=2,column=1)


mainloop()