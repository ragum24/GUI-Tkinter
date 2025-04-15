from tkinter import *

root=Tk()

root.title("Celsius To Fahrenheit Converter")

def convert_maths():
    farri=float(entry1.get())*1.8+32
    
    text1.delete("1.0",END)
    text1.insert(END,farri)

label1=Label(root,text="Enter Temperature in Celsius:")
label1.pack(pady=10)
entry1=Entry(root,bg="thistle")
entry1.pack(pady=10)
button1=Button(root,text="Convert",bg="thistle",fg="dark slate blue",command=convert_maths)
button1.pack(pady=10)
label2=Label(root,text="Fahrenheit:")
label2.pack(pady=10)
text1=Text(root,fg="purple",height=1,width=20)
text1.pack(pady=10)

mainloop()