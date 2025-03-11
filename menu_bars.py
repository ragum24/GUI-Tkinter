from tkinter import *
from tkinter.ttk import *
root=Tk()
root.title("Menu-")

#creating the menu bar

'''menu_bar=Menu(root)

#creating the menu options and commands

file=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="File",menu=file)
file.add_command(label="New File",command=None)
file.add_command(label="Open File",command=None)
file.add_command(label="Save",command=None)
file.add_command(label="Share",command=None)
file.add_separator()
file.add_command(label="Exit",command=root.destroy)
root.config(menu=menu_bar)'''

#progress bar widget

def bar():
    import time
    progress["value"]=20
    root.update_idletasks()
    time.sleep(1)
    progress["value"]=40
    root.update_idletasks()
    time.sleep(1)
    progress["value"]=60
    root.update_idletasks()
    time.sleep(1)
    progress["value"]=80
    root.update_idletasks()
    time.sleep(1)
    progress["value"]=100
progress=Progressbar(root,orient=HORIZONTAL,length=100,mode="determinate")
b=Button(root,text="Start",command=bar)
progress.pack(pady=10)
b.pack(pady=10)







mainloop()
