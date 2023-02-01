''' importing prefrences or getting required datas from the modules'''
import os  # for file and folder operation

import time  # for 'time-delays' activities

import wx  # for GUI apps using 'Wxpython'

from playsound import playsound  # for playing audio files

import winshell  # mimic windows powershell activities

from win32com.client import Dispatch  # Creates a Dispatch based COM object using win32 modules

import datetime  # getting real-time datas of today

from gtts import gTTS  # using google-text-to-speech (gtts) service

import wikipedia  # wikia operations

import webbrowser

import os

import subprocess

import json



'''Source files'''
#wDir_path = os.path.dirname(os.path.realpath(__file__))  # curent working directory or the 'Now'-location of the file.
wDir_path = os.getcwd()
# icon source image file -> eg: 'image_file_name'.ico
for file in os.listdir(wDir_path):
    if '.ico' in file:
        # pass
        try:
            ico_flpath = os.path.join(wDir_path, file)
        except FileNotFoundError:
            pass
    else:
        pass

'''File name & File extension'''
file_name, file_type = os.path.splitext(os.path.basename(os.path.realpath(__file__)))

# browser_path_jsonsrc_incognito = '{} %s -incognito'.format(browser_path_jsonsrc)

# settings json file and folders
# dependies_folder_root=os.path.join(wDir_path,".datas")

# settings_folder_path=os.path.join(dependies_folder_root,"settings")

# browser path json files
chrome_path_json_name = "chrome_browser_path"

chrome_path_json = "{}.json".format(chrome_path_json_name)

chrome_path_json_srcfl = os.path.join(wDir_path, chrome_path_json)

main_app_title = "Search Online C13 [Perfected.Further+]: Auto"

shortcut_path = os.path.join(wDir_path, '{} - Shortcut.lnk'.format('Chrome-Exe'))

batch_name ="run"
bat_fl = "{}.bat".format(batch_name)

bat_rt_fl= os.path.join(wDir_path,bat_fl)

# "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"


def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    # use buildin check_output right away
    output = subprocess.check_output(call).decode()
    # check in last line for process name
    last_line = output.strip().split('\r\n')[-1]
    # because Fail message could be translated
    return last_line.lower().startswith(process_name.lower())

def chrome_shortcut_maker(shorcut_path_var,browser_path_json_var):
    #target_rt = browser_path_json_var
    #wDir_rt = browser_path_json_var
    shell = Dispatch('WScript.Shell')

    if os.path.exists(shorcut_path_var) == False:

        shortcut = shell.CreateShortCut(shorcut_path_var)
        shortcut.Targetpath = browser_path_json_var
        shortcut.WorkingDirectory = browser_path_json_var
        shortcut.save()
    else:
        pass

def batch_runner_maker():
    pass

def delay(float):
    time.sleep(float)  # time delay seconnds for each sequence or activities

def check_chrome_b12(browser_path_json_var,shortcut_path_var):
    if process_exists(os.path.basename(browser_path_json_var)) == False:

        cmd = "start chrome /in http://www.google.com/images?q=Iron+Man"

        f = open(bat_rt_fl, 'w')
        f.write(cmd)
        f.close()
        os.startfile(shortcut_path_var)
        delay(1.3)
    else:
        #print('\n-> Chrome is running')
        pass
    
def open_incognito_browser(batch_file_path,url_req):
    
    cmd = f"start opera -private {url_req}"

    f = open(batch_file_path, 'w')
    f.write(cmd)
    f.close()
    os.startfile(batch_file_path)
    delay(1.3)

def open_browser(batch_file_path,url_req):
   
   cmd = f"start opera {url_req}"

   f = open(batch_file_path, 'w')
   f.write(cmd)
   f.close()
   os.startfile(batch_file_path)
   delay(1.3)

# using 'class' or "blueprint" to extract all the 'frame' supports existing within the 'wx' module for GUI apps
class AppUi(wx.Frame):

    # Starts frame upon user request or 'CLICKING' the app
    def __init__(self, parent, id):

        # Window (Frame) with parametres i.e (frame, parent=None,id=-1.'window title',size=(int,int),style=wx.(obj))
        wx.Frame.__init__(self, parent, id, main_app_title, size=(657, 563),
                          style=wx.DEFAULT_FRAME_STYLE & ~wx.MAXIMIZE_BOX ^ wx.RESIZE_BORDER)

        try:
            self.SetIcon(wx.Icon(ico_flpath))  # sets icon on the window title bar
        except NameError:
            pass

        self.wpanel = wx.Panel(self)  # setting 'container' to have wxpython GUI parts

        self.wpanel.SetBackgroundColour('Steel Blue')  # sets the panel or app background

        # Text

        # creates fonts for 'Text' input field
        lblfont = wx.Font(22, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        ## label text

        self.custom_txt_lbl = wx.StaticText(self.wpanel, -1, "Search:", (33, 38), (24, 24), wx.TEXT_ALIGNMENT_CENTRE)

        self.custom_txt_lbl.SetFont(lblfont)  # sets font for the 'Text' label using variable 'textfieldfont'

        self.custom_txt_lbl.SetForegroundColour('White')  # sets the 'Text' label text colour as red

        self.custom_txt_lbl.SetBackgroundColour('Indian Red')  # sets the 'Text' label colour as white

        # text input field font
        textfieldfont = wx.Font(22, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        # creates text input field
        self.textCtrl = wx.TextCtrl(self.wpanel, pos=(152, 35), size=(462, 34),
                                    style=wx.TE_HT_ON_TEXT & ~ wx.TEXT_ALIGNMENT_JUSTIFIED & ~ wx.TE_WORDWRAP)

        self.textCtrl.SetFont(textfieldfont)  # sets font for the text input field using variable 'textfieldfont'

        self.textCtrl.SetForegroundColour('Red')  # sets input field text as red

        self.textCtrl.SetToolTip('Type here.')

        # type combobox

        # creates fonts for modes
        type_lists_font = wx.Font(22, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        type_lbl_font = wx.Font(22, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        ## label accent

        # creates  'Select accent' label appear on the panel
        self.typelbl = wx.StaticText(self.wpanel, -1, "Select:", (31, 106), (24, 24))  #

        self.typelbl.SetFont(
            type_lbl_font)  # sets 'Select accent:" label fonts uing parameters from 'accentfont' variable

        self.typelbl.SetForegroundColour('White')  # sets the 'Select accent:' label text colour as white

        self.typelbl.SetBackgroundColour('Black')  # sets the 'Select accent:' label colour as 'Black'

        # collection or lists conataining accent items
        self.type_lists = ['Google', 'Google images','Bing','Bing images', 'Yahoo','Yahoo images', 'YouTube videos', 'YouTube channels', 'Wikipedia',
                           'Amazon products', 'Flipkart products', 'Myntra products', 'Ajio products','Deviantarts collections','Danbaroo pics']

        self.typecomboBox = wx.ComboBox(self.wpanel, -1, self.type_lists[0], (156, 103), (321, 34), self.type_lists,
                                        wx.CB_READONLY | wx.ALIGN_CENTER)

        self.typecomboBox.SetFont(
            type_lists_font)  # sets fonts for the accent items containing in the 'acccent' combobox

        self.typecomboBox.SetForegroundColour('Blue')

        # self.typecomboBox.SetBackgroundColour('Light Orange')

        self.typecomboBox.SetToolTip('Select any type of information your are searching for.')

        # Search button

        # creates fonts for click button
        btn_search_font = wx.Font(21, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        # combines 'Exit' button with its functions
        self.search_btn = wx.Button(self.wpanel, label='Search', pos=(67, 188 + 45), size=(156, 45),
                                    style=wx.BORDER_RAISED)

        self.search_btn.SetFont(btn_search_font)  # sets 'Click here' button font using variable 'btn_click_font'

        self.search_btn.SetForegroundColour('White')  # sets 'Click here' button text as white

        self.search_btn.SetBackgroundColour('Dark Green')  # sets 'Click here' button as dark green

        self.search_btn.SetToolTip("Click here to search in browser.")

        # self.wbtn.SetForegroundColour('Black')

        # self.Bind(wx.EVT_STC,self.print)

        self.Bind(wx.EVT_BUTTON, self.onlineSearch, self.search_btn)  # combines 'Click here' button with its functions

        # Exit button

        # creates fonts for exit button
        btn_exit_font = wx.Font(21, wx.ROMAN, wx.FONTSTYLE_NORMAL,
                                wx.FONTWEIGHT_BOLD)  # Creates  fonts for 'Exit' button

        # Exit button
        # creates  'Exit' button
        self.exit_btn = wx.Button(self.wpanel, label='Exit', pos=(67, 376), size=(156, 45), style=wx.BORDER_RAISED)

        self.exit_btn.SetFont(btn_exit_font)  # sets font for the exit button using variable 'btn_exit_font'

        self.exit_btn.SetForegroundColour('White')  # sets 'Exit' button text as white

        self.exit_btn.SetBackgroundColour('Red')  # sets 'Exit' button coloer as red

        self.exit_btn.SetToolTip('Click here to exit the app.')

        self.Bind(wx.EVT_BUTTON, self.exitbutton, self.exit_btn)  # combines 'Exit' button with its functions

        # Incognito search button

        # creates fonts for exit button
        btn_incognito_font = wx.Font(21, wx.ROMAN, wx.FONTSTYLE_NORMAL,
                                     wx.FONTWEIGHT_BOLD)  # Creates  fonts for 'Exit' button

        # Exit button
        # creates  'Exit' button
        self.incognito_btn = wx.Button(self.wpanel, label='Search (incognito)', pos=(201, 304), size=(256, 45),
                                       style=wx.BORDER_RAISED)

        self.incognito_btn.SetFont(btn_incognito_font)  # sets font for the exit button using variable 'btn_exit_font'

        self.incognito_btn.SetForegroundColour('Black')  # sets 'Exit' button text as white

        self.incognito_btn.SetBackgroundColour('Yellow')  # sets 'Exit' button coloer as red

        self.incognito_btn.SetToolTip('Click here to search in incognito browser.')

        self.Bind(wx.EVT_BUTTON, self.onlineSearchprivate,
                  self.incognito_btn)  # combines 'Exit' button with its functions

        # Reset button

        # creates fonts for reset button
        btn_rst_font = wx.Font(21, wx.ROMAN, wx.FONTSTYLE_NORMAL,
                               wx.FONTWEIGHT_BOLD)  # Creates  fonts for 'Reset' button

        # reset button

        # creates  'Reset' button
        self.rst_btn = wx.Button(self.wpanel, label='Reset', pos=(412, 233), size=(156, 45), style=wx.BORDER_RAISED)

        self.rst_btn.SetFont(btn_rst_font)  # sets font for the exit button using variable 'btn_rst_font'

        self.rst_btn.SetForegroundColour('White')  # sets 'Reset' button text as white

        self.rst_btn.SetBackgroundColour('Purple')  # sets 'Reset' button coloer as Purple

        self.rst_btn.SetToolTip('Click here to set everything to default.')

        self.Bind(wx.EVT_BUTTON, self.rst, self.rst_btn)  # combines 'Reset' button with its functions

        # Modify button

        btn_mod_font = wx.Font(21, wx.ROMAN, wx.FONTSTYLE_NORMAL,
                               wx.FONTWEIGHT_BOLD)  # Creates  fonts for 'Reset' button

        # reset button

        # creates  'Modify' button
        self.modify_btn = wx.Button(self.wpanel, label='Modify', pos=(412, 376), size=(156, 45), style=wx.BORDER_RAISED)

        self.modify_btn.SetFont(btn_mod_font)  # sets font for the exit button using variable 'btn_rst_font'

        self.modify_btn.SetForegroundColour('White')  # sets 'Reset' button Text as white

        self.modify_btn.SetBackgroundColour('Blue')  # sets 'Reset' button coloer as Blue

        self.modify_btn.SetToolTip("Click here to change browser path.")

        #self.Bind(wx.EVT_BUTTON, self.modify, self.modify_btn)  # combines 'Reset' button with its functions

        # close window button

        self.Bind(wx.EVT_CLOSE, self.Close)  # combines 'X' window button with its functions

    def restrt(self):

        self.Destroy()

        app = wx.App()

        encrypt_window = AppUi(parent=None, id=-1)

        encrypt_window.Show()

        app.MainLoop()

    def onlineSearchprivate(self, event):

        # json_file_exists = os.path.exists(chrome_path_json_srcfl)

        q = self.textCtrl.GetValue()  # gets the text value that within input field

        if q == "":
            ae_msg = wx.MessageDialog(self.wpanel, "No words to search on the internet.", "Invalid request Error: ",
                                      wx.OK | wx.ICON_ERROR)

            ae_msg.ShowModal()

            # delay(1.2)

            self.textCtrl.Clear()  # clears texts that exists within the input feilds

            # self.modeComboBox.SetValue(self.type_lists[0])# setting the type combobox back to default

            # self.concealcombobox.SetValue(self.yn_lists[0])# setting the Yes\No combobox back to default
        else:

            str_type = self.typecomboBox.GetStringSelection()  # gets the types value  from the combobox

            ##incognito_q = self.concealcombobox.GetStringSelection()# gets the incognito? Yes\No

            # #delay(1.2)

            q_re = q.replace(" ", "+")

            q_re2 = q.replace(" ", "_")

            ''' URLs ( Uniform Resource Locator ) '''
            g_img_srch_link = f'http://www.google.com/images?q={q_re}'

            g_srch_link = f"https://www.google.com/search?q={q_re}"

            yt_v_srch_link = f'https://www.youtube.com/results?search_query={q_re}'

            amazon_link = f'https://www.amazon.in/s?k={q_re}&crid=2S55AVQK41W&sprefix=p%2Caps%2C351&ref=nb_sb_ss_ts-doa-p_4_1'

            ajio_link = f'https://www.ajio.com/search/?text={q_re}'

            myntra_link = f'https://www.myntra.com/{q_re}'

            flipkart_link = f'https://www.flipkart.com/search?q={q_re}'

            yt_ch_srch_link = f'https://www.youtube.com/{q_re}'

            bing_srh_link = f'https://www.bing.com/search?q={q_re}&qs=n&form=QBRE&sp=-1&pq={q_re}&sc=8-3&sk=&cvid=4589D01C2A3540BE8BC6BE49EDFB6DB6'

            bing_img_srch_link = f'https://www.bing.com/images/search?q={q_re}&qs=n&form=QBIDMH&sp=-1&pq={q_re}&sc=8-2&cvid=74607D228BC84807B39DCEDAA03A2CBA&first=1&tsc=ImageBasicHover'

            yahoo_srch_link = f'https://in.search.yahoo.com/search;_ylt=AwrxzRWDKeVhrh4AoQG6HAx.;_ylc=X1MDMjExNDcyMzAwMgRfcgMyBGZyAwRmcjIDc2ItdG9wLXNlYXJjaARncHJpZANGdlh3X2lOOVNjaWNPUENpR2dYTXhBBG5fcnNsdAMwBG5fc3VnZwMxMARvcmlnaW4DaW4uc2VhcmNoLnlhaG9vLmNvbQRwb3MDMARwcXN0cgMEcHFzdHJsAzAEcXN0cmwDNgRxdWVyeQNkcml2ZXIEdF9zdG1wAzE2NDI0MDg3ODc-?p={q_re}&fr=sfp&iscqry=&fr2=sb-top-search'

            yahoo_img_srch_link = f'https://in.images.search.yahoo.com/search/images;_ylt=Awrxy8yMKeVhNDYAzAK7HAx.;_ylu=Y29sbwNzZzMEcG9zAzEEdnRpZAMEc2VjA3BpdnM-?p={q_re}&fr2=piv-web&fr=sfp'

            danbaroo_srch_link = f'https://danbooru.donmai.us/posts?tags={q_re2}'

            devinatart_srch_link = f'https://www.deviantart.com/search?q={q_re}'

            hyperpreg_srch_link = f'{q_re}'
           
            # chrome_shortcut_maker(shorcut_path_var=shortcut_path, browser_path_json_var=browser_path_jsonsrc)

            if "Google images" in str_type:

                # g_Img = f'https://www.google.com/search?q={q_re}&hl=en&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi6v8SR0KPpAhUh63MBHXQPBwsQ_AUoBHoECBgQBg'

                # delay(1.2)

                # os.startfile(g_Img)

                # check_chrome_b12(browser_path_json_var=browser_path_jsonsrc,shortcut_path_var=shortcut_path)

                # wb = webbrowser.get(browser_open_cmd)
                # wb.open(g_img_srch_link)

                # wx.BeginBusyCursor()

                # wx.EndBusyCursor()

                open_incognito_browser(batch_file_path=bat_rt_fl, url_req=g_img_srch_link)


            elif "Google" in str_type:

                # g_srch = f"https://www.google.com/search?q={q_re}"

                # delay(1.2)

                # check_chrome_b12(browser_path_json_var=browser_path_jsonsrc, shortcut_path_var=shortcut_path)

                # os.startfile(g_srch)

                # wb = webbrowser.get(browser_path_jsonsrc).open(g_srch)

                # wb = webbrowser.get(browser_open_cmd)

                # wb.open(g_srch_link)

                open_incognito_browser(batch_file_path=bat_rt_fl, url_req=g_srch_link)

            elif "Bing images" in str_type:

                # check_chrome_b12(browser_path_json_var=browser_path_jsonsrc, shortcut_path_var=shortcut_path)

                # os.startfile(g_Yt)

                # wb = webbrowser.get(browser_open_cmd)

                # wb.open(bing_img_srch_link)

                open_incognito_browser(batch_file_path=bat_rt_fl, url_req=bing_img_srch_link)

            elif "Bing" in str_type:

                # check_chrome_b12(browser_path_json_var=browser_path_jsonsrc, shortcut_path_var=shortcut_path)

                # os.startfile(g_Yt)

                # wb = webbrowser.get(browser_open_cmd)

                # wb.open(bing_srh_link)

                open_incognito_browser(batch_file_path=bat_rt_fl, url_req=bing_srh_link)

            elif "Yahoo images" in str_type:

                # check_chrome_b12(browser_path_json_var=browser_path_jsonsrc, shortcut_path_var=shortcut_path)

                # os.startfile(g_Yt)

                # wb = webbrowser.get(browser_open_cmd)

                # wb.open(yahoo_img_srch_link)

                open_incognito_browser(batch_file_path=bat_rt_fl, url_req=yahoo_img_srch_link)

            elif "Yahoo" in str_type:

                # check_chrome_b12(browser_path_json_var=browser_path_jsonsrc, shortcut_path_var=shortcut_path)

                # os.startfile(g_Yt)

                # wb = webbrowser.get(browser_open_cmd)

                # wb.open(yahoo_srch_link)

                open_incognito_browser(batch_file_path=bat_rt_fl, url_req=yahoo_srch_link)
            elif "YouTube videos" in str_type:

                # v_yt = f'https://www.youtube.com/results?search_query={q_re}'

                # delay(1.2)

                # check_chrome_b12(browser_path_json_var=browser_path_jsonsrc, shortcut_path_var=shortcut_path)

                # os.startfile(g_Yt)

                # wb = webbrowser.get(browser_open_cmd)

                # wb.open(yt_v_srch_link)

                open_incognito_browser(batch_file_path=bat_rt_fl, url_req=yt_v_srch_link)

            elif "Amazon" in str_type:

                # amazon_link = f'https://www.amazon.in/s?k={q_re}&crid=2S55AVQK41W&sprefix=p%2Caps%2C351&ref=nb_sb_ss_ts-doa-p_4_1'

                # delay(1.2)

                # os.startfile(amazon_link)

                # check_chrome_b12(browser_path_json_var=browser_path_jsonsrc,shortcut_path_var=shortcut_path)

                # wb = webbrowser.get(browser_open_cmd)
                # wb.open(amazon_link)

                open_incognito_browser(batch_file_path=bat_rt_fl, url_req=amazon_link)

            elif "Ajio" in str_type:

                # ajio_links = f'https://www.ajio.com/search/?text={q_re}'

                # delay(1.2)

                # os.startfile(ajio_links)

                # check_chrome_b12(browser_path_json_var=browser_path_jsonsrc,shortcut_path_var=shortcut_path)

                # wb = webbrowser.get(browser_open_cmd)
                # wb.open(ajio_link)
                open_incognito_browser(batch_file_path=bat_rt_fl, url_req=ajio_link)

            elif "Myntra" in str_type:

                # myntra_links = f'https://www.myntra.com/{q_re}'

                # delay(1.2)

                # os.startfile(myntra_links)

                # check_chrome_b12(browser_path_json_var=browser_path_jsonsrc,shortcut_path_var=shortcut_path)

                # wb = webbrowser.get(browser_open_cmd)
                # wb.open(myntra_link)

                open_incognito_browser(batch_file_path=bat_rt_fl, url_req=myntra_link)

            elif "Flipkart" in str_type:

                # flipkart_links = f'https://www.flipkart.com/search?q={q_re}'

                # delay(1.2)

                # os.startfile(flipkart_links)

                # check_chrome_b12(browser_path_json_var=browser_path_jsonsrc,shortcut_path_var=shortcut_path)

                # wb = webbrowser.get(browser_open_cmd)
                # wb.open(flipkart_link)

                open_incognito_browser(batch_file_path=bat_rt_fl, url_req=flipkart_link)

            elif "Wikipedia" in str_type:

                results = wikipedia.summary(q, sentences=3)

                # delay(1.2)

                results_msg = wx.MessageDialog(self.wpanel, results, "Wiki results:", wx.OK)

                results_msg.ShowModal()

            elif "YouTube channel" in str_type:

                # YouTube_ch = f'https://www.youtube.com/{q_re}'

                # delay(1.2)

                # os.startfile(YouTube_ch)

                # check_chrome_b12(browser_path_json_var=browser_path_jsonsrc,shortcut_path_var=shortcut_path)

                # wb = webbrowser.get(browser_open_cmd)
                # wb.open(yt_ch_srch_link)

                open_incognito_browser(batch_file_path=bat_rt_fl, url_req=yt_ch_srch_link)


            elif "Danbaroo" in str_type:

                open_incognito_browser(batch_file_path=bat_rt_fl, url_req=danbaroo_srch_link)

            elif "Deviantarts" in str_type:

                open_incognito_browser(batch_file_path=bat_rt_fl, url_req=devinatart_srch_link)

            elif "hyperpreg" in str_type:

                open_incognito_browser(batch_file_path=bat_rt_fl, url_req=hyperpreg_srch_link)
            else:

                pass

            delay(1.1)

            ''' Asks user whether to clear for assurance as message box. if yes, clears the values for the user, or exits the app if no  '''
            yn_msgbox = wx.MessageDialog(self.wpanel, "Do you wish to search again?", "Yes/No",
                                         wx.YES_NO | wx.ICON_NONE)

            yn_var = yn_msgbox.ShowModal()

            if yn_var == wx.ID_YES:
                self.textCtrl.Clear()  # clears texts that exists within the input fields

                self.typecomboBox.SetValue(self.type_lists[0])  # setting the mode combobox back to default

                # self.concealcombobox.SetValue(self.yn_lists[0])# setting the Yes\No combobox back to default

    def onlineSearch(self, event):

        #json_file_exists = os.path.exists(chrome_path_json_srcfl)

        q = self.textCtrl.GetValue()  # gets the text value that within input field

        if q == "":
            ae_msg = wx.MessageDialog(self.wpanel, "No words to search on the internet.", "Invalid request Error: ",
                                      wx.OK | wx.ICON_ERROR)

            ae_msg.ShowModal()

            #delay(1.2)

            self.textCtrl.Clear()  # clears texts that exists within the input feilds

            # self.modeComboBox.SetValue(self.type_lists[0])# setting the type combobox back to default

            # self.concealcombobox.SetValue(self.yn_lists[0])# setting the Yes\No combobox back to default
        else:

            str_type = self.typecomboBox.GetStringSelection()  # gets the types value  from the combobox

            ##incognito_q = self.concealcombobox.GetStringSelection()# gets the incognito? Yes\No

            # #delay(1.2)

            q_re = q.replace(" ", "+")

            q_re2 = q.replace(" ", "_")

            ''' URLs ( Uniform Resource Locator ) '''
            g_img_srch_link = f'http://www.google.com/images?q={q_re}'

            g_srch_link = f"https://www.google.com/search?q={q_re}"

            yt_v_srch_link = f'https://www.youtube.com/results?search_query={q_re}'

            amazon_link = f'https://www.amazon.in/s?k={q_re}&crid=2S55AVQK41W&sprefix=p%2Caps%2C351&ref=nb_sb_ss_ts-doa-p_4_1'

            ajio_link = f'https://www.ajio.com/search/?text={q_re}'

            myntra_link = f'https://www.myntra.com/{q_re}'

            flipkart_link = f'https://www.flipkart.com/search?q={q_re}'

            yt_ch_srch_link = f'https://www.youtube.com/{q_re}'

            bing_srh_link = f'https://www.bing.com/search?q={q_re}&qs=n&form=QBRE&sp=-1&pq={q_re}&sc=8-3&sk=&cvid=4589D01C2A3540BE8BC6BE49EDFB6DB6'

            bing_img_srch_link = f'https://www.bing.com/images/search?q={q_re}&qs=n&form=QBIDMH&sp=-1&pq={q_re}&sc=8-2&cvid=74607D228BC84807B39DCEDAA03A2CBA&first=1&tsc=ImageBasicHover'

            yahoo_srch_link = f'https://in.search.yahoo.com/search;_ylt=AwrxzRWDKeVhrh4AoQG6HAx.;_ylc=X1MDMjExNDcyMzAwMgRfcgMyBGZyAwRmcjIDc2ItdG9wLXNlYXJjaARncHJpZANGdlh3X2lOOVNjaWNPUENpR2dYTXhBBG5fcnNsdAMwBG5fc3VnZwMxMARvcmlnaW4DaW4uc2VhcmNoLnlhaG9vLmNvbQRwb3MDMARwcXN0cgMEcHFzdHJsAzAEcXN0cmwDNgRxdWVyeQNkcml2ZXIEdF9zdG1wAzE2NDI0MDg3ODc-?p={q_re}&fr=sfp&iscqry=&fr2=sb-top-search'

            yahoo_img_srch_link = f'https://in.images.search.yahoo.com/search/images;_ylt=Awrxy8yMKeVhNDYAzAK7HAx.;_ylu=Y29sbwNzZzMEcG9zAzEEdnRpZAMEc2VjA3BpdnM-?p={q_re}&fr2=piv-web&fr=sfp'
            
            danbaroo_srch_link = f'https://danbooru.donmai.us/posts?tags={q_re2}'

            devinatart_srch_link = f'https://www.deviantart.com/search?q={q_re}'

            hyperpreg_srch_link = f'{q_re}'
            #chrome_shortcut_maker(shorcut_path_var=shortcut_path, browser_path_json_var=browser_path_jsonsrc)


            if "Google images" in str_type:

                #g_Img = f'https://www.google.com/search?q={q_re}&hl=en&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi6v8SR0KPpAhUh63MBHXQPBwsQ_AUoBHoECBgQBg'

                #delay(1.2)

                # os.startfile(g_Img)

                #check_chrome_b12(browser_path_json_var=browser_path_jsonsrc,shortcut_path_var=shortcut_path)

                #wb = webbrowser.get(browser_open_cmd)
                #wb.open(g_img_srch_link)

                # wx.BeginBusyCursor()

                # wx.EndBusyCursor()

                open_incognito_browser(batch_file_path=bat_rt_fl,url_req=g_img_srch_link)
                        

            elif "Google" in str_type:

                #g_srch = f"https://www.google.com/search?q={q_re}"

                #delay(1.2)

                #check_chrome_b12(browser_path_json_var=browser_path_jsonsrc, shortcut_path_var=shortcut_path)

                # os.startfile(g_srch)

                # wb = webbrowser.get(browser_path_jsonsrc).open(g_srch)

                #wb = webbrowser.get(browser_open_cmd)

                #wb.open(g_srch_link)

                open_browser(batch_file_path=bat_rt_fl, url_req=g_srch_link)

            elif "Bing images" in str_type:

                #check_chrome_b12(browser_path_json_var=browser_path_jsonsrc, shortcut_path_var=shortcut_path)

                # os.startfile(g_Yt)

                #wb = webbrowser.get(browser_open_cmd)

                #wb.open(bing_img_srch_link)

                open_browser(batch_file_path=bat_rt_fl, url_req=bing_img_srch_link)

            elif "Bing" in str_type:

                #check_chrome_b12(browser_path_json_var=browser_path_jsonsrc, shortcut_path_var=shortcut_path)

                # os.startfile(g_Yt)

                #wb = webbrowser.get(browser_open_cmd)

                #wb.open(bing_srh_link)

                open_browser(batch_file_path=bat_rt_fl, url_req=bing_srh_link)

            elif "Yahoo images" in str_type:

                #check_chrome_b12(browser_path_json_var=browser_path_jsonsrc, shortcut_path_var=shortcut_path)

                # os.startfile(g_Yt)

                #wb = webbrowser.get(browser_open_cmd)

                #wb.open(yahoo_img_srch_link)

                open_browser(batch_file_path=bat_rt_fl, url_req=yahoo_img_srch_link)

            elif "Yahoo" in str_type:

                #check_chrome_b12(browser_path_json_var=browser_path_jsonsrc, shortcut_path_var=shortcut_path)

                # os.startfile(g_Yt)

                #wb = webbrowser.get(browser_open_cmd)

                #wb.open(yahoo_srch_link)

                open_browser(batch_file_path=bat_rt_fl, url_req=yahoo_srch_link)
            elif "YouTube videos" in str_type:

                #v_yt = f'https://www.youtube.com/results?search_query={q_re}'

                #delay(1.2)

                #check_chrome_b12(browser_path_json_var=browser_path_jsonsrc, shortcut_path_var=shortcut_path)

                # os.startfile(g_Yt)

                #wb = webbrowser.get(browser_open_cmd)

                #wb.open(yt_v_srch_link)

                open_browser(batch_file_path=bat_rt_fl, url_req=yt_v_srch_link)

            elif "Amazon" in str_type:

                #amazon_link = f'https://www.amazon.in/s?k={q_re}&crid=2S55AVQK41W&sprefix=p%2Caps%2C351&ref=nb_sb_ss_ts-doa-p_4_1'

                #delay(1.2)

                # os.startfile(amazon_link)

                #check_chrome_b12(browser_path_json_var=browser_path_jsonsrc,shortcut_path_var=shortcut_path)

                #wb = webbrowser.get(browser_open_cmd)
                #wb.open(amazon_link)

                open_browser(batch_file_path=bat_rt_fl, url_req=amazon_link)

            elif "Ajio" in str_type:

                #ajio_links = f'https://www.ajio.com/search/?text={q_re}'

                #delay(1.2)

                # os.startfile(ajio_links)

                #check_chrome_b12(browser_path_json_var=browser_path_jsonsrc,shortcut_path_var=shortcut_path)

                #wb = webbrowser.get(browser_open_cmd)
                #wb.open(ajio_link)
                open_browser(batch_file_path=bat_rt_fl, url_req=ajio_link)

            elif "Myntra" in str_type:

                #myntra_links = f'https://www.myntra.com/{q_re}'

                #delay(1.2)

                # os.startfile(myntra_links)

                #check_chrome_b12(browser_path_json_var=browser_path_jsonsrc,shortcut_path_var=shortcut_path)

                #wb = webbrowser.get(browser_open_cmd)
                #wb.open(myntra_link)

                open_browser(batch_file_path=bat_rt_fl, url_req=myntra_link)

            elif "Flipkart" in str_type:

                #flipkart_links = f'https://www.flipkart.com/search?q={q_re}'

                #delay(1.2)

                # os.startfile(flipkart_links)

                #check_chrome_b12(browser_path_json_var=browser_path_jsonsrc,shortcut_path_var=shortcut_path)

                #wb = webbrowser.get(browser_open_cmd)
                #wb.open(flipkart_link)

                open_browser(batch_file_path=bat_rt_fl, url_req=flipkart_link)

            elif "Wikipedia" in str_type:

                results = wikipedia.summary(q, sentences=3)

                #delay(1.2)

                results_msg = wx.MessageDialog(self.wpanel, results, "Wiki results:", wx.OK)

                results_msg.ShowModal()

            elif "Danbaroo" in str_type:

                open_browser(batch_file_path=bat_rt_fl, url_req=danbaroo_srch_link)


            elif "Deviantarts" in str_type:

                open_browser(batch_file_path=bat_rt_fl, url_req=devinatart_srch_link)

            elif "Hyperpreg" in str_type:

                open_browser(batch_file_path=bat_rt_fl, url_req=hyperpreg_srch_link)


            elif "YouTube channel" in str_type:

                #YouTube_ch = f'https://www.youtube.com/{q_re}'

                #delay(1.2)

                # os.startfile(YouTube_ch)

                #check_chrome_b12(browser_path_json_var=browser_path_jsonsrc,shortcut_path_var=shortcut_path)

                #wb = webbrowser.get(browser_open_cmd)
                #wb.open(yt_ch_srch_link)

                open_browser(batch_file_path=bat_rt_fl, url_req=yt_ch_srch_link)
            else:

                pass

            delay(1.1)

            ''' Asks user whether to clear for assurance as message box. if yes, clears the values for the user, or exits the app if no  '''
            yn_msgbox = wx.MessageDialog(self.wpanel, "Do you wish to search again?", "Yes/No",
                                                 wx.YES_NO | wx.ICON_NONE)


            yn_var = yn_msgbox.ShowModal()

            if yn_var == wx.ID_YES:
                self.textCtrl.Clear()  # clears texts that exists within the input fields

                self.typecomboBox.SetValue(self.type_lists[0])  # setting the mode combobox back to default

                # self.concealcombobox.SetValue(self.yn_lists[0])# setting the Yes\No combobox back to default


    def exitbutton(self, event):
        ''' Asks user whether to use again as message box. if not, clears the values for the user, or exits the app if yes  '''
        yn_msgbox = wx.MessageDialog(self.wpanel, "Are you sure you want to exit the app?", "Yes/No",
                                     wx.YES_NO | wx.ICON_WARNING)

        yn_var = yn_msgbox.ShowModal()

        if yn_var == wx.ID_NO:

            self.textCtrl.Clear()  # clears texts that exists within the input feilds

            self.typecomboBox.SetValue(self.type_lists[0])  # setting the mode combobox back to default

            # self.concealcombobox.SetValue(self.yn_lists[0])# setting the Yes\No combobox back to default

        else:
            self.Destroy()  # closes app when 'EXIT' button is click

    def Close(self, event):
        self.Destroy()  # closes app  when 'CLOSE' or 'X' on the window is pressed

    def modify(self, event):

        while True:

            self.browser_path_in = wx.TextEntryDialog(self, "Please paste the browser path to br updated:",
                                                      "Bowser path regsistry:")

            if self.browser_path_in.ShowModal() == wx.ID_OK:

                browser_path = str(self.browser_path_in.GetValue()).replace('"', '')

                # browser_path = r"C:\Users\{0}\AppData\Local\UiPath\app-{1}\UiRobot.exe".format(username,version_in)

                if browser_path != "":

                    if os.path.exists(browser_path) == True:

                        settings_json = open(chrome_path_json_srcfl, 'w')

                        settings_json.write("{"'"browser_path"'":")

                        chrome_exe_path = {
                            "browser_path": str(browser_path).replace('""', '')
                        }

                        with open(chrome_path_json_srcfl, "w") as json_settings_file_datas:

                            json.dump(chrome_exe_path, json_settings_file_datas)

                        json_settings_file_datas.close()

                        settings_json.close()

                        # print("Data Changed...")

                        mod_ver_msg_box = wx.MessageDialog(None, "Change updated...", "{} - info".format(main_app_title),
                                                           wx.ICON_INFORMATION | wx.STAY_ON_TOP)

                        mod_ver_msg_box.ShowModal()

                        break
                    else:

                        browser_path_exists_err = wx.MessageDialog(None,
                                                                   "Opps! Sorry coundn't save the requested browser path since it is not found in the system.",
                                                                   "{} - browser path updation error".format(main_app_title),
                                                                   wx.ICON_ERROR | wx.STAY_ON_TOP)

                        browser_path_exists_err.ShowModal()
                else:
                    invalid_err = wx.MessageDialog(None, "Input invalid.",
                                                   "{} - input verifier error".format(main_app_title),
                                                   wx.ICON_ERROR | wx.STAY_ON_TOP)

                    invalid_err.ShowModal()
            else:
                break

    def rst(self, event):
        self.textCtrl.Clear()  # clears texts that exists within the input feilds

        self.typecomboBox.SetValue(self.type_lists[0])  # setting the type combobox back to default

        # self.concealcombobox.SetValue(self.yn_lists[0])# setting the Yes\No combobox back to default


if __name__ == '__main__':
    app = wx.App()  # Start the app

    frame = AppUi(parent=None, id=-1)  # Gives parametres or infos to the class or 'Frame' components

    wx.BeginBusyCursor()

    wx.EndBusyCursor()

    frame.Show()  # Shows the commponents existed within the app

    app.MainLoop()  # loops the window as systems close apps within milliseconds or more
