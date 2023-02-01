from moviepy.video.io.VideoFileClip import VideoFileClip
import os
import pyttsx3
import time
import random
import sys
import shutil
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate  = engine.getProperty('rate')
rate = rate + 50
engine.setProperty('vioces',voices[0].id)

engine.setProperty('rate',104.3)

def speak(text):
    engine.say(text)
    engine.runAndWait()
Intro_1 = ("Hi, I am Eve.", "Yo! I am Eve.","It's pleased to meet you! I am Eve.","Hey! I am Eve.","Glad to meet you. I am Eve.","Glad I met you. I am Eve. ","Hello, I am Eve.")
Intro_2 = ("How may I help you?","Is there anything i can do for you? ","Do you need any help?")
Intro_3 = ("You are using Video-2-Audio version 2.3.9.2 ","This is Video-2-Audio version 2.3.9.2 ","This is version 2.3.9.2 of Video-2-Audio ","You are using version 2.3.9.2 of Video-2-Audio ")
Intro_4 = ("made by Benjamin Sooraj Ignacy.","created by Benjamin Sooraj Ignacy.","programmed by Benjamin Sooraj Ignacy.","coded by Benjamin Sooraj Ignacy.")


Intro_01 = random.choice(Intro_1)
Intro_02 = random.choice(Intro_2)
Intro_03 = random.choice(Intro_3)
Intro_04 = random.choice(Intro_4)

own_00 = Intro_03 + Intro_04

print(Intro_01)
speak(Intro_01)

print("Your personal A.I. Assistant.")
#speak("Your personal A.I. Assistant.")

print(Intro_02)
#speak(Intro_02)

time.sleep(1.3)
os.system('cls')

print(Intro_03 + Intro_04.replace('Sooraj','Suraj'))
#speak(own_00)
#
time.sleep(1.3)
os.system('cls')
while True:
    try:
        s_0 = "Type the name of the video file to be converted into audio. \n"
        print(s_0)
        #speak(s_0)
        f = input("Type the name of the video file: \n")
        time.sleep(0.45)
        os.system('cls')
        s_2 = "Copy and paste the path where your video file "+''+f+" exists from folder tab. \n"
        print(s_2)
        #speak(s_2)
        destination = input("Paste the path of your video file :\n")
        time.sleep(0.45)
        os.system('cls')
        s_1 = "Type the format of the folder video file (for example like this: mp4, m4a, m4v, f4v, f4a, m4b, m4r, f4b, mov, webm). \n"
        print(s_1)
        #speak(s_1)
        extnts = input("Type the video file format: \n").lower()
        time.sleep(0.45)
        os.system('cls')
        #vfl = destination+"\\"+f+"."+extnts
        
        vfl = os.path.join(destination,"{0}.{1}".format(f,extnts))
# 
        my_clip =VideoFileClip(vfl)
#
        my_vclip.audio.write_audiofile(vfl.replace(extnts,".mp3"))
        my_clip.close()

        print("I have successfully converted your "+f+"."+extnts+" video file into"+f+"."+"mp3 .")
        #speak("I have successfully converted your "+f+".."+extnts+" video file into"+f+".."+"mp3 .")

        sys.exit()
 #   
    except FileNotFoundError:
        pass
            
