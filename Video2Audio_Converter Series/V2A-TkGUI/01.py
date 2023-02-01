from tkinter import *
import tkinter.messagebox
import os 
import pyttsx3
import random
import time 
import shutil
from moviepy.video.io.VideoFileClip import VideoFileClip
master = Tk()
#900X400
master.geometry('800x500')
master.title('Video 2 Audio converter')
master.resizable(0, 0) #
def exit_btn():
    answer = tkinter.messagebox.askquestion("AI Eve","DO you wish to exit?")
    if answer == "yes":
        print("Apps closed.")
        quit()
    return
def clr_btn():
    global fl_name
    global fl_path
    fl_name.delete(0, END)
    fl_path.delete(0, END)
def V_2_A():
    global fl_name
    global fl_path
    global lbl
    global lbl_00
    global lbl_03


    file_name = fl_name.get()
    file_path = fl_path.get()
    Complete_path = file_path+"\\"+file_name
    print( Complete_path )
    file_to_audio_fl = Complete_path+".mp4"
    '''my_clip =VideoFileClip(file_to_audio_fl)
#
    my_clip.audio.write_audiofile(file_to_audio_fl.replace(".mp4",".mp3"))
    '''
    '''
    my_clip.close()
    audio_fl_path = Complete_path+".mp3"
    move_path = os.getcwd()+"\\"+"Media"
    destination = move_path+"\\"+file_name+".mp3"'''

    time.sleep(1.23)
    move_path = os.getcwd()+"\\"+"Media"
    tkinter.messagebox.showinfo("AI Eve - Audio Converted","Audio file stored at "+move_path)

    answer = tkinter.messagebox.askquestion("AI Eve","DO you wish to convert another video file?")
    if answer == "yes":
        fl_name.delete(0, END)
        fl_path.delete(0, END)
    return

 
    '''try:
        os.makedirs(move_path)
    except  OSError:
        pass
    shutil.move(audio_fl_path,destination)'''

lbl_q = Label(master, text = " ")
lbl_q.grid(row=12, column=0,sticky=EW)

lbl_a = Label(master, text = " ")
lbl_a.grid(row=9, column=2,sticky=EW)

lbl_r= Label(master, text = " ")
lbl_r.grid(row=1, column=3,sticky=EW)

label_1 = Label(master,text =" Name of the video file name: ",bg="red",fg="white")
label_1.grid(row=1, column=2,sticky=N)
fl_name = Entry(master, relief=SUNKEN)
fl_name.grid(row=1, column=3,sticky=N,padx=0, pady=0,ipadx=200,ipady=0)
#fl_name.configure(background='red')

label_2 = Label(master,text =" Path of the video file: ",bg="blue",fg="white")
label_2.grid(row=10, column=2,sticky=N)
fl_path = Entry(master, relief=SUNKEN)
fl_path.grid(row=10, column=3,padx=0, pady=0,ipadx=200,ipady=0)

lbl = Label(master, text = " ")
lbl.grid(row=12, column=2,sticky=NSEW)

Btn1 = Button(master, text="Input",fg="white",bg="dark green", command=V_2_A)
Btn1.grid(row=20, column=3,sticky=N,padx=0, pady=0,ipadx=17,ipady=0) 

lbl = Label(master, text = " ")
lbl.grid(row=22, column=2,sticky=NSEW)

Btn3 = Button(master, text="clear",fg="white",bg="green", command=clr_btn)
Btn3.grid(row=29, column=3,sticky = N,padx=0, pady=0,ipadx=20,ipady=0) 
lbl = Label(master, text = " ")
lbl.grid(row=22, column=3,sticky=EW)

lbl_v = Label(master, text = " ")
lbl_v.grid(row=30, column=2,sticky=NSEW)

Btn2 = Button(master, text="Exit",fg="white",bg="red", command=exit_btn)
Btn2.grid(row=22, column=4,sticky=N,padx=0, pady=0,ipadx=20,ipady=0) 

#staus bar

from PIL import ImageTk, Image
image_fl = r"E:\Vs_2020_data_files\AI_Eve_YouTube_Saver_prototype_Vr00\Video-Audio_Converter_prototype_02\unnamed_tng_icon.ico"
img = ImageTk.PhotoImage(Image.open(image_fl))  
l=Label(image=img)
l.grid(row=0, column=3,sticky = W+E,padx=0, pady=0,ipadx=0,ipady=0) 

#

    #time.sleep(1.3)
lbl = Label(master, text = " ")
lbl.grid(row=22, column=2,sticky=NSEW)
#
#master.rowconfigure(1, weight=1)
'''
lbl = Label(master)
lbl.grid(row=6, column=2) 
'''
#master.grid_columnconfigure(22, weight=9)
#master.grid_rowconfigure(2, weight=1)
master.mainloop()
