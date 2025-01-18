from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES



def change(text,src,dest):
    text1=text
    src1=src
    dest1=dest
    trans=Translator()
    trans1=trans.translate(text1,src=src1,dest=dest1)
    return trans1.text



def data():
    s = box1.get()
    d =  box3.get()
    msg= Sortxt.get(1.0,END)
    textget=change(msg,s,d)
    inptxt.delete(1.0,END)
    inptxt.insert(END,textget)
  
core=Tk()
core.title("LANGUAGE TRANSLATOR BY 'DEV'")
core.geometry("500x700")
core.config(bg='Black')

text1=Label(core,text="Translator",font=("Time New Roman",40,"bold"))
text1.place(x=100,y=40,height=50,width=300)

text1=Label(core,text="Source Text",font=("Time New Roman",20,"bold"),bg="Black", fg="White")
text1.place(x=150,y=100,height=30,width=200)

Sortxt=Text(core,font=("Time New Roman",15,"bold"),wrap=WORD, bg="white", fg="black")
Sortxt.place(x=10, y=150, height=300, width=480)

lst=list(LANGUAGES.values())

box1=ttk.Combobox(core,value=lst)
box1.place(x=10,y=450,height=40,width=110)
box1.set("Select Language")

box2=Button(core,text="Translate",relief=RAISED,command=data)
box2.place(x=125,y=450,height=40,width=110)

box3=ttk.Combobox(core,value=lst)
box3.place(x=240,y=450,height=40,width=110)
box3.set("Select Language")

desttxt=Label(core,text="Destination Text",font=("Time New Roman",20,"bold"),bg="Black", fg="White")
desttxt.place(x=100,y=500,height=30,width=300)

inptxt=Text(core,font=("Time New Roman",15,"bold"),wrap=WORD, bg="white", fg="black")
inptxt.place(x=10, y=550, height=300, width=480)

core.mainloop()