''' importing prefrences or getting required datas from the modules'''
import os  # for file and folder operation

import time  # for 'time-delays' activities

from gtts.tts import gTTSError

import wx  # for GUI apps using 'Wxpython'

from playsound import playsound# for playing audio files

import winshell# mimic windows powershell activities

from win32com.client import Dispatch# Creates a Dispatch based COM object using win32 modules

import datetime# getting real-time datas of today

import json# used for data-files operations

from gtts import gTTS# using google-text-to-speech (gtts) service

import speech_recognition as sr

'''Source files'''
#wDir_path = os.path.dirname(os.path.realpath(__file__))# curent working directory or the 'Now'-location of the file.

wDir_path = os.getcwd()

#icon source image file -> eg: 'image_file_name'.ico
"""
for (root, dirs, file) in os.walk(wDir_path):
    for f in file:
        if '.ico' in f:
            try:
                ico_flpath = os.path.join(wDir_path,f)
                #pass
            except OSError:
                pass
""" 
for file in os.listdir(wDir_path):
    print(file)
    if '.ico' in file:
        try:
            ico_flpath =os.path.join(wDir_path,file)
        except OSError:
            pass
    else:
        pass


# Current file name infos
'''File name & File extension'''
file_name, file_type = os.path.splitext(os.path.basename(os.path.abspath(__file__)))

# App Json files details
paths_name_json = 'path_datas'

json_fl_name = '{}.json'.format(paths_name_json)

settings_json_fl_rt = os.path.join(wDir_path,json_fl_name) 

''' Settings file path '''
# Dynamic [Earky-Tests type] App Json files details
et_json_name = '{}_datas'.format(file_name)

et_paths_infos_flname_json= '{}.json'.format(et_json_name)

et_settings_json_fl_rt = os.path.join(wDir_path,et_paths_infos_flname_json) 

# -----------------------------------------------------------------------------------------
''' App Details '''
# Dynamic [Earky-Tests type] app title PF+
et_app_title = "Txt2Mp3-6.3 PEF++ I.V.U-en [early-tests.Id: {}]".format(file_name)

# App title PF+
app_title = "Txt2Mp3-6.3 (Perfected.Even.Further++) [Individual.Variable.Utility-enhanced]"


# --------------------------------------------------------------------------------
''' Folder names '''
# Audio folder with app name

main_mp3s_folder_name = 'Txt2Mp3-6.3PEF++IVU-en'
audio_app_folder_name = '{} audios'.format(main_mp3s_folder_name)

# Dynamic [Early-test type] audio folder with dynamic app name
et_audio_app_folder_name = '{} audios'.format(file_name)

# --------------------------------------------------------------------------------------------------

''' Real-Time Date&Time datas '''
#Time
dt_clockH = datetime.datetime.now().strftime("%I").lstrip("0").replace(" 0", " ")

dt_clockM = datetime.datetime.now().strftime("%M").lstrip("0").replace(" 0", " ")

dt_clockS = datetime.datetime.now().strftime("%S").lstrip("0").replace(" 0", " ")

dt_clockMS = datetime.datetime.now().strftime("%f")

epoch_miliseconds = int(time.time() * 1000)

dt_TMR = "{0}-{1}-{2}".format(dt_clockH,dt_clockM,dt_clockS)

dt_DN = datetime.datetime.now().strftime('%p').lower() 

#Date
dt_dd = datetime.datetime.now().strftime("%#d")

dt_mm = datetime.datetime.now().strftime("%#m")

dt_yyyy = datetime.datetime.now().strftime("%Y")

dt_wdys = datetime.datetime.now().strftime("%A").lower()

dt_mnths = datetime.datetime.now().strftime("%B").lower()

dt_date = "{0}.{1}.{2}".format(dt_dd,dt_mm,dt_yyyy)

# ---------------------------------------------------------------------------

def tmr2(var):
    time.sleep(var)# time delay seconnds for each sequence or activities

def appMp3s_foldershortcut_maker_dt(root,rootdt,root_yrs):

    try:
        os.makedirs(root)
    except OSError:
        pass

    try:
        os.makedirs(root_yrs)
    except OSError:
        pass

    try:
        os.makedirs(rootdt)
    except OSError:
        pass

    ''' Make 'AppName' shortcut '''
    desktop = winshell.desktop()
    path = os.path.join(desktop, '{} - Shortcut.lnk'.format(audio_app_folder_name))

    target_rt = root
    wDir_rt = root
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target_rt
    shortcut.WorkingDirectory = wDir_rt
    shortcut.save()

def gtts_audios(text_val,lang_val,tdl_val,audio_root_val):

    gtts_audios = gTTS(text=text_val,lang=lang_val,slow=False,lang_check=True,tld=tdl_val)

    gtts_audios.save(audio_root_val)

# ---------------------------------------------------------------------------

# using 'class' or "blueprint" to extract all the 'frame' supports existing within the 'wx' module for GUI apps
class app_ui(wx.Frame):

    # Starts frame upon user request or 'CLICKING' the app  
    def __init__(self,parent,id):
        
        # Window (Frame) with parametres i.e (frame, parent=None,id=-1.'window title',size=(int,int),style=wx.(obj))
        wx.Frame.__init__(self,parent,id,app_title, size=(772,563),style = wx.DEFAULT_FRAME_STYLE & ~wx.MAXIMIZE_BOX ^ wx.RESIZE_BORDER)

        try:
            self.SetIcon(wx.Icon(ico_flpath))# sets icon on the window title bar

            #print(ico_flpath)
        except NameError:
            pass
        
        self.wpanel = wx.Panel(self)# setting 'container' to have wxpython GUI parts

        self.wpanel.SetBackgroundColour('Steel blue')# sets the panel or app background

    # -------------------------------------------------------------------------------------

    # Text

        # creates fonts for 'Text' input field
        lblfont = wx.Font(22, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
       
        self.custom_txt_lbl = wx.StaticText(self.wpanel,-1,"Text:",(33,38),(22,22),wx.TEXT_ALIGNMENT_CENTRE)

        self.custom_txt_lbl.SetFont(lblfont)# sets font for the 'Text' label using variable 'textfieldfont'

        self.custom_txt_lbl.SetForegroundColour('White')# sets the 'Text' label text colour as red

        self.custom_txt_lbl.SetBackgroundColour('Indian red')# sets the 'Text' label colour as white

        # text input field font
        textfieldfont = wx.Font(21, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) 

        # creates  'Text' label appear on the panel  
        self.textCtrl = wx.TextCtrl(self.wpanel, pos=(121,35),size =(602,36), style = wx.TE_HT_ON_TEXT &~ wx.TEXT_ALIGNMENT_JUSTIFIED &~ wx.TE_WORDWRAP)

        self.textCtrl.SetFont(textfieldfont)#sets font for the text input field using variable 'textfieldfont'

        self.textCtrl.SetToolTip("Type your text here.")# sets features pop-up details

        self.textCtrl.SetForegroundColour('Indian red')#sets input field text as red

    # -------------------------------------------------------------------------------------

    # Convert button
 
        # creates fonts for convrt button
        btn_convrt_font = wx.Font(21, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) 

        # combines 'convrt' button with its functions
        self.convrt_btn = wx.Button(self.wpanel,label='Convert',pos=(113,267),size=(156,45),style=wx.BORDER_RAISED)

        self.convrt_btn.SetFont(btn_convrt_font)# sets button font

        self.convrt_btn.SetForegroundColour('White')# sets button text as white

        self.convrt_btn.SetBackgroundColour('Dark Green')# sets button as dark green

        self.convrt_btn.SetToolTip("Click here to convert text into audio (.mp3) file.")# sets features pop-up details

        self.Bind(wx.EVT_BUTTON,self.txt2Mp3,self.convrt_btn)# combines button with its functions

    # Exit button

        # creates fonts for exit button
        btn_exit_font = wx.Font(21, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)# Creates  fonts for 'Exit' button 

        # creates  'Exit' button  
        self.exit_btn = wx.Button(self.wpanel,label='Exit',pos=(113,404),size=(156,45),style=wx.BORDER_RAISED)

        self.exit_btn.SetFont(btn_exit_font)# sets font for the button

        self.exit_btn.SetForegroundColour('White')# sets button text as white

        self.exit_btn.SetBackgroundColour('Red')# sets button coloer as red

        self.exit_btn.SetToolTip("Click here to exit or close the app.")# sets features exit details

        self.Bind(wx.EVT_BUTTON,self.exitbutton,self.exit_btn)# combines button with its functions

    # Reset button

        # creates fonts for 'Reset' button
        btn_rst_font = wx.Font(21, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)# Creates  fonts for 'Reset' button  

        # creates  'Reset' button  
        self.rst_btn = wx.Button(self.wpanel,label='Reset',pos=(549,267),size=(156,45),style=wx.BORDER_RAISED)

        self.rst_btn.SetFont(btn_rst_font)# sets font for the button

        self.rst_btn.SetForegroundColour('White')# sets button text as white

        self.rst_btn.SetBackgroundColour('Purple')# sets button coloer as Purple

        self.rst_btn.SetToolTip("Click here to reset the values back to default.")# sets features pop-up details

        self.Bind(wx.EVT_BUTTON,self.rst,self.rst_btn)# combines button with its functions

    # Access folder button

        # creates fonts for 'Access folder' button
        btn_rst_font = wx.Font(21, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)# Creates  fonts for 'Reset' button 

        # creates 'Access folder' button  
        self.open_folder_btn = wx.Button(self.wpanel,label='Access',pos=(549,404),size=(156,45),style=wx.BORDER_RAISED)

        self.open_folder_btn.SetFont(btn_rst_font)# sets font for the button

        self.open_folder_btn.SetForegroundColour('Black')# sets button text as white

        self.open_folder_btn.SetBackgroundColour('Yellow')# sets button coloer as Purple

        self.open_folder_btn.SetToolTip("Click here to open real-time date '{0}' sub folder.".format(dt_date))# sets features pop-up details

        self.Bind(wx.EVT_BUTTON,self.open_mp3_folder_dt,self.open_folder_btn)# combines button with its functions

    # Modify button

        # creates fonts for 'Modify' button
        btn_mod_font = wx.Font(21, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)# Creates  fonts for 'Reset' button 

        # creates 'Modify' button  
        self.mod_btn = wx.Button(self.wpanel,label='Modify',pos=(334,267),size=(156,45),style=wx.BORDER_RAISED)

        self.mod_btn.SetFont(btn_mod_font)# sets font for the button

        self.mod_btn.SetForegroundColour('White')# sets button text as white

        self.mod_btn.SetBackgroundColour('Orange')# sets button coloer as Purple

        self.mod_btn.SetToolTip("Click here to change path settings.")# sets features pop-up details

        self.Bind(wx.EVT_BUTTON,self.change_dir,self.mod_btn)# combines button with its functions
    
    # Play Mp3 button

        # creates fonts for 'Play Mp3' button
        btn_play_font = wx.Font(21, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)# Creates  fonts for 'Reset' button 

        # creates 'Play Mp3' button  
        self.play_btn = wx.Button(self.wpanel,label='Play Mp3-2',pos=(334,404),size=(156,45),style=wx.BORDER_RAISED)

        self.play_btn.SetFont(btn_play_font)# sets font for the button

        self.play_btn.SetForegroundColour('White')# sets button text as white

        self.play_btn.SetBackgroundColour('Black')# sets button coloer as Purple

        self.play_btn.SetToolTip("Click here to play audio.")# sets features pop-up details

        self.Bind(wx.EVT_BUTTON,self.playMP32,self.play_btn)# combines button with its functions
    
    # close window button
        self.Bind(wx.EVT_CLOSE,self.Close)# combines 'X' window button with its functions

    # ---------------------------------------------------------------------------

    # Accents option

        # creates  fonts for tdl
        accentfont = wx.Font(21, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) 

        # creates  'Select accent' label appear on the panel  
        self.accentlbl = wx.StaticText(self.wpanel, -1, "Select accent:", (31, 123))# 

        self.accentlbl.SetFont(accentfont)# sets 'Select accent:" label fonts uing parameters from 'accentfont' variable 

        self.accentlbl.SetForegroundColour('White')# sets the 'Select accent:' label text colour as white

        self.accentlbl.SetBackgroundColour('Blue')# sets the 'Select accent:' label colour as 'Black' 

        # collection or lists conataining accent items
        self.accent_lists = ['en','fr','zh-CN','zh-TW','pt','es']
        
        # accents comboboox
        self.accentComboBox = wx.ComboBox(self.wpanel, -1, self.accent_lists[0], (114, 178),(78,56),self.accent_lists, wx.CB_READONLY | wx.ALIGN_CENTER)

        self.accentComboBox.SetFont(accentfont)# sets fonts for the accent items containing in the 'acccent' combobox

        self.accentComboBox.SetToolTip("Click here to choose accent (Language).")# sets features pop-up details

    # Top-Level Domain - Tlds option

        # collection or lists conataining tdl items
        self.tdl_lists = ['com.au','co.uk','com','ca','co.in','ie','co.za','ca','fr','com.br','pt','com.mx','es']

        # Creates  fonts for tdl
        tdlfont = wx.Font(19, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) 

        # Creates  'Select Top.Domain.Level (tdl):' label appear on the panel
        self.tdllbl = wx.StaticText(self.wpanel, -1, "Select Top-Level Domain (tld) from Google:", (256, 123))

        self.tdllbl.SetFont(tdlfont)# sets 'Select Top.Domain.Level (tdl):" label fonts uing parameters from 'tdlfont' variable 

        self.tdllbl.SetForegroundColour('White')# sets 'Select Top.Domain.Level (tdl):" label text as white 

        self.tdllbl.SetBackgroundColour('Black')# sets 'Select Top.Domain.Level (tdl):" label background as black 

        # Creates  Top.Domain.Level (tdl) combobox box with 'tdl' items from list (tdl_lists)
        self.tdlComboBox = wx.ComboBox(self.wpanel, -1,self.tdl_lists[0], (598, 179),(123,67),self.tdl_lists, wx.CB_READONLY | wx.ALIGN_CENTER)

        self.tdlComboBox.SetFont(tdlfont)# sets fonts for the tdl items containing in the 'tdl' combobox

        self.tdlComboBox.SetToolTip("Click here to choose tld.")# sets features pop-up details

    def change_dir(self, event):

        dir_dlgbox = wx.DirDialog(self.wpanel,"Please choose directory (or Path):","",wx.DD_DEFAULT_STYLE | wx.DD_CHANGE_DIR)

        if dir_dlgbox.ShowModal()==wx.ID_OK:

            try:

                usr_rt_v = dir_dlgbox.GetPath()

                json_fl_r = open(settings_json_fl_rt, "r")

                json_src_data = json.load(json_fl_r)

                json_src_data["path"] = usr_rt_v

                json_fl_w = open(settings_json_fl_rt, "w")

                json.dump(json_src_data, json_fl_w)

                json_fl_r.close()

                json_fl_w.close()

                update_made_msg =wx.MessageDialog(self.wpanel,"Path changed.","Path update - Complete",wx.OK | wx.ICON_INFORMATION )

                update_made_msg.ShowModal()

                path_json = open(settings_json_fl_rt, 'r')

                data = path_json.read()

                path_infos_v = json.loads(data)["path"]
            
            except FileNotFoundError:

                settings_json = open(settings_json_fl_rt,'w')
                                
                settings_json.write("{"'"path"'":")
                                
                usr_path ={
                        "path" : str(usr_rt_v)
                         }

                json_settings_file_datas = open(settings_json_fl_rt, "w")
                       
                json.dump(usr_path, json_settings_file_datas)

                json_settings_file_datas.close()

                settings_json.close()

                settings_path_saved_msg =wx.MessageDialog(self.wpanel,"Path saved.","Path update - Complete",wx.OK | wx.ICON_INFORMATION )

                settings_path_saved_msg.ShowModal()

                path_json = open(settings_json_fl_rt, 'r')

                data = path_json.read()

                path_infos_v = json.loads(data)["path"]

            '''  Variable AppName audio folder path '''
            app_audio_folder_v = os.path.join(path_infos_v,et_audio_app_folder_name)

            ''' Variable current year folder path '''
            now_yrs_sub_folder_v = os.path.join(app_audio_folder_v,dt_yyyy)

            ''' Variable current date folder path '''
            now_date_sub_folder_v = os.path.join(now_yrs_sub_folder_v,dt_date)

            appMp3s_foldershortcut_maker_dt(root=app_audio_folder_v,rootdt=now_date_sub_folder_v,root_yrs=now_yrs_sub_folder_v)
  
            #pass
        else:
            pass

    def playMP32(self,event):

        """ Verify 'path.json' if exists or not """
        settings_json_fl_exists = os.path.exists(settings_json_fl_rt)

        if settings_json_fl_exists == False:

            dir_dlgbox = wx.DirDialog(self.wpanel,"Please choose directory (or Path):","",wx.DD_DEFAULT_STYLE | wx.DD_CHANGE_DIR)

            #dir_dlgbox.Set(wDir_path)

            if dir_dlgbox.ShowModal()==wx.ID_OK:

                usr_rt_v = dir_dlgbox.GetPath()

                settings_json = open(settings_json_fl_rt,'w')
                                
                settings_json.write("{"'"path"'":")
                                
                usr_path ={
                        "path" : str(usr_rt_v)
                                    }

                json_settings_file_datas = open(settings_json_fl_rt, "w")
                       
                json.dump(usr_path, json_settings_file_datas)

                json_settings_file_datas.close()

                settings_json.close()

            else:
                pass
        else:
            pass

        try:

            path_json = open(settings_json_fl_rt, 'r')

            data = path_json.read()

            path_infos_v = json.loads(data)["path"]

            ''' Variable AppName audio folder path '''
            app_audio_folder_v = os.path.join(path_infos_v,et_audio_app_folder_name)

            ''' Variable current year folder path '''
            now_yrs_sub_folder_v = os.path.join(app_audio_folder_v,dt_yyyy)

            ''' Variable current date folder path '''
            now_date_sub_folder_v = os.path.join(now_yrs_sub_folder_v,dt_date)

            appMp3s_foldershortcut_maker_dt(root=app_audio_folder_v,rootdt=now_date_sub_folder_v,root_yrs=now_yrs_sub_folder_v)

            if settings_json_fl_exists == True:

                try:
                    str_txtin = self.textCtrl.GetValue()# gets the text value that within input field

                    str_tdlin = self.tdlComboBox.GetStringSelection()# gets the tdl value that from the tdl combobox

                    str_langin = self.accentComboBox.GetStringSelection()# gets the accemt value that from the accent combobox

                    audio_name_mp3 = "{0}-{1},{2}-{3}.mp3".format(str_txtin,str_langin,str_tdlin,"audio")

                    audio_full_path = os.path.join(now_date_sub_folder_v,audio_name_mp3)
                    
                    playsound(audio_full_path)

                except Exception:
                    
                    try:
                        
                        gtts_audios(text_val=str_txtin,lang_val=str_langin,tdl_val=str_tdlin,audio_root_val=audio_full_path)

                        #tmr2()
                        
                        success_made_msg =wx.MessageDialog(self.wpanel,"'{0}' text sucessfully converted into '{1}' audio file.".format(str_txtin,audio_name_mp3),"Text to audio file (.Mp3) status - Complete",wx.OK | wx.ICON_INFORMATION )

                        #tmr2()

                        success_made_msg.ShowModal()

                        tmr2(0.16)

                        playsound(audio_full_path)

                    # Active when there is no text to convert
                    except AssertionError:

                        tmr2(0.16)

                        ae_msg =wx.MessageDialog(self.wpanel,"No words to convert into audio file (.mp3)","Assertion Error: ",wx.OK | wx.ICON_ERROR)

                        ae_msg.ShowModal()

                        tmr2(0.19)

                        saltr_msg = wx.MessageDialog(self.wpanel,"Seeking alternative.....","Notify",wx.OK)

                        saltr_msg.ShowModal()

                        try:
                            r=sr.Recognizer()

                            m = sr.Microphone()

                            with m as source:
                                sr_get_notify_msg = wx.MessageDialog(self.wpanel,"You can speak now after clicking 'Ok'.","Text-2-Speech: Google-Speech Recognition (BETA)",wx.OK)

                                sr_get_notify_msg.ShowModal()

                                r.pause_threshold=2

                                audio = r.listen(source)

                            try:
                                
                                str_sr_var=r.recognize_google(audio,language="{0}-{1}".format(str_langin,str_tdlin))

                                audio_name_mp3_sr = "{0}-{1},{2}-{3}.mp3".format(str(str_sr_var),str_langin,str_tdlin,"audio")

                                audio_full_path_sr = os.path.join(now_date_sub_folder_v,audio_name_mp3_sr)

                                sr_rec_msg = wx.MessageDialog(self.wpanel,"Speech recognized..","Text-2-Speech: Google-Speech Recognition (BETA)",wx.OK)

                                sr_rec_msg.ShowModal()

                                if os.path.exists(audio_full_path_sr)==False:

                                    gtts_audios(text_val=str(str_sr_var),lang_val=str_langin,tdl_val=str_tdlin,audio_root_val=audio_full_path_sr)

                                    success_made_msg =wx.MessageDialog(self.wpanel,"'{0}' text sucessfully converted into '{1}' audio file.".format(str(str_sr_var),audio_name_mp3_sr),"Text to audio file (.Mp3) status - Complete",wx.OK | wx.ICON_INFORMATION )

                                    #tmr2()

                                    success_made_msg.ShowModal()

                                    playsound(audio_full_path_sr)

                                    tmr2(0.16)
                        
                                    if str_tdlin == self.tdl_lists[0] or str_tdlin == self.accent_lists[0]:

                                        pass

                                    else:
                                
                                        ''' Asks user whether to use the app for assurance as message box. if yes, clears the values for the user '''
                                        yn_clr_msgbox = wx.MessageDialog(self.wpanel,"Do you wish to convert another text into audio?","Clear - Yes/No",wx.YES_NO| wx.ICON_NONE)

                                        yn_clr_var = yn_clr_msgbox.ShowModal()

                                        if yn_clr_var == wx.ID_YES:

                                            #self.textCtrl.Clear()#            clears texts that exists within the input feilds

                                            self.tdlComboBox.SetValue(self.tdl_lists[0])# setting the tdl combobox back to default

                                            self.accentComboBox.SetValue(self.accent_lists[0])# setting the accent combobox back to default
                                        else:
                                            pass

                                else:
                                    
                                    #self.textCtrl.Clear()#            clears texts that exists within the input feilds
                            
                                    self.tdlComboBox.SetValue(self.tdl_lists[0])# setting the tdl combobox back to default

                                    self.accentComboBox.SetValue(self.accent_lists[0])# setting the accent combobox back to default

                                    audio_exists_msg =wx.MessageDialog(self.wpanel,"'{0}' text already converted into '{1}' audio file.".format(str(str_sr_var),audio_name_mp3_sr),"Text to audio file (.Mp3) status - Audio Exists",wx.OK | wx.ICON_INFORMATION )

                                    #tmr2()

                                    audio_exists_msg.ShowModal()    

                            except sr.UnknownValueError:

                                self.tdlComboBox.SetValue(self.tdl_lists[0])# setting the tdl combobox back to default

                                self.accentComboBox.SetValue(self.accent_lists[0])# setting the accent combobox back to default

                                sr_catch_err_msg =wx.MessageDialog(self.wpanel,"Oops! Didn't catch that.","Speech-Recognition Error: ",wx.OK | wx.ICON_ERROR)

                                sr_catch_err_msg.ShowModal()
                                    
                            except sr.RequestError:

                                self.tdlComboBox.SetValue(self.tdl_lists[0])# setting the tdl combobox back to default

                                self.accentComboBox.SetValue(self.accent_lists[0])# setting the accent combobox back to default

                                google_sr_neterr_msg =wx.MessageDialog(self.wpanel,"Opps! couldn't request results from Google Speech Recognition service at the moment. So please check the device network is online and ready.","Speech-Recognition Connection Error: ",wx.OK | wx.ICON_ERROR)

                                google_sr_neterr_msg.ShowModal()

                            # Active there is no internet connection 'google Text-to-speech' (gTTS) server
                            except gTTSError:

                                os.remove(audio_full_path_sr)

                                self.textCtrl.Clear()#            clears texts that exists within the input feilds

                                self.tdlComboBox.SetValue(self.tdl_lists[0])# setting the tdl combobox back to default

                                self.accentComboBox.SetValue(self.accent_lists[0])# setting the accent combobox back to default

                                tmr2(0.16)

                                neterr_msg =wx.MessageDialog(self.wpanel,"Opps! couldn't convert text into audio because of no internet connection at the moment. So please check the device network is online and ready.","Connection Error: ",wx.OK | wx.ICON_ERROR)

                                neterr_msg.ShowModal()

                            # Active when an error is not recognizible         
                            except:

                                os.remove(audio_full_path_sr)

                                #self.textCtrl.Clear()#            clears texts that exists within the input feilds

                                self.tdlComboBox.SetValue(self.tdl_lists[0])# setting the tdl combobox back to default

                                self.accentComboBox.SetValue(self.accent_lists[0])# setting the accent combobox back to default
                            
                                tmr2(0.16)

                                ue_msg =wx.MessageDialog(self.wpanel,"Unknown error occurred...","Error: ",wx.OK | wx.ICON_ERROR)
                                
                                ue_msg.ShowModal()

                        except KeyboardInterrupt:
                            pass 


                    # Active when there is program run time error     
                    except RuntimeError:

                        re_msg =wx.MessageDialog(self.wpanel,"Program did not function properly.","Runtime Error: ",wx.OK | wx.ICON_ERROR)

                        re_msg.ShowModal()

                        tmr2(0.16)

                        self.textCtrl.Clear()#            clears texts that exists within the input feilds

                        self.tdlComboBox.SetValue(self.tdl_lists[0])# setting the tdl combobox back to default

                        self.accentComboBox.SetValue(self.accent_lists[0])# setting the accent combobox back to default

                        self.Destroy()

                        tmr2(0.16)

                        os.startfile(os.path.basename(__file__))

                    # Active there is no internet connection 'google Text-to-speech' (gTTS) server
                    except gTTSError as err:

                        os.remove(audio_full_path)

                        self.textCtrl.Clear()#            clears texts that exists within the input feilds

                        self.tdlComboBox.SetValue(self.tdl_lists[0])# setting the tdl combobox back to default

                        self.accentComboBox.SetValue(self.accent_lists[0])# setting the accent combobox back to default

                        tmr2(0.16)

                        neterr_msg =wx.MessageDialog(self.wpanel,"Opps! couldn't convert text into audio because of no internet connection at the moment. So please check the device network is online and ready.","Connection Error: ",wx.OK | wx.ICON_ERROR)

                        neterr_msg.ShowModal()

                    # Active when an error is not recognizible         
                    except:

                        os.remove(audio_full_path)

                        self.textCtrl.Clear()#            clears texts that exists within the input feilds

                        self.tdlComboBox.SetValue(self.tdl_lists[0])# setting the tdl combobox back to default

                        self.accentComboBox.SetValue(self.accent_lists[0])# setting the accent combobox back to default
                    
                        tmr2(0.16)

                        ue_msg =wx.MessageDialog(self.wpanel,"Unknown error occurred...","Error: ",wx.OK | wx.ICON_ERROR)
                        
                        ue_msg.ShowModal()

            else:
                pass

            path_json.close()
        except FileNotFoundError:
            pass

    def open_mp3_folder_dt(self,event):

        """ Verify 'path.json' if exists or not """
        settings_json_fl_exists = os.path.exists(settings_json_fl_rt)

        if settings_json_fl_exists == False:

            dir_dlgbox = wx.DirDialog(self.wpanel,"Please choose directory (or Path):","",wx.DD_DEFAULT_STYLE | wx.DD_CHANGE_DIR)

            #dir_dlgbox.Set(wDir_path)

            if dir_dlgbox.ShowModal()==wx.ID_OK:

                usr_rt_v = dir_dlgbox.GetPath()

                settings_json = open(settings_json_fl_rt,'w')
                                
                settings_json.write("{"'"path"'":")
                                
                usr_path ={
                        "path" : str(usr_rt_v)
                                    }

                json_settings_file_datas = open(settings_json_fl_rt, "w")
                       
                json.dump(usr_path, json_settings_file_datas)

                json_settings_file_datas.close()

                settings_json.close()

                settings_path_saved_msg =wx.MessageDialog(self.wpanel,"Path saved.","Path update - Complete",wx.OK | wx.ICON_INFORMATION )

                settings_path_saved_msg.ShowModal()

            else:
                pass
        else:
            pass

        try:
            path_json = open(settings_json_fl_rt, 'r')

            data = path_json.read()

            path_infos_v = json.loads(data)["path"]

            '''  Variable AppName audio folder path '''
            app_audio_folder_v = os.path.join(path_infos_v,et_audio_app_folder_name)

            ''' Variable current year folder path '''
            now_yrs_sub_folder_v = os.path.join(app_audio_folder_v,dt_yyyy)

            ''' Variable current date folder path '''
            now_date_sub_folder_v = os.path.join(now_yrs_sub_folder_v,dt_date)

            appMp3s_foldershortcut_maker_dt(root=app_audio_folder_v,rootdt=now_date_sub_folder_v,root_yrs=now_yrs_sub_folder_v)

            os.startfile(now_date_sub_folder_v)

            path_json.close()

        except FileNotFoundError:
            pass
    def txt2Mp3(self,event):

        """ Verify 'path.json' if exists or not """
        settings_json_fl_exists = os.path.exists(settings_json_fl_rt)

        if settings_json_fl_exists == False:

            dir_dlgbox = wx.DirDialog(self.wpanel,"Please choose directory (or Path):","",wx.DD_DEFAULT_STYLE | wx.DD_CHANGE_DIR)

            #dir_dlgbox.Set(wDir_path)

            if dir_dlgbox.ShowModal()==wx.ID_OK:

                usr_rt_v = dir_dlgbox.GetPath()

                settings_json = open(settings_json_fl_rt,'w')
                                
                settings_json.write("{"'"path"'":")
                                
                usr_path ={
                        "path" : str(usr_rt_v)
                                    }

                json_settings_file_datas = open(settings_json_fl_rt, "w")
                       
                json.dump(usr_path, json_settings_file_datas)

                json_settings_file_datas.close()

                settings_json.close()

            else:
                pass
        else:
            pass

        try:
            path_json = open(settings_json_fl_rt, 'r')

            data = path_json.read()

            self.path_infos_v = json.loads(data)["path"]

            self.gtts_V()

            path_json.close()

        except FileNotFoundError:
            pass
    def gtts_V(self):

        src_path_data = self.path_infos_v

        ''' Variable AppName audio folder path '''
        app_audio_folder_v = os.path.join(src_path_data,audio_app_folder_name)

        ''' Variable current year folder path '''
        now_yrs_sub_folder_v = os.path.join(app_audio_folder_v,dt_yyyy)

        ''' Variable current date folder path '''
        now_date_sub_folder_v = os.path.join(now_yrs_sub_folder_v,dt_date)

        appMp3s_foldershortcut_maker_dt(root=app_audio_folder_v,rootdt=now_date_sub_folder_v,root_yrs=now_yrs_sub_folder_v)

        """ Verify json file if exists or not """
        settings_json_fl_exists = os.path.exists(settings_json_fl_rt)

        str_txtin = self.textCtrl.GetValue()# gets the text value that within input field

        str_tdlin = self.tdlComboBox.GetStringSelection()# gets the tdl value that from the tdl combobox

        str_langin = self.accentComboBox.GetStringSelection()# gets the accemt value that from the accent combobox

        if settings_json_fl_exists == True:
        
            try:
                
                audio_name_mp3 = "{0}-{1},{2}-{3}.mp3".format(str_txtin,str_langin,str_tdlin,"audio")

                audio_full_path = os.path.join(now_date_sub_folder_v,audio_name_mp3)
                
                if os.path.exists(audio_full_path)==False:
                   
                    gtts_audios(text_val=str_txtin,lang_val=str_langin,tdl_val=str_tdlin,audio_root_val=audio_full_path)

                    #tmr2()
                    
                    success_made_msg =wx.MessageDialog(self.wpanel,"'{0}' text sucessfully converted into '{1}' audio file.".format(str_txtin,audio_name_mp3),"Text to audio file (.Mp3) status - Complete",wx.OK | wx.ICON_INFORMATION )

                    #tmr2()

                    success_made_msg.ShowModal()

                    tmr2(0.16)

                    ''' Asks user whether to play the audio for assurance as message box. if yes, plays the audio for the user '''
                    yn_play_audio_msgbox = wx.MessageDialog(self.wpanel,"Do you wish to play the audio?","Audio player - Yes/No",wx.YES_NO| wx.ICON_NONE)

                    yn_play_audio_msgbox_val = yn_play_audio_msgbox.ShowModal()

                    if yn_play_audio_msgbox_val == wx.ID_YES:

                       playsound(audio_full_path)
                    
                    else:
                        pass

                    tmr2(0.16)

                    if str_tdlin == self.tdl_lists[0] or str_tdlin == self.accent_lists[0]:

                        pass

                    else:
                
                        ''' Asks user whether to use the app for assurance as message box. if yes, clears the values for the user '''
                        yn_clr_msgbox = wx.MessageDialog(self.wpanel,"Do you wish to convert another text into audio?","Clear - Yes/No",wx.YES_NO| wx.ICON_NONE)

                        yn_clr_var = yn_clr_msgbox.ShowModal()

                        if yn_clr_var == wx.ID_YES:

                            #self.textCtrl.Clear()#            clears texts that exists within the input feilds

                            self.tdlComboBox.SetValue(self.tdl_lists[0])# setting the tdl combobox back to default

                            self.accentComboBox.SetValue(self.accent_lists[0])# setting the accent combobox back to default
                        else:
                            pass
                else:

                    self.textCtrl.Clear()#            clears texts that exists within the input feilds
        
                    self.tdlComboBox.SetValue(self.tdl_lists[0])# setting the tdl combobox back to default

                    self.accentComboBox.SetValue(self.accent_lists[0])# setting the accent combobox back to default

                    audio_exists_msg =wx.MessageDialog(self.wpanel,"'{0}' text already converted into '{1}' audio file.".format(str_txtin,audio_name_mp3),"Text to audio file (.Mp3) status - Audio Exists",wx.OK | wx.ICON_INFORMATION )

                    #tmr2()

                    audio_exists_msg.ShowModal()

            # Active when there is no text to convert
            except AssertionError:

                tmr2(0.16)

                #self.textCtrl.Clear()#            clears texts that exists within the input feilds

                #self.tdlComboBox.SetValue(self.tdl_lists[0])# setting the tdl combobox back to default

                #self.accentComboBox.SetValue(self.accent_lists[0])# setting the accent combobox back to default

                ae_msg =wx.MessageDialog(self.wpanel,"No words to convert into audio file (.mp3)","Assertion Error: ",wx.OK | wx.ICON_ERROR)

                ae_msg.ShowModal()

                tmr2(0.19)

                saltr_msg = wx.MessageDialog(self.wpanel,"Seeking alternative.....","Notify",wx.OK)

                saltr_msg.ShowModal()

                try:
                    r=sr.Recognizer()

                    m = sr.Microphone()

                    with m as source:
                        sr_get_notify_msg = wx.MessageDialog(self.wpanel,"You can speak now after clicking 'Ok'.","Text-2-Speech: Google-Speech Recognition (BETA)",wx.OK)

                        sr_get_notify_msg.ShowModal()

                        r.pause_threshold=2

                        audio = r.listen(source)

                    try:
                        
                        str_sr_var=r.recognize_google(audio,language="{0}-{1}".format(str_langin,str_tdlin))

                        audio_name_mp3_sr = "{0}-{1},{2}-{3}.mp3".format(str(str_sr_var),str_langin,str_tdlin,"audio")

                        audio_full_path_sr = os.path.join(now_date_sub_folder_v,audio_name_mp3_sr)

                        sr_rec_msg = wx.MessageDialog(self.wpanel,"Speech recognized..","Text-2-Speech: Google-Speech Recognition (BETA)",wx.OK)

                        sr_rec_msg.ShowModal()

                        if os.path.exists(audio_full_path_sr)==False:

                            gtts_audios(text_val=str(str_sr_var),lang_val=str_langin,tdl_val=str_tdlin,audio_root_val=audio_full_path_sr)

                            success_made_msg =wx.MessageDialog(self.wpanel,"'{0}' text sucessfully converted into '{1}' audio file.".format(str(str_sr_var),audio_name_mp3_sr),"Text to audio file (.Mp3) status - Complete",wx.OK | wx.ICON_INFORMATION )

                            #tmr2()

                            success_made_msg.ShowModal()

                            ''' Asks user whether to play the audio for assurance as message box. if yes, plays the audio for the user '''
                            yn_play_audio_msgbox = wx.MessageDialog(self.wpanel,"Do you wish to play the audio?","Audio player - Yes/No",wx.YES_NO| wx.ICON_NONE)

                            yn_play_audio_msgbox_val = yn_play_audio_msgbox.ShowModal()

                            if yn_play_audio_msgbox_val == wx.ID_YES:

                                playsound(audio_full_path_sr)
                            
                            else:
                                pass

                            tmr2(0.16)
                
                            if str_tdlin == self.tdl_lists[0] or str_tdlin == self.accent_lists[0]:

                                pass

                            else:
                        
                                ''' Asks user whether to use the app for assurance as message box. if yes, clears the values for the user '''
                                yn_clr_msgbox = wx.MessageDialog(self.wpanel,"Do you wish to convert another text into audio?","Clear - Yes/No",wx.YES_NO| wx.ICON_NONE)

                                yn_clr_var = yn_clr_msgbox.ShowModal()

                                if yn_clr_var == wx.ID_YES:

                                    #self.textCtrl.Clear()#            clears texts that exists within the input feilds

                                    self.tdlComboBox.SetValue(self.tdl_lists[0])# setting the tdl combobox back to default

                                    self.accentComboBox.SetValue(self.accent_lists[0])# setting the accent combobox back to default
                                else:
                                    pass

                        else:
                            
                            #self.textCtrl.Clear()#            clears texts that exists within the input feilds
                    
                            self.tdlComboBox.SetValue(self.tdl_lists[0])# setting the tdl combobox back to default

                            self.accentComboBox.SetValue(self.accent_lists[0])# setting the accent combobox back to default

                            audio_exists_msg =wx.MessageDialog(self.wpanel,"'{0}' text already converted into '{1}' audio file.".format(str(str_sr_var),audio_name_mp3_sr),"Text to audio file (.Mp3) status - Audio Exists",wx.OK | wx.ICON_INFORMATION )

                            #tmr2()

                            audio_exists_msg.ShowModal()    

                    except sr.UnknownValueError:

                        self.tdlComboBox.SetValue(self.tdl_lists[0])# setting the tdl combobox back to default

                        self.accentComboBox.SetValue(self.accent_lists[0])# setting the accent combobox back to default

                        sr_catch_err_msg =wx.MessageDialog(self.wpanel,"Oops! Didn't catch that.","Speech-Recognition Error: ",wx.OK | wx.ICON_ERROR)

                        sr_catch_err_msg.ShowModal()
                            
                    except sr.RequestError:

                        self.tdlComboBox.SetValue(self.tdl_lists[0])# setting the tdl combobox back to default

                        self.accentComboBox.SetValue(self.accent_lists[0])# setting the accent combobox back to default

                        google_sr_neterr_msg =wx.MessageDialog(self.wpanel,"Opps! couldn't request results from Google Speech Recognition service at the moment. So please check the device network is online and ready.","Speech-Recognition Connection Error: ",wx.OK | wx.ICON_ERROR)

                        google_sr_neterr_msg.ShowModal()

                    # Active there is no internet connection 'google Text-to-speech' (gTTS) server
                    except gTTSError:

                        os.remove(audio_full_path_sr)

                        #self.textCtrl.Clear()#            clears texts that exists within the input feilds

                        self.tdlComboBox.SetValue(self.tdl_lists[0])# setting the tdl combobox back to default

                        self.accentComboBox.SetValue(self.accent_lists[0])# setting the accent combobox back to default

                        tmr2(0.16)

                        neterr_msg =wx.MessageDialog(self.wpanel,"Opps! couldn't convert text into audio because of no internet connection at the moment. So please check the device network is online and ready.","Connection Error: ",wx.OK | wx.ICON_ERROR)

                        neterr_msg.ShowModal()

                    # Active when an error is not recognizible         
                    except:

                        os.remove(audio_full_path_sr)

                        #self.textCtrl.Clear()#            clears texts that exists within the input feilds

                        self.tdlComboBox.SetValue(self.tdl_lists[0])# setting the tdl combobox back to default

                        self.accentComboBox.SetValue(self.accent_lists[0])# setting the accent combobox back to default
                    
                        tmr2(0.16)

                        ue_msg =wx.MessageDialog(self.wpanel,"Unknown error occurred...","Error: ",wx.OK | wx.ICON_ERROR)
                        
                        ue_msg.ShowModal()

                except KeyboardInterrupt:
                    pass 


            # Active when there is program run time error     
            except RuntimeError:

                re_msg =wx.MessageDialog(self.wpanel,"Program did not function properly.","Runtime Error: ",wx.OK | wx.ICON_ERROR)

                re_msg.ShowModal()

                tmr2(0.16)

                self.textCtrl.Clear()#            clears texts that exists within the input feilds

                self.tdlComboBox.SetValue(self.tdl_lists[0])# setting the tdl combobox back to default

                self.accentComboBox.SetValue(self.accent_lists[0])# setting the accent combobox back to default

                self.Destroy()

                tmr2(0.16)

                os.startfile(os.path.basename(__file__))

            # Active there is no internet connection 'google Text-to-speech' (gTTS) server
            except gTTSError:

                os.remove(audio_full_path)

                self.textCtrl.Clear()#            clears texts that exists within the input feilds

                self.tdlComboBox.SetValue(self.tdl_lists[0])# setting the tdl combobox back to default

                self.accentComboBox.SetValue(self.accent_lists[0])# setting the accent combobox back to default

                tmr2(0.16)

                neterr_msg =wx.MessageDialog(self.wpanel,"Opps! couldn't convert text into audio because of no internet connection at the moment. So please check the device network is online and ready.","Connection Error: ",wx.OK | wx.ICON_ERROR)

                neterr_msg.ShowModal()

            # Active when an error is not recognizible         
            except:

                os.remove(audio_full_path)

                self.textCtrl.Clear()#            clears texts that exists within the input feilds

                self.tdlComboBox.SetValue(self.tdl_lists[0])# setting the tdl combobox back to default

                self.accentComboBox.SetValue(self.accent_lists[0])# setting the accent combobox back to default
            
                tmr2(0.16)

                ue_msg =wx.MessageDialog(self.wpanel,"Unknown error occurred...","Error: ",wx.OK | wx.ICON_ERROR)
                
                ue_msg.ShowModal()

        else:
            pass

    def exitbutton(self,event):
        ''' Asks user whether to use again as message box. if not, clears the values for the user, or exits the app if yes  '''
        yn_msgbox = wx.MessageDialog(self.wpanel,"Are you sure you want to exit the app?","Yes/No",wx.YES_NO| wx.ICON_WARNING)

        yn_var = yn_msgbox.ShowModal()

        if yn_var == wx.ID_NO:

            self.textCtrl.Clear()#            clears texts that exists within the input feilds
       
            self.tdlComboBox.SetValue(self.tdl_lists[0])# setting the tdl combobox back to default

            self.accentComboBox.SetValue(self.accent_lists[0])# setting the accent combobox back to default
        
        else:
            self.Destroy()# closes app when 'EXIT' button is click

    def Close(self,event):
        self.Destroy()# closes app  when 'CLOSE' or 'X' on the window is pressed

    def rst(self,event):
        self.textCtrl.Clear()#            clears texts that exists within the input feilds

        self.tdlComboBox.SetValue(self.tdl_lists[0])# setting the tdl combobox back to default

        self.accentComboBox.SetValue(self.accent_lists[0])# setting the accent combobox back to default

if __name__=='__main__':

    app=wx.App()# Start the app

    frame = app_ui(parent=None,id=-1)# Gives parametres or infos to the class or 'Frame' components

    frame.Show()# Shows the commponents existed within the app

    app.MainLoop()# loops the window as systems close apps within milliseconds or more
