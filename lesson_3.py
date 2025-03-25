from tkinter import *

root=Tk()

root.title("Yummeh Food List")
label=Label(root,text="Yummeh Food List-",font=("Calibri",15))
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
list=Listbox(root,height=5,width=20,bg="plum",fg="white",font="Calibri",yscrollcommand=scrollbar.set)
label.pack()
list.pack()
scrollbar.config(command=list.yview)
list.insert(1,"Pizza")
list.insert(2,"Pizza Roll")
list.insert(3,"Pizza Cup")
list.insert(4,"Pizza Cheese")
list.insert(5,"Pasta")
list.insert(6,"Cupcake")
list.insert(7,"Candy 4 ever")
list.insert(8,"Salad")
list.insert(9,"Noodles")
list.insert(10,"Pizza Noodles Salad?")









mainloop()