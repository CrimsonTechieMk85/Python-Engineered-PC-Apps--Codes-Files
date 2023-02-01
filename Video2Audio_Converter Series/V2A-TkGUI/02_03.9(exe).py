try:
    from Tkinter import *
    import Tkinter.messagebox
except:
    from tkinter import *
    import tkinter.messagebox
import os 
import pyttsx3
import random
import time 
import shutil
from moviepy.video.io.VideoFileClip import VideoFileClip

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
rate = rate+50
engine.setProperty('voices',voices[0].id)
engine.setProperty('rate',104.3)
def speak(text):
    engine.say(text)
    engine.runAndWait()

root = Tk()
root.geometry('800x430')
root.title('Video 2 Audio The Converter')
root.resizable(0, 0)

topFrame =  Frame(root)
topFrame.pack()

Midframe =  Frame(root)
Midframe.pack()

bottomFrame  = Frame(root)
bottomFrame.pack()
def AI_eve():

    Intro_1 = ("Hi, I am Eve.", "Yo! I am Eve.","It's pleased to meet you! I am Eve.","Hey! I am Eve.","Glad to meet you. I am Eve.","Glad I met you. I am Eve. ","Hello, I am Eve.")
    Intro_2 = ("How may I help you?","Is there anything i can do for you? ","Do you need any help?")
    Intro_3 = ("You are using Video-2-Audio The Converter version 4.5.2 ","This is Video-2-Audio The Converter version 4.5.2 ","This is version 4.5.2 of Video-2-Audio The Converter ","You are using version 4.5.2 of Video-2-Audio The Converter ")
    Intro_4 = ("made by Benjamin Sooraj Ignacy.","created by Benjamin Sooraj Ignacy.","programmed by Benjamin Sooraj Ignacy.","coded by Benjamin Sooraj Ignacy.")


    Intro_01 = random.choice(Intro_1)
    Intro_02 = random.choice(Intro_2)
    Intro_03 = random.choice(Intro_3)
    Intro_04 = random.choice(Intro_4)

    own_00 = Intro_03 + Intro_04

    speak(Intro_01)

    speak("Your personal A.I. Assistant.")

    speak(Intro_02)

    time.sleep(1.3)

    speak(own_00)
def exit_btn():
    speak("Do you wish to exit the Video-2-Audio The Converter ?")
    answer = tkinter.messagebox.askquestion("AI Eve: Video-2-Audio The Conveter ","DO you wish to exit?")
    if answer == "yes":
        print("Apps closed.")
        quit()
    return

def clr_btn():
    global fl_name
    global fl_path
    fl_name.delete(0, END)
    fl_path.delete(0, END)
    return
def V_2_A():
    global fl_name
    global fl_path


    file_name = fl_name.get()
    file_path = fl_path.get()
    Complete_path = file_path+"\\"+file_name
    #print( Complete_path )
    file_to_audio_fl = Complete_path+".mp4"

    try:
        my_clip =VideoFileClip(file_to_audio_fl)
#
        my_clip.audio.write_audiofile(file_to_audio_fl.replace(".mp4",".mp3"))

        speak("I am converting your video file into audio.")

        status = Label(root,text="converting...",bd=1,relief=SUNKEN,anchor=W)
        status.pack(side=BOTTOM,fill=X) 

        time.sleep(1.23)

        my_clip.close()
        audio_fl_path = Complete_path+".mp3"
        move_path = os.getcwd()+"\\"+"Media"
        destination = move_path+"\\"+file_name+".mp3"

        status.after(30000, lambda: status.place_forget())
    
        status_00 = Label(root,text="Video converted into audio.",bd=1,relief=SUNKEN,anchor=W)
        status_00.pack(side=BOTTOM,fill=X) 
        speak("Your video file has been converted into audio.")
        try:
            os.makedirs(move_path)
        except  OSError:
            pass
        shutil.move(audio_fl_path,destination)

    
        time.sleep(1.23)
        move_path = os.getcwd()+"\\"+"Media"
        tkinter.messagebox.showinfo("AI Eve - Audio Convertion complete.","Audio file stored at "+move_path)

        answer = tkinter.messagebox.askquestion("AI Eve","DO you wish to convert another video into audio?")
        if answer == "yes":
            fl_name.delete(0, END)
            fl_path.delete(0, END)
    except OSError:
        fl_name.delete(0, END)
        fl_path.delete(0, END)
        speak("An error as been occurred")
        tkinter.messagebox.showinfo("AI Eve - Audio Convertion Error.","Video file not found or is not supportive.")

    return

lbl = Label(topFrame, text = " ")
lbl.grid(row=1,column=3)

label_name = Label(Midframe,text ="Name of the file: ",fg="red")
label_name.grid(row=4,column=2,sticky=N)

fl_name = Entry(Midframe, relief=SUNKEN,bg="white",fg="red")
fl_name.grid(row=4,column=3,sticky=N,padx=0, pady=0,ipadx=200,ipady=0)

lbl = Label(Midframe, text = " ")
lbl.grid(row=5,column=1,sticky=N)

label_path = Label(bottomFrame,text ="Path of the file: ",fg="blue")
label_path.grid(row=7,column=2,sticky=N)

fl_path = Entry(bottomFrame, relief=SUNKEN,bg="white",fg="blue")
fl_path.grid(row=7,column=3,sticky=N,padx=0, pady=0,ipadx=200,ipady=0)

lbl = Label(bottomFrame, text = " ")
lbl.grid(row=16,column=2,sticky=E)


button_fl = Button(bottomFrame,text="Input",fg="white",bg="green",command=V_2_A)
button_fl.grid(row=18,column=3,padx=0, pady=0,ipadx=68,ipady=0) 


lbl_btn_fl = Label(bottomFrame, text = " ")
lbl_btn_fl.grid(row=20,column=2)


button_clr = Button(bottomFrame, text="clear",fg="white",bg="blue", command=clr_btn)
button_clr.grid(row=30,column=3,padx=0, pady=0,ipadx=68,ipady=0) 

lbl_btn_clr = Label(bottomFrame, text = " ")
lbl_btn_clr.grid(row=33,column=3,sticky=E)

button_exit = Button(bottomFrame,text="exit",fg="white",bg="red",command=exit_btn,anchor=S)
button_exit.grid(row=55,column=3,padx=0, pady=0,ipadx=68,ipady=0) 

lbl_btn_clr = Label(bottomFrame, text = " ")
lbl_btn_clr.grid(row=65,column=3,sticky=E)

button_Intro = Button(bottomFrame,text="Speak",fg="white",bg="purple",command=AI_eve,anchor=S)
button_Intro.grid(row=77,column=3,padx=0, pady=0,ipadx=68,ipady=0) 
root.mainloop()