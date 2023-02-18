import os
import shutil

import wx
import json
import datetime
from PySide2.QtCore import QTimer
from PySide2.QtWidgets import QApplication , QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QPushButton, QFileDialog, QVBoxLayout
import time
import winshell
from win32com.client import Dispatch
'''Source files'''
#wDir_path = os.path.dirname(os.path.realpath(__file__))# curent working directory or the 'Now'-location of the file.

wDir_path = os.getcwd()

for file in os.listdir(wDir_path):
    #print(file)
    if '.ico' in file:
        try:
            ico_flpath =os.path.join(wDir_path,file)
        except OSError:
            pass
    else:
        pass


# --------------------------------------------------------------------------------------------------

''' Real-Time Date&Time datas '''
# Time
dt_clockH = datetime.datetime.now().strftime("%I").lstrip("0").replace(" 0", " ")

dt_clockM = datetime.datetime.now().strftime("%M").lstrip("0").replace(" 0", " ")

dt_clockS = datetime.datetime.now().strftime("%S").lstrip("0").replace(" 0", " ")

dt_clockMS = datetime.datetime.now().strftime("%f")

epoch_miliseconds = int(time.time() * 1000)

dt_TMR = "{0}-{1}-{2}".format(dt_clockH,dt_clockM,dt_clockS)

dt_DN = datetime.datetime.now().strftime('%p').lower()

# Date
dt_dd = datetime.datetime.now().strftime("%d")

dt_mm = datetime.datetime.now().strftime("%m")

dt_yyyy = datetime.datetime.now().strftime("%Y")

dt_wdys = datetime.datetime.now().strftime("%A").lower()

dt_mnths = datetime.datetime.now().strftime("%B")

dt_mnths_no = datetime.datetime.now().strftime("%m")

dt_date = "{0}.{1}.{2}".format(dt_dd,dt_mm,dt_yyyy)

dt_mnthsno_mnths = "{0}-{1}".format(dt_mnths_no,dt_mnths)

dtdd_dtmnths = "{0}-{1}".format(dt_dd,dt_mnths)

# print(dt_mnthsno_mnths)
# print(dt_date)
# print(dtdd_dtmnths)

# Current file name infos
'''File name & File extension'''
file_name, file_type = os.path.splitext(os.path.basename(os.path.abspath(__file__)))

# =======================================================================================

#                     eT [Early-Tests] App infos

# ---------------------------------------------------------------------------------------
''' Settings file path '''
# eT [Early-Tests] type type App Json files details
et_json_name = '{}_datas'.format(file_name)

et_paths_infos_flname_json= '{}.json'.format(et_json_name)

et_settings_json_fl_rt = os.path.join(wDir_path,et_paths_infos_flname_json)

''' App Details '''
# eT [Early-Tests] type type app title PF+
et_app_title = "Folder Create:Auto PF+ (Sf-c) [early-tests.Id: {}]".format(file_name)

# eT [Early-Tests] type type audio folder with app name
et_audio_app_folder_name = '{} audios'.format(file_name)

# -----------------------------------------------------------------------------------------


# =======================================================================================

#                     App infos

# ---------------------------------------------------------------------------------------
''' Folder names '''
# Folder with app name
main_folder_name = 'Folder Create Auto-2 PEF++ (Sudha Fashion-custom)'
#audio_app_folder_name = '{} audios'.format(main_mp3s_folder_name)

# -----------------------------------------------------------------------------------------

''' Settings file path '''
# App Json files details
json_name = 'app_datas'

json_fl_name = '{}.json'.format(json_name)

appdatas_json_fl_rt = os.path.join(wDir_path,json_fl_name)

# Path json files details
json_name1 = 'path_datas'

json_fl_name = '{}.json'.format(json_name1)

path_json_fl_rt = os.path.join(wDir_path,json_fl_name)

# App title
app_title = "Folder Create: Auto-2 [Perfected.Even.Further++] (Sudha Fashion-custom)"

# App datas
# Client lists
client_lsts = []

# ---------------------------------------------------------------------------

def delay(var):
    time.sleep(var)

def msg_autoClose(msg_title,msg_text,close_tmr):

    qm = QMessageBox()
    qm.setWindowTitle(msg_title)
    qm.setText(msg_text)
    qm.setStandardButtons(QMessageBox.Ok)
    QTimer.singleShot(close_tmr*1000,lambda : qm.done(0))
    qm.setFixedWidth(800)
    qm.setFixedHeight(1755)
    qm.exec_()

def dirs_shortcut__make(path0,path1,path2,path3):
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

    ''' Make 'AppName' shortcut '''
    desktop = winshell.desktop()
    path = os.path.join(desktop, '{} - Shortcut.lnk'.format(main_folder_name))

    target_rt = path0
    wDir_rt = path0

    if os.path.exists(path)==False:

        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = target_rt
        shortcut.WorkingDirectory = wDir_rt
        shortcut.save()
    else:
        pass


class app_ui(wx.Frame):

    # Starts frame upon user request or 'CLICKING' the app
    def __init__(self, parent, id):

        # Window (Frame) with parametres i.e (frame, parent=None,id=-1.'window title',size=(int,int),style=wx.(obj))
        wx.Frame.__init__(self, parent, id, app_title, size=(695, 386),
                          style=wx.DEFAULT_FRAME_STYLE & ~wx.MAXIMIZE_BOX ^ wx.RESIZE_BORDER)

        try:
            self.SetIcon(wx.Icon(ico_flpath))  # sets icon on the window title bar

            # print(ico_flpath)
        except NameError:
            pass

        self.wpanel = wx.Panel(self)  # setting 'container' to have wxpython GUI parts

        self.wpanel.SetBackgroundColour('Steel blue')  # sets the panel or app background

    # ------------------------------------------------------------------------------------
    # Exit button

        # creates fonts for button
        btn_exit_font = wx.Font(22, wx.ROMAN, wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_BOLD)

        # creates button
        self.exit_btn = wx.Button(self.wpanel, label='Exit', pos=(54, 221), size=(164, 45), style=wx.BORDER_RAISED)

        self.exit_btn.SetFont(btn_exit_font)  # sets font for the button

        # sets button text color
        self.exit_btn.SetForegroundColour('White')

        # sets button color
        self.exit_btn.SetBackgroundColour('Red')

        # sets features exit details
        self.exit_btn.SetToolTip("Click here to exit or close the app.")

        # combines button with its functions
        self.Bind(wx.EVT_BUTTON, self.exitbutton, self.exit_btn)

    # Create button

        # Creates fonts for button
        btn_access_font = wx.Font(21, wx.ROMAN, wx.FONTSTYLE_NORMAL,
                                  wx.FONTWEIGHT_BOLD)

        # Creates button
        self.make_dirs_btn = wx.Button(self.wpanel, label='Update/Create name', pos=(177, 148), size=(268, 45),
                                         style=wx.BORDER_RAISED)

        # Sets font for the button using variable
        self.make_dirs_btn.SetFont(btn_access_font)

        # Sets the given colour for the button text
        self.make_dirs_btn.SetForegroundColour('Black')

        # Sets the given colour for the button ( button BG colour )
        self.make_dirs_btn.SetBackgroundColour('Green')

        # Sets tooltip (pop-up details)
        self.make_dirs_btn.SetToolTip("Click here to add name to the lists.")

        # Combines button with its respective functions
        self.Bind(wx.EVT_BUTTON, self.update_names, self.make_dirs_btn)

    # Delete button

        # Creates fonts for the button
        btn_del_font = wx.Font(21, wx.ROMAN, wx.FONTSTYLE_NORMAL,
                               wx.FONTWEIGHT_BOLD)

        # Creates button
        self.del_btn = wx.Button(self.wpanel, label='Delete name', pos=(397, 78), size=(226, 45),
                                    style=wx.BORDER_RAISED)

        # Sets font for the button using variable
        self.del_btn.SetFont(btn_del_font)

        # Sets the given colour for the button text
        self.del_btn.SetForegroundColour('Red')

        # Sets the given colour for the button ( button BG colour )
        self.del_btn.SetBackgroundColour('Black')

        # Sets features pop-up with given details
        self.del_btn.SetToolTip("Click here to delete name from the lists.")

        # Combines buttons with it's respective functions
        self.Bind(wx.EVT_BUTTON, self.delete_names, self.del_btn)

    # Access button

        # creates fonts for button
        btn_access_font = wx.Font(22, wx.ROMAN, wx.FONTSTYLE_NORMAL,
                               wx.FONTWEIGHT_BOLD)

        # creates 'Access folder' button
        self.open_folder_btn = wx.Button(self.wpanel, label='Access', pos=(54, 78), size=(164, 45),
                                         style=wx.BORDER_RAISED)
        # sets font for the button
        self.open_folder_btn.SetFont(btn_access_font)

        # sets button text colour
        self.open_folder_btn.SetForegroundColour('Black')

        # sets button colour
        self.open_folder_btn.SetBackgroundColour('Yellow')

        self.open_folder_btn.SetToolTip(
            "Click here to open real-time date '{0}' sub folder.".format(dt_date))  # sets features pop-up details

    # Change path button

        # Creates fonts for the button
        btn_mod_font = wx.Font(21, wx.ROMAN, wx.FONTSTYLE_NORMAL,
                               wx.FONTWEIGHT_BOLD)

        # Creates button
        self.modify_btn = wx.Button(self.wpanel, label='Change path', pos=(397, 221), size=(226, 45), style=wx.BORDER_RAISED)

        # Sets font for the button using variable
        self.modify_btn.SetFont(btn_mod_font)

        # Sets the given colour for the button text
        self.modify_btn.SetForegroundColour('Red')

        # Sets the given colour for the button ( button BG colour )
        self.modify_btn.SetBackgroundColour('Yellow')

        # Sets features pop-up with given details
        self.modify_btn.SetToolTip("Click here to change path.")

        # Combines buttons with it's respective functions
        self.Bind(wx.EVT_BUTTON, self.changedir, self.modify_btn)

        self.Bind(wx.EVT_BUTTON, self.open_folder_dt, self.open_folder_btn)  # combines button with its functions

    def Close(self, event):
        self.Destroy()  # closes app  when 'CLOSE' or 'X' on the window is pressed

    def changedir(self,event):

        dir_dlgbox = wx.DirDialog(self.wpanel, "Please choose directory (or Path) to be changed:", "",
                                  wx.DD_DEFAULT_STYLE | wx.DD_CHANGE_DIR)

        if dir_dlgbox.ShowModal() == wx.ID_OK:

            try:

                usr_rt_v = dir_dlgbox.GetPath()

                pathjson_fl_r = open(path_json_fl_rt, "r")

                json_src_data = json.load(pathjson_fl_r)

                json_src_data["path"] = usr_rt_v

                pathjson_fl_w = open(path_json_fl_rt, "w")

                json.dump(json_src_data, pathjson_fl_w)

                pathjson_fl_r.close()

                pathjson_fl_w.close()

                pathjson_datas = open(path_json_fl_rt, 'r')

                data = pathjson_datas.read()

                self.path_infos_v = json.loads(data)["path"]

                src_path_data = self.path_infos_v

                appdatas_json_settings = open(appdatas_json_fl_rt, 'r')

                data2 = appdatas_json_settings.read()

                self.name_infos_v = json.loads(data2)["names_lsts"]

                src_name_data = self.name_infos_v

                print(src_name_data)

                for name in src_name_data:
                    print(name)
                    name_dirs_path_v = os.path.join(src_path_data, name)
                    now_yrs_sub_folder_v = os.path.join(name_dirs_path_v, dt_yyyy)
                    now_dtdd_dtmnth_sub_folder_v = os.path.join(now_yrs_sub_folder_v, dtdd_dtmnths)
                    dirs_shortcut__make(path0=src_path_data, path1=name_dirs_path_v, path2=now_yrs_sub_folder_v,
                                        path3=now_dtdd_dtmnth_sub_folder_v)

                update_made_msg = wx.MessageDialog(self.wpanel, "Path changed.", "Path update - Complete",
                                                   wx.OK | wx.ICON_INFORMATION)

                update_made_msg.ShowModal()

                appdatas_json_settings.close()

                pathjson_datas.close()

            except FileNotFoundError:

                usr_path = {
                    "path": str(usr_rt_v),


                }

                pathjson_file_datas = open(path_json_fl_rt, "w")

                json.dump(usr_path, pathjson_file_datas)

                pathjson_file_datas.close()

                appdatas_json = open(path_json_fl_rt, 'r')

                data = appdatas_json.read()

                self.path_infos_v = json.loads(data)["path"]

                src_path_data = self.path_infos_v

                appdatas_json_settings = open(appdatas_json_fl_rt, 'r')

                data2 = appdatas_json_settings.read()

                self.name_infos_v = json.loads(data2)["names_lsts"]

                src_name_data = self.name_infos_v

                for name in src_name_data:

                    name_dirs_path_v = os.path.join(src_path_data, name)
                    now_yrs_sub_folder_v = os.path.join(name_dirs_path_v, dt_yyyy)
                    now_dtdd_dtmnth_sub_folder_v = os.path.join(now_yrs_sub_folder_v, dtdd_dtmnths)
                    dirs_shortcut__make(path0=src_path_data, path1=name_dirs_path_v, path2=now_yrs_sub_folder_v,
                                        path3=now_dtdd_dtmnth_sub_folder_v)

                settings_path_saved_msg = wx.MessageDialog(self.wpanel, "Path saved.", "Path update - Complete",
                                                           wx.OK | wx.ICON_INFORMATION)

                settings_path_saved_msg.ShowModal()

    def delete_names(self,event):
        """ Verify '.json' if exists or not """
        path_settings_json_fl_exists = os.path.exists(path_json_fl_rt)
        data_settings_json_fl_exists = os.path.exists(appdatas_json_fl_rt)

        if data_settings_json_fl_exists == False:
            usr_datas = {

                "names_lsts": client_lsts
            }

            path_json_settings = open(appdatas_json_fl_rt, "w")

            json.dump(usr_datas, path_json_settings)

            path_json_settings.close()

            # msg_autoClose(msg_text="Data saved.                        ",
            #  msg_title="Datas update - Complete", close_tmr=3)
        else:
            pass


        if path_settings_json_fl_exists == False:

            dir_dlgbox = wx.DirDialog(self.wpanel, "Please choose directory (or Path):", "",
                                      wx.DD_DEFAULT_STYLE | wx.DD_CHANGE_DIR)

            # dir_dlgbox.Set(wDir_path)

            if dir_dlgbox.ShowModal() == wx.ID_OK:

                usr_rt_v = dir_dlgbox.GetPath()

                usr_path = {
                    "path": str(usr_rt_v)
                }

                path_json_settings_datas = open(path_json_fl_rt, "w")

                json.dump(usr_path, path_json_settings_datas)

                path_json_settings_datas.close()

                # msg_autoClose(msg_text="Data saved.                        ",
                # msg_title="Datas update - Complete", close_tmr=3)

            else:
                pass
        else:
            pass

        try:
            path_json_settings_datas = open(path_json_fl_rt, 'r')

            data1 = path_json_settings_datas.read()

            self.path_infos_v = json.loads(data1)["path"]

            src_path_data = self.path_infos_v

            appdatas_json_settings = open(appdatas_json_fl_rt, 'r')

            data2 = appdatas_json_settings.read()

            self.name_infos_v = json.loads(data2)["names_lsts"]

            src_name_data = self.name_infos_v

            print(src_name_data)

            while True:

                name_del_title = "{} - name delete entry".format(app_title)

                self.name_del_input = wx.TextEntryDialog(self.wpanel, "Please type the name to be removed below:",
                                                         name_del_title, '')

                if self.name_del_input.ShowModal() == wx.ID_OK:

                    name_del_in = self.name_del_input.GetValue()

                    if name_del_in != "":
                        if name_del_in in src_name_data:
                            src_name_data.remove(str(name_del_in))

                            print(src_name_data)

                            usr_datas_new_name_lists = {
                                "names_lsts": src_name_data
                            }

                            json_settings_file_datas = open(appdatas_json_fl_rt, "w")

                            json.dump(usr_datas_new_name_lists, json_settings_file_datas)

                            json_settings_file_datas.close()


                            name_del_dirs = os.path.join(src_path_data,name_del_in)

                            name_removed_msg = wx.MessageDialog(self.wpanel, "Name removed from the lists.",
                                                                "Name - Delete complete",
                                                                wx.OK | wx.ICON_INFORMATION)

                            name_removed_msg.ShowModal()

                            yn_del_msgbox = wx.MessageDialog(self.wpanel,
                                                         "Do you wish to delete '{}' folder.".format(name_del_in),
                                                         "Yes/No",
                                                         wx.YES_NO | wx.ICON_WARNING)

                            yn_del_var = yn_del_msgbox.ShowModal()

                            if yn_del_var == wx.ID_NO:

                                pass

                            else:

                                shutil.rmtree(name_del_dirs)

                                name_dirs_removed_msg = wx.MessageDialog(self.wpanel,
                                                        "'{}' folder deleted successfully.".format(name_del_in),
                                                                         "Folder - Delete complete",
                                                                         wx.OK | wx.ICON_INFORMATION)

                                name_dirs_removed_msg.ShowModal()

                            break
                        else:
                            name_not_found_err_msg = wx.MessageDialog(self.wpanel, "Name already removed or not found from the lists.",
                                                                "{} - input verifier error:".format(app_title),
                                                                wx.OK | wx.ICON_INFORMATION)

                            name_not_found_err_msg.ShowModal()
                    else:
                        invld_err_input = wx.MessageDialog(self.wpanel, "Null values are not accepted.",
                                                                   "{} - input verifier error:".format(
                                                                       app_title),
                                                                   wx.ICON_ERROR | wx.STAY_ON_TOP)

                        invld_err_input.ShowModal()
                else:
                    break

            path_json_settings_datas.close()
            appdatas_json_settings.close()
        except FileNotFoundError:
            pass

    def update_names(self,event):
        """ Verify '.json' if exists or not """
        path_settings_json_fl_exists = os.path.exists(path_json_fl_rt)
        data_settings_json_fl_exists = os.path.exists(appdatas_json_fl_rt)

        if data_settings_json_fl_exists == False:
            usr_datas = {

                "names_lsts": client_lsts
            }

            path_json_settings = open(appdatas_json_fl_rt, "w")

            json.dump(usr_datas, path_json_settings)

            path_json_settings.close()

            # msg_autoClose(msg_text="Data saved.                        ",
            #  msg_title="Datas update - Complete", close_tmr=3)
        else:
            pass


        if path_settings_json_fl_exists == False:

            dir_dlgbox = wx.DirDialog(self.wpanel, "Please choose directory (or Path):", "",
                                      wx.DD_DEFAULT_STYLE | wx.DD_CHANGE_DIR)

            # dir_dlgbox.Set(wDir_path)

            if dir_dlgbox.ShowModal() == wx.ID_OK:

                usr_rt_v = dir_dlgbox.GetPath()

                usr_path = {
                    "path": str(usr_rt_v)
                }

                path_json_settings_datas = open(path_json_fl_rt, "w")

                json.dump(usr_path, path_json_settings_datas)

                path_json_settings_datas.close()

                # msg_autoClose(msg_text="Data saved.                        ",
                # msg_title="Datas update - Complete", close_tmr=3)

            else:
                pass
        else:
            pass

        try:
            path_json_settings_datas = open(path_json_fl_rt, 'r')

            data1 = path_json_settings_datas.read()

            self.path_infos_v = json.loads(data1)["path"]

            src_path_data = self.path_infos_v

            appdatas_json_settings = open(appdatas_json_fl_rt, 'r')

            data2 = appdatas_json_settings.read()

            self.name_infos_v = json.loads(data2)["names_lsts"]

            src_name_data = self.name_infos_v

            print(src_name_data)

            while True:

                name_add_title = "{} - name update entry".format(app_title)

                self.name_add_input = wx.TextEntryDialog(self.wpanel, "Please type the name to be added below:",
                                                                name_add_title,'')

                if self.name_add_input.ShowModal() == wx.ID_OK:

                    name_in = self.name_add_input.GetValue()

                    if name_in != "":

                        if name_in not in src_name_data:

                            src_name_data.append(str(name_in))

                            usr_datas_new_name_lists = {
                                        "names_lsts": src_name_data
                            }

                            json_settings_file_datas = open(appdatas_json_fl_rt, "w")

                            json.dump(usr_datas_new_name_lists, json_settings_file_datas)

                            json_settings_file_datas.close()

                            appdatas_json_r = open(appdatas_json_fl_rt, 'r')

                            data2 = appdatas_json_r.read()

                            self.name_infos_v = json.loads(data2)["names_lsts"]

                            src_path_data = self.path_infos_v
                            src_name_data = self.name_infos_v

                            name_dirs_path_v = os.path.join(src_path_data, name_in)
                            now_yrs_sub_folder_v = os.path.join(name_dirs_path_v, dt_yyyy)
                            now_dtdd_dtmnth_sub_folder_v = os.path.join(now_yrs_sub_folder_v, dtdd_dtmnths)
                            dirs_shortcut__make(path0=src_path_data, path1=name_dirs_path_v,
                            path2=now_yrs_sub_folder_v, path3=now_dtdd_dtmnth_sub_folder_v)

                            # msg_autoClose(msg_text="All folders are made successfully.                        ",
                            #                msg_title="Folders creation - Complete", close_tmr=3)


                            appdatas_json_r.close()

                            #  msg_autoClose(msg_text="Data saved.     ",
                            # msg_title="Name update - Complete", close_tmr=3)

                            # print("'{0}' and '{1}' folders successfully made.".format(name, dtdd_dtmnths))

                            # msg_autoClose(msg_text="'{0}' and '{1}' folders successfully made.                        ".format(
                            #         name, dtdd_dtmnths),msg_title="Folder creation - Complete", close_tmr=3)

                            print("'{0}' and '{1}' folders successfully made.".format(name_in, dtdd_dtmnths))

                            name_added_msg = wx.MessageDialog(self.wpanel, "Name added to the lists and folder created.",
                                                                      "Name - Update complete",
                                                                      wx.OK | wx.ICON_INFORMATION)

                            name_added_msg.ShowModal()

                            break
                        else:
                            name_add_err_input = wx.MessageDialog(self.wpanel,"'{}' already been added to the lists.".format(
                                name_in),"{} - input verifier error:".format(app_title),
                                         wx.ICON_ERROR | wx.STAY_ON_TOP)

                            name_add_err_input.ShowModal()

                            #break

                    else:
                        invld_err_input = wx.MessageDialog(self.wpanel, "Null values are not accepted.",
                                                                   "{} - input verifier error:".format(
                                                                       app_title),
                                                                   wx.ICON_ERROR | wx.STAY_ON_TOP)

                        invld_err_input.ShowModal()

                        #break


                        #break
                else:
                    break
                #break
            ''' Variable current year folder path '''
            # now_yrs_sub_folder_v = os.path.join(src_path_data, dt_yyyy)

            ''' Variable current date folder path '''
            # now_date_sub_folder_v = os.path.join(now_yrs_sub_folder_v, dt_date)

            # os.startfile(now_date_sub_folder_v)

            appdatas_json_settings.close()

            path_json_settings_datas.close()

        except FileNotFoundError:
            pass


    def fc_make(self,event):
        """ Verify 'path.json' if exists or not """
        path_settings_json_fl_exists = os.path.exists(path_json_fl_rt)

        data_settings_json_fl_exists = os.path.exists(appdatas_json_fl_rt)

        if data_settings_json_fl_exists == False:
            usr_datas = {

                "names_lsts": client_lsts
            }

            path_json_settings = open(appdatas_json_fl_rt, "w")

            json.dump(usr_datas, path_json_settings)

            path_json_settings.close()

            # msg_autoClose(msg_text="Data saved.                        ",
            #               msg_title="Datas update - Complete", close_tmr=3)
        else:
            pass

        if path_settings_json_fl_exists == False:

            dir_dlgbox = wx.DirDialog(self.wpanel, "Please choose directory (or Path) to hold:".format(main_folder_name), "",
                                      wx.DD_DEFAULT_STYLE | wx.DD_CHANGE_DIR)

            # dir_dlgbox.Set(wDir_path)

            if dir_dlgbox.ShowModal() == wx.ID_OK:

                usr_rt_v = dir_dlgbox.GetPath()

                usr_datas = {
                    "path": str(usr_rt_v)
                }

                json_settings_file_datas = open(appdatas_json_fl_rt, "w")

                json.dump(usr_datas, json_settings_file_datas)

                json_settings_file_datas.close()

            else:
                pass
        else:
            pass

        try:
            path_json_r = open(path_json_fl_rt, 'r')

            data1 = path_json_r.read()

            self.path_infos_v = json.loads(data1)["path"]

            appdatas_json_r = open(appdatas_json_fl_rt, 'r')

            data2 = appdatas_json_r.read()

            self.name_infos_v = json.loads(data2)["names_lsts"]

            src_path_data = self.path_infos_v
            src_name_data = self.name_infos_v

            for name in src_name_data:
                print(name)
                name_dirs_path_v = os.path.join(src_path_data,name)
                now_yrs_sub_folder_v = os.path.join(name_dirs_path_v, dt_yyyy)
                now_dtdd_dtmnth_sub_folder_v = os.path.join(now_yrs_sub_folder_v, dtdd_dtmnths)
                dirs_shortcut__make(path0=src_path_data,path1=name_dirs_path_v,path2=now_yrs_sub_folder_v,path3=now_dtdd_dtmnth_sub_folder_v)

                # # msg_autoClose(msg_text="'{0}' and '{1}' folders successfully made.                        ".format(name,dtdd_dtmnths),
                #               msg_title="Folder creation - Complete", close_tmr=3)


            # msg_autoClose(msg_text="All folders are made successfully.                        ",
            #                msg_title="Folders creation - Complete", close_tmr=3)

            path_json_r.close()
            appdatas_json_r.close()

        except FileNotFoundError:
            pass

    def open_folder_dt(self, event):

        """ Verify '.json' if exists or not """
        settings_json_fl_exists = os.path.exists(appdatas_json_fl_rt)

        if settings_json_fl_exists == False:

            dir_dlgbox = wx.DirDialog(self.wpanel, "Please choose directory (or Path):", "",
                                      wx.DD_DEFAULT_STYLE | wx.DD_CHANGE_DIR)

            # dir_dlgbox.Set(wDir_path)

            if dir_dlgbox.ShowModal() == wx.ID_OK:

                usr_rt_v = dir_dlgbox.GetPath()

                usr_datas = {
                    "path": str(usr_rt_v),
                    "names_lsts":client_lsts,
                    "folder_name":dtdd_dtmnths
                }

                json_settings_file_datas = open(appdatas_json_fl_rt, "w")

                json.dump(usr_datas, json_settings_file_datas)

                json_settings_file_datas.close()

                settings_path_saved_msg = wx.MessageDialog(self.wpanel, "Path updated.", "Path update - Complete",
                                                           wx.OK | wx.ICON_INFORMATION)

                settings_path_saved_msg.ShowModal()

            else:
                pass
        else:
            pass

        try:
            path_json_settings_datas = open(path_json_fl_rt,'r')
            appdatas_json = open(appdatas_json_fl_rt, 'r')

            data1 = path_json_settings_datas.read()
            data2 = appdatas_json.read()

            self.path_infos_v = json.loads(data1)["path"]
            self.name_infos_v = json.loads(data2)["names_lsts"]


            src_path_data = self.path_infos_v
            src_name_data = self.name_infos_v


            ''' Variable current year folder path '''
            # now_yrs_sub_folder_v = os.path.join(src_path_data, dt_yyyy)

            ''' Variable current date folder path '''
            # now_date_sub_folder_v = os.path.join(now_yrs_sub_folder_v, dt_date)

            os.startfile(src_path_data)

            appdatas_json.close()
            path_json_settings_datas.close()

        except FileNotFoundError:
            pass

    def exitbutton(self, event):
        ''' Asks user whether to use again as message box. if not, clears the values for the user, or exits the app if yes  '''
        yn_msgbox = wx.MessageDialog(self.wpanel, "Are you sure you want to exit the app?", "Yes/No",
                                     wx.YES_NO | wx.ICON_WARNING)

        yn_var = yn_msgbox.ShowModal()

        if yn_var == wx.ID_NO:
            pass
        else:
            self.Destroy()  # closes app when 'EXIT' button is click


if __name__=='__main__':

    app=wx.App()# Start the app

    frame = app_ui(parent=None,id=-1)# Gives parametres or infos to the class or 'Frame' components

    frame.Show()# Shows the commponents existed within the app

    app.MainLoop()# loops the window as systems close apps within milliseconds or more
