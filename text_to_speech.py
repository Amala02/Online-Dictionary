'''-->project done by Amala Shwetah, cse 2nd year
-->The project imports modules tkinter, playsound and json
-->The following mini project allows user to enter any word into the search box and obtain
the meaning of the same as well as an audio output of the word by text-to-speech
implementation
'''

from tkinter import *
import tkinter as tk
from gtts import gTTS
from playsound import playsound
import requests
import json

#creating the GUI 
root = Tk()
root.geometry('600x600')
root.resizable(0,0)
root.config(bg= '#73cef0')
root.title('Text_to_speech')


Label(root, text= 'TEXT-TO-SPEECH', font = 'Poppins 20 italic',  foreground="white", background="black", width= '20').pack(side='top')
Msg= StringVar()
Label(root, text= "enter the text here", font = 'Open-sans 15 italic underline').place(x=20, y=60)
searchbar= Entry(root, textvariable= 'Msg', width='50')
searchbar.place(x=20, y=100)


#the function for getting meanings using an api available online

def define():
    word= searchbar.get()
    print(word)
    req= requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    ans=req.json()
    ans= ans[0]
    ans= ans['meanings']
    ans=ans[0]
    print(ans)
    #meaning display
    T= Text(root, height=20, width= 50)
    T.insert(END, ans)
    T.place(x=25, y=300)

#function for the text to speech conversion
def Text_To_Speech():
    Message= searchbar.get()
    speech= gTTS(text= Message)
    speech.save('Speech.mp3')
    playsound('Speech.mp3')

def Exit():
    root.destroy()

def Reset():
    Msg.set("")

Button(root, text= "Hear", font = 'arial 15 bold', command=Text_To_Speech, width =4).place(x=25, y=140)
Button(root, text= "Exit", font= 'arial 15 bold',  command= Exit, width= 4).place(x=100, y=140)
Button(root, text= "Reset", font = 'arial 15 bold', command=Reset, width =4).place(x=175, y=140)
Button(root, text="Definition", font ='arial 15 bold', command= define, width =10).place(x=25, y= 200)
root.mainloop()
