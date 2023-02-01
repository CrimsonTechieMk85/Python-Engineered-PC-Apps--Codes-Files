''' importing prefrences or getting required datas from the modules'''
import os  # for file and folder operation

import time  # for 'time-delays' activities

import wx  # for GUI apps using 'Wxpython'

from playsound import playsound# for playing audio files

import winshell# mimic windows powershell activities

from win32com.client import Dispatch# Creates a Dispatch based COM object using win32 modules

import datetime# getting real-time datas of today

from gtts import gTTS# using google-text-to-speech (gtts) service

'''Source files'''
wDir_path = os.path.dirname(os.path.realpath(__file__))# curent working directory or the 'Now'-location of the file.

#icon source image file -> eg: 'image_file_name'.ico
for (root, dirs, file) in os.walk(wDir_path):
    for f in file:
        if '.ico' in f:
            print(f)
            ico_flpath = os.path.join(wDir_path,f)

'''File name & File extension'''
file_name, file_type = os.path.splitext(os.path.basename(os.path.realpath(__file__)))

# Real-Time Date&Time datas:
'''Time'''
dt_clockH = datetime.datetime.now().strftime("%I").lstrip("0").replace(" 0", " ")
#
dt_clockM = datetime.datetime.now().strftime("%M").lstrip("0").replace(" 0", " ")
#
dt_clockS = datetime.datetime.now().strftime("%S").lstrip("0").replace(" 0", " ")
#
dt_clockMS = datetime.datetime.now().strftime("%f")
#
epoch_miliseconds = int(time.time() * 1000)
#
dt_TMR = "{0}-{1}-{2}".format(dt_clockH,dt_clockM,dt_clockS)
#
dt_DN = datetime.datetime.now().strftime('%p').lower() 

'''Date'''
dt_dd = datetime.datetime.now().strftime("%#d")
#
dt_mm = datetime.datetime.now().strftime("%#m")
#
dt_yyyy = datetime.datetime.now().strftime("%Y")
#
dt_wdys = datetime.datetime.now().strftime("%A").lower()
#
dt_mnths = datetime.datetime.now().strftime("%B").lower()
#
dt_date = "{0}-{1}-{2}".format(dt_dd,dt_mm,dt_yyyy)
#

def timeDelay():
    time.sleep(1.2)# time delay seconnds for each sequence or activities

# using 'class' or "blueprint" to extract all the 'frame' supports existing within the 'wx' module for GUI apps
class txt2Mp3_453(wx.Frame):

    # Starts frame upon user request or 'CLICKING' the app  
    def __init__(self,parent,id):
        
        # Window (Frame) with parametres i.e (frame, parent=None,id=-1.'window title',size=(int,int),style=wx.(obj))
        wx.Frame.__init__(self,parent,id,file_name, size=(642,356),style = wx.DEFAULT_FRAME_STYLE & ~wx.MAXIMIZE_BOX ^ wx.RESIZE_BORDER)

        self.SetIcon(wx.Icon(ico_flpath))# sets icon on the window title bar

        self.wpanel = wx.Panel(self)# setting 'container' to have wxpython GUI parts

        self.wpanel.SetBackgroundColour('Light blue')# sets the panel or app background

    #Text

        # creates fonts for 'Text' input field
        lblfont = wx.Font(18, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)


        ## label text 

        self.custom_txt_lbl = wx.StaticText(self.wpanel,-1,"Text:",(33,38),(22,22),wx.TEXT_ALIGNMENT_CENTRE)

        self.custom_txt_lbl.SetFont(lblfont)# sets font for the 'Text' label using variable 'textfieldfont'

        self.custom_txt_lbl.SetForegroundColour('Red')# sets the 'Text' label text colour as red

        self.custom_txt_lbl.SetBackgroundColour('White')# sets the 'Text' label colour as white

        # text input field font
        textfieldfont = wx.Font(18, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) 

        # creates text input field
        self.textCtrl = wx.TextCtrl(self.wpanel, pos=(99,35),size =(490,32.1), style = wx.TE_HT_ON_TEXT &~ wx.TEXT_ALIGNMENT_JUSTIFIED &~ wx.TE_WORDWRAP)

        self.textCtrl.SetFont(textfieldfont)#sets font for the text input field using variable 'textfieldfont'

        self.textCtrl.SetForegroundColour('Red')#sets input field text as red


    #click here
 
        # creates fonts for click button
        btn_click_font = wx.Font(18, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) 

        # combines 'Exit' button with its functions
        self.click_btn = wx.Button(self.wpanel,label='Convert',pos=(280,156),size=(122,34),style=wx.BORDER_RAISED)

        self.click_btn.SetFont(btn_click_font)# sets 'Click here' button font using variable 'btn_click_font'

        self.click_btn.SetForegroundColour('White')# sets 'Click here' button text as white

        self.click_btn.SetBackgroundColour('Dark Green')# sets 'Click here' button as dark green

        #self.wbtn.SetForegroundColour('Black')

        #self.Bind(wx.EVT_STC,self.print)

        self.Bind(wx.EVT_BUTTON,self.txt2Mp34,self.click_btn)# combines 'Click here' button with its functions

    #Exit

        # creates fonts for exit button
        btn_exit_font = wx.Font(18, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)# Creates  fonts for 'Exit' button 

        # Exit button 

        # creates  'Exit' button  
        self.exit_btn = wx.Button(self.wpanel,label='Exit',pos=(280,200),size=(122,34),style=wx.BORDER_RAISED)

        self.exit_btn.SetFont(btn_exit_font)# sets font for the exit button using variable 'btn_exit_font'

        self.exit_btn.SetForegroundColour('White')# sets 'Exit' button text as white

        self.exit_btn.SetBackgroundColour('Red')# sets 'Exit' button coloer as red

        self.Bind(wx.EVT_BUTTON,self.exitbutton,self.exit_btn)# combines 'Exit' button with its functions


    #Reset

        # creates fonts for reset button
        btn_rst_font = wx.Font(18, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)# Creates  fonts for 'Reset' button 

        # reset button 

        # creates  'Reset' button  
        self.rst_btn = wx.Button(self.wpanel,label='Reset',pos=(280,245),size=(122,34),style=wx.BORDER_RAISED)

        self.rst_btn.SetFont(btn_rst_font)# sets font for the exit button using variable 'btn_rst_font'

        self.rst_btn.SetForegroundColour('White')# sets 'Reset' button text as white

        self.rst_btn.SetBackgroundColour('Purple')# sets 'Reset' button coloer as Purple

        self.Bind(wx.EVT_BUTTON,self.rst,self.rst_btn)# combines 'Reset' button with its functions


    # close window button

        self.Bind(wx.EVT_CLOSE,self.Close)# combines 'X' window button with its functions


    # Accents

        # creates  fonts for tdl
        accentfont = wx.Font(18, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) 
        
        ## label accent  

        # creates  'Select accent' label appear on the panel  
        self.accentlbl = wx.StaticText(self.wpanel, -1, "Select accent:", (31, 103))# 

        self.accentlbl.SetFont(accentfont)# sets 'Select accent:" label fonts uing parameters from 'accentfont' variable 

        self.accentlbl.SetForegroundColour('White')# sets the 'Select accent:' label text colour as white

        self.accentlbl.SetBackgroundColour('Blue')# sets the 'Select accent:' label colour as 'Black' 

        # collection or lists conataining accent items
        self.accent_lists = ['en','fr','zh-CN','zh-TW','pt','es']
        
        # accents comboboox
        self.accentComboBox = wx.ComboBox(self.wpanel, -1, "en", (94.8, 141.4),(78,56),self.accent_lists, wx.CB_READONLY | wx.ALIGN_CENTER)

        self.accentComboBox.SetFont(accentfont)# sets fonts for the accent items containing in the 'acccent' combobox

        #self.accentComboBox.SetForegroundColour('Black')

        #self.accentComboBox.SetBackgroundColour('Light Orange')


    #Tdls

        # collection or lists conataining tdl items
        self.tdl_lists = ['com.au','co.uk','com','ca','co.in','ie','co.za','ca','fr','com.br','pt','com.mx','es']

        # Creates  fonts for tdl
        tdlfont = wx.Font(18, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) 

        ## label tdl

        # Creates  'Select Top.Domain.Level (tdl):' label appear on the panel
        self.tdllbl = wx.StaticText(self.wpanel, -1, "Select Top-Level.Domain (tld):", (269, 103))

        self.tdllbl.SetFont(tdlfont)# sets 'Select Top.Domain.Level (tdl):" label fonts uing parameters from 'tdlfont' variable 

        self.tdllbl.SetForegroundColour('White')# sets 'Select Top.Domain.Level (tdl):" label text as white 

        self.tdllbl.SetBackgroundColour('Black')# sets 'Select Top.Domain.Level (tdl):" label background as black 

        # Creates  Top.Domain.Level (tdl) combobox box with 'tdl' items from list (tdl_lists)
        self.tdlComboBox = wx.ComboBox(self.wpanel, -1, "com", (498.1, 141.4),(81,56),self.tdl_lists, wx.CB_READONLY | wx.ALIGN_CENTER)

        self.tdlComboBox.SetFont(tdlfont)# sets fonts for the tdl items containing in the 'tdl' combobox

        #self.tdlComboBox.SetForegroundColour('white')

        #self.tdlComboBox.SetBackgroundColour('black')

       

    def txt2Mp34(self,event):
          
        ''' to make AppName folder '''
        app_folder = os.path.join(wDir_path,file_name)

        try:
            os.makedirs(app_folder)
                
            #sys.exit()

            #app_folder_made_msg =wx.MessageDialog(None,"'{}' main app folder created.".format(file_name),"Folder maker status - App main",wx.OK | wx.ICON_NONE)

            #app_folder_made_msg.ShowModal()
                
            #timeDelay()

            # creates  fonts for tdl

            #app_folder_made_stats_bar = self.CreateStatusBar()# creates status bar

            #app_folder_made_stats_bar.SetStatusText("Folder maker status - '{}' main app folder created.".format(file_name))# shows that the realtime date sub folder has made in app main folder

            #app_folder_made_stats_font = wx.Font(18, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) 

            #app_folder_made_stats_bar.SetFont(app_folder_made_stats_font)

            #timeDelay()

            #print(file_name)

            #app_folder_made_msg.Destroy()

            #app_folder_made_stats_bar.Destroy()

            #self.timer.Stop()

            #timeDelay()

        except OSError:
            pass

        ''' to make sub current date folder '''
        now_date_sub_folder = os.path.join(app_folder,dt_date)
        try:
            os.makedirs(now_date_sub_folder)

            #print("\nFolder {} created.".format(file_name))
            
            # wipeout()
            
            #dt_folder_made_msg =wx.MessageDialog(None,"'{0}' sub folder created in '{1}' main app folder.".format(dt_date,file_name),"Folder maker status - Real-time date sub folder",wx.OK | wx.ICON_NONE)

            #dt_folder_made_msg.ShowModal()

            #timeDelay()

            #dt_sub_folder_made_stats_bar = self.CreateStatusBar()# creates status bar

            #dt_sub_folder_made_stats_bar.SetStatusText("Folder maker status - '{0}' sub folder created in '{1}' main app folder.".format(dt_date,file_name))# shows that the realtime date sub folder has made in app main folder

            #dt_sub_folder_made_stats_font = wx.Font(18, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) 

            #dt_sub_folder_made_stats_bar.SetFont(dt_sub_folder_made_stats_font)
            
            #timeDelay()

            #dt_sub_folder_made_stats_bar.Destroy()

            #self.timer.Stop()

            #timeDelay()
        except OSError:
            pass

        ''' Make 'AppName' shortcut '''
        desktop = winshell.desktop()
        path = os.path.join(desktop, "{}.lnk".format(file_name))

        ''' Make 'AppName' using "shortcut maker" protcol '''
        # 'if' -> if shortcut is not found at system desktop, creates it
        # Or 'else' -> skips 'shortcut maker' protocol if the json is found

        shortcut_exists = os.path.exists(path)

        if shortcut_exists is False:

            target = app_folder
            wDir = app_folder
                    #file_name, file_type = os.path.splitext(os.path.basename(os.path.realpath(__file__)))
            shell = Dispatch('WScript.Shell')
            shortcut = shell.CreateShortCut(path)
            shortcut.Targetpath = target
            shortcut.WorkingDirectory = wDir
            shortcut.save()

            #shortcut_made_msg =wx.MessageDialog(None,"Shortcut '{}' created.".format(file_name),"Shortcut maker status - App main",wx.OK | wx.ICON_NONE)

            #shortcut_made_msg.ShowModal()

            #timeDelay()

            #shortcut_made_stats_bar = self.CreateStatusBar()# creates status bar

            #shortcut_made_stats_bar.SetStatusText("App main Shortcut '{}' created.".format(file_name))# shows that the app main shotcut has been converted made

            #shortcut_made_stats_font = wx.Font(18, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) 

            #shortcut_made_stats_bar.SetFont(shortcut_made_stats_font)

            #timeDelay()

            #shortcut_made_stats_bar.Destroy()
                    
        else:
            pass
        try:

            str_txtin = self.textCtrl.GetValue()# gets the text value that within input field

            str_tdlin = self.tdlComboBox.GetStringSelection()# gets the tdl value that from the tdl combobox

            str_langin = self.accentComboBox.GetStringSelection()# gets the accemt value that from the accent combobox

            audio_name_mp3 = "{0}-{1},{2}-{3}.mp3".format("audio",str_langin,str_tdlin,epoch_miliseconds)
            #
            self.audio = os.path.join(now_date_sub_folder,audio_name_mp3)
            #
            sp = gTTS(text=str_txtin,lang=str_langin,slow=False,lang_check=True,tld=str_tdlin)
            #
            sp.save(self.audio)
            #
            playsound(self.audio)

            #teskcomplete_bar = self.CreateStatusBar()# creates status bar

            #teskcomplete_bar.SetStatusText("Text to audio file (.Mp3): Complete")# shows that the text has been converted into audio file sw=ucessfully
        
            timeDelay()
            
            success_made_msg =wx.MessageDialog(self.wpanel,"'{0}' text sucessfully converted into '{1}'.".format(str_txtin,audio_name_mp3),"Success",wx.OK | wx.ICON_INFORMATION )

            #timeDelay()

            success_made_msg.ShowModal()

            timeDelay()

            ''' Asks user whether to clear for assurance as message box. if yes, clears the values for the user, or exits the app if no  '''
            yn_msgbox = wx.MessageDialog(self.wpanel,"Do you wish to use the app again?","Yes/No",wx.YES_NO| wx.ICON_NONE)

            yn_var = yn_msgbox.ShowModal()

            if yn_var == wx.ID_YES:
                #teskcomplete_bar.Destroy()# clears the status bar

                self.textCtrl.Clear()#            clears texts that exists within the input fields

                self.tdlComboBox.SetValue("com")# setting the tdl combobox back to default

                self.accentComboBox.SetValue("en")# setting the accent combobox back to default


        # Active when there is no text to convert
        except AssertionError as ae:
       #     print("\n{}".format(ae))

            ae_msg =wx.MessageDialog(self.wpanel,"No words to convert into audio file (.mp3)","Assertion Error: ",wx.OK | wx.ICON_ERROR)

         #   wx.CallLater(2000, ae_msg.Destroy)

            ae_msg.ShowModal()

            timeDelay()

            #ae_msg.EndModal(True)

            self.textCtrl.Clear()#            clears texts that exists within the input feilds

            self.tdlComboBox.SetValue("com")# setting the tdl combobox back to default

            self.accentComboBox.SetValue("en")# setting the accent combobox back to default

            #teskcomplete_bar.Destroy()# clears the status bar
        #    wipeout()
        #    i = i-1

        # Active when there is program run time error     
        except RuntimeError as re:
           # print("\n{}".format(re))

            re_msg =wx.MessageDialog(self.wpanel,"Program did not function properly.","Runtime Error: ",wx.OK | wx.ICON_ERROR)

            re_msg.ShowModal()

        #    wx.CallLater(200, re_msg.Destroy)
            timeDelay()

          #  re_msg.Destroy()

            self.textCtrl.Clear()#            clears texts that exists within the input feilds

            self.tdlComboBox.SetValue("com")# setting the tdl combobox back to default

            self.accentComboBox.SetValue("en")# setting the accent combobox back to default

            self.Destroy()

            timeDelay()

            os.startfile(os.path.basename(__file__))

        # Active when an error is not recognizible          
        except:
            print("\nUnknown error ocurred...")

            ue_msg =wx.MessageDialog(self.wpanel,"Unknown error ocurred...","Error: ",wx.OK | wx.ICON_ERROR)

            ue_msg.ShowModal()

            timeDelay()

            #ue_msg.Destroy()
        
            os.remove(self.audio)

            self.textCtrl.Clear()#            clears texts that exists within the input feilds

            self.tdlComboBox.SetValue("com")# setting the tdl combobox back to default

            self.accentComboBox.SetValue("en")# setting the accent combobox back to default
         


    def exitbutton(self,event):
        ''' Asks user whether to use again as message box. if not, clears the values for the user, or exits the app if yes  '''
        yn_msgbox = wx.MessageDialog(self.wpanel,"Are you sure you want to exit the app?","Yes/No",wx.YES_NO| wx.ICON_WARNING)

        yn_var = yn_msgbox.ShowModal()

        if yn_var == wx.ID_NO:

            self.textCtrl.Clear()#            clears texts that exists within the input feilds
       
            self.tdlComboBox.SetValue("com")# setting the tdl combobox back to default

            self.accentComboBox.SetValue("en")# setting the accent combobox back to default
        
        else:
            #self.Destroy()# closes app  when task is not required again
            self.Destroy()# closes app when 'EXIT' button is click

    def Close(self,event):
        self.Destroy()# closes app  when 'CLOSE' or 'X' on the window is pressed


    def rst(self,event):
        self.textCtrl.Clear()#            clears texts that exists within the input feilds

        self.tdlComboBox.SetValue("com")# setting the tdl combobox back to default

        self.accentComboBox.SetValue("en")# setting the accent combobox back to default



if __name__=='__main__':

    app=wx.App()# Start the app

    frame = txt2Mp3_453(parent=None,id=-1)# Gives parametres or infos to the class or 'Frame' components

    frame.Show()# Shows the commponents existed within the app


    app.MainLoop()# loops the window as systems close apps within milliseconds or more