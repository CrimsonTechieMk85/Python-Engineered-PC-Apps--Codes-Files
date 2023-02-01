''' importing prefrences or getting required datas from the modules'''
import os  # for file and folder operation

import time  # for 'time-delays' activities

import wx  # for GUI apps using 'Wxpython'

from playsound import playsound# for playing audio files

import winshell# mimic windows powershell activities

from win32com.client import Dispatch# Creates a Dispatch based COM object using win32 modules

import datetime# getting real-time datas of today

from gtts import gTTS# using google-text-to-speech (gtts) service

import wikipedia# wikia operations

import webbrowser

import os

import psutil

import json
'''Source files'''
wDir_path = os.path.dirname(os.path.realpath(__file__))# curent working directory or the 'Now'-location of the file.

wDir_path = os.getcwd()
#icon source image file -> eg: 'image_file_name'.ico
for file in os.listdir(wDir_path):
    if '.ico' in file:
        #pass
        try:
            ico_flpath = os.path.join(wDir_path,f)
        except FileNotFoundError:
            pass
    else:
        pass
'''File name & File extension'''
file_name, file_type = os.path.splitext(os.path.basename(os.path.realpath(__file__)))

#browser_path_jsonsrc = '"C:\Program Files\Google\Chrome\Application\edge.exe"'

#browser_path_jsonsrc_incognito = '{} %s -incognito'.format(browser_path_jsonsrc)

# settings json file and folders
#dependies_folder_root=os.path.join(wDir_path,".datas") 

#settings_folder_path=os.path.join(dependies_folder_root,"settings")

# browser path json files
browser_path_jsonfl_name = "Operabrowser_paths"

browser_path_json = "{}.json".format(browser_path_jsonfl_name)

browser_path_json_srcfl=os.path.join(wDir_path,browser_path_json)

# browser mode json files
browser_modes_jsonfl_name = "Operabrowser_modes"

browser_modes_json = "{}.json".format(browser_modes_jsonfl_name)

mode_lsts = ['Google','Google images','YouTube videos','YouTube channels','Wikipedia','Amazon products','Flipkart products','Myntra products','Ajio products']

browser_modes_json_srcfl=os.path.join(wDir_path,browser_modes_json)

main_app_title = "Search-Online (ver.Opera-A1) Perfected.Even.Further++"

def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process

    exe = os.path.basename(processName)
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if exe in proc.name():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def timerDelay2(float):
    time.sleep(float)# time delay seconnds for each sequence or activities

# using 'class' or "blueprint" to extract all the 'frame' supports existing within the 'wx' module for GUI apps
class AppUi(wx.Frame):

    # Starts frame upon user request or 'CLICKING' the app  
    def __init__(self,parent,id):
        
        # Window (Frame) with parametres i.e (frame, parent=None,id=-1.'window title',size=(int,int),style=wx.(obj))
        wx.Frame.__init__(self,parent,id,main_app_title, size=(657,563),style = wx.DEFAULT_FRAME_STYLE & ~wx.MAXIMIZE_BOX ^ wx.RESIZE_BORDER)

        try:
            self.SetIcon(wx.Icon(ico_flpath))# sets icon on the window title bar
        except NameError:
            pass

        self.wpanel = wx.Panel(self)# setting 'container' to have wxpython GUI parts

        self.wpanel.SetBackgroundColour('Steel Blue')# sets the panel or app background

    #Text

        # creates fonts for 'Text' input field
        lblfont = wx.Font(22, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        ## label text 

        self.custom_txt_lbl = wx.StaticText(self.wpanel,-1,"Search:",(33,38),(24,24),wx.TEXT_ALIGNMENT_CENTRE)

        self.custom_txt_lbl.SetFont(lblfont)# sets font for the 'Text' label using variable 'textfieldfont'

        self.custom_txt_lbl.SetForegroundColour('White')# sets the 'Text' label text colour as red

        self.custom_txt_lbl.SetBackgroundColour('Indian Red')# sets the 'Text' label colour as white

        # text input field font
        textfieldfont = wx.Font(22, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) 

        # creates text input field
        self.textCtrl = wx.TextCtrl(self.wpanel, pos=(152,35),size =(462,34), style = wx.TE_HT_ON_TEXT &~ wx.TEXT_ALIGNMENT_JUSTIFIED &~ wx.TE_WORDWRAP)

        self.textCtrl.SetFont(textfieldfont)#sets font for the text input field using variable 'textfieldfont'

        self.textCtrl.SetForegroundColour('Red')#sets input field text as red

        self.textCtrl.SetToolTip('Type here.')

    # type combobox

        # creates fonts for modes
        type_lists_font = wx.Font(22, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) 
        type_lbl_font = wx.Font(22, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) 
        ## label accent  

        # creates  'Select accent' label appear on the panel  
        self.typelbl = wx.StaticText(self.wpanel, -1, "Select:", (31, 106),(24,24))# 

        self.typelbl.SetFont(type_lbl_font)# sets 'Select accent:" label fonts uing parameters from 'accentfont' variable 

        self.typelbl.SetForegroundColour('White')# sets the 'Select accent:' label text colour as white

        self.typelbl.SetBackgroundColour('Black')# sets the 'Select accent:' label colour as 'Black' 

        # collection or lists conataining accent items
        self.type_lists = ['Google','Google images','YouTube videos'
            ,'YouTube channels','Wikipedia','Amazon products',
            'Flipkart products','Myntra products','Ajio products' ,
            'Gelbooru gallery search','Rule 34 gallery search']
        
        self.typecomboBox = wx.ComboBox(self.wpanel, -1, 'Google', (156, 103),(321,34),self.type_lists, wx.CB_READONLY | wx.ALIGN_CENTER)

        self.typecomboBox.SetFont(type_lists_font)# sets fonts for the accent items containing in the 'acccent' combobox

        self.typecomboBox.SetForegroundColour('Blue')

        #self.typecomboBox.SetBackgroundColour('Light Orange')

        self.typecomboBox.SetToolTip('Select any type of information youa are searching for.')

    #Search button
 
        # creates fonts for click button
        btn_search_font = wx.Font(21, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) 

        # combines 'Exit' button with its functions
        self.search_btn = wx.Button(self.wpanel,label='Search',pos=(67,188+45),size=(156,45),style=wx.BORDER_RAISED)

        self.search_btn.SetFont(btn_search_font)# sets 'Click here' button font using variable 'btn_click_font'

        self.search_btn.SetForegroundColour('White')# sets 'Click here' button text as white

        self.search_btn.SetBackgroundColour('Dark Green')# sets 'Click here' button as dark green

        self.search_btn.SetToolTip("Click here to search in browser.")

        #self.wbtn.SetForegroundColour('Black')

        #self.Bind(wx.EVT_STC,self.print)

        self.Bind(wx.EVT_BUTTON,self.onlineSearch,self.search_btn)# combines 'Click here' button with its functions

    #Exit button

        # creates fonts for exit button
        btn_exit_font = wx.Font(21, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)# Creates  fonts for 'Exit' button 

        # Exit button 
        # creates  'Exit' button  
        self.exit_btn = wx.Button(self.wpanel,label='Exit',pos=(67,376),size=(156,45),style=wx.BORDER_RAISED)

        self.exit_btn.SetFont(btn_exit_font)# sets font for the exit button using variable 'btn_exit_font'

        self.exit_btn.SetForegroundColour('White')# sets 'Exit' button text as white

        self.exit_btn.SetBackgroundColour('Red')# sets 'Exit' button coloer as red

        self.exit_btn.SetToolTip('Click here to exit the app.')

        self.Bind(wx.EVT_BUTTON,self.exitbutton,self.exit_btn)# combines 'Exit' button with its functions


    #Incognito search button

        # creates fonts for exit button
        btn_incognito_font = wx.Font(21, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)# Creates  fonts for 'Exit' button 

        # Exit button 
        # creates  'Exit' button  
        self.incognito_btn = wx.Button(self.wpanel,label='Search (incognito)',pos=(201,304),size=(256,45),style=wx.BORDER_RAISED)

        self.incognito_btn.SetFont(btn_incognito_font)# sets font for the exit button using variable 'btn_exit_font'

        self.incognito_btn.SetForegroundColour('Black')# sets 'Exit' button text as white

        self.incognito_btn.SetBackgroundColour('Yellow')# sets 'Exit' button coloer as red

        self.incognito_btn.SetToolTip('Click here to search in incognito browser.')

        self.Bind(wx.EVT_BUTTON,self.onlineSearchprivate,self.incognito_btn)# combines 'Exit' button with its functions

    #Reset button

        # creates fonts for reset button
        btn_rst_font = wx.Font(21, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)# Creates  fonts for 'Reset' button 

        # reset button 

        # creates  'Reset' button  
        self.rst_btn = wx.Button(self.wpanel,label='Reset',pos=(412,233),size=(156,45),style=wx.BORDER_RAISED)

        self.rst_btn.SetFont(btn_rst_font)# sets font for the exit button using variable 'btn_rst_font'

        self.rst_btn.SetForegroundColour('White')# sets 'Reset' button text as white

        self.rst_btn.SetBackgroundColour('Purple')# sets 'Reset' button coloer as Purple

        self.rst_btn.SetToolTip('Click here to set everything to default.')

        self.Bind(wx.EVT_BUTTON,self.rst,self.rst_btn)# combines 'Reset' button with its functions

    # Modify button

        btn_mod_font = wx.Font(21, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)# Creates  fonts for 'Reset' button 

        # reset button 

        # creates  'Modify' button  
        self.modify_btn = wx.Button(self.wpanel,label='Modify',pos=(412,376),size=(156,45),style=wx.BORDER_RAISED)

        self.modify_btn.SetFont(btn_mod_font)# sets font for the exit button using variable 'btn_rst_font'

        self.modify_btn.SetForegroundColour('White')# sets 'Reset' button Text as white

        self.modify_btn.SetBackgroundColour('Blue')# sets 'Reset' button coloer as Blue

        self.modify_btn.SetToolTip("Click here to change browser path.")

        self.Bind(wx.EVT_BUTTON,self.modify,self.modify_btn)# combines 'Reset' button with its functions

    # close window button

        self.Bind(wx.EVT_CLOSE,self.Close)# combines 'X' window button with its functions

    def restrt(self):

        self.Destroy()
            
        app = wx.App()

        encrypt_window = AppUi(parent=None,id=-1)

        encrypt_window.Show()

        app.MainLoop()
    

    def onlineSearchprivate(self,event):
        
        json_file_exists = os.path.exists(browser_path_json_srcfl)

        if json_file_exists is False:

            while True:
             
                self.browser_path_in = wx.TextEntryDialog(self,"Please paste the browser path: ","Bowser path regsistry")
                    
                if self.browser_path_in.ShowModal() == wx.ID_OK:

                    browser_path_in = str(self.browser_path_in.GetValue()).replace('"','')

                    if browser_path_in !="":

                        #uipath_bot_rt = r"C:\Users\{0}\AppData\Local\UiPath\app-{1}\UiRobot.exe".format(username,version_in)
                        
                        if os.path.exists(browser_path_in)==True and 'opera' in browser_path_json_srcfl:
                            
                            settings_json = open(browser_path_json_srcfl,'w')
                            
                            settings_json.write("{"'"browser_path"'":")
                            
                            UiPath_appvernos ={
                                    "browser_path" : browser_path_in
                                }
                            
                            with open(browser_path_json_srcfl, "w") as json_settings_file_datas:
                                json.dump(UiPath_appvernos, json_settings_file_datas)

                            json_settings_file_datas.close()

                            settings_json.close()

                            data_transfer_msg_box = wx.MessageDialog(None,"Data transferred...","{} - info".format(file_name),wx.ICON_INFORMATION| wx.STAY_ON_TOP)
                                        
                            data_transfer_msg_box.ShowModal()

                            break

                        else:

                            browser_path_exists_err = wx.MessageDialog(None,"Opps! Sorry coundn't save the requested browser path since it is not found in the system.","{} - browser path updation error".format(file_name),wx.ICON_ERROR| wx.STAY_ON_TOP)
                        
                            browser_path_exists_err.ShowModal()

                    else:
                        invalid_err = wx.MessageDialog(None,"Input invalid.","{} - input verifier error".format(file_name),wx.ICON_ERROR| wx.STAY_ON_TOP)
                        
                        invalid_err.ShowModal()

                else:
                    break

        else:
            pass

        q = self.textCtrl.GetValue()# gets the text value that within input field

        if q == "":
            ae_msg =wx.MessageDialog(self.wpanel,"No words to search on the internet.","Invalid request Error: ",wx.OK | wx.ICON_ERROR)

            ae_msg.ShowModal()

            timerDelay2(1.2)

            self.textCtrl.Clear()#            clears texts that exists within the input feilds

            #self.modeComboBox.SetValue(self.type_lists[0])# setting the type combobox back to default

            #self.concealcombobox.SetValue(self.yn_lists[0])# setting the Yes\No combobox back to default
        else:

            str_type = self.typecomboBox.GetStringSelection()# gets the types value  from the combobox
            
            #incognito_q = self.concealcombobox.GetStringSelection()# gets the incognito? Yes\No

            #timerDelay2(1.2)

            try:
                json_fl_read = open(browser_path_json_srcfl,'r')

                data = json_fl_read.read()

                browser_path_jsonsrc = json.loads(data)["browser_path"]

                incognito_browser_open_cmd = r'"{}" --private %s'.format(browser_path_jsonsrc)

                incognito_browser_open = r'"{}" --incognito'.format(browser_path_jsonsrc)

                if os.path.exists(browser_path_jsonsrc)==True and "opera" in browser_path_jsonsrc :

                    if "Google images" in str_type:

                        g_Img_private = f'https://www.google.com/search?q={q}&hl=en&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi6v8SR0KPpAhUh63MBHXQPBwsQ_AUoBHoECBgQBg'

                        timerDelay2(1.2)

                        #os.startfile(browser_path_jsonsrc)

                        #os.startfile('https://www.google.com')

                        #os.startfile('"C:\Program Files\Google\Chrome\Application\chrome.exe"')

                        #os.startfile("'{}' --incognito".format(browser_path_jsonsrc))

                        #os.system(r''+browser_path_jsonsrc)

                        import subprocess

                        #subprocess.call(browser_path_jsonsrc)

                        if checkIfProcessRunning(browser_path_jsonsrc):
                            print('Yes a opera process was running')
                            #os.system(browser_path_jsonsrc)

                        else:
                            print('No opera process was running')

                        #subprocess.Popen([browser_path_jsonsrc, '-incognito'])

                        wb = webbrowser.get(incognito_browser_open_cmd)

                        wb.open_new_tab(g_Img_private)

                        #wx.BeginBusyCursor()

                        #wx.EndBusyCursor()

                    elif "Google" in str_type:

                        g_srch_private = f"https://www.google.com/search?q={q}"

                        timerDelay2(1.2)

                        #os.startfile(g_srch)

                        wb = webbrowser.get(incognito_browser_open_cmd)

                        wb.open(g_srch_private)

                    elif "Gelbooru" in str_type:

                        srch_gelbooru_private = f"https://gelbooru.com/index.php?page=post&s=list&tags={q}"

                        wb = webbrowser.get(incognito_browser_open_cmd)
                        wb.open(srch_gelbooru_private)

                    elif "Rule 34" in str_type:

                        srch_rule34_private = f"https://rule34.us/index.php?r=posts/index&q={q}"

                        wb = webbrowser.get(incognito_browser_open_cmd)
                        wb.open(srch_rule34_private)

                    elif "YouTube videos" in str_type:

                        v_yt_private = f'https://www.youtube.com/results?search_query={q}'

                        timerDelay2(1.2)

                        #os.startfile(g_Yt)

                        wb = webbrowser.get(incognito_browser_open_cmd)
                        wb.open(v_yt_private)

                    elif "Amazon" in str_type:

                        amazon_link_private = f'https://www.amazon.in/s?k={q}&crid=2S55AVQK41W&sprefix=p%2Caps%2C351&ref=nb_sb_ss_ts-doa-p_4_1'

                        timerDelay2(1.2)

                        #os.startfile(amazon_link)

                        wb = webbrowser.get(incognito_browser_open_cmd)
                        wb.open(amazon_link_private)

                    elif "Ajio" in str_type:

                        ajio_links_private = f'https://www.ajio.com/search/?text={q}'

                        timerDelay2(1.2)

                        #os.startfile(ajio_links)

                        wb = webbrowser.get(incognito_browser_open_cmd)
                        wb.open(ajio_links_private)

                    elif "Myntra" in str_type:

                        myntra_links_private = f'https://www.myntra.com/{q}'

                        timerDelay2(1.2)

                        #os.startfile(myntra_links)

                        wb = webbrowser.get(incognito_browser_open_cmd)
                        wb.open(myntra_links_private)

                    elif "Flipkart" in str_type:

                        flipkart_links_private = f'https://www.flipkart.com/search?q={q}'

                        timerDelay2(1.2)

                        #os.startfile(flipkart_links)

                        wb = webbrowser.get(incognito_browser_open_cmd)
                        wb.open(flipkart_links_private)

                    elif "Wikipedia" in  str_type :

                        results = wikipedia.summary(q, sentences= 3)

                        timerDelay2(1.2)

                        results_msg = wx.MessageDialog(self.wpanel,results,"Wiki results:",wx.OK)

                        results_msg.ShowModal()

                    else:

                        YouTube_ch_private = f'https://www.youtube.com/{q}'

                        timerDelay2(1.2)

                        #os.startfile(YouTube_ch)

                        wb = webbrowser.get(incognito_browser_open_cmd)
                        wb.open(YouTube_ch_private)


                    #wx.BeginBusyCursor()

                    #wx.EndBusyCursor()

                    timerDelay2(1.1)

                    ''' Asks user whether to clear for assurance as message box. if yes, clears the values for the user, or exits the app if no  '''
                    yn_msgbox = wx.MessageDialog(self.wpanel,"Do you wish to search again?","Yes/No",wx.YES_NO| wx.ICON_NONE)

                    yn_var = yn_msgbox.ShowModal()

                    if yn_var == wx.ID_YES:

                        self.textCtrl.Clear()#            clears texts that exists within the input fields

                        self.typecomboBox.SetValue(self.type_lists[0])# setting the mode combobox back to default

                        #self.concealcombobox.SetValue(self.yn_lists[0])# setting the Yes\No combobox back to default

                else:
                    browser_err_msgbox = wx.MessageDialog(self.wpanel,"Browser not found.","Browser Availability error:",wx.OK| wx.ICON_ERROR)

                    browser_err_msgbox.ShowModal()

                    self.textCtrl.Clear()#            clears texts that exists within the input feilds

                    self.typecomboBox.SetValue(self.type_lists[0])# setting the mode combobox back to default

                    #self.concealcombobox.SetValue(self.yn_lists[0])# setting the Yes\No combobox back to default

            except FileNotFoundError:
                pass
    def onlineSearch(self,event):

        json_file_exists = os.path.exists(browser_path_json_srcfl)

        if json_file_exists is False :

            while True:

                self.browser_path_in = wx.TextEntryDialog(self,"Please paste the browser path: ","Bowser path regsistry")

                if self.browser_path_in.ShowModal() == wx.ID_OK:

                    browser_path_in = str(self.browser_path_in.GetValue()).replace('"','')

                    if browser_path_in !="":

                        #uipath_bot_rt = r"C:\Users\{0}\AppData\Local\UiPath\app-{1}\UiRobot.exe".format(username,version_in)

                        if os.path.exists(browser_path_in)==True:

                            settings_json = open(browser_path_json_srcfl,'w')

                            settings_json.write("{"'"browser_path"'":")

                            UiPath_appvernos ={
                                    "browser_path" : browser_path_in
                                }

                            with open(browser_path_json_srcfl, "w") as json_settings_file_datas:
                                json.dump(UiPath_appvernos, json_settings_file_datas)

                            json_settings_file_datas.close()

                            settings_json.close()

                            data_transfer_msg_box = wx.MessageDialog(None,"Data transferred...","{} - info".format(file_name),wx.ICON_INFORMATION| wx.STAY_ON_TOP)

                            data_transfer_msg_box.ShowModal()

                            break

                        else:

                            browser_path_exists_err = wx.MessageDialog(None,"Opps! Sorry coundn't save the requested browser path since it is not found in the system.","{} - browser path updation error".format(file_name),wx.ICON_ERROR| wx.STAY_ON_TOP)

                            browser_path_exists_err.ShowModal()

                    else:
                        invalid_err = wx.MessageDialog(None,"Input invalid.","{} - input verifier error".format(file_name),wx.ICON_ERROR| wx.STAY_ON_TOP)

                        invalid_err.ShowModal()

                else:
                    break

        else:
            pass

        q = self.textCtrl.GetValue()# gets the text value that within input field

        if q == "":
            ae_msg =wx.MessageDialog(self.wpanel,"No words to search on the internet.","Invalid request Error: ",wx.OK | wx.ICON_ERROR)

            ae_msg.ShowModal()

            timerDelay2(1.2)

            self.textCtrl.Clear()#            clears texts that exists within the input feilds

            #self.modeComboBox.SetValue(self.type_lists[0])# setting the type combobox back to default

            #self.concealcombobox.SetValue(self.yn_lists[0])# setting the Yes\No combobox back to default
        else:

            str_type = self.typecomboBox.GetStringSelection()# gets the types value  from the combobox

            ##incognito_q = self.concealcombobox.GetStringSelection()# gets the incognito? Yes\No

            #timerDelay2(1.2)

            try:

                json_fl_read = open(browser_path_json_srcfl,'r')

                data = json_fl_read.read()

                browser_path_jsonsrc = str(json.loads(data)["browser_path"])

                browser_open_cmd = '"{}" %s'.format(browser_path_jsonsrc)

                if os.path.exists(browser_path_jsonsrc)==True and "opera" in browser_path_jsonsrc:

                    if "Google images" in str_type:

                        g_Img = f'https://www.google.com/search?q={q}&hl=en&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi6v8SR0KPpAhUh63MBHXQPBwsQ_AUoBHoECBgQBg'

                        timerDelay2(1.2)

                        #os.startfile(g_Img)

                        wb = wb = webbrowser.get(browser_open_cmd)
                        wb.open(g_Img)

                        #wx.BeginBusyCursor()

                        #wx.EndBusyCursor()

                    elif "Google" in str_type:
                                
                        g_srch = f"https://www.google.com/search?q={q}"
                                
                        timerDelay2(1.2)

                        #os.startfile(g_srch)

                    # wb = webbrowser.get(browser_path_jsonsrc).open(g_srch)
                        wb = wb = webbrowser.get(browser_open_cmd)
                        
                        wb.open(g_srch)
                    elif "YouTube videos" in str_type:

                        v_yt = f'https://www.youtube.com/results?search_query={q}'

                        timerDelay2(1.2)

                        #os.startfile(g_Yt)

                        wb = wb = webbrowser.get(browser_open_cmd)
                        
                        wb.open(v_yt)

                    elif "Amazon" in str_type:

                        amazon_link = f'https://www.amazon.in/s?k={q}&crid=2S55AVQK41W&sprefix=p%2Caps%2C351&ref=nb_sb_ss_ts-doa-p_4_1'

                        timerDelay2(1.2)

                        #os.startfile(amazon_link)

                        wb = webbrowser.get(browser_open_cmd)
                        wb.open(amazon_link)

                    elif "Ajio" in str_type:

                        ajio_links = f'https://www.ajio.com/search/?text={q}'

                        timerDelay2(1.2)

                        #os.startfile(ajio_links)

                        wb = webbrowser.get(browser_open_cmd)
                        wb.open(ajio_links)

                    elif "Myntra" in str_type:

                        myntra_links = f'https://www.myntra.com/{q}'

                        timerDelay2(1.2)

                        #os.startfile(myntra_links)

                        wb = webbrowser.get(browser_open_cmd)
                        wb.open(myntra_links)

                    elif "Flipkart" in str_type:

                        flipkart_links = f'https://www.flipkart.com/search?q={q}'

                        timerDelay2(1.2)

                        #os.startfile(flipkart_links)

                        wb = webbrowser.get(browser_open_cmd)
                        wb.open(flipkart_links)

                    elif "Wikipedia" in  str_type :                          

                        results = wikipedia.summary(q, sentences= 3)

                        timerDelay2(1.2)

                        results_msg = wx.MessageDialog(self.wpanel,results,"Wiki results:",wx.OK)

                        results_msg.ShowModal()

                    else:
        
                        YouTube_ch = f'https://www.youtube.com/{q}'
        
                        timerDelay2(1.2)

                        #os.startfile(YouTube_ch)

                        wb = webbrowser.get(browser_open_cmd)
                        wb.open(YouTube_ch)

                    timerDelay2(1.1)

                    ''' Asks user whether to clear for assurance as message box. if yes, clears the values for the user, or exits the app if no  '''
                    yn_msgbox = wx.MessageDialog(self.wpanel,"Do you wish to search again?","Yes/No",wx.YES_NO| wx.ICON_NONE)

                    yn_var = yn_msgbox.ShowModal()

                    if yn_var == wx.ID_YES:

                        self.textCtrl.Clear()#            clears texts that exists within the input fields

                        self.typecomboBox.SetValue(self.type_lists[0])# setting the mode combobox back to default

                        #self.concealcombobox.SetValue(self.yn_lists[0])# setting the Yes\No combobox back to default
            
                else:
                    browser_err_msgbox = wx.MessageDialog(self.wpanel,"Browser not found.","Browser Availability error:",wx.OK| wx.ICON_ERROR)

                    browser_err_msgbox.ShowModal()

                    self.textCtrl.Clear()#            clears texts that exists within the input feilds
        
                    self.typecomboBox.SetValue(self.type_lists[0])# setting the mode combobox back to default

                    #self.concealcombobox.SetValue(self.yn_lists[0])# setting the Yes\No combobox back to default
                
            except FileNotFoundError:
                pass

    def exitbutton(self,event):
        ''' Asks user whether to use again as message box. if not, clears the values for the user, or exits the app if yes  '''
        yn_msgbox = wx.MessageDialog(self.wpanel,"Are you sure you want to exit the app?","Yes/No",wx.YES_NO| wx.ICON_WARNING)

        yn_var = yn_msgbox.ShowModal()

        if yn_var == wx.ID_NO:

            self.textCtrl.Clear()#            clears texts that exists within the input feilds
       
            self.typecomboBox.SetValue(self.type_lists[0])# setting the mode combobox back to default

            #self.concealcombobox.SetValue(self.yn_lists[0])# setting the Yes\No combobox back to default
        
        else:
            self.Destroy()# closes app when 'EXIT' button is click

    def Close(self,event):
        self.Destroy()# closes app  when 'CLOSE' or 'X' on the window is pressed

    def modify(self,event):

        while True:

            self.browser_path_in = wx.TextEntryDialog(self,"Please paste the browser path to br updated:","Bowser path regsistry:")
                        
            if self.browser_path_in.ShowModal() == wx.ID_OK:

                browser_path = str(self.browser_path_in.GetValue()).replace('"','')

                #browser_path = r"C:\Users\{0}\AppData\Local\UiPath\app-{1}\UiRobot.exe".format(username,version_in)

                if browser_path!="":
                
                    if os.path.exists(browser_path)==True:
    
                        settings_json = open(browser_path_json_srcfl,'w')
                        
                        settings_json.write("{"'"browser_path"'":")
                        
                        UiPath_appvernos ={
                                "browser_path" : str(browser_path).replace('""','')
                            }
                        
                        with open(browser_path_json_srcfl, "w") as json_settings_file_datas:

                            json.dump(UiPath_appvernos, json_settings_file_datas)

                        json_settings_file_datas.close()

                        settings_json.close()

                        #print("Data Changed...")

                        mod_ver_msg_box = wx.MessageDialog(None,"Change updated...","{} - info".format(file_name),wx.ICON_INFORMATION| wx.STAY_ON_TOP)
                                    
                        mod_ver_msg_box.ShowModal()

                        break
                    else:

                        browser_path_exists_err = wx.MessageDialog(None,"Opps! Sorry coundn't save the requested browser path since it is not found in the system.","{} - browser path updation error".format(file_name),wx.ICON_ERROR| wx.STAY_ON_TOP)
                            
                        browser_path_exists_err.ShowModal()
                else:
                    invalid_err = wx.MessageDialog(None,"Input invalid.","{} - input verifier error".format(file_name),wx.ICON_ERROR| wx.STAY_ON_TOP)
                        
                    invalid_err.ShowModal()
            else:
                break
            
    def rst(self,event):
        self.textCtrl.Clear()#            clears texts that exists within the input feilds

        self.typecomboBox.SetValue(self.type_lists[0])# setting the type combobox back to default

        #self.concealcombobox.SetValue(self.yn_lists[0])# setting the Yes\No combobox back to default

if __name__=='__main__':

    app=wx.App()# Start the app

    frame = AppUi(parent=None,id=-1)# Gives parametres or infos to the class or 'Frame' components

    wx.BeginBusyCursor()

    wx.EndBusyCursor()

    frame.Show()# Shows the commponents existed within the app

    app.MainLoop()# loops the window as systems close apps within milliseconds or more       