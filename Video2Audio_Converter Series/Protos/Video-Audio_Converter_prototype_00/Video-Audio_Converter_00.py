import pyttsx3
import os 
import time
import sys
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate  = engine.getProperty('rate')
rate = rate + 50
engine.setProperty('vioces',voices[0].id)

engine.setProperty('rate',104.3)

def speak(text):
    engine.say(text)
    engine.runAndWait()

while True:
    try:
        s_0 = "Type the name of the video file to be converted into audio. \n"
        print(s_0)
        speak(s_0)
        f = input("Type the name of the video file: \n")
        time.sleep(0.45)
        os.system('cls')
        s_2 = "Copy and paste the path where your video file "+''+f+" exists from folder tab. \n"
        print(s_2)
        speak(s_2)
        destination = input("Paste the path of your video file :\n")
        time.sleep(0.45)
        os.system('cls')
        s_1 = "Type the format of the folder video file (for example like this: mp4, m4a, m4v, f4v, f4a, m4b, m4r, f4b, mov, webm). \n"
        print(s_1)
        speak(s_1)
        extnts = input("Type the video file format: \n").lower()
        time.sleep(0.45)
        os.system('cls')
        fl = destination+"\\"+f+"."+extnts 
        output = fl.replace("\\"+f+"."+extnts,"\\"+f+".mp3")
        with open(fl,'rb') as r:
            data = r.read()
        s = open(output,'wb')
        s.write(data)
        s.close()
        r.close() 
        print("Your audio file "+f+" created .")
        speak("Your audio file "+f.replace("."+extnts,"..mp3")+" has been created .")
        break
    except FileNotFoundError:
       A_ = "Sorry, file "+f+"."+extnts+" does not exist at the moment"
       print(A_)
       speak(A_.replace(".",".."))
       time.sleep(0.45)
       os.system('cls')
       pass
    except PermissionError:
        pass
time.sleep(1.2)
os.system('cls')
print("Thank you. \n")
speak("Thank you.")
time.sleep(1.3)
print("Have a nice day.")
speak("Have a nice day.")
time.sleep(1.3)
os.system('cls')    
time.sleep(1.31)  
sys.exit()