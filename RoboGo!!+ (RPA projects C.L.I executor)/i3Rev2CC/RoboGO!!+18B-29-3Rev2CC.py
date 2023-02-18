''' importing prefrences or getting required datas from the modules'''
import os # for file and folder operation

#from sys import flags  

import time  # for 'time-delays' activities

import wx  # for GUI apps using 'Wxpython'

import winshell# mimic windows powershell activities

from win32com.client import Dispatch# Creates a Dispatch based COM object using win32 modules

#import random 

import datetime

#import pyttsx3

import json

#import requests
'''Source files'''

wfile_path = os.path.realpath(__file__)

# Current directory or the 'Now'-location of the running file 
wDir_path = os.path.dirname(wfile_path)

# wDir_path = os.getcwd()

# File name & File extension
wfl_basename = os.path.basename(wDir_path)

file_name, file_type = os.path.splitext(wfl_basename)

#icon source image file -> eg: 'image_file_name'.ico
for file in os.listdir(wDir_path):
    if '.ico' in file:
        try:
            ico_flpath = os.path.join(wDir_path,file)
            #pass
        except OSError:
            pass

#Get user name from the system
#username = getpass.getuser()

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
dt_mnths = datetime.datetime.now().strftime("%B")
#
dt_mnths_no = datetime.datetime.now().strftime("%m")

dt_date = "{0}-{1}-{2}".format(dt_dd,dt_mm,dt_yyyy)

dt_mnthsno_mnths = "{0}-{1}".format(dt_mnths_no,dt_mnths)

# --------------------------------------------------------------------------------------------------

''' Dependies folder details '''
# settings json file and folders
dependies_folder_path=os.path.join(wDir_path,".dependies293-Rev2C")

settings_folder_path=os.path.join(dependies_folder_path,"settings")

UiRobot_infos_dirs = os.path.join(dependies_folder_path,"UiPath UiBot 2.9-3-Rev2C infos")
#------------------------------------------------------------------------------------------

# App path Json files details
json_flname = 'app_datas293Rev2C'

json_file = '{}.json'.format(json_flname)

app_datas_json_file_path = os.path.join(settings_folder_path, json_file)

# --------------------------------------------------------------------------------------------------
''' Init batch file details '''
# Output batch folder & files
bat_folder_name = "UiPath-RoboGo!!+ 18B-2.9-3 Rev2C batch files"

#batch_folder_dir = os.path.join(wDir_path,bat_folder_name)

#now_date_sub_folder = os.path.join(batch_folder_dir,dt_date)

# Init batch file path - default
init_batfl_name = "init293Rev2C_UipathRobot.bat"
#init_bat_fl_path= os.path.join(wDir_path,"init_UipathRobot.bat")

# --------------------------------------------------------------------------------------------------
''' Settings details '''
# App settings json files
uiPath_jsonfl_name = "AppInfos293Rev2C_Uipath"

uiPath_appinfos_json = "{}.json".format(uiPath_jsonfl_name)

uipath_appinfos_srcfl_path=os.path.join(UiRobot_infos_dirs,uiPath_appinfos_json)

# Dynamic [Early-tests type] App Json files details
et_json_fl_name = '{}_infos'.format(file_name)

et_paths_infos_flname_json= '{}.json'.format(et_json_fl_name)

# Dynamic [Early-tests type] json file with path infos
et_uipath_ver_srcfl_path = os.path.join(wDir_path,et_paths_infos_flname_json)

# ----------------------------------------------------------------------------------
# UiPath bot executor application
uipath_botexecutr_name = "UiRobot"

uiexe_fl = "{}.exe".format(uipath_botexecutr_name)

# -----------------------------------------------------------------------------------------
''' App Details '''
# Dynamic [Early-tests type] app title 
et_app_title= "RoboGO!!+ 18B-2.9-3 Rev2CC [Early-Tests.Id: {}]".format(file_name)

# App title 
app_title = "RoboGO!!+ 18B-2.9-3 [Revised-2CC]"

# --------------------------------------------------------------------------------
''' Clear-system '''
def wipeout(float):

  time.sleep(float)

  os.system('cls')

''' Nxt-2-Nxt activity '''
def delay(var):

    time.sleep(var)# time delay seconnds for each sequence or activities
#uipath_batch_support_runner_2(uipath_infos_json=uiPath_appinfos_json,uipath_files_rt=xaml_rt_fl,init_dirs_var=init_bat_dir,yrs_dirs=crnt_yrs_folder_path,date_dirs=now_date_folder_path,init_fl_pathvar=init_bat_fl_path)
def uipath_batch_support_runner_maker_3Rev2C(uipath_infos_json, uipath_files_rt,init_bat_fl_path1):

    json_fl_read = open(uipath_infos_json, 'r')

    data = json_fl_read.read()

    # version_no = json.loads(data)["UiPath_version"]

    uibot_exe_path = json.loads(data)["UiBot_exePath"]

    # app_ver = str(version_no)

    # uipath_bot_rt = r"C:\Users\{0}\AppData\Local\UiPath\app-{1}\UiRobot.exe".format(username,app_ver)

    cmd = '"{0}" -file "{1}"'.format(uibot_exe_path, uipath_files_rt)

    # print(cmd)

    f = open(init_bat_fl_path1, 'w')

    f.write(cmd)

    f.close()

    json_fl_read.close()

    os.startfile(init_bat_fl_path1)  # Runs the batch file

def dirs_shortcut_maker3Rev2C(path1,path2,path3,path4):
    try:
        os.makedirs(path1)
    except OSError:
        pass

    try:
        os.makedirs(path2)
    except OSError:
        pass

    try:
        os.makedirs(path3)
    except OSError:
        pass

    try:
        os.makedirs(path4)
    except OSError:
        pass

    ''' Make 'AppName' shortcut '''
    desktop = winshell.desktop()
    cpath = os.path.join(desktop, '{} - Shortcut.lnk'.format(bat_folder_name))

    if os.path.exists(cpath) == False:

        target = path1
        wDir = path1
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateshortCut(cpath)
        shortcut.Targetpath = target
        shortcut.WorkingDirectory = wDir
        shortcut.save()

    else:
        pass

def dirs_maker(path1,path2,path3):
    try:
        os.makedirs(path1)
    except OSError:
        pass

    try:
        os.makedirs(path2)
    except OSError:
        pass

    try:
        os.makedirs(path3)
    except OSError:
        pass

def save_uipath_infos_json(json_flpath,infos):
    jsonfl_w_datas = open(json_flpath, 'w')

    json.dump(infos, jsonfl_w_datas)

    jsonfl_w_datas.close()

    # pass

# Save path in a json file
def save_json(json_flpath, infos1,infos2):

    # json_write = open(json_flpath, 'w')

    # json_w.write("{"'"path"'":,")
    # json_write.write("{"'"path"'":,"'"bot_executor"'":")

    usr_path = {
        "path": str(infos1),
        "bot_executor":str(infos2)
    }

    json_override = open(json_flpath, "w")

    json.dump(usr_path, json_override)

    json_override.close()

    # json_write.close()


# Update path to the existing value in a json file
def update_json_path(json_flpath, infos):
    json_fl_r = open(json_flpath, "r")

    json_src_data = json.load(json_fl_r)

    json_src_data["path"] = infos

    json_fl_w = open(json_flpath, "w")

    json.dump(json_src_data, json_fl_w)

    json_fl_w.close()

    json_fl_r.close()


# Update path to the existing value in a json file
def update_json_exe(json_flpath, infos):
    json_fl_r = open(json_flpath, "r")

    json_src_data = json.load(json_fl_r)

    json_src_data["bot_executor"] = infos

    json_fl_w = open(json_flpath, "w")

    json.dump(json_src_data, json_fl_w)

    json_fl_w.close()

    json_fl_r.close()


# Read the json file and give the existing value
def read_json(json_flpath):
    try:

        read_json = open(json_flpath, 'r')

        data = read_json.read()

        path_infos_v = json.loads(data)["path"]

        executor_infos_v = json.loads(data)["bot_executor"]

        read_json.close()

        return path_infos_v , executor_infos_v
    except json.decoder.JSONDecodeError:

        read_json = open(json_flpath, 'r')

        read_json.close()
        os.remove(json_flpath)

def find_file(key1,infos1,jsonfl_path1):
    pass

def override_json(json_flpath, infos1,infos2):
    pass

# using 'class' or "blueprint" to extract all the 'frame' supports existing within the 'wx' module for GUI apps
class app_ui(wx.Frame):

    # Starts frame upon user request or 'CLICKING' the app  
    def __init__(self,parent,id):
        
        # Window (Frame) with parametres i.e (frame, parent=None,id=-1.'window title',size=(int,int),style=wx.(obj))
        wx.Frame.__init__(self,parent,id,app_title, size=(644, 416),style = wx.DEFAULT_FRAME_STYLE & ~wx.MAXIMIZE_BOX ^ wx.RESIZE_BORDER & ~wx.STAY_ON_TOP)

        try:
            self.SetIcon(wx.Icon(ico_flpath))# sets icon on the window title bar
        except NameError:
            pass

        self.wpanel = wx.Panel(self)# setting 'container' to have wxpython GUI parts

        self.wpanel.SetBackgroundColour('Coral')# sets the panel or app background
    
    # ----->  Buttons 

    # Start button
 
        # creates fonts for 'START' button
        strt_font = wx.Font(21, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) 

        self.strt_btn = wx.Button(self.wpanel,label='START',pos=(233, 159),size=(156,65),style=wx.BORDER_RAISED)

        self.strt_btn.SetFont(strt_font)# sets 'Click here' button font using variable 'strt_font'

        self.strt_btn.SetForegroundColour('White')# sets 'START' button Text as white

        self.strt_btn.SetBackgroundColour('Dark Green')# sets 'START' button as dark green

        #self.wbtn.SetForegroundColour('Black')

        #self.Bind(wx.EVT_STC,self.print)

        self.strt_btn.SetToolTip("Click here to run the UiPath (.xaml) or (.nupkg) file.")

        self.Bind(wx.EVT_BUTTON,self.start,self.strt_btn)# combines 'Click here' button with its functions

    # Exit button

        # creates fonts for exit button
        btn_exit_font = wx.Font(19, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)# Creates  fonts for 'Exit' button 
      
        # creates  'Exit' button  
        self.exit_btn = wx.Button(self.wpanel,label='EXIT',pos=(67,263),size=(156,65),style=wx.BORDER_RAISED)

        self.exit_btn.SetFont(btn_exit_font)# sets font for the exit button using variable 'btn_exit_font'

        self.exit_btn.SetForegroundColour('White')# sets 'Exit' button Text as white

        self.exit_btn.SetBackgroundColour('Red')# sets 'Exit' button coloer as red

        self.exit_btn.SetToolTip("Click here to exit or close the app.")

        self.Bind(wx.EVT_BUTTON,self.exitbutton,self.exit_btn)# combines 'Exit' button with its functions

    # Modify button

        btn_mod_font = wx.Font(19, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)# Creates  fonts for 'Reset' button 

        # creates 'Modify' button  
        self.modify_btn = wx.Button(self.wpanel,label='MODIFY',pos=(412,263),size=(156,65),style=wx.BORDER_RAISED)

        self.modify_btn.SetFont(btn_mod_font)# sets font for the exit button using variable 'btn_rst_font'

        self.modify_btn.SetForegroundColour('White')# sets 'Reset' button Text as white

        self.modify_btn.SetBackgroundColour('Steel Blue')# sets 'Reset' button coloer as Blue

        self.modify_btn.SetToolTip("Click here to change settings.")

        self.Bind(wx.EVT_BUTTON,self.modify,self.modify_btn)# combines 'Modify' button with its functions

    # Restart 

        btn_restart_font = wx.Font(19, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)# Creates  fonts for 'Reset' button 

        # creates 'Restart' button  
        self.restart_btn = wx.Button(self.wpanel,label='RESTART',pos=(67, 67),size=(156,65),style=wx.BORDER_RAISED)

        self.restart_btn.SetFont(btn_restart_font)# sets font for the exit button using variable 'btn_rst_font'

        self.restart_btn.SetForegroundColour('Black')# sets 'Reset' button Text as white

        self.restart_btn.SetBackgroundColour('Yellow')# sets 'Reset' button coloer as Blue

        self.restart_btn.SetToolTip("Click here to start again.")

        self.Bind(wx.EVT_BUTTON,self.restart,self.restart_btn)# combines 'Reset' button with its functions
     
    # Access button

        # Creates fonts for the  button
        btn_access_font = wx.Font(21, wx.ROMAN, wx.FONTSTYLE_NORMAL,
                                  wx.FONTWEIGHT_BOLD)  # Creates  fonts for 'Reset' button

        # Creates button
        self.open_folder_btn = wx.Button(self.wpanel, label='ACCESS', pos=(412,67), size=(156,65),
                                         style=wx.BORDER_RAISED)

        # Sets font for the button
        self.open_folder_btn.SetFont(btn_access_font)

        # Sets the given colour for the button
        self.open_folder_btn.SetForegroundColour('White')

        # Sets the given colour for the button
        self.open_folder_btn.SetBackgroundColour('CORNFLOWER BLUE')

        # Sets features pop-up with given details
        self.open_folder_btn.SetToolTip("Click here to open '{}' folder.".format(bat_folder_name))

        # Combines buttons with it's respective functions
        self.Bind(wx.EVT_BUTTON, self.open_batdirs, self.open_folder_btn)

    # close window button

        self.Bind(wx.EVT_CLOSE,self.Close)# combines 'X' window button with its functions

    def open_batdirs(self,event):
        """ Verify 'path.json' if exists or not """
        path_json_fl_exists = os.path.exists(app_datas_json_file_path)

        if path_json_fl_exists == False:

            dir_dlgbox = wx.DirDialog(self.wpanel,"Please choose path (or directory) to hold '{}'".format(bat_folder_name), "",
                                      wx.DD_DEFAULT_STYLE | wx.DD_CHANGE_DIR)

            # dir_dlgbox.Set(wDir_path)

            if dir_dlgbox.ShowModal() == wx.ID_OK:

                usr_rt_v = dir_dlgbox.GetPath()

                # returned_path, returned_executor = read_json(json_flpath=app_datas_json_file_path)

                save_json(json_flpath=app_datas_json_file_path,infos1=usr_rt_v,infos2=uiexe_fl)

                settings_path_saved_msg = wx.MessageDialog(self.wpanel, "Path saved.", "Path save - Complete:",
                                                           wx.OK | wx.ICON_INFORMATION)

                settings_path_saved_msg.ShowModal()

            else:
                pass
        else:
            pass

        try:

            returned_path, returned_executor = read_json(json_flpath=app_datas_json_file_path)

            init_bat_dir = os.path.join(returned_path ,bat_folder_name)

            crnt_yrs_folder_path = os.path.join(init_bat_dir, dt_yyyy)

            crnt_mnthsno_months = os.path.join(crnt_yrs_folder_path, dt_mnthsno_mnths)

            now_date_folder_path = os.path.join(crnt_mnthsno_months, dt_date)

            dirs_shortcut_maker3Rev2C(path1=init_bat_dir,path2=crnt_yrs_folder_path,path3=crnt_mnthsno_months,path4=now_date_folder_path)

            os.startfile(now_date_folder_path)
        except FileNotFoundError:
            pass
    

    def save_appdatas(self):
        """ Verify 'path.json' if exists or not """
        path_json_fl_exists = os.path.exists(app_datas_json_file_path)

        if path_json_fl_exists == False:

            dir_dlgbox = wx.DirDialog(self.wpanel,"Please choose path (or directory) to hold '{}'".format(bat_folder_name), "",
                                      wx.DD_DEFAULT_STYLE | wx.DD_CHANGE_DIR)

            # dir_dlgbox.Set(wDir_path)

            if dir_dlgbox.ShowModal() == wx.ID_OK:

                usr_rt_v = dir_dlgbox.GetPath()

                # returned_path, returned_executor = read_json(json_flpath=app_datas_json_file_path)

                save_json(json_flpath=app_datas_json_file_path,infos1=usr_rt_v,infos2=uiexe_fl)

                settings_path_saved_msg = wx.MessageDialog(self.wpanel, "Path saved.", "Path save - Complete:",
                                                           wx.OK | wx.ICON_INFORMATION)

                settings_path_saved_msg.ShowModal()

            else:
                pass
        else:
            pass

    def modify(self,event):

        mode_modify_path_lists = ["Choose here to change the path of UiPath's executor (UiRobot.exe app) automatically.",
                                  "Choose here to change the path of UiPath's executor (UiRobot.exe app) manually.",
                                  "Choose here to change path of the '{}' folder.".format(bat_folder_name),
                                  "Choose here to change the UiPath's executor (UiRobot.exe app) name automatically.",
                                  "Choose here to change the UiPath's executor (UiRobot.exe app) path manually.",
                                  "Choose here to change the UiPath's executor (UiRobot.exe app) name manually."]

        onechoice_modes = wx.SingleChoiceDialog(self.wpanel, "Which settings do you wish to change?",
                                                 'Settings modify:', mode_modify_path_lists)

        # choosen_choice_var = onechoice_modes.GetStringSelection()

        if onechoice_modes.ShowModal() == wx.ID_OK:

            # print ("YT saver mode, %s\n" % onechoice.GetStringSelection())
            # print(onechoice_modes.GetStringSelection())

            if onechoice_modes.GetStringSelection() == mode_modify_path_lists[0]:

                try:

                    returned_path, returned_executor = read_json(json_flpath=app_datas_json_file_path)

                    for root, dirs, files in os.walk("c:\\"):

                        for file in files:
                            if file == returned_executor:
                                full_exe_path = os.path.join(root, file)

                                uiPath_appinfos_dict = {
                                    "Bot_executorpath": str(full_exe_path)
                                }

                                save_uipath_infos_json(json_flpath=uipath_appinfos_srcfl_path,infos=uiPath_appinfos_dict)

                                print("Data saved...")

                                data_transfer_msg_box = wx.MessageDialog(self.wpanel, "Data transferred...",
                                                                         "{} - UiPath version updation success:".format(
                                                                             app_title),
                                                                         wx.ICON_INFORMATION | wx.STAY_ON_TOP)
                                data_transfer_msg_box.ShowModal()

                                print("Data transferred...")

                                # delay(0.16)

                                break
                            else:
                                pass

                        if os.path.exists(uipath_appinfos_srcfl_path) == True:
                            break
                        else:
                            pass

                except FileNotFoundError:
                    self.save_appdatas()

                    if os.path.exists(app_datas_json_file_path) == True:
                        returned_path, returned_executor = read_json(json_flpath=app_datas_json_file_path)

                        for root, dirs, files in os.walk("c:\\"):

                            for file in files:
                                if file == returned_executor:
                                    full_exe_path = os.path.join(root, file)

                                    uiPath_appinfos_dict = {
                                        "Bot_executorpath": str(full_exe_path)
                                    }

                                    save_uipath_infos_json(json_flpath=uipath_appinfos_srcfl_path,infos=uiPath_appinfos_dict)

                                    print("Data saved...")

                                    data_transfer_msg_box = wx.MessageDialog(self.wpanel, "Data transferred...",
                                                                             "{} - UiPath version updation success:".format(
                                                                                 app_title),
                                                                             wx.ICON_INFORMATION | wx.STAY_ON_TOP)
                                    data_transfer_msg_box.ShowModal()

                                    print("Data transferred...")

                                    # delay(0.16)

                                    break
                                else:
                                    pass

                            if os.path.exists(uipath_appinfos_srcfl_path) == True:
                                break
                            else:
                                pass

            elif onechoice_modes.GetStringSelection() == mode_modify_path_lists[4]:
                while True:
                    manual_modify_UiRobot_execfl_dlgbox = wx.TextEntryDialog(frame, 'Enter the full path of the bot executor file (Eg: UiRobot.exe)', 'Executor file modify settings:')

                    if manual_modify_UiRobot_execfl_dlgbox.ShowModal() == wx.ID_OK:
                        manual_botexec_v = manual_modify_UiRobot_execfl_dlgbox.GetValue()

                        manual_botexecfl_v = os.path.basename(manual_botexec_v)

                        if os.path.exists(manual_botexec_v)== True:

                            try:

                                update_json_exe(json_flpath=app_datas_json_file_path, infos=str(manual_botexecfl_v))

                                update_made_msg = wx.MessageDialog(self.wpanel, "App name changed.",
                                                                   "App update - Complete",
                                                                   wx.OK | wx.ICON_INFORMATION)

                                update_made_msg.ShowModal()

                                # [Early-tests type] 'folder json file' operation
                                # path_json = open(et_app_datas_json_file_path, 'r')

                                returned_path, returned_executor = read_json(json_flpath=app_datas_json_file_path)

                                init_bat_dir = os.path.join(returned_path, bat_folder_name)

                                crnt_yrs_folder_path = os.path.join(init_bat_dir, dt_yyyy)

                                crnt_mnthsno_months = os.path.join(crnt_yrs_folder_path, dt_mnthsno_mnths)

                                now_date_folder_path = os.path.join(crnt_mnthsno_months, dt_date)

                                dirs_shortcut_maker3Rev2C(path1=init_bat_dir, path2=crnt_yrs_folder_path,
                                                      path3=crnt_mnthsno_months, path4=now_date_folder_path)

                                break

                            except FileNotFoundError:

                                returned_path, returned_executor = read_json(json_flpath=app_datas_json_file_path)

                                save_json(json_flpath=app_datas_json_file_path, infos1=returned_path,
                                          infos2=str(manual_botexecfl_v))

                                settings_path_saved_msg = wx.MessageDialog(self.wpanel, "App name saved.",
                                                                           "App save - Complete",
                                                                           wx.OK | wx.ICON_INFORMATION)

                                settings_path_saved_msg.ShowModal()

                                # [Early-tests type] 'folder json file' operation
                                # path_json = open(et_app_datas_json_file_path, 'r')

                                init_bat_dir = os.path.join(returned_path, bat_folder_name)

                                crnt_yrs_folder_path = os.path.join(init_bat_dir, dt_yyyy)

                                crnt_mnthsno_months = os.path.join(crnt_yrs_folder_path, dt_mnthsno_mnths)

                                now_date_folder_path = os.path.join(crnt_mnthsno_months, dt_date)

                                dirs_shortcut_maker3Rev2C(path1=init_bat_dir, path2=crnt_yrs_folder_path,
                                                      path3=crnt_mnthsno_months, path4=now_date_folder_path)

                                break

                        else:

                            file_missing_msgbox = wx.MessageDialog(self.wpanel, "File not found.",
                                                               "{} - file found error:".format(app_title),
                                                               wx.ICON_ERROR | wx.STAY_ON_TOP)

                            file_missing_msgbox.ShowModal()

                            # break
                    # pass
                    else:
                        break

            elif onechoice_modes.GetStringSelection() == mode_modify_path_lists[5]:
                while True:
                    manual_modify_UiRobot_execfl_dlgbox = wx.TextEntryDialog(frame, 'Enter the name of the bot executor file (Eg: UiRobot.exe)', 'Executor file modify settings:')

                    if manual_modify_UiRobot_execfl_dlgbox.ShowModal() == wx.ID_OK:
                        manual_botexecfl_v = manual_modify_UiRobot_execfl_dlgbox.GetValue()

                        try:

                            update_json_exe(json_flpath=app_datas_json_file_path, infos=str(manual_botexecfl_v))

                            update_made_msg = wx.MessageDialog(self.wpanel, "App name changed.",
                                                               "App update - Complete",
                                                               wx.OK | wx.ICON_INFORMATION)

                            update_made_msg.ShowModal()

                            # [Early-tests type] 'folder json file' operation
                            # path_json = open(et_app_datas_json_file_path, 'r')

                            returned_path, returned_executor = read_json(json_flpath=app_datas_json_file_path)

                            init_bat_dir = os.path.join(returned_path, bat_folder_name)

                            crnt_yrs_folder_path = os.path.join(init_bat_dir, dt_yyyy)

                            crnt_mnthsno_months = os.path.join(crnt_yrs_folder_path, dt_mnthsno_mnths)

                            now_date_folder_path = os.path.join(crnt_mnthsno_months, dt_date)

                            dirs_shortcut_maker3Rev2C(path1=init_bat_dir, path2=crnt_yrs_folder_path,
                                                  path3=crnt_mnthsno_months, path4=now_date_folder_path)

                            break

                        except FileNotFoundError:

                            returned_path, returned_executor = read_json(json_flpath=app_datas_json_file_path)

                            save_json(json_flpath=app_datas_json_file_path, infos1=returned_path,
                                      infos2=str(manual_botexecfl_v))

                            settings_path_saved_msg = wx.MessageDialog(self.wpanel, "App name saved.",
                                                                       "App save - Complete",
                                                                       wx.OK | wx.ICON_INFORMATION)

                            settings_path_saved_msg.ShowModal()

                            # [Early-tests type] 'folder json file' operation
                            # path_json = open(et_app_datas_json_file_path, 'r')

                            init_bat_dir = os.path.join(returned_path, bat_folder_name)

                            crnt_yrs_folder_path = os.path.join(init_bat_dir, dt_yyyy)

                            crnt_mnthsno_months = os.path.join(crnt_yrs_folder_path, dt_mnthsno_mnths)

                            now_date_folder_path = os.path.join(crnt_mnthsno_months, dt_date)

                            dirs_shortcut_maker3Rev2C(path1=init_bat_dir, path2=crnt_yrs_folder_path,
                                                  path3=crnt_mnthsno_months, path4=now_date_folder_path)

                            break

                    else:
                        break


            elif onechoice_modes.GetStringSelection() == mode_modify_path_lists[2]:

                while True:

                    modify_dir_dlgbox = wx.DirDialog(self.wpanel, "Please choose directory (or Path) to be changed:", "",
                                                    wx.DD_DEFAULT_STYLE | wx.DD_CHANGE_DIR)

                    if modify_dir_dlgbox.ShowModal() == wx.ID_OK:

                        usr_rt_v = modify_dir_dlgbox.GetPath()

                        if usr_rt_v == "":

                            invld_err_input = wx.MessageDialog(self.wpanel, "Null values are not accepted.",
                                                            "{} - input verifier error:".format(app_title),
                                                            wx.ICON_ERROR | wx.STAY_ON_TOP)

                            invld_err_input.ShowModal()

                        else:

                            try:
                                update_json_path(json_flpath=app_datas_json_file_path,infos=str(usr_rt_v))

                                update_made_msg = wx.MessageDialog(self.wpanel, "Path changed.", "Path update - Complete",
                                                                wx.OK | wx.ICON_INFORMATION)

                                update_made_msg.ShowModal()

                                # [Early-tests type] 'folder json file' operation
                                # path_json = open(et_app_datas_json_file_path, 'r')

                                returned_path, returned_executor = read_json(json_flpath=app_datas_json_file_path)

                                init_bat_dir = os.path.join(returned_path, bat_folder_name)

                                crnt_yrs_folder_path = os.path.join(init_bat_dir, dt_yyyy)

                                crnt_mnthsno_months = os.path.join(crnt_yrs_folder_path, dt_mnthsno_mnths)

                                now_date_folder_path = os.path.join(crnt_mnthsno_months, dt_date)

                                dirs_shortcut_maker3Rev2C(path1=init_bat_dir, path2=crnt_yrs_folder_path,
                                                      path3=crnt_mnthsno_months, path4=now_date_folder_path)

                                break

                            except FileNotFoundError:

                                save_json(json_flpath=app_datas_json_file_path, infos1=usr_rt_v, infos2=uiexe_fl)

                                settings_path_saved_msg = wx.MessageDialog(self.wpanel, "Path saved.", "Path update - Complete",
                                                                        wx.OK | wx.ICON_INFORMATION)

                                settings_path_saved_msg.ShowModal()

                                # [Early-tests type] 'folder json file' operation
                                # path_json = open(et_app_datas_json_file_path, 'r')

                                returned_path, returned_executor = read_json(json_flpath=app_datas_json_file_path)

                                init_bat_dir = os.path.join(returned_path ,bat_folder_name)

                                crnt_yrs_folder_path = os.path.join(init_bat_dir, dt_yyyy)

                                crnt_mnthsno_months = os.path.join(crnt_yrs_folder_path, dt_mnthsno_mnths)

                                now_date_folder_path = os.path.join(crnt_mnthsno_months, dt_date)

                                dirs_shortcut_maker3Rev2C(path1=init_bat_dir, path2=crnt_yrs_folder_path,
                                                      path3=crnt_mnthsno_months, path4=now_date_folder_path)

                                break
            
                    else:
                        break

            elif onechoice_modes.GetStringSelection() == mode_modify_path_lists[1]:
                while True:

                    returned_path, returned_executor = read_json(json_flpath=app_datas_json_file_path)

                    modify_filedir_dlgbox = wx.FileDialog(self.wpanel, "Please choose '{}' file:".format(returned_executor), "C:",returned_executor,"Application files (.exe) |*.exe",wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

                    if modify_filedir_dlgbox.ShowModal() == wx.ID_OK:

                        fileroot_v = modify_filedir_dlgbox.GetPath()

                        #print(fileroot_v)

                        if fileroot_v == "":

                            invld_err_input = wx.MessageDialog(self.wpanel, "Null values are not accepted.",
                                                            "{} - input verifier error:".format(app_title),
                                                            wx.ICON_ERROR | wx.STAY_ON_TOP)

                            invld_err_input.ShowModal()

                        else:

                            if returned_executor in fileroot_v:

                                #full_exe_path2 = os.path.join(root_v, returned_executor)

                                try:
                                    uiPath_appinfos_dict= {
                                        "Bot_executorpath": str(fileroot_v)
                                        }

                                    save_uipath_infos_json(json_flpath=uipath_appinfos_srcfl_path,infos=uiPath_appinfos_dict)

                                    data_transfer_msg_box = wx.MessageDialog(self.wpanel, "Data transferred...",
                                                                            "{} - UiPath version updation success:".format(
                                                                                app_title), wx.ICON_INFORMATION | wx.STAY_ON_TOP)
                                    data_transfer_msg_box.ShowModal()

                                    delay(0.16)

                                    break

                                except FileNotFoundError:

                                    settings_json = open(uipath_appinfos_srcfl_path, 'w')

                                    settings_json.write("{"'"Bot_executorpath"'":")

                                    uiPath_appinfos_dict = {
                                            "Bot_executorpath": str(fileroot_v)
                                    }

                                    save_uipath_infos_json(json_flpath=uipath_appinfos_srcfl_path,infos=uiPath_appinfos_dict)

                                    settings_json.close()

                                    data_transfer_msg_box = wx.MessageDialog(self.wpanel, "Data transferred...",
                                                                            "{} - UiPath version updation success:".format(
                                                                                app_title), wx.ICON_INFORMATION | wx.STAY_ON_TOP)
                                    data_transfer_msg_box.ShowModal()

                                    # [Early-tests type] 'folder json file' operation
                                        # path_json = open(et_app_datas_json_file_path, 'r')

                                    break
                            else:

                                app_not_UiRobot_err = wx.MessageDialog(self.wpanel,"Opps! Sorry coundn't save changes since requested application is not '{}' file.".format(returned_executor),"{} - UiPath settings update error:".format(app_title),wx.ICON_ERROR| wx.STAY_ON_TOP)
                                            
                                app_not_UiRobot_err.ShowModal()
                    else:
                        break


            elif onechoice_modes.GetStringSelection() == mode_modify_path_lists[3]:
                while True:

                    modify_UiRobot_execfl_dlgbox = wx.FileDialog(self.wpanel, "Please choose file to change executor name:", "","",wildcard="All files (*.*)|*.*; | Application exceutor file (*.exe) |*.exe",style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

                    if modify_UiRobot_execfl_dlgbox.ShowModal() == wx.ID_OK:

                        usr_botexec_v = modify_UiRobot_execfl_dlgbox.GetPath()

                        usr_botexecfl_v = os.path.basename(usr_botexec_v)

                        try:

                            update_json_exe(json_flpath=app_datas_json_file_path, infos=str(usr_botexecfl_v))

                            update_made_msg = wx.MessageDialog(self.wpanel, "App name changed.",
                                                                   "App update - Complete",
                                                                   wx.OK | wx.ICON_INFORMATION)

                            update_made_msg.ShowModal()

                            # [Early-tests type] 'folder json file' operation
                            # path_json = open(et_app_datas_json_file_path, 'r')

                            returned_path, returned_executor = read_json(json_flpath=app_datas_json_file_path)

                            init_bat_dir = os.path.join(returned_path, bat_folder_name)

                            crnt_yrs_folder_path = os.path.join(init_bat_dir, dt_yyyy)

                            crnt_mnthsno_months = os.path.join(crnt_yrs_folder_path, dt_mnthsno_mnths)

                            now_date_folder_path = os.path.join(crnt_mnthsno_months, dt_date)

                            dirs_shortcut_maker3Rev2C(path1=init_bat_dir, path2=crnt_yrs_folder_path,
                                                  path3=crnt_mnthsno_months, path4=now_date_folder_path)
                            break

                        except FileNotFoundError:

                            returned_path, returned_executor = read_json(json_flpath=app_datas_json_file_path)

                            save_json(json_flpath=app_datas_json_file_path, infos1=returned_path, infos2=str(usr_botexecfl_v))

                            settings_path_saved_msg = wx.MessageDialog(self.wpanel, "App name saved.",
                                                                           "App save - Complete",
                                                                           wx.OK | wx.ICON_INFORMATION)

                            settings_path_saved_msg.ShowModal()

                            # [Early-tests type] 'folder json file' operation
                            # path_json = open(et_app_datas_json_file_path, 'r')

                            init_bat_dir = os.path.join(returned_path, bat_folder_name)

                            crnt_yrs_folder_path = os.path.join(init_bat_dir, dt_yyyy)

                            crnt_mnthsno_months = os.path.join(crnt_yrs_folder_path, dt_mnthsno_mnths)

                            now_date_folder_path = os.path.join(crnt_mnthsno_months, dt_date)

                            dirs_shortcut_maker3Rev2C(path1=init_bat_dir, path2=crnt_yrs_folder_path,
                                                  path3=crnt_mnthsno_months, path4=now_date_folder_path)

                            break

                    else:
                        break

                # pass

            else:
                pass

        else:
            pass

    def start(self,event):

        #sys.exit()

        """ Verify 'path.json' if exists or not """
        settings_json_paths_exists = os.path.exists(app_datas_json_file_path)

        if settings_json_paths_exists == False:

            dir_dlgbox = wx.DirDialog(self.wpanel,"Please choose path (or directory) to hold '{}'".format(bat_folder_name), "",
                                      wx.DD_DEFAULT_STYLE | wx.DD_CHANGE_DIR)

            # dir_dlgbox.Set(wDir_path)
            if dir_dlgbox.ShowModal() == wx.ID_OK:

                usr_rt_v = dir_dlgbox.GetPath()

                # returned_path, returned_executor = read_json(json_flpath=app_datas_json_file_path)

                save_json(json_flpath=app_datas_json_file_path,infos1=usr_rt_v,infos2=uiexe_fl)

                settings_path_saved_msg = wx.MessageDialog(self.wpanel, "Path saved.", "Path update - Complete",
                                                           wx.OK | wx.ICON_INFORMATION)

                settings_path_saved_msg.ShowModal()

            else:
                pass
        else:
            pass

        try:
            # [Early-tests type] 'folder json file' operation
            #path_json = open(et_app_datas_json_file_path, 'r')

            returned_path, returned_executor = read_json(json_flpath=app_datas_json_file_path)

            init_bat_dir = os.path.join(returned_path, bat_folder_name)

            crnt_yrs_folder_path = os.path.join(init_bat_dir, dt_yyyy)

            crnt_mnthsno_months = os.path.join(crnt_yrs_folder_path, dt_mnthsno_mnths)

            now_date_folder_path = os.path.join(crnt_mnthsno_months, dt_date)

            dirs_shortcut_maker3Rev2C(path1=init_bat_dir, path2=crnt_yrs_folder_path, path3=crnt_mnthsno_months,
                                  path4=now_date_folder_path)

            init_bat_fl_path = os.path.join(now_date_folder_path, init_batfl_name)

            json_file_exists = os.path.exists(uipath_appinfos_srcfl_path)

            if json_file_exists is False:

                for root, dirs, files in os.walk("c:\\"):

                    for file in files:
                        if file == returned_executor:
                            full_exe_path = os.path.join(root, file)
                            
                            uiPath_appinfos_dict = {
                                "Bot_executorpath" : str(full_exe_path)
                            }


                            save_uipath_infos_json(json_flpath=uipath_appinfos_srcfl_path,infos=uiPath_appinfos_dict)

                            data_transfer_msg_box = wx.MessageDialog(self.wpanel, "Data transferred...",
                                                                    "{} - UiPath version updation success:".format(
                                                                        app_title), wx.ICON_INFORMATION | wx.STAY_ON_TOP)
                            data_transfer_msg_box.ShowModal()

                            #delay(0.16)

                            break
                        else:
                            pass

            else:
                pass

            #delay(2.89)

            while True:

                uipath_filedir_dlgbox = wx.FileDialog(self.wpanel, "Please choose file:", "Main","",wildcard="All files (*.*)|*.*; | Workflow files (*.xaml) |*.xaml; | Workflow project packages (*.nupkg) |*.nupkg",style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
                
                if uipath_filedir_dlgbox.ShowModal() == wx.ID_OK:

                    file_choosen = uipath_filedir_dlgbox.GetPath()

                    if '.xaml'in file_choosen :

                        data_transfer_sucess_msg_box = wx.MessageDialog(self.wpanel,"Data successfully accquired and ready to run UiPath project package '{}'.".format(os.path.basename(file_choosen)),"{} - UiPath robot execution success:".format(app_title),wx.ICON_INFORMATION| wx.STAY_ON_TOP)
                                
                        data_transfer_sucess_msg_box.ShowModal()

                        uipath_batch_support_runner_maker_3Rev2C(uipath_infos_json=uipath_appinfos_srcfl_path,
                                                             uipath_files_rt=file_choosen,
                                                             init_bat_fl_path1=init_bat_fl_path)

                        break

                    elif ".nupkg" in file_choosen:

                        data_transfer_sucess_msg_box = wx.MessageDialog(self.wpanel,"Data successfully accquired and ready to run UiPath project package '{}'.".format(os.path.basename(file_choosen)),"{} - UiPath robot execution success:".format(app_title),wx.ICON_INFORMATION| wx.STAY_ON_TOP)
                                
                        data_transfer_sucess_msg_box.ShowModal()

                        uipath_batch_support_runner_maker_3Rev2C(uipath_infos_json=uipath_appinfos_srcfl_path,
                                                             uipath_files_rt=file_choosen,
                                                                 init_bat_fl_path1=init_bat_fl_path)

                        break
                    else:
                        invalid_err = wx.MessageDialog(self.wpanel,"Input invalid.","{} - input verifier error:".format(app_title),wx.ICON_ERROR| wx.STAY_ON_TOP)
                                        
                        invalid_err.ShowModal()
                else:
                    break

        except OSError:
            pass
    def restart(self,event):

        """ Verify 'path.json' if exists or not """
        paths_json_paths_exists = os.path.exists(app_datas_json_file_path)

        if paths_json_paths_exists == False:

            dir_dlgbox = wx.DirDialog(self.wpanel,"Please choose path (or directory) to hold '{}'".format(bat_folder_name), "",
                                      wx.DD_DEFAULT_STYLE | wx.DD_CHANGE_DIR)

            # dir_dlgbox.Set(wDir_path)
            if dir_dlgbox.ShowModal() == wx.ID_OK:

                usr_rt_v = dir_dlgbox.GetPath()

                returned_path, returned_executor = read_json(json_flpath=app_datas_json_file_path)

                save_json(json_flpath=app_datas_json_file_path,infos1=usr_rt_v,infos2=uiexe_fl)

                settings_path_saved_msg = wx.MessageDialog(self.wpanel, "Path saved.", "Path update - Complete",
                                                           wx.OK | wx.ICON_INFORMATION)

                settings_path_saved_msg.ShowModal()

            else:
                pass
        else:
            pass

        try:
            # [Early-tests type] 'folder json file' operation
            #path_json = open(et_app_datas_json_file_path, 'r')

            returned_path, returned_executor = read_json(json_flpath=app_datas_json_file_path)

            init_bat_dir = os.path.join(returned_path, bat_folder_name)

            crnt_yrs_folder_path = os.path.join(init_bat_dir, dt_yyyy)

            crnt_mnthsno_months = os.path.join(crnt_yrs_folder_path, dt_mnthsno_mnths)

            now_date_folder_path = os.path.join(crnt_mnthsno_months, dt_date)

            dirs_shortcut_maker3Rev2C(path1=init_bat_dir, path2=crnt_yrs_folder_path, path3=crnt_mnthsno_months,
                                  path4=now_date_folder_path)
            
            json_file_exists = os.path.exists(uipath_appinfos_srcfl_path)

            if json_file_exists is False:

                for root, dirs, files in os.walk("c:\\"):

                    for file in files:
                        if file == returned_executor:
                            full_exe_path = os.path.join(root, file)

                            uiPath_appinfos_dict = {
                                "Bot_executorpath": str(full_exe_path)
                            }

                            save_uipath_infos_json(json_flpath=uipath_appinfos_srcfl_path,infos=uiPath_appinfos_dict)

                            data_transfer_msg_box = wx.MessageDialog(self.wpanel, "Data transferred...",
                                                                    "{} - UiPath version updation success:".format(
                                                                        app_title), wx.ICON_INFORMATION | wx.STAY_ON_TOP)
                            data_transfer_msg_box.ShowModal()

                            delay(0.16)

                            break
                        else:
                            pass

                    if os.path.exists(uipath_appinfos_srcfl_path)==True:
                        break
                    else:
                        pass
            else:
                pass


            init_bat_fl_path = os.path.join(now_date_folder_path ,init_batfl_name)

            init_bat_flexists = os.path.exists(init_bat_fl_path)

            if init_bat_flexists==False:
                self.start(event)
            else:
                os.startfile(init_bat_fl_path)


        except FileNotFoundError:
            pass               
    def exitbutton(self,event):
        
        ''' Asks user whether to use again as message box. if not, clears the values for the user, or exits the app if yes  '''
        yn_msgbox = wx.MessageDialog(self.wpanel,"Are you sure you want to exit the app?","Yes/No:",wx.YES_NO| wx.ICON_WARNING)

        yn_var = yn_msgbox.ShowModal()

        if yn_var == wx.ID_NO:
            pass
        else:
            self.Destroy()# closes app when 'EXIT' button is click

    def Close(self,event):
        self.Destroy()# closes app  when 'CLOSE' or 'X' on the window is pressed

if __name__=='__main__':

    dirs_maker(path1=dependies_folder_path,path2=settings_folder_path,path3=UiRobot_infos_dirs)

    app=wx.App()# Start the app

    frame = app_ui(parent=None,id=-1)# Gives parametres or infos to the class or 'Frame' components

    frame.Show()# Shows the commponents existed within the app

    app.MainLoop()# loops the window as systems close apps within milliseconds or more
