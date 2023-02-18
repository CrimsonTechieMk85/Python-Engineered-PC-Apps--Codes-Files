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
# wDir_path = os.path.dirname(os.path.realpath(__file__))# curent working directory or the 'Now'-location of the file.

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
# eT [Early-Tests] type - Path Json files details
et_path_json_name = '{}-path_datas'.format(file_name)

path_jsonfl_key = "eT_path"

et_pathjson_fl_name= '{}.json'.format(et_path_json_name)

pathdatas_json_fl_path = os.path.join(wDir_path,et_pathjson_fl_name)

# eT [Early-Tests] type - App Json files details
et_app_json_name = '{}-app_datas'.format(file_name)

appdata_jsonfl_key = "eT_names"

appjson_fl_name = '{}.json'.format(et_app_json_name)

appdatas_json_fl_path = os.path.join(wDir_path,appjson_fl_name)

''' App Details '''
# eT [Early-Tests] type app title PF+
et_app_title = "Folder Create:Auto PEF++ (Sf-c) [early-tests.Id: {}]".format(file_name)

# eT [Early-Tests] type audio folder with app name
app_collection_folder_name = '{} collections'.format(file_name)

# -----------------------------------------------------------------------------------------


# =======================================================================================

#                     App infos

# ---------------------------------------------------------------------------------------
''' Folder names '''
# Folder with app name
main_folder_name = 'Folder Create Auto-2 PEF++ (Sudha Fashion-custom)'
app_collection_folder_name = '{} collections'.format(main_folder_name)

# -----------------------------------------------------------------------------------------

''' Settings file path '''
# App Json files details
app_json_name = 'app_datas'

appdata_jsonfl_key = "names"

appjson_fl_name = '{}.json'.format(app_json_name)

appdatas_json_fl_path = os.path.join(wDir_path,appjson_fl_name)

# Path json files details
path_json_name = 'path_datas'

path_jsonfl_key = "path"

pathjson_fl_name = '{}.json'.format(path_json_name)

pathdatas_json_fl_path = os.path.join(wDir_path,pathjson_fl_name)

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

def dirs_shortcut_maker2B(paths,folder_name):

    for n in range(0,len(paths),1):
        try:
            os.makedirs(paths[n])
        except OSError:
            pass

        # Make shortcut
        desktop = winshell.desktop()
        path = os.path.join(desktop, '{} - Shortcut.lnk'.format(app_collection_folder_name))

        target_rt = paths[n]
        wDir_rt = paths[n]
        if n==0 and os.path.exists(path)==False:  
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
        btn_make_dirs_font = wx.Font(21, wx.ROMAN, wx.FONTSTYLE_NORMAL,
                                  wx.FONTWEIGHT_BOLD)

        # Creates button
        self.make_dirs_btn = wx.Button(self.wpanel, label='Update/Create name', pos=(177, 148), size=(268, 45),
                                         style=wx.BORDER_RAISED)

        # Sets font for the button using variable
        self.make_dirs_btn.SetFont(btn_make_dirs_font)

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
            "Click here to open 'Collection' folder.")  # sets features pop-up details

        self.Bind(wx.EVT_BUTTON, self.open_folder_dt, self.open_folder_btn)  # combines button with its functions

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

    def save_json(self,jsonfl_path1,k1,v1,msg_txt1,msg_title1):

        usr_datas = {

                k1: v1
            }

        with open(jsonfl_path1, "w") as jsonfl_save:
            
            json.dump(usr_datas, jsonfl_save)

        saved_msg = wx.MessageDialog(self.wpanel, msg_txt1, msg_title1,
                                                           wx.OK | wx.ICON_INFORMATION)

        saved_msg.ShowModal()

    def read_json(self,jsonfl_path2,k2):

       with open(jsonfl_path2,'r') as pathjson_fl_r:
            data = pathjson_fl_r.read()

            infos_v = json.loads(data)[k2]

            return infos_v

    def update_json(self,json_flpath3,key3,info3,msg_txt3,msg_title3):
        with open(json_flpath3,'r') as json_data_r:
            json_src_data = json.load(json_data_r)

            json_src_data[key3] = info3

            with open(json_flpath3,'w') as json_fl_w:
                json.dump(json_src_data,json_fl_w)

        update_msg3 = wx.MessageDialog(self.wpanel, msg_txt3, msg_title3,
                                                           wx.OK | wx.ICON_INFORMATION)

        update_msg3.ShowModal()

    def save_path_json(self):

        if os.path.exists(pathdatas_json_fl_path)==False:

            dir_dlgbox = wx.DirDialog(self.wpanel, "Please choose directory (or Path):", "",
                                        wx.DD_DEFAULT_STYLE | wx.DD_CHANGE_DIR)

            if dir_dlgbox.ShowModal() == wx.ID_OK:

                usr_rt_v = dir_dlgbox.GetPath()  

                self.save_json(jsonfl_path1=pathdatas_json_fl_path,k1=path_jsonfl_key,v1=usr_rt_v,msg_txt1="Path saved.",msg_title1="Path save - Complete")

                # msg_autoClose(msg_text="Data saved.                        ",
                # msg_title="Datas update - Complete", close_tmr=3)              

            else:
                pass
        else:
            pass

    def save_names_json(self):
     
        if os.path.exists(appdatas_json_fl_path) == False:
     
            self.save_json(jsonfl_path1=appdatas_json_fl_path,k1=appdata_jsonfl_key,v1=client_lsts,msg_txt1="Name(s) data saved.",msg_title1="Name(s) save - Complete")
 
            # msg_autoClose(msg_text="Data saved.                        ",
            #  msg_title="Datas update - Complete", close_tmr=3)
        else:
            pass

    def overwrite_path_json(self):
        dir_dlgbox = wx.DirDialog(self.wpanel, "Please choose directory (or Path) to be reseted:", "",
                                      wx.DD_DEFAULT_STYLE | wx.DD_CHANGE_DIR)

        return dir_dlgbox
        
    def overwrite_name_json(self):
        self.save_json(jsonfl_path1=appdatas_json_fl_path,k1=appdata_jsonfl_key,v1=client_lsts,msg_txt1="'{}' json file reseted.".format(appjson_fl_name),msg_title1="App Data Json file reset - Complete")

    def get_paths(self,jsonfl_path5,k5):

        self.save_path_json()

        while True:

            try:

                if os.path.exists(pathdatas_json_fl_path)==True:

                    returned_path = self.read_json(jsonfl_path2=pathdatas_json_fl_path,k2=path_jsonfl_key)

                    try:
                        with open(appdatas_json_fl_path, 'r') as jsonfl_r:

                            data2 = jsonfl_r.read()

                            infos_v5 = json.loads(data2)[appdata_jsonfl_key]

                            print(infos_v5)

                        collection_folder_path = os.path.join(returned_path,app_collection_folder_name)

                        if infos_v5 !=[]:

                            for name in infos_v5:
                            
                                
                                name_dirs_path_v = os.path.join(collection_folder_path, name)
                                now_yrs_sub_folder_v = os.path.join(name_dirs_path_v, dt_yyyy)
                                now_dtdd_dtmnth_sub_folder_v = os.path.join(now_yrs_sub_folder_v, dtdd_dtmnths)

                                path_lsts = [collection_folder_path,name_dirs_path_v,now_yrs_sub_folder_v
                                                    ,now_dtdd_dtmnth_sub_folder_v]

                                print(path_lsts)
                                dirs_shortcut_maker2B(paths=path_lsts, folder_name=app_collection_folder_name)

                                return collection_folder_path
                        else:
                            return collection_folder_path

                    except json.decoder.JSONDecodeError:
                        self.overwrite_name_json()
                    except KeyError:
                        self.overwrite_name_json()
                else:
                    return None


            except json.decoder.JSONDecodeError:

                returned_dir_dlgbox_out3 = self.overwrite_path_json()

                if returned_dir_dlgbox_out3.ShowModal() == wx.ID_OK:

                    usr_rt_v1 = returned_dir_dlgbox_out3.GetPath()
                                
                    self.save_json(jsonfl_path1=pathdatas_json_fl_path,k1=path_jsonfl_key,v1=usr_rt_v1,msg_txt1="'{}' json file reseted.".format(pathjson_fl_name),msg_title1="Path Data Json file reset - Complete")
                else:
                    break

            except KeyError:

                returned_dir_dlgbox_out3 = self.overwrite_path_json()

                if returned_dir_dlgbox_out3.ShowModal() == wx.ID_OK:

                    usr_rt_v1 = returned_dir_dlgbox_out3.GetPath()
                                
                    self.save_json(jsonfl_path1=pathdatas_json_fl_path,k1=path_jsonfl_key,v1=usr_rt_v1,msg_txt1="'{}' json file reseted.".format(pathjson_fl_name),msg_title1="Path Data Json file reset - Complete")
                else:
                    break


    def Close(self, event):
        self.Destroy()  # closes app  when 'CLOSE' or 'X' on the window is pressed

    def changedir(self,event):
        
        try:

            if os.path.exists(pathdatas_json_fl_path)==True:

                dir_dlgbox = wx.DirDialog(self.wpanel, "Please choose directory (or Path) to be changed:", "",
                                        wx.DD_DEFAULT_STYLE | wx.DD_CHANGE_DIR)

                if dir_dlgbox.ShowModal() == wx.ID_OK:

                    usr_rt_v = dir_dlgbox.GetPath()

                    self.update_json(json_flpath3=pathdatas_json_fl_path,key3=path_jsonfl_key,info3=usr_rt_v,msg_txt3="Path changed.",msg_title3= "Path update - Complete")

                    self.get_paths(jsonfl_path5=pathdatas_json_fl_path,k5=path_jsonfl_key)                        

                else:
                    pass

            else:
                self.get_paths(jsonfl_path5=pathdatas_json_fl_path,k5=path_jsonfl_key)          

        except json.decoder.JSONDecodeError:

            returned_dir_dlgbox_out3 = self.overwrite_path_json()

            if returned_dir_dlgbox_out3.ShowModal() == wx.ID_OK:

                usr_rt_v1 = returned_dir_dlgbox_out3.GetPath()
                            
                self.save_json(jsonfl_path1=pathdatas_json_fl_path,k1=path_jsonfl_key,v1=usr_rt_v1,msg_txt1="'{}' json file reseted.".format(pathjson_fl_name),msg_title1="Path Data Json file reset - Complete")
            else:
                pass


        except KeyError:

            returned_dir_dlgbox_out4 = self.overwrite_path_json()   

            if returned_dir_dlgbox_out4.ShowModal() == wx.ID_OK:

                usr_rt_v1 = returned_dir_dlgbox_out4.GetPath()
                            
                self.save_json(jsonfl_path1=pathdatas_json_fl_path,k1=path_jsonfl_key,v1=usr_rt_v1,msg_txt1="'{}' json file reseted.".format(pathjson_fl_name),msg_title1="Path Data Json file reset - Complete")
            else:
                pass

    def delete_names(self,event):

        try:

            if os.path.exists(pathdatas_json_fl_path) != False:
                returned_names = self.read_json(jsonfl_path2=appdatas_json_fl_path,k2=appdata_jsonfl_key)

                print(returned_names)

                while True:

                    name_del_title = "{} - name delete entry".format(app_title)

                    self.name_del_input = wx.TextEntryDialog(self.wpanel, "Please type the name to be removed below:",
                                                            name_del_title, '')

                    if self.name_del_input.ShowModal() == wx.ID_OK:

                        name_del_in = self.name_del_input.GetValue()

                        if name_del_in != "":
                            if name_del_in in returned_names:
                                returned_names.remove(str(name_del_in))

                                print(returned_names)
                    
                                self.save_json(jsonfl_path1=appdatas_json_fl_path,k1=appdata_jsonfl_key,v1=returned_names,msg_txt1="Name(s) removed from data.",msg_title1="Name Delete - Complete.")
                                try:
                                    returned_collection_path_data  = self.get_paths(jsonfl_path5=pathdatas_json_fl_path,k5=path_jsonfl_key)

                                    name_del_dirs = os.path.join(returned_collection_path_data,name_del_in)

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
                                except json.decoder.JSONDecodeError:
 
                                    returned_dir_dlgbox_out1= self.overwrite_path_json()

                                    if returned_dir_dlgbox_out1.ShowModal() == wx.ID_OK:

                                        usr_rt_v1 = returned_dir_dlgbox_out1.GetPath()
                            
                                        self.save_json(jsonfl_path1=pathdatas_json_fl_path,k1=path_jsonfl_key,v1=usr_rt_v1,msg_txt1="'{}' json file reseted.".format(pathjson_fl_name),msg_title1="Path Data Json file reset - Complete")
                                    else:
                                        break

                                except KeyError:

                                    returned_dir_dlgbox_out2= self.overwrite_path_json()

                                    if returned_dir_dlgbox_out2.ShowModal() == wx.ID_OK:

                                        usr_rt_v1 = returned_dir_dlgbox_out2.GetPath()
                            
                                        self.save_json(jsonfl_path1=pathdatas_json_fl_path,k1=path_jsonfl_key,v1=usr_rt_v1,msg_txt1="'{}' json file reseted.".format(pathjson_fl_name),msg_title1="Path Data Json file reset - Complete")
                                    else:
                                        break
                            else:
                                name_not_found_err_msg = wx.MessageDialog(self.wpanel, "Name already removed or not found from the lists.",
                                                                    "{} - input verifier error:".format(app_title),
                                                                    wx.OK | wx.ICON_INFORMATION)

                                name_not_found_err_msg.ShowModal()

                                returned_collection_path_data = self.get_paths(jsonfl_path5=pathdatas_json_fl_path,k5=path_jsonfl_key)

                                name_del_dirs = os.path.join(returned_collection_path_data,name_del_in)

                                if os.path.exists(name_del_dirs)==True:

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
                                else:
                                    pass
                        else:
                            invld_err_input = wx.MessageDialog(self.wpanel, "Null values are not accepted.",
                                                                    "{} - input verifier error:".format(
                                                                        app_title),
                                                                    wx.ICON_ERROR | wx.STAY_ON_TOP)

                            invld_err_input.ShowModal()
                    else:
                        break
            else:
                pass
        except json.decoder.JSONDecodeError:

            returned_dir_dlgbox_out3 = self.overwrite_path_json()

            if returned_dir_dlgbox_out3.ShowModal() == wx.ID_OK:

                usr_rt_v3 = returned_dir_dlgbox_out3.GetPath()
                            
                self.save_json(jsonfl_path1=pathdatas_json_fl_path,k1=path_jsonfl_key,v1=usr_rt_v3,msg_txt1="'{}' json file reseted.".format(pathjson_fl_name),msg_title1="Path Data Json file reset - Complete")
            else:
                pass

        except KeyError:

            returned_dir_dlgbox_out4 = self.overwrite_path_json()

            if returned_dir_dlgbox_out4.ShowModal() == wx.ID_OK:

                usr_rt_v4 = returned_dir_dlgbox_out4.GetPath()
                            
                self.save_json(jsonfl_path1=pathdatas_json_fl_path,k1=path_jsonfl_key,v1=usr_rt_v4,msg_txt1="'{}' json file reseted.".format(pathjson_fl_name),msg_title1="Path Data Json file reset - Complete")
            else:
                pass

    def update_names(self,event):
        self.save_path_json()

        if os.path.exists(pathdatas_json_fl_path)==True:
            self.save_names_json()
           
            returned_name_data = self.read_json(jsonfl_path2=appdatas_json_fl_path,k2=appdata_jsonfl_key)

            print(returned_name_data)

            while True:

                name_add_title = "{} - name update entry".format(app_title)

                self.name_add_input = wx.TextEntryDialog(self.wpanel, "Please type the name to be added below:",
                                                                name_add_title,'')

                if self.name_add_input.ShowModal() == wx.ID_OK:

                    name_in = self.name_add_input.GetValue()

                    if name_in != "":

                        if name_in not in returned_name_data:

                            returned_name_data.append(str(name_in))

                            print(returned_name_data) 

                            self.save_json(jsonfl_path1=appdatas_json_fl_path,k1=appdata_jsonfl_key,v1=returned_name_data,msg_title1="Named update - Complete",msg_txt1="Name added to the list")

                            self.get_paths(jsonfl_path5=appdatas_json_fl_path,k5=appdata_jsonfl_key)

                            print("'{0}' and '{1}' folders successfully made.".format(name_in, dtdd_dtmnths))
 
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
 
                else:
                    break
                #break
 
        else:
            pass

    def fc_make(self,event):

        self.save_names_json()

        self.get_paths(jsonfl_path5=pathdatas_json_fl_path,k5=path_jsonfl_key)

    def open_folder_dt(self, event):

        try:

            self.save_path_json()

            if os.path.exists(pathdatas_json_fl_path)==True:

                self.save_names_json()

                returned_collection_path_data  = self.get_paths(jsonfl_path5=pathdatas_json_fl_path,k5=path_jsonfl_key)

                os.startfile(returned_collection_path_data)
            else:
                pass
        except json.decoder.JSONDecodeError:

            returned_dir_dlgbox_out7 = self.overwrite_path_json()

            if returned_dir_dlgbox_out7.ShowModal() == wx.ID_OK:

                usr_rt_v7 = returned_dir_dlgbox_out7.GetPath()
                            
                self.save_json(jsonfl_path1=pathdatas_json_fl_path,k1=path_jsonfl_key,v1=usr_rt_v7,msg_txt1="'{}' json file reseted.".format(pathjson_fl_name),msg_title1="Path Data Json file reset - Complete")
            else:
                pass

        except KeyError:

            returned_dir_dlgbox_out8 = self.overwrite_path_json()

            if returned_dir_dlgbox_out8.ShowModal() == wx.ID_OK:

                usr_rt_v8 = returned_dir_dlgbox_out8.GetPath()
                            
                self.save_json(jsonfl_path1=pathdatas_json_fl_path,k1=path_jsonfl_key,v1=usr_rt_v8,msg_txt1="'{}' json file reseted.".format(pathjson_fl_name),msg_title1="Path Data Json file reset - Complete")
            else:
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
