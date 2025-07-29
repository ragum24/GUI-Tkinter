from tkinter import *
import speech_recognition as sr

groot_daa_root=Tk()

groot_daa_root.geometry("500x300")

def translate():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Start Talking!!!")
        telldaprogram=r.listen(source,timeout=20)
        try:
            text=r.recognize_google(telldaprogram)
        except:
            text="Sorry... Talk to me later."
        text_space.delete(1.0,END)
        text_space.insert(END,text)


title=Label(groot_daa_root,text="Voice Notepad",font="30")
title.grid(row=0,column=2,columnspan=3)

click_me_button=Button(groot_daa_root,text="Click one me 2\nstart recording!",width=12,command=translate)
click_me_button.grid(row=2,column=2,pady=15)

text_space=Text(groot_daa_root,width=40,height=4)
text_space.grid(row=1,column=2,padx=10)

save_text_b=Button(groot_daa_root,text="Save The Text")
save_text_b.grid(row=1,column=3)

mainloop()