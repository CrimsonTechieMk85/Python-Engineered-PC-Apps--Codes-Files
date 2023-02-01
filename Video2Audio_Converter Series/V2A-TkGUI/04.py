a = "Starting..."
print("\n"+a)
import time 
import tqdm  
try:
    from Tkinter import *
    import Tkinter.messagebox
    from tkinter import ttk
    
except:
    from tkinter import *
    import tkinter.messagebox
    from tkinter import ttk
import os 
import pyttsx3
import random
import shutil
import sys
from moviepy.video.io.VideoFileClip import VideoFileClip
import ctypes

for i in tqdm.tqdm(range(1000)):
    time.sleep(0.01)
time.sleep(1.7)

#
kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')

SW_HIDE = 0

hWnd = kernel32.GetConsoleWindow()

if hWnd:
    user32.ShowWindow(hWnd, SW_HIDE)
#
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
    Intro_3 = ("You are using Video-2-Audio The Converter version 4.5.2.1 ","This is Video-2-Audio The Converter version 4.5.2.1 ","This is version 4.5.2.1 of Video-2-Audio The Converter ","You are using version 4.5.2.1 of Video-2-Audio The Converter ")
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
        speak("Thank you")
        time.sleep(1.3)
        speak("Have a nice day.")
        time.sleep(0.23)
        root.destroy()

def clr_btn():
    global fl_name
    global fl_path
    global media_exnts
    fl_name.delete(0, END)
    fl_path.delete(0, END)
    media_exnts.delete(0,END)
    
    status = Label(root,text="converting.... ",bd=1,anchor=W)
    #status.pack(side=BOTTOM,fill=X) 

    status.after(300, lambda : status.place_forget())

    status_00 = Label(root,text="Video converted into audio.",bd=2,relief=SUNKEN,anchor=W)
    #status_00.pack(side=BOTTOM,fill=X) 

    status.after(300, lambda : status.destroy())
    return
def V_2_A():
    global fl_name
    global fl_path
    global media_exnts


    try:
        file_name =  fl_name.get()
        file_path =  fl_path.get()
        file_type  = media_exnts.get()
        Complete_path = str(file_path)+"\\"+str(file_name)
    #print( Complete_path )
        file_to_audio_fl = Complete_path+"."+str(file_type).lower()
        print(file_to_audio_fl)


        status = Label(root,text=" ",bd=1,anchor=W)
        status.pack(side=BOTTOM,fill=X) 

        status.after(3000, lambda : status.place_forget())

        status_00 = Label(root,text=" ",bd=2,anchor=W)
        status_00.pack(side=BOTTOM,fill=X) 

        status.after(3000, lambda : status.destroy())

     

        my_clip =VideoFileClip(file_to_audio_fl)
#

        speak("I am converting your video into audio.")

        my_clip.audio.write_audiofile(file_to_audio_fl.replace("."+str(file_type).lower(),".mp3"))

        time.sleep(1.23)

        my_clip.close()
        audio_fl_path = Complete_path+".mp3"
        move_path = os.path.dirname(os.path.realpath(__file__))+"\\"+"Media"
        destination = move_path+"\\"+file_name+".mp3"
   
        speak("Your video file has been converted into audio.")
        try:
            os.makedirs(move_path)
        except  OSError:
            pass
        shutil.move(audio_fl_path,destination)

        status_00.after(339, lambda : status.destroy())

    
        time.sleep(1.23)
        move_path = os.getcwd()+"\\"+"Media"
        tkinter.messagebox.showinfo("AI Eve - Audio Convertion complete.","Audio file stored at "+move_path)

        speak("DO you wish to convert another video into audio?")
        answer = tkinter.messagebox.askquestion("AI Eve","DO you wish to convert another video into audio?")
        if answer == "yes": 
            fl_name.delete(0, END)
            fl_path.delete(0, END)
        
    except OSError:
        fl_name.delete(0, END)
        fl_path.delete(0, END)
         
        speak("An error as been occurred")
        tkinter.messagebox.showinfo("AI Eve - Audio Convertion Error.","Video file not found or is not supportive.")
    except KeyError:
        fl_name.delete(0, END)
        fl_path.delete(0, END)
        
        speak("An error as been occurred")
        tkinter.messagebox.showinfo("AI Eve - Audio Convertion Error.","Video file not found or is not supportive.")
     
    return

lbl = Label(topFrame, text = " ")
lbl.grid(row=1,column=3)

label_name = Label(Midframe,text ="Name of the video file: ",fg="red",font = ("Times New Roman", 10))
label_name.grid(row=4,column=2,sticky=N)

fl_name = Entry(Midframe, relief=SUNKEN,bg="white",fg="red",font = ("Times New Roman", 10))
fl_name.grid(row=4,column=3,sticky=N,padx=0, pady=0,ipadx=200,ipady=0)

lbl = Label(Midframe, text = " ")
lbl.grid(row=5,column=1,sticky=N)


l_extnts = Label(bottomFrame, text = "Select the extension :", 
          font = ("Times New Roman", 10))
l_extnts.grid(row = 7,column=2, padx = 10, pady = 0) 

n = StringVar() 
media_exnts = ttk.Combobox(bottomFrame, textvariable = n)
# Adding combobox drop down list 
media_exnts['values'] = ('mp4',  
                          'm4a', 
                          'webm', 
                          'm4v', 
                          'f4v', 
                          'f4a', 
                          'm4b', 
                          'm4r', 
                          'f4b', 
                          'mov')
media_exnts.grid(row=7,column=3,sticky=N,padx=0, pady=0,ipadx=195,ipady=0)

 
lbl_btn_optn = Label(bottomFrame, text = " ")
lbl_btn_optn.grid(row=9,column=3,sticky=E)
 

label_path = Label(bottomFrame,text ="Path of the video file: ",fg="blue",font = ("Times New Roman", 10))
label_path.grid(row=12,column=2,sticky=N)

fl_path = Entry(bottomFrame, relief=SUNKEN,bg="white",fg="blue")
fl_path.grid(row=12,column=3,sticky=N,padx=0, pady=0,ipadx=200,ipady=0)

lbl = Label(bottomFrame, text = " ")
lbl.grid(row=34,column=2,sticky=E)


button_fl = Button(bottomFrame,text="Click to convert",fg="white",bg="green",font = ("Times New Roman", 10),command=V_2_A)
button_fl.grid(row=46,column=3,padx=0, pady=0,ipadx=56,ipady=0) 


lbl_btn_fl = Label(bottomFrame, text = " ")
lbl_btn_fl.grid(row=50,column=2)


button_clr = Button(bottomFrame, text="Click to clear",fg="white",bg="blue",font = ("Times New Roman", 10),command=clr_btn)
button_clr.grid(row=56,column=3,padx=0, pady=0,ipadx=66,ipady=0) 

lbl_btn_clr = Label(bottomFrame, text = " ")
lbl_btn_clr.grid(row=62,column=3,sticky=E)

button_exit = Button(bottomFrame,text="Click to say good bye to Eve",fg="white",bg="red",font = ("Times New Roman", 10),command=exit_btn,anchor=S)
button_exit.grid(row=68,column=3,padx=0, pady=0,ipadx=30,ipady=0) 

lbl_btn_clr = Label(bottomFrame, text = " ")
lbl_btn_clr.grid(row=76,column=3,sticky=E)

button_Intro = Button(bottomFrame,text="Click to speak with Eve",fg="white",bg="purple",font = ("Times New Roman", 10),command=AI_eve,anchor=S)
button_Intro.grid(row=88,column=3,padx=0, pady=0,ipadx=44,ipady=0) 

media_exnts.current(0) 
root.mainloop()

#    s_1 = "Type the format of the folder video file (for example like this: mp4, m4a, m4v, f4v, f4a, m4b, m4r, f4b, mov, webm). \n"