from tkinter import *
from gtts import gTTS 
import os

root=Tk()

root.config()
root.geometry("300x300")

def text_2_speech():
    gtttts=gTTS(text=entry.get(),lang="ta",tld="co.in")
    gtttts.save("AUDIOOH.wav")
    os.system("AUDIOOH.wav")

text2speech=Label(root,text="Text To Speech")
text2speech.pack(pady=20)

entry=Entry(root,width=30)
entry.pack(pady=40)

submit_b=Button(root,text="SUBMIT",fg="white",bg="dark orange",width=5,command=text_2_speech)
submit_b.pack(pady=10)

mainloop()