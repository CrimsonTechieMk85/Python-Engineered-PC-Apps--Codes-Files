from operator import sub
from re import A
import wx

import shutil

#from PyQt5.QtCore import dec
from wx.core import EVT_CLOSE, TE_PASSWORD

from cryptography.fernet import Fernet  # encryption/decryption process support format module

import os  # for file and folder operation

import time  # for 'time-delays' activities

import json  # for 'JSON' file operation

import datetime  # getting real-time datas of today

import sys

import winshell

from win32com.client import Dispatch

import zipfile

# from reloading import reloading

''' Nxt2Nxt time delay '''
def delay(var):
    time.sleep(var)


''' clear system '''
def wipeout():
    time.sleep(2.16)

    os.system('cls')


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

epoch_miliseconds_str = str(epoch_miliseconds)
#
dt_TMR = "{0}-{1}-{2}".format(dt_clockH, dt_clockM, dt_clockS)
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
dt_date = "{0}-{1}-{2}".format(dt_dd, dt_mm, dt_yyyy)

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
dt_TMR = "{0}-{1}-{2}".format(dt_clockH, dt_clockM, dt_clockS)
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
dt_date = "{0}.{1}.{2}".format(dt_dd, dt_mm, dt_yyyy)
#

'''Files,Paths&Folders'''
# Current working directory

wFile_path = os.path.realpath(__file__)
#wDir_path = os.path.dirname(wFile_path)

wDir_path = os.getcwd()

# icon source image file -> eg: 'image_file_name'.ico
for file in os.listdir(wDir_path):
    # print(file)
    if '.ico' in file:
        try:
            ico_flpath = os.path.join(wDir_path, file)
        except OSError:
            pass
    else:
        pass

# File name & File extension
file_name, file_type = os.path.splitext(os.path.basename(os.path.realpath(__file__)))

# print(file_name)
# file_name, file_type = os.path.splitext(os.path.basename(wDir_path))
# print(file_name)

# sys.exit()
# ---------------------------------------------------------------------------

''' Early-tests type App details '''
# [Early-tests] app folder name
app_name = "PS 12 PEF++ (210-F3.6)"
et_app_title = "{0} [Early-tests type == {1}]".format(app_name, file_name)

# [Early-tests type] database folder
et_database_folder_name = "{}_database".format(file_name)

et_database_folder_path = os.path.join(wDir_path, et_database_folder_name)

# [Early-tests type] settings folder
et_settings_folder_name = '{}_settings'.format(file_name)

et_settings_folder_path = os.path.join(et_database_folder_path, et_settings_folder_name)

# [Early-tests type] backup folder
et_backups_folder_name = '{}_backups'.format(file_name)

et_backups_folder_path = os.path.join(et_database_folder_path, et_backups_folder_name)

# [Early-tests type] backup folders
et_folder_backup_json_name = "{}_folderbackup_infos".format(file_name)

et_folder_backup_json_file_name = "{}.json".format(et_folder_backup_json_name)

et_json_folder_backups_file_path = os.path.join(et_backups_folder_path, et_folder_backup_json_file_name)

# [Early-tests type] backup files
et_file_backup_json_name = "{}_filebackup_infos".format(file_name)

et_file_backup_json_file_name = "{}.json".format(et_file_backup_json_name)

et_json_file_backups_file_path = os.path.join(et_backups_folder_path, et_file_backup_json_file_name)

# [Early-tests type] passwords details
et_passwords_json_name = "{}_passwords".format(file_name)

et_passwords_json_file_name = "{}.json".format(et_passwords_json_name)

et_passwords_json_file_path = os.path.join(et_settings_folder_path, et_passwords_json_file_name)

# [Early-tests type] App path Json files details
et_paths_json_name = '{}_pathsdatas'.format(file_name)

et_paths_json_file = '{}.json'.format(et_paths_json_name)

et_paths_datas_json_file_path = os.path.join(et_settings_folder_path, et_paths_json_file)

# [Early-tests type] Collections folder details
et_collections_folder_name = "{}_collections".format(file_name)

# [Early-tests type] Encrypted folder name
et_enc_folder_name = "{}_encrypted-files".format(file_name)

# [Early-tests type] Decrypted folder name
et_dec_folder_name = "{}_decrypted-files".format(file_name)

''' Main App detials '''
# App details
app_title = "Portfolio secure 12 Perfected.Even.Further ++ (210-F3.6)"

# GUI messages heading app title
# sub_app_title = 'Portfolio secure 12 Perfected.Even.Further ++ (210-F3.6)'

# database folder
app_db_folder_name = 'PS-12PEF++210F36'
database_folder_name = "{} database".format(app_db_folder_name)

database_folder_path = os.path.join(wDir_path, database_folder_name)

# settings folder
settings_folder_path = os.path.join(database_folder_path, ".settings")

# backup folder
backups_folder_path = os.path.join(database_folder_path, ".backups")

# backup files
file_backups_json_name = "file_backup_infos"

file_backup_json_file = "{}.json".format(file_backups_json_name)

json_file_backups_file_path = os.path.join(backups_folder_path, file_backup_json_file)

# backup folders
folder_backups_json_name = "folder_backup_infos"

folder_backup_json_file = "{}.json".format(folder_backups_json_name)

json_folder_backups_file_path = os.path.join(backups_folder_path, folder_backup_json_file)

# passwords details
passwords_json_name = "My_passwords"

passwords_json__file = "{}.json".format(passwords_json_name)

passwords_json_file_path = os.path.join(settings_folder_path, passwords_json__file)

# Collections folder details
main_app_folder_name = 'Portfolio secure 12 P.E.F ++ (210-F3.6)'
collections_folder_name = "{} collections".format(main_app_folder_name)

# App path Json files details
paths_json_name = 'path_datas'

paths_json_file = '{}.json'.format(paths_json_name)

paths_datas_json_file_path = os.path.join(settings_folder_path, paths_json_file)

# Encrypted folder name
enc_folder_name = "Encrypted archive"

# Decrypted folder name
dec_folder_name = "Decrypted archive"

# Encrypted files  folder
encfiles_subfolder2_name="Encrypted files"
# Encrypted folders folder
encfolders_subfolder2_name="Encrypted folders"

# Decrypted files  folder
decfiles_subfolder2_name="Decrypted files"
# Decrypted folders folder
decfolders_subfolder2_name="Decrypted folders"


# encryptor key
key = "54NxGh1jHbQKeUl_mHM0PXg363MkmtFsrpgRGA1rI2g="

cipher = Fernet(key)

# pascode_json_exists = os.path.exists(settings_json_full_path)

# Encrypted passwords  - Default
pass_enc_no = 13

pass_dec_no = 12

encrypt_passcode_no_encrypted = cipher.encrypt(bytes(str(pass_enc_no), 'utf-8')).decode()
decrypt_passcode_no_encrypted =cipher.encrypt(bytes(str(pass_dec_no), 'utf-8')).decode()

''' Folder Maker '''
def DirMake(path_val):
    try:
        os.makedirs(path_val)

        # delay(0.16)

        # print("\n- '{}' database folder made.".format(database_folder_name))
    except OSError:
        pass

''' Password json file maker '''
def password_json_make(json_path_val):
    ''' make passwords json files in settings files '''
    pwd_var = {
        "encrypt_passcode": encrypt_passcode_no_encrypted,
        "decrypt_passcode": decrypt_passcode_no_encrypted
    }

    # Tranfers data And then stores it on the json file
    if os.path.exists(json_path_val) is False:

        try:

            sfl = open(json_path_val, "w")

            json.dump(pwd_var, sfl)

            sfl.close()
        except FileNotFoundError:
            pass

        # print("\n- 'My_passwords' json file made.")

        # wipeout()
    else:
        pass

'''' Password json overwrite '''
def password_json_overwrite(json_path_val, enc_pswrd_var, dec_pswrd_var):
    ''' make passwords json files in settings files '''
    pwd_var = {
        "encrypt_pass code": enc_pswrd_var,
        "decrypt_passcode": dec_pswrd_var
    }

    sfl_w = open(json_path_val, "w")

    json.dump(pwd_var, sfl_w)

    sfl_w.close()

''' Main app, Encrypted & Decrypted folders shortcut maker '''
def enc_dec_folder_shortcut_maker_dt(app_main_folder_root_var,years_sub_folder_root_var_enc,years_sub_folder_root_var_dec, date_sub_folder_root_var_enc,date_sub_folder_root_var_dec,subfolder2_root_var_encfiles,subfolder2_root_var_decfiles,subfolder2_root_var_encdirs,subfolder2_root_var_decdirs, folder_name_var):
    try:
        os.makedirs(app_main_folder_root_var)
    except OSError:
        pass

    try:
        os.makedirs(years_sub_folder_root_var_enc)
    except OSError:
        pass

    try:
        os.makedirs(years_sub_folder_root_var_dec)
    except OSError:
        pass

    try:
        os.makedirs(date_sub_folder_root_var_dec)
    except OSError:
        pass

    try:
        os.makedirs(date_sub_folder_root_var_enc)
    except OSError:
        pass

    try:
        os.makedirs(subfolder2_root_var_encfiles)
    except OSError:
        pass

    try:
        os.makedirs(subfolder2_root_var_decfiles)
    except OSError:
        pass

    try:
        os.makedirs(subfolder2_root_var_encdirs)
    except OSError:
        pass

    try:
        os.makedirs(subfolder2_root_var_decdirs)
    except OSError:
        pass



    ''' Make 'AppName' shortcut '''
    desktop = winshell.desktop()
    path = os.path.join(desktop, '{} - Shortcut.lnk'.format(folder_name_var))

    if os.path.exists(path) == False:

        target = app_main_folder_root_var
        wDir = app_main_folder_root_var
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateshortCut(path)
        shortcut.Targetpath = target
        shortcut.WorkingDirectory = wDir
        shortcut.save()

    else:
        pass


# using 'class' or "blueprint" to extract all the 'frame' supports existing within the 'wx' module for GUI apps
class appUI(wx.Frame):

    # Starts frame upon user request or 'CLICKING' the app
    def __init__(self, parent, id):
        # Window (Frame) with parametres i.e (frame, parent=None,id=-1.'window title',size=(int,int),style=wx.(obj))
        wx.Frame.__init__(self, parent, id, app_title, size=(692, 416),
                          style=wx.DEFAULT_FRAME_STYLE & ~wx.MAXIMIZE_BOX ^ wx.RESIZE_BORDER)

        try:
            self.SetIcon(wx.Icon(ico_flpath))  # Sets icon on the window title bar
        except NameError:
            pass

        self.wpanel = wx.Panel(self)  # setting 'container' to have wxpython GUI parts

        self.wpanel.SetBackgroundColour('Steel blue')  # Sets the panel or app background

        # ----->  Buttons

        # Encrypt folder button

        # Creates fonts for the button
        enc_dir_btn_font = wx.Font(21, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        # Creates button
        self.enc_dir_btn = wx.Button(self.wpanel, label="Encrypt folder", pos=(67, 67), size=(226, 45))

        # Sets font for the button using variable
        self.enc_dir_btn.SetFont(enc_dir_btn_font)

        # Sets the button text colour
        self.enc_dir_btn.SetForegroundColour('White')

        # Sets the given colour for the button ( button BG colour )
        self.enc_dir_btn.SetBackgroundColour('Black')

        # Combines the button with its functions
        self.Bind(wx.EVT_BUTTON, self.dir_secure, self.enc_dir_btn)

        # Encrypt file button

        # Creates fonts for the button
        enc_file_btn_font = wx.Font(21, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        # Creates button
        self.enc_file_btn = wx.Button(self.wpanel, label="Encrypt file", pos=(387, 67), size=(226, 45))

        # Sets font for the button using variable
        self.enc_file_btn.SetFont(enc_file_btn_font)

        # Sets the given colour for the button ( button BG colour)
        self.enc_file_btn.SetForegroundColour('White')

        # Sets the given colour for the button
        self.enc_file_btn.SetBackgroundColour('Blue')

        # Combines buttons with it's respective functions
        self.Bind(wx.EVT_BUTTON, self.file_secure, self.enc_file_btn)

        # Exit button

        # Creates fonts for the button
        exit_btn_font = wx.Font(21, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        # Creates button
        self.exit_btn = wx.Button(self.wpanel, label="Exit", pos=(67, 263), size=(226, 45))

        # Sets font for the button using variable
        self.exit_btn.SetFont(exit_btn_font)

        # Sets the given colour for the button text
        self.exit_btn.SetForegroundColour('White')

        # Sets the given colour for the button ( button BG colour )
        self.exit_btn.SetBackgroundColour('Red')

        # Combines buttons with it's respective functions
        self.Bind(wx.EVT_BUTTON, self.exitbutton, self.exit_btn)

        # Access button

        # Creates fonts for the  button
        btn_access_font = wx.Font(21, wx.ROMAN, wx.FONTSTYLE_NORMAL,
                                  wx.FONTWEIGHT_BOLD)  # Creates  fonts for 'Reset' button

        # Creates button
        self.open_folder_btn = wx.Button(self.wpanel, label='ACCESS', pos=(224, 163), size=(226, 45),
                                         style=wx.BORDER_RAISED)

        # Sets font for the button using variable
        self.open_folder_btn.SetFont(btn_access_font)

        # Sets the given colour for the button text
        self.open_folder_btn.SetForegroundColour('White')

        # Sets the given colour for the button ( button BG colour )
        self.open_folder_btn.SetBackgroundColour('CORNFLOWER BLUE')

        # Sets features pop-up with given details
        self.open_folder_btn.SetToolTip("Click here to open '{}' folder.".format(collections_folder_name))

        # Combines buttons with it's respective functions
        self.Bind(wx.EVT_BUTTON, self.open_collection_folder_dt2, self.open_folder_btn)

        # Modify button

        # Creates fonts for the button
        btn_mod_font = wx.Font(21, wx.ROMAN, wx.FONTSTYLE_NORMAL,
                               wx.FONTWEIGHT_BOLD)  # Creates  fonts for 'Reset' button

        # Creates button
        self.modify_btn = wx.Button(self.wpanel, label='MODIFY', pos=(387, 263), size=(226, 45), style=wx.BORDER_RAISED)

        # Sets font for the button using variable
        self.modify_btn.SetFont(btn_mod_font)

        # Sets the given colour for the button text
        self.modify_btn.SetForegroundColour('Red')

        # Sets the given colour for the button ( button BG colour )
        self.modify_btn.SetBackgroundColour('Yellow')

        # Sets features pop-up with given details
        self.modify_btn.SetToolTip("Click here to change settings.")

        # Combines buttons with it's respective functions
        self.Bind(wx.EVT_BUTTON, self.modify2, self.modify_btn)

        # 'X' close button

        # Combines buttons with it's respective functions
        self.Bind(wx.EVT_CLOSE, self.Closewindow)

        try:

            self.json_data_fl = open(passwords_json_file_path, "r")

            data = json.load(self.json_data_fl)

            #cipher.encrypt(bytes(str(data["decrypt_passcode"]), 'utf-8')).decode()

            self.decrypt_pass = cipher.decrypt(bytes(str(data["decrypt_passcode"]), 'utf-8')).decode()

            self.encrypt_pass = cipher.decrypt(bytes(str(data["encrypt_passcode"]), 'utf-8')).decode()

        except json.decoder.JSONDecodeError:
            password_json_overwrite(json_path_val=passwords_json_file_path,enc_pswrd_var=encrypt_passcode_no_encrypted,dec_pswrd_var=decrypt_passcode_no_encrypted)
        except FileNotFoundError:
            pass

    def open_collection_folder_dt2(self, event):

        """ Verify 'path.json' if exists or not """
        settings_json_fl_exists = os.path.exists(paths_datas_json_file_path)

        if settings_json_fl_exists == False:

            dir_dlgbox = wx.DirDialog(self.wpanel, "Please choose folder (or directory) to hold '{}' folder:".format(collections_folder_name), "",
                                      wx.DD_DEFAULT_STYLE | wx.DD_CHANGE_DIR)

            # dir_dlgbox.Set(wDir_path)

            if dir_dlgbox.ShowModal() == wx.ID_OK:

                usr_rt_v = dir_dlgbox.GetPath()

                settings_json = open(paths_datas_json_file_path, 'w')

                settings_json.write("{"'"path"'":")

                usr_path = {
                    "path": str(usr_rt_v)
                }

                json_settings_file_datas = open(paths_datas_json_file_path, "w")

                json.dump(usr_path, json_settings_file_datas)

                json_settings_file_datas.close()

                settings_json.close()

                settings_path_saved_msg = wx.MessageDialog(self.wpanel, "Path saved.", "Path save - Complete:",
                                                           wx.OK | wx.ICON_INFORMATION)

                settings_path_saved_msg.ShowModal()

            else:
                pass
        else:
            pass

        try:
            # [Early-tests type] 'folder json file' operation
            # path_json = open(et_paths_datas_json_file_path, 'r')

            path_json = open(paths_datas_json_file_path, 'r')

            data = path_json.read()

            path_infos_v = json.loads(data)["path"]

            # [Early-tests] app folders ->

            # [Early-tests type] Main app folder path
            self.et_collections_folder_path = os.path.join(path_infos_v, et_collections_folder_name)

            # encrypted [Early-tests type] folder path
            self.et_encrypted_files_folder_path = os.path.join(self.et_collections_folder_path, et_enc_folder_name)

            # decrypted [Early-tests type] folder path
            self.et_decrypted_files_folder_path = os.path.join(self.et_collections_folder_path, et_dec_folder_name)

            # [Early-tests type] real-time 'Year' folder in 'Encrypted files' folder path
            self.et_crnt_yrs_folder_path_enc = os.path.join(self.et_encrypted_files_folder_path, dt_yyyy)

            # [Early-tests type] real-time 'Year' folder in 'Decrypted files' folder path
            self.et_crnt_yrs_folder_path_dec = os.path.join(self.et_decrypted_files_folder_path, dt_yyyy)

            # [Early-tests type] real-time 'date' folder in 'Encrypted files' folder path
            self.et_now_date_folder_enc_path = os.path.join(self.et_crnt_yrs_folder_path_enc, dt_date)

            # [Early-tests type] real-time 'date' folder in 'Decrypted files' folder path
            self.et_now_date_folder_dec_path = os.path.join(self.et_crnt_yrs_folder_path_dec, dt_date)

            # os.startfile(now_date_sub_folder_path)

            # [Early-tests type] folder-shorcut maker
            # enc_dec_folder_shortcut_maker_dt(app_main_folder_root_var=self.et_collections_folder_path,years_sub_folder_root_var_enc=self.et_crnt_yrs_folder_path_enc,years_sub_folder_root_var_dec=self.et_crnt_yrs_folder_path_dec,date_sub_folder_root_var_enc=self.et_now_date_folder_enc_path,date_sub_folder_root_var_dec=self.et_now_date_folder_dec_path,folder_name_var=et_collections_folder_name)

            # Encrypted-name folder
            # self.enc_item_name_folder_path = os.path.join(self.now_date_folder_enc_path,epoch_miliseconds_str)

            # [Early-tests type] open collection folder
            # os.startfile(self.et_collections_folder_path)

        # Main app folders ->

            # Main collections folder path
            self.collections_folder_path = os.path.join(path_infos_v, collections_folder_name)

            # encrypted folder path
            self.encrypted_files_folder_path = os.path.join(self.collections_folder_path, enc_folder_name)

            # decrypted folder path
            self.decrypted_files_folder_path = os.path.join(self.collections_folder_path, dec_folder_name)

            # real-time 'years' folder in 'Encrypted files' folder path
            self.crnt_yrs_folder_path_enc = os.path.join(self.encrypted_files_folder_path, dt_yyyy)

            # real-time 'years' folder in 'Decrypted files' folder path
            self.crnt_yrs_folder_path_dec = os.path.join(self.decrypted_files_folder_path, dt_yyyy)

            # real-time 'date' folder in 'Encrypted files' folder path
            self.now_date_folder_enc_path = os.path.join(self.crnt_yrs_folder_path_enc, dt_date)

            # real-time 'date' folder in 'Decrypted files' folder path
            self.now_date_folder_dec_path = os.path.join(self.crnt_yrs_folder_path_dec, dt_date)

            # Encrypted files secondary sub-folder
            self.subfolder2_encfiles_path = os.path.join(self.now_date_folder_enc_path,encfiles_subfolder2_name)

            # Encrypted folders secondary sub-folder
            self.subfolder2_encfolders_path = os.path.join(self.now_date_folder_enc_path, encfolders_subfolder2_name)

            # Deccrypted files secondary sub-folder
            self.subfolder2_decfiles_path = os.path.join(self.now_date_folder_dec_path, decfiles_subfolder2_name)

            # Deccrypted folders secondary sub-folder
            self.subfolder2_decfolders_path = os.path.join(self.now_date_folder_dec_path, decfolders_subfolder2_name)

            # collection folder-shorcut maker
            enc_dec_folder_shortcut_maker_dt(app_main_folder_root_var=self.collections_folder_path,years_sub_folder_root_var_enc=self.crnt_yrs_folder_path_enc,years_sub_folder_root_var_dec=self.crnt_yrs_folder_path_dec,date_sub_folder_root_var_enc=self.now_date_folder_enc_path,date_sub_folder_root_var_dec=self.now_date_folder_dec_path,
                                             subfolder2_root_var_encfiles=self.subfolder2_encfiles_path,subfolder2_root_var_decfiles=self.subfolder2_decfiles_path,subfolder2_root_var_encdirs=self.subfolder2_encfolders_path,subfolder2_root_var_decdirs=self.subfolder2_decfolders_path,
                                             folder_name_var=collections_folder_name)

            # open collection folder
            os.startfile(self.collections_folder_path)
        except FileNotFoundError:
            pass

    def Closewindow(self, event):

        self.Destroy()

        # decompress_dir_frame.Show()

        sys.exit()

    def exitbutton(self, event):

        ''' Asks user whether to use again as message box. if not, clears the values for the user, or exits the app if yes  '''
        yn_msgbox = wx.MessageDialog(self.wpanel, "Are you sure you want to exit the app?", "Yes/No",
                                     wx.YES_NO | wx.ICON_WARNING)

        yn_var = yn_msgbox.ShowModal()

        if yn_var == wx.ID_NO:

            pass

        else:
            
            self.Destroy()  # closes app when 'EXIT' button is click

            sys.exit()

    def dir_secure(self, event):

        try:

            self.dir_fg = FolderGuardian(parent=self.wpanel, id=-1)

            self.dir_fg.ShowModal()

        except AttributeError:
            pass
        except RuntimeError:
            pass

    def file_secure(self, event):

        try:

            self.file_fg = FileGuardian(parent=self.wpanel,id=-1)

            self.file_fg.ShowModal()

        except AttributeError:
            pass
        except RuntimeError:
            pass

        # sys.exit()

        # pass

    def modify2(self, event):

        fg_modify_lists = ["Choose here to change path for '{}' folder.".format(collections_folder_name), "Choose here to change password.",
                           "Choose here to change encrypted file name.","Choose here to change encrypted folder name."]

        onechoice = wx.SingleChoiceDialog(self.wpanel, "Which settings do you wish to change?",
                                          '{} - modify settings:'.format(app_name), fg_modify_lists)

        # choosen_choice_var = onechoice.GetStringSelection()

        if onechoice.ShowModal() == wx.ID_OK:

            # print ("Choosen mode -> %s\n" % onechoice.GetStringSelection())

            if onechoice.GetStringSelection() == fg_modify_lists[0]:
                self.changedir()
            elif onechoice.GetStringSelection() == fg_modify_lists[2]:
                self.files_encname_changer()
                # pass
            elif onechoice.GetStringSelection() == fg_modify_lists[3]:
                self.dirs_encname_changer()
            else:
                self.pswrds_changer()
        else:
            pass
        # pass

    def restrt_main(self):

        try:
            self.fg_dirs = FolderGuardian(parent=None, id=-1)
            self.fg_dirs.Destroy()

        except AttributeError:
            pass
        except RuntimeError:
            pass

        try:
            self.fg_files = FileGuardian(parent=None, id=-1)
            self.fg_files.Destroy()

        except AttributeError:
            pass
        except RuntimeError:
            pass

        self.Destroy()

        app = wx.App()

        encrypt_window = appUI(parent=None, id=-1)

        encrypt_window.Show()

        app.MainLoop()

    def files_encname_changer(self):

        while True:

            enc_pass_title = "{} - Encryption passcode entry".format(app_name)

            self.cipher_pass_input = wx.PasswordEntryDialog(self.wpanel, "Please type the encryption password:",
                                                            enc_pass_title, style=wx.TextEntryDialogStyle)

            if self.cipher_pass_input.ShowModal() == wx.ID_OK:

                # src_json_pswrd_enc = #self.json_passcode_access()

                if self.cipher_pass_input.GetValue() == "":

                    invld_err_input = wx.MessageDialog(self.wpanel, "Null values are not accepted.",
                                                       "{} - input verifier error:".format(app_name),
                                                       wx.ICON_ERROR | wx.STAY_ON_TOP)

                    invld_err_input.ShowModal()

                    # pass
                else:

                    if self.cipher_pass_input.GetValue() == self.encrypt_pass:

                        access_granted_msg_box = wx.MessageDialog(self.wpanel, "Password correct.",
                                                                  "{} - Access granted:".format(app_name),
                                                                  wx.ICON_INFORMATION | wx.STAY_ON_TOP)

                        access_granted_msg_box.ShowModal()

                        path_json = open(paths_datas_json_file_path, 'r')

                        data = path_json.read()

                        path_infos_v = json.loads(data)["path"]

                        # [Early-tests] app folders ->

                        # [Early-tests type] Main app folder path
                        self.et_collections_folder_path = os.path.join(path_infos_v, et_collections_folder_name)

                        # encrypted [Early-tests type] folder path
                        self.et_encrypted_files_folder_path = os.path.join(self.et_collections_folder_path,
                                                                           et_enc_folder_name)

                        # decrypted [Early-tests type] folder path
                        self.et_decrypted_files_folder_path = os.path.join(self.et_collections_folder_path,
                                                                           et_dec_folder_name)

                        # [Early-tests type] real-time 'Year' folder in 'Encrypted files' folder path
                        self.et_crnt_yrs_folder_path_enc = os.path.join(self.et_encrypted_files_folder_path, dt_yyyy)

                        # [Early-tests type] real-time 'Year' folder in 'Decrypted files' folder path
                        self.et_crnt_yrs_folder_path_dec = os.path.join(self.et_decrypted_files_folder_path, dt_yyyy)

                        # [Early-tests type] real-time 'date' folder in 'Encrypted files' folder path
                        self.et_now_date_folder_enc_path = os.path.join(self.et_crnt_yrs_folder_path_enc, dt_date)

                        # [Early-tests type] real-time 'date' folder in 'Decrypted files' folder path
                        self.et_now_date_folder_dec_path = os.path.join(self.et_crnt_yrs_folder_path_dec, dt_date)

                        # os.startfile(now_date_sub_folder_path)

                        # [Early-tests type] folder-shorcut maker
                        # enc_dec_folder_shortcut_maker_dt(app_main_folder_root_var=self.et_collections_folder_path,years_sub_folder_root_var_enc=self.et_crnt_yrs_folder_path_enc,years_sub_folder_root_var_dec=self.et_crnt_yrs_folder_path_dec,date_sub_folder_root_var_enc=self.et_now_date_folder_enc_path,date_sub_folder_root_var_dec=self.et_now_date_folder_dec_path,folder_name_var=et_collections_folder_name)

                        # Encrypted-name folder
                        # self.enc_item_name_folder_path = os.path.join(self.now_date_folder_enc_path,epoch_miliseconds_str)

                        # Main app folders ->

                        # Main collections folder path
                        self.collections_folder_path = os.path.join(path_infos_v, collections_folder_name)

                        # encrypted folder path
                        self.encrypted_files_folder_path = os.path.join(self.collections_folder_path, enc_folder_name)

                        # decrypted folder path
                        self.decrypted_files_folder_path = os.path.join(self.collections_folder_path, dec_folder_name)

                        # real-time 'years' folder in 'Encrypted files' folder path
                        self.crnt_yrs_folder_path_enc = os.path.join(self.encrypted_files_folder_path, dt_yyyy)

                        # real-time 'years' folder in 'Decrypted files' folder path
                        self.crnt_yrs_folder_path_dec = os.path.join(self.decrypted_files_folder_path, dt_yyyy)

                        # real-time 'date' folder in 'Encrypted files' folder path
                        self.now_date_folder_enc_path = os.path.join(self.crnt_yrs_folder_path_enc, dt_date)

                        # real-time 'date' folder in 'Decrypted files' folder path
                        self.now_date_folder_dec_path = os.path.join(self.crnt_yrs_folder_path_dec, dt_date)

                        # Encrypted files secondary sub-folder
                        self.subfolder2_encfiles_path = os.path.join(self.now_date_folder_enc_path,
                                                                     encfiles_subfolder2_name)

                        # Deccrypted files secondary sub-folder
                        self.subfolder2_decfiles_path = os.path.join(self.now_date_folder_enc_path,
                                                                     decfiles_subfolder2_name)

                        # Encrypted folders secondary sub-folder
                        self.subfolder2_encfolders_path = os.path.join(self.now_date_folder_enc_path,
                                                                       encfolders_subfolder2_name)

                        # Deccrypted folders secondary sub-folder
                        self.subfolder2_decfolders_path = os.path.join(self.now_date_folder_enc_path,
                                                                       decfolders_subfolder2_name)

                        # collection folder-shorcut maker
                        enc_dec_folder_shortcut_maker_dt(app_main_folder_root_var=self.collections_folder_path,
                                                         years_sub_folder_root_var_enc=self.crnt_yrs_folder_path_enc,
                                                         years_sub_folder_root_var_dec=self.crnt_yrs_folder_path_dec,
                                                         date_sub_folder_root_var_enc=self.now_date_folder_enc_path,
                                                         date_sub_folder_root_var_dec=self.now_date_folder_dec_path,
                                                         subfolder2_root_var_encfiles=self.subfolder2_encfiles_path,
                                                         subfolder2_root_var_decfiles=self.subfolder2_decfiles_path,
                                                         subfolder2_root_var_encdirs=self.subfolder2_encfolders_path,
                                                         subfolder2_root_var_decdirs=self.subfolder2_decfolders_path,
                                                         folder_name_var=collections_folder_name)

                        delay(0.16)

                        enc_filedir_dlgbox = wx.FileDialog(self.wpanel, "Please choose encryption file:",
                                                           self.subfolder2_encfiles_path, "",
                                                           wildcard="All files (*.*)|*.*; | Encrypted files (*.enc) | *.enc;",
                                                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

                        if enc_filedir_dlgbox.ShowModal() == wx.ID_OK:
                            enc_complete_file_rt = enc_filedir_dlgbox.GetPath()

                            enc_fl_basename = os.path.basename(enc_complete_file_rt)
                            try:

                                json_fl_r = open(json_file_backups_file_path, "r")

                                json_src_data = json.load(json_fl_r)

                                json_src_data["encrypted_file_name"] = enc_fl_basename.replace('.enc', '')

                                json_fl_w = open(json_file_backups_file_path, "w")

                                json.dump(json_src_data, json_fl_w)

                                json_fl_r.close()

                                json_fl_w.close()

                                update_made_msg = wx.MessageDialog(self.wpanel, "Encrypted file name changed.",
                                                                   "Name update - Complete:",
                                                                   wx.OK | wx.ICON_INFORMATION)

                                update_made_msg.ShowModal()

                                self.restrt()

                                break

                            except FileNotFoundError:

                                backup_fl_infos = {
                                    "encrypted_file_name": str(self.modify_cipher_name_input.GetValue()).replace(
                                        '.enc', '')
                                }

                                # Tranfers data And then stores it on the json file
                                jfl = open(json_file_backups_file_path, "w")

                                json.dump(backup_fl_infos, jfl)

                                jfl.close()

                                save_made_msg = wx.MessageDialog(self.wpanel, "Encrypted file name saved.",
                                                                 "Name save - Complete:",
                                                                 wx.OK | wx.ICON_INFORMATION)

                                save_made_msg.ShowModal()

                                self.restrt()

                                break
                        else:
                            break
                    else:

                        passcode_err_enc = wx.MessageDialog(self.wpanel, "Wrong password.",
                                                            "{} - passcode verifier error".format(app_name),
                                                            wx.ICON_ERROR | wx.STAY_ON_TOP)

                        passcode_err_enc.ShowModal()
            else:
                break
        pass

    def dirs_encname_changer(self):

        while True:

            enc_pass_title = "{} - Encrypted passcode entry".format(app_name)

            self.cipher_pass_input = wx.PasswordEntryDialog(self.wpanel, "Please type the encryption password:",
                                                            enc_pass_title, style=wx.TextEntryDialogStyle)

            if self.cipher_pass_input.ShowModal() == wx.ID_OK:

                # src_json_pswrd_enc = #self.json_passcode_access()

                if self.cipher_pass_input.GetValue() == "":

                    invld_err_input = wx.MessageDialog(self.wpanel, "Null values are not accepted.",
                                                       "{} - input verifier error:".format(app_name),
                                                       wx.ICON_ERROR | wx.STAY_ON_TOP)

                    invld_err_input.ShowModal()

                    # pass
                else:

                    if self.cipher_pass_input.GetValue() == self.encrypt_pass:

                        access_granted_msg_box = wx.MessageDialog(self.wpanel, "Password correct.",
                                                                  "{} - Access granted:".format(app_name),
                                                                  wx.ICON_INFORMATION | wx.STAY_ON_TOP)

                        access_granted_msg_box.ShowModal()

                        path_json = open(paths_datas_json_file_path, 'r')

                        data = path_json.read()

                        path_infos_v = json.loads(data)["path"]

                        # [Early-tests] app folders ->

                        # [Early-tests type] Main app folder path
                        self.et_collections_folder_path = os.path.join(path_infos_v, et_collections_folder_name)

                        # encrypted [Early-tests type] folder path
                        self.et_encrypted_files_folder_path = os.path.join(self.et_collections_folder_path,
                                                                           et_enc_folder_name)

                        # decrypted [Early-tests type] folder path
                        self.et_decrypted_files_folder_path = os.path.join(self.et_collections_folder_path,
                                                                           et_dec_folder_name)

                        # [Early-tests type] real-time 'Year' folder in 'Encrypted files' folder path
                        self.et_crnt_yrs_folder_path_enc = os.path.join(self.et_encrypted_files_folder_path, dt_yyyy)

                        # [Early-tests type] real-time 'Year' folder in 'Decrypted files' folder path
                        self.et_crnt_yrs_folder_path_dec = os.path.join(self.et_decrypted_files_folder_path, dt_yyyy)

                        # [Early-tests type] real-time 'date' folder in 'Encrypted files' folder path
                        self.et_now_date_folder_enc_path = os.path.join(self.et_crnt_yrs_folder_path_enc, dt_date)

                        # [Early-tests type] real-time 'date' folder in 'Decrypted files' folder path
                        self.et_now_date_folder_dec_path = os.path.join(self.et_crnt_yrs_folder_path_dec, dt_date)

                        # os.startfile(now_date_sub_folder_path)

                        # [Early-tests type] folder-shorcut maker
                        # enc_dec_folder_shortcut_maker_dt(app_main_folder_root_var=self.et_collections_folder_path,years_sub_folder_root_var_enc=self.et_crnt_yrs_folder_path_enc,years_sub_folder_root_var_dec=self.et_crnt_yrs_folder_path_dec,date_sub_folder_root_var_enc=self.et_now_date_folder_enc_path,date_sub_folder_root_var_dec=self.et_now_date_folder_dec_path,folder_name_var=et_collections_folder_name)

                        # Encrypted-name folder
                        # self.enc_item_name_folder_path = os.path.join(self.now_date_folder_enc_path,epoch_miliseconds_str)

                        # Main app folders ->

                        # Main collections folder path
                        self.collections_folder_path = os.path.join(path_infos_v, collections_folder_name)

                        # encrypted folder path
                        self.encrypted_files_folder_path = os.path.join(self.collections_folder_path, enc_folder_name)

                        # decrypted folder path
                        self.decrypted_files_folder_path = os.path.join(self.collections_folder_path, dec_folder_name)

                        # real-time 'years' folder in 'Encrypted files' folder path
                        self.crnt_yrs_folder_path_enc = os.path.join(self.encrypted_files_folder_path, dt_yyyy)

                        # real-time 'years' folder in 'Decrypted files' folder path
                        self.crnt_yrs_folder_path_dec = os.path.join(self.decrypted_files_folder_path, dt_yyyy)

                        # real-time 'date' folder in 'Encrypted files' folder path
                        self.now_date_folder_enc_path = os.path.join(self.crnt_yrs_folder_path_enc, dt_date)

                        # real-time 'date' folder in 'Decrypted files' folder path
                        self.now_date_folder_dec_path = os.path.join(self.crnt_yrs_folder_path_dec, dt_date)

                        # Encrypted files secondary sub-folder
                        self.subfolder2_encfiles_path = os.path.join(self.now_date_folder_enc_path,
                                                                     encfiles_subfolder2_name)

                        # Encrypted folders secondary sub-folder
                        self.subfolder2_encfolders_path = os.path.join(self.now_date_folder_enc_path,
                                                                       encfolders_subfolder2_name)

                        # Deccrypted files secondary sub-folder
                        self.subfolder2_decfiles_path = os.path.join(self.now_date_folder_dec_path,
                                                                     decfiles_subfolder2_name)

                        # Deccrypted folders secondary sub-folder
                        self.subfolder2_decfolders_path = os.path.join(self.now_date_folder_dec_path,
                                                                       decfolders_subfolder2_name)

                        # collection folder-shorcut maker
                        enc_dec_folder_shortcut_maker_dt(app_main_folder_root_var=self.collections_folder_path,
                                                         years_sub_folder_root_var_enc=self.crnt_yrs_folder_path_enc,
                                                         years_sub_folder_root_var_dec=self.crnt_yrs_folder_path_dec,
                                                         date_sub_folder_root_var_enc=self.now_date_folder_enc_path,
                                                         date_sub_folder_root_var_dec=self.now_date_folder_dec_path,
                                                         subfolder2_root_var_encfiles=self.subfolder2_encfiles_path,
                                                         subfolder2_root_var_decfiles=self.subfolder2_decfiles_path,
                                                         subfolder2_root_var_encdirs=self.subfolder2_encfolders_path,
                                                         subfolder2_root_var_decdirs=self.subfolder2_decfolders_path,
                                                         folder_name_var=collections_folder_name)

                        delay(0.16)

                        enc_filedir_dlgbox = wx.FileDialog(self.wpanel, "Please choose encryption file:", self.subfolder2_encfolders_path, "",
                                                       wildcard="All files (*.*)|*.*; | Encrypted files (*.enc) | *.enc;",
                                                       style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

                        if enc_filedir_dlgbox.ShowModal() == wx.ID_OK:
                            enc_complete_file_rt = enc_filedir_dlgbox.GetPath()

                            enc_fl_basename = os.path.basename(enc_complete_file_rt)
                            try:

                                json_fl_r = open(json_folder_backups_file_path, "r")

                                json_src_data = json.load(json_fl_r)

                                json_src_data["encrypted_zip_folder_name"] = enc_fl_basename.replace('.enc', '')

                                json_fl_w = open(json_file_backups_file_path, "w")

                                json.dump(json_src_data, json_fl_w)

                                json_fl_r.close()

                                json_fl_w.close()

                                update_made_msg = wx.MessageDialog(self.wpanel, "Encrypted folder name changed.",
                                                                       "Encrypted Folder Name update - Complete:",
                                wx.OK | wx.ICON_INFORMATION)

                                update_made_msg.ShowModal()

                                self.restrt()

                                break

                            except FileNotFoundError:

                                backup_dirs_infos = {
                                "encrypted_zip_folder_name": enc_fl_basename.replace('.enc', '')
                                   }

                                # Tranfers data And then stores it on the json file
                                jfl = open(json_folder_backups_file_path, "w")

                                json.dump(backup_dirs_infos, jfl)

                                jfl.close()

                                save_made_msg = wx.MessageDialog(self.wpanel, "Encrypted folder name saved.",
                                                                     "Encrypted Folder Name save - Complete:",
                                wx.OK | wx.ICON_INFORMATION)

                                save_made_msg.ShowModal()

                                self.restrt()

                                break
                        else:
                            break
                    else:

                        passcode_err_enc = wx.MessageDialog(self.wpanel, "Wrong password.",
                                                            "{} - passcode verifier error".format(app_name),
                                                            wx.ICON_ERROR | wx.STAY_ON_TOP)

                        passcode_err_enc.ShowModal()
            else:
                break
        pass

    def pswrds_changer(self):

        fg_modify_pswrds_lists = ['Choose here to change password for encryption.           ', 'Choose here to change password for decryption.       ']

        onechoice_pswrds = wx.SingleChoiceDialog(self.wpanel, "Which password do you wish to change?",
                                                 '{} - modify passwords:'.format(app_name), fg_modify_pswrds_lists)

        choosen_choice_var_pswrds = onechoice_pswrds.GetStringSelection()

        if onechoice_pswrds.ShowModal() == wx.ID_OK:

            # print ("YT saver mode, %s\n" % onechoice.GetStringSelection())

            if onechoice_pswrds.GetStringSelection() == fg_modify_pswrds_lists[0]:

                # self.changeenc()

                while True:

                    enc_pass_title = "{} - Encryption passcode entry".format(app_name)

                    self.cipher_pass_input = wx.PasswordEntryDialog(self.wpanel, "Please type the encryption password:",
                                                                    enc_pass_title, style=wx.TextEntryDialogStyle)

                    if self.cipher_pass_input.ShowModal() == wx.ID_OK:

                        # src_json_pswrd_enc = #self.json_passcode_access()

                        if self.cipher_pass_input.GetValue() == "":

                            invld_passwrd_err_input = wx.MessageDialog(self.wpanel, "Null passwords are not accepted.",
                                                                       "{} input verifier error - Password invalid:".format(
                                                                           app_name), wx.ICON_ERROR | wx.STAY_ON_TOP)

                            invld_passwrd_err_input.ShowModal()

                            # pass

                        else:

                            if self.cipher_pass_input.GetValue() == self.encrypt_pass:

                                access_granted_msg_box = wx.MessageDialog(self.wpanel, "Password correct.",
                                                                          "{} - Access granted:".format(app_name),
                                                                          wx.ICON_INFORMATION | wx.STAY_ON_TOP)

                                access_granted_msg_box.ShowModal()

                                delay(0.16)

                                modify_enc_pass_title = "{} - Modify encryption passcode entry:".format(app_name)

                                self.modify_cipher_pass_input = wx.PasswordEntryDialog(self.wpanel,
                                                                                       "Please type the encryption password to be modified.",
                                                                                       modify_enc_pass_title,
                                                                                       style=wx.TextEntryDialogStyle)

                                if self.modify_cipher_pass_input.ShowModal() == wx.ID_OK:

                                    if self.modify_cipher_pass_input.GetValue() == "":

                                        invld_err_input = wx.MessageDialog(self.wpanel, "Null values are not accepted.",
                                                                           "{} - input verifier error:".format(
                                                                               app_name),
                                                                           wx.ICON_ERROR | wx.STAY_ON_TOP)

                                        invld_err_input.ShowModal()

                                        # pass
                                    else:

                                        json_fl_r = open(passwords_json_file_path, "r")

                                        json_src_data = json.load(json_fl_r)

                                        json_src_data["encrypt_passcode"] = cipher.encrypt(bytes(str(self.modify_cipher_pass_input.GetValue()), 'utf-8')).decode()

                                        #json_src_data["encrypt_passcode"] = self.modify_cipher_pass_input.GetValue()

                                        json_fl_w = open(passwords_json_file_path, "w")

                                        json.dump(json_src_data, json_fl_w)

                                        json_fl_r.close()

                                        json_fl_w.close()

                                        update_made_msg = wx.MessageDialog(self.wpanel, "Encryption password changed.",
                                                                           "Password update - Complete",
                                                                           wx.OK | wx.ICON_INFORMATION)

                                        update_made_msg.ShowModal()

                                        self.restrt_main()

                                        break
                                else:
                                    break
                            else:

                                passcode_err_enc = wx.MessageDialog(self.wpanel, "Wrong password.",
                                                                    "{} - passcode verifier error".format(app_name),
                                                                    wx.ICON_ERROR | wx.STAY_ON_TOP)

                                passcode_err_enc.ShowModal()
                    else:
                        break

            else:
                # pass

                # self.changedec()

                while True:

                    dec_pass_title = "{} - Decryption passcode entry:".format(app_name)

                    self.decipher_pass_input = wx.PasswordEntryDialog(self.wpanel,
                                                                      "Please type the decryption password:",
                                                                      dec_pass_title, style=wx.TextEntryDialogStyle)

                    if self.decipher_pass_input.ShowModal() == wx.ID_OK:

                        # src_json_pswrd_dec = #self.json_passcode_access()

                        if self.decipher_pass_input.GetValue() == "":

                            invld_err_input = wx.MessageDialog(self.wpanel, "Null values are not accepted.",
                                                               "{} - input verifier error:".format(app_name),
                                                               wx.ICON_ERROR | wx.STAY_ON_TOP)

                            invld_err_input.ShowModal()

                            # pass
                        else:

                            if self.decipher_pass_input.GetValue() == self.decrypt_pass:

                                access_granted_msg_box = wx.MessageDialog(self.wpanel, "Password correct.",
                                                                          "{} - Access granted:".format(app_name),
                                                                          wx.ICON_INFORMATION | wx.STAY_ON_TOP)

                                access_granted_msg_box.ShowModal()

                                delay(0.16)

                                modify_enc_pass_title = "{} - Modify decryption passcode entry:".format(app_name)

                                self.modify_decipher_pass_input = wx.PasswordEntryDialog(self.wpanel,
                                                                                         "Please type the decryption password to be modified.",
                                                                                         modify_enc_pass_title,
                                                                                         style=wx.TextEntryDialogStyle)

                                if self.modify_decipher_pass_input.ShowModal() == wx.ID_OK:

                                    if self.modify_decipher_pass_input.GetValue() == "":

                                        invld_passwrd_err_input = wx.MessageDialog(self.wpanel,
                                                                                   "Null passwords are not accepted.",
                                                                                   "{} input verifier error - Password invalid:".format(
                                                                                       app_name),
                                                                                   wx.ICON_ERROR | wx.STAY_ON_TOP)

                                        invld_passwrd_err_input.ShowModal()

                                    else:

                                        json_fl_r = open(passwords_json_file_path, "r")

                                        json_src_data = json.load(json_fl_r)

                                        json_src_data["decrypt_passcode"] = cipher.encrypt(bytes(str(self.modify_decipher_pass_input.GetValue()), 'utf-8')).decode()

                                        #json_src_data["decrypt_passcode"] = self.modify_decipher_pass_input.GetValue()

                                        json_fl_w = open(passwords_json_file_path, "w")

                                        json.dump(json_src_data, json_fl_w)

                                        json_fl_r.close()

                                        json_fl_w.close()

                                        update_made_msg = wx.MessageDialog(self.wpanel, "Decryption password changed.",
                                                                           "Password update - Complete",
                                                                           wx.OK | wx.ICON_INFORMATION)

                                        update_made_msg.ShowModal()

                                        self.restrt_main()

                                        break
                                else:
                                    break
                            else:

                                passcode_err_dec = wx.MessageDialog(self.wpanel, "Wrong password.",
                                                                    "{} - passcode verifier error".format(app_name),
                                                                    wx.ICON_ERROR | wx.STAY_ON_TOP)

                                passcode_err_dec.ShowModal()
                    else:
                        break
            # self.json_data_fl.close()

    def changedir(self):

        while True:

            modify_dir_dlgbox = wx.DirDialog(self.wpanel, "Please choose folder (or directory) to be changed:", "",
                                             wx.DD_DEFAULT_STYLE | wx.DD_CHANGE_DIR)

            if modify_dir_dlgbox.ShowModal() == wx.ID_OK:

                usr_rt_v = modify_dir_dlgbox.GetPath()

                if usr_rt_v == "":

                    invld_err_input = wx.MessageDialog(self.wpanel, "Null values are not accepted.",
                                                       "{} - input verifier error:".format(app_name),
                                                       wx.ICON_ERROR | wx.STAY_ON_TOP)

                    invld_err_input.ShowModal()

                else:

                    try:
                        json_fl_r = open(paths_datas_json_file_path, "r")

                        json_src_data = json.load(json_fl_r)

                        json_src_data["path"] = usr_rt_v

                        json_fl_w = open(paths_datas_json_file_path, "w")

                        json.dump(json_src_data, json_fl_w)

                        json_fl_r.close()

                        json_fl_w.close()

                        update_made_msg = wx.MessageDialog(self.wpanel, "Path changed.", "Path update - Complete",
                                                           wx.OK | wx.ICON_INFORMATION)

                        update_made_msg.ShowModal()

                        # [Early-tests type] 'folder json file' operation
                        # path_json = open(et_paths_datas_json_file_path, 'r')

                        path_json = open(paths_datas_json_file_path, 'r')

                        data = path_json.read()

                        path_infos_v = json.loads(data)["path"]

                        path_json.close()

                    except FileNotFoundError:

                        settings_json = open(paths_datas_json_file_path, 'w')

                        settings_json.write("{"'"path"'":")

                        usr_path = {
                            "path": str(usr_rt_v)
                        }

                        json_settings_file_datas = open(paths_datas_json_file_path, "w")

                        json.dump(usr_path, json_settings_file_datas)

                        json_settings_file_datas.close()

                        settings_json.close()

                        settings_path_saved_msg = wx.MessageDialog(self.wpanel, "Path saved.", "Path update - Complete",
                                                                   wx.OK | wx.ICON_INFORMATION)

                        settings_path_saved_msg.ShowModal()

                        # [Early-tests type] 'folder json file' operation
                        # path_json = open(et_paths_datas_json_file_path, 'r')

                        path_json = open(paths_datas_json_file_path, 'r')

                        data = path_json.read()

                        path_infos_v = json.loads(data)["path"]

                        # et_pascode_json_exists = os.path.exists(et_settings_json_full_path)

                        # [Early-tests type] Main app folder path
                        self.et_collections_folder_path = os.path.join(path_infos_v, et_collections_folder_name)

                        # [Early-tests type] encrypted folder path
                        self.et_encrypted_files_folder_path = os.path.join(self.et_collections_folder_path,
                                                                           et_enc_folder_name)

                        # [Early-tests type]  decrypted folder path
                        self.et_decrypted_files_folder_path = os.path.join(self.et_collections_folder_path,
                                                                           et_dec_folder_name)

                        # [Early-tests type] real-time 'Year' folder in 'Encrypted files' folder path
                        self.et_crnt_yrs_folder_enc_path = os.path.join(self.et_encrypted_files_folder_path, dt_yyyy)

                        # [Early-tests type] real-time 'Year' folder in 'Decrypted files' folder path
                        self.et_crnt_yrs_folder_dec_path = os.path.join(self.et_decrypted_files_folder_path, dt_yyyy)

                        # [Early-tests type] real-time 'date' folder in 'Encrypted files' folder
                        self.et_now_date_folder_enc_path = os.path.join(self.et_crnt_yrs_folder_enc_path, dt_date)

                        # [Early-tests type] real-time 'date' folder in 'Decrypted files' folder
                        self.et_now_date_folder_dec_path = os.path.join(self.et_crnt_yrs_folder_dec_path, dt_date)

                        # [Early-tests type] Folder-shorcut maker
                        # enc_dec_folder_shortcut_maker_dt(app_main_folder_root_var=self.et_collections_folder_path,years_sub_folder_root_var_enc=self.et_crnt_yrs_folder_path,date_sub_folder_root_var_enc=self.et_now_date_folder_enc_path,date_sub_folder_root_var_dec=self.et_now_date_folder_dec_path,folder_name_var=et_collections_folder_name)

                        # [Early-tests type] Encrypted-name folder
                        # self.enc_item_name_folder_path = os.path.join(self.now_date_folder_enc_path,epoch_miliseconds_str)

                    # Main app folders ->

                        # Main collections folder path
                        self.collections_folder_path = os.path.join(path_infos_v, collections_folder_name)

                        # encrypted folder
                        self.encrypted_files_folder_path = os.path.join(self.collections_folder_path, enc_folder_name)

                        # Real-time 'Year' folder in 'Encrypted files' folder path
                        self.crnt_yrs_folder_path = os.path.join(self.et_encrypted_files_folder_path, dt_yyyy)

                        # decrypted folder
                        self.decrypted_files_folder_path = os.path.join(self.collections_folder_path, dec_folder_name)

                        # real-time 'date' folder in 'Encrypted files' folder
                        self.et_now_date_folder_enc_path = os.path.join(self.crnt_yrs_folder_path_enc, dt_date)

                        # real-time 'date' folder in 'Decrypted files' folder
                        self.now_date_folder_dec_path = os.path.join(self.crnt_yrs_folder_path_dec, dt_date)

                        # Encrypted files secondary sub-folder
                        self.subfolder2_encfiles_path = os.path.join(self.now_date_folder_enc_path,
                                                                     encfiles_subfolder2_name)

                        # Encrypted folders secondary sub-folder
                        self.subfolder2_encfolders_path = os.path.join(self.now_date_folder_enc_path,
                                                                       encfolders_subfolder2_name)

                        # Deccrypted files secondary sub-folder
                        self.subfolder2_decfiles_path = os.path.join(self.now_date_folder_dec_path,
                                                                     decfiles_subfolder2_name)

                        # Deccrypted folders secondary sub-folder
                        self.subfolder2_decfolders_path = os.path.join(self.now_date_folder_dec_path,
                                                                       decfolders_subfolder2_name)

                        # collection folder-shorcut maker
                        enc_dec_folder_shortcut_maker_dt(app_main_folder_root_var=self.collections_folder_path,
                                                         years_sub_folder_root_var_enc=self.crnt_yrs_folder_path_enc,
                                                         years_sub_folder_root_var_dec=self.crnt_yrs_folder_path_dec,
                                                         date_sub_folder_root_var_enc=self.now_date_folder_enc_path,
                                                         date_sub_folder_root_var_dec=self.now_date_folder_dec_path,
                                                         subfolder2_root_var_encfiles=self.subfolder2_encfiles_path,
                                                         subfolder2_root_var_decfiles=self.subfolder2_decfiles_path,
                                                         subfolder2_root_var_encdirs=self.subfolder2_encfolders_path,
                                                         subfolder2_root_var_decdirs=self.subfolder2_decfolders_path,
                                                         folder_name_var=collections_folder_name)

                        path_json.close()
                break
            else:
                break

    def exitbutton(self, event):
        ''' Asks user whether to use again as message box. if not, clears the values for the user, or exits the app if yes  '''
        yn_msgbox = wx.MessageDialog(self.wpanel, "Are you sure you want to exit the app?", "Yes/No",
                                     wx.YES_NO | wx.ICON_WARNING)

        yn_var = yn_msgbox.ShowModal()

        if yn_var == wx.ID_NO:

            pass

        else:

            try:
                self.fg_dirs = FolderGuardian(parent=None, id=-1)
                self.fg_dirs.Destroy()

            except AttributeError:
                pass
            except RuntimeError:
                pass

            try:
                self.fg_files = FileGuardian(parent=None, id=-1)
                self.fg_files.Destroy()

            except AttributeError:
                pass
            except RuntimeError:
                pass

            self.Destroy()  # closes app when 'EXIT' button is click

            sys.exit()

    def Close(self, event):
        self.Destroy()  # closes app  when 'CLOSE' or 'X' on the window is pressed

        sys.exit()


class FolderGuardian(wx.Dialog):

    # Unzips frame upon user request or 'CLICKING' the app
    def __init__(self, parent, id):

        # et_folder_guardian_title = '{} - Folder Guardian'.format(file_name)

        folder_guardian_title = '{} - Folder Guardian'.format(app_title)

        # Window (Frame) with parametres i.e (frame, parent=None,id=-1.'window title',size=(int,int),style=wx.(obj))
        wx.Frame.__init__(self, parent, id,folder_guardian_title, size=(657, 563))

        try:
            self.SetIcon(wx.Icon(ico_flpath))  # Sets icon on the window title bar
        except NameError:
            pass

        self.wpanel = wx.Panel(self)  # setting 'container' to have wxpython GUI parts

        self.wpanel.SetBackgroundColour('Steel blue')  # Sets the panel or app background

        # -----> labels & inputs

        # Foler Name

        # Creates fonts for the label
        name1_lbl_font = wx.Font(22, wx.ROMAN, wx.FONTSTYLE_MAX, wx.FONTWEIGHT_BOLD)

        self.name1_lbl = wx.StaticText(self.wpanel, -1, "Portfolio secure 12 P.E.F ++ (210-F3.6) - \nFolder Guardian", (67, 85), (24, 24),
                                             wx.TEXT_ALIGNMENT_CENTRE)

        # Sets font for the label text variable
        self.name1_lbl.SetFont(name1_lbl_font)

        # Sets the label Text colour
        self.name1_lbl.SetForegroundColour('white')

        # Sets the given colour for the label ( label BG colour )
        self.name1_lbl.SetBackgroundColour('Indian Red')

        # Creates fonts for the label
        encdirs_details_lblfont = wx.Font(22, wx.ROMAN, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD)

        self.encdirs_details_lbl = wx.StaticText(self.wpanel, -1, "Encrypting and decrypting folders.", (67, 194), (24, 24), wx.TEXT_ALIGNMENT_CENTRE)

        # Sets font for the label using variable
        self.encdirs_details_lbl.SetFont(encdirs_details_lblfont)

        # Sets the given colour for the button text
        self.encdirs_details_lbl.SetForegroundColour('Black')

        # Sets the given colour for the button ( button BG colour )
        self.encdirs_details_lbl.SetBackgroundColour('white')


        # ----->  Buttons

        # Encryot button - folder guardian

        # Creates fonts for the button
        encdirs_font = wx.Font(21, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        # Creates button with parameters
        self.encdirs_btn = wx.Button(self.wpanel, label='ENCRYPT', pos=(67, 301), size=(156, 45), style=wx.BORDER_RAISED)

        # Creates font for the button
        self.encdirs_btn.SetFont(encdirs_font)

        # Sets the given colour for the button text
        self.encdirs_btn.SetForegroundColour('White')

        # Sets the given colour for the button ( button BG colour )
        self.encdirs_btn.SetBackgroundColour('Dark Green')

        # Sets tooltip (pop-up details)
        self.encdirs_btn.SetToolTip("Click here to encrypt the folder.")

        # Combines the button with its respective functions
        self.Bind(wx.EVT_BUTTON, self.cipher_folder_accesscode,
                  self.encdirs_btn)

        # Exit button

        # Creates fonts for exit button
        btn_exit_font = wx.Font(21, wx.ROMAN, wx.FONTSTYLE_NORMAL,
                                wx.FONTWEIGHT_BOLD)  # Creates  fonts for 'Exit' button

        # Creates button
        self.exit_btn = wx.Button(self.wpanel, label='EXIT', pos=(67, 404), size=(156, 45), style=wx.BORDER_RAISED)

        # Sets font for the button
        self.exit_btn.SetFont(btn_exit_font)

        # Sets the given colour for the button text
        self.exit_btn.SetForegroundColour('White')

        # Sets the given colour for the button ( button BG colour )
        self.exit_btn.SetBackgroundColour('Red')

        # Sets pop-up details
        self.exit_btn.SetToolTip("Click here to close.")

        # Combines button with its respective functions
        self.Bind(wx.EVT_BUTTON, self.exitbutton, self.exit_btn)


        # Decrypt button

        # Creates fonts for 'Access folder' button
        btn_dec_font = wx.Font(21, wx.ROMAN, wx.FONTSTYLE_NORMAL,
                               wx.FONTWEIGHT_BOLD)  # Creates  fonts for 'Reset' button

        # Creates button
        self.open_folder_btn = wx.Button(self.wpanel, label='DECRYPT', pos=(412, 301), size=(156, 45),
                                         style=wx.BORDER_RAISED)

        # Sets font for the button using variable
        self.open_folder_btn.SetFont(btn_dec_font)

        # Sets the given colour for the button text
        self.open_folder_btn.SetForegroundColour('White')

        # Sets the given colour for the button ( button BG colour )
        self.open_folder_btn.SetBackgroundColour('BLUE')

        # Sets tooltip (pop-up details)
        self.open_folder_btn.SetToolTip("Click here to decrypt folder.")

        # Combines button with its respective functions
        self.Bind(wx.EVT_BUTTON, self.decipher_folder_accesscode, self.open_folder_btn)

        # Access button

        # Creates fonts for the button
        btn_rst_font = wx.Font(21, wx.ROMAN, wx.FONTSTYLE_NORMAL,
                               wx.FONTWEIGHT_BOLD)  # Creates  fonts for 'Reset' button

        # Creates the button
        self.open_folder_btn = wx.Button(self.wpanel, label='ACCESS', pos=(242, 349), size=(156, 45),
                                         style=wx.BORDER_RAISED)

        # Sets font for the button using variable
        self.open_folder_btn.SetFont(btn_rst_font)

        # Sets the given colour for the button text
        self.open_folder_btn.SetForegroundColour('White')

        # Sets the given colour for the button ( button BG colour )
        self.open_folder_btn.SetBackgroundColour('CORNFLOWER BLUE')

        # Sets tooltip (pop-up details)
        self.open_folder_btn.SetToolTip("Click here to open '{}' folder.".format(collections_folder_name))

        # Combines button with its respective functions
        self.Bind(wx.EVT_BUTTON, self.open_collection_folder_dt2, self.open_folder_btn)

        # Modify button

        # Creates fonts for the button
        btn_mod_font = wx.Font(18, wx.ROMAN, wx.FONTSTYLE_NORMAL,
                               wx.FONTWEIGHT_BOLD)

        #  Creates button
        self.modify_btn = wx.Button(self.wpanel, label='MODIFY', pos=(412, 404), size=(156, 45), style=wx.BORDER_RAISED)

        # Sets font for the button using variable
        self.modify_btn.SetFont(btn_mod_font)

        # Sets the given colour for the button text
        self.modify_btn.SetForegroundColour('Red')

        # Sets the given colour for the button ( button BG colour )
        self.modify_btn.SetBackgroundColour('Yellow')

        # Sets tooltip (pop-up details)
        self.modify_btn.SetToolTip("Click here to change path settings.")

        # Combines button with its respective functions
        self.Bind(wx.EVT_BUTTON, self.modify2, self.modify_btn)

        # close window button
        self.Bind(wx.EVT_CLOSE, self.Close)

        try:

            self.json_data_fl = open(passwords_json_file_path, "r")

            data = json.load(self.json_data_fl)

            self.decrypt_pass = cipher.decrypt(bytes(str(data["decrypt_passcode"]), 'utf-8')).decode()

            self.encrypt_pass = cipher.decrypt(bytes(str(data["encrypt_passcode"]), 'utf-8')).decode()

        except json.decoder.JSONDecodeError:
            password_json_overwrite(json_path_val=passwords_json_file_path,enc_pswrd_var=encrypt_passcode_no_encrypted,dec_pswrd_var=decrypt_passcode_no_encrypted)
        except FileNotFoundError:
            pass

    def open_collection_folder_dt2(self, event):

        """ Verify 'path.json' if exists or not """
        settings_json_fl_exists = os.path.exists(paths_datas_json_file_path)

        if settings_json_fl_exists == False:

            dir_dlgbox = wx.DirDialog(self.wpanel, "Please choose folder (or directory) to hold '{}' folder:".format(collections_folder_name), "",
                                      wx.DD_DEFAULT_STYLE | wx.DD_CHANGE_DIR)

            # dir_dlgbox.Set(wDir_path)

            if dir_dlgbox.ShowModal() == wx.ID_OK:

                usr_rt_v = dir_dlgbox.GetPath()

                settings_json = open(paths_datas_json_file_path, 'w')

                settings_json.write("{"'"path"'":")

                usr_path = {
                    "path": str(usr_rt_v)
                }

                json_settings_file_datas = open(paths_datas_json_file_path, "w")

                json.dump(usr_path, json_settings_file_datas)

                json_settings_file_datas.close()

                settings_json.close()

                settings_path_saved_msg = wx.MessageDialog(self.wpanel, "Path saved.", "Path update - Complete:",
                                                           wx.OK | wx.ICON_INFORMATION)

                settings_path_saved_msg.ShowModal()

            else:
                pass
        else:
            pass

        try:

            # [Early-tests type] 'folder json file' operation
            # path_json = open(et_paths_datas_json_file_path, 'r')

            path_json = open(paths_datas_json_file_path, 'r')

            data = path_json.read()

            path_infos_v = json.loads(data)["path"]

            # [Early-tests] app folders ->

            # [Early-tests type] Main app folder path
            self.et_collections_folder_path = os.path.join(path_infos_v, et_collections_folder_name)

            # encrypted [Early-tests type] folder path
            self.et_encrypted_files_folder_path = os.path.join(self.et_collections_folder_path, et_enc_folder_name)

            # [Early-tests type] real-time 'Year' folder in 'Encrypted files' folder path
            self.et_crnt_yrs_folder_path_enc = os.path.join(self.et_encrypted_files_folder_path, dt_yyyy)

            # [Early-tests type] real-time 'Year' folder in 'Decrypted files' folder path
            self.et_crnt_yrs_folder_path_dec = os.path.join(self.et_encrypted_files_folder_path, dt_yyyy)

            # decrypted [Early-tests type] folder path
            self.et_decrypted_files_folder_path = os.path.join(self.et_collections_folder_path, et_dec_folder_name)

            # [Early-tests type] real-time 'date' folder in 'Encrypted files' folder path
            self.et_now_date_folder_enc_path = os.path.join(self.et_crnt_yrs_folder_path_enc, dt_date)

            # [Early-tests type] real-time 'date' folder in 'Decrypted files' folder path
            self.et_now_date_folder_dec_path = os.path.join(self.et_crnt_yrs_folder_path_dec, dt_date)
            # os.startfile(now_date_sub_folder_path)

            # [Early-tests type] folder-shorcut maker
            # enc_dec_folder_shortcut_maker_dt(app_main_folder_root_var=self.et_collections_folder_path,years_sub_folder_root_var_enc=self.et_crnt_yrs_folder_path_enc,years_sub_folder_root_var_dec=self.et_crnt_yrs_folder_path_dec,date_sub_folder_root_var_enc=self.et_now_date_folder_enc_path,date_sub_folder_root_var_dec=self.et_now_date_folder_dec_path,folder_name_var=et_collections_folder_name)

            # Encrypted-name folder
            # self.enc_item_name_folder_path = os.path.join(self.now_date_folder_enc_path,epoch_miliseconds_str)

            # [Early-tests type] open collection folder
            # os.startfile(self.et_collections_folder_path)

        # Main app folders ->
            # Main collections folder path
            self.collections_folder_path = os.path.join(path_infos_v, collections_folder_name)

            # encrypted folder path
            self.encrypted_files_folder_path = os.path.join(self.collections_folder_path, enc_folder_name)

            # decrypted folder path
            self.decrypted_files_folder_path = os.path.join(self.collections_folder_path, dec_folder_name)

            # real-time 'Year' folder in 'Encrypted files' folder path
            self.crnt_yrs_folder_path_enc = os.path.join(self.encrypted_files_folder_path, dt_yyyy)

            # real-time 'years' folder in 'Decrypted files' folder path
            self.crnt_yrs_folder_path_dec = os.path.join(self.decrypted_files_folder_path, dt_yyyy)

            # real-time 'date' folder in 'Encrypted files' folder path
            self.now_date_folder_enc_path = os.path.join(self.crnt_yrs_folder_path_enc, dt_date)

            # real-time 'date' folder in 'Decrypted files' folder path
            self.now_date_folder_dec_path = os.path.join(self.crnt_yrs_folder_path_dec, dt_date)

            # Encrypted files secondary sub-folder
            self.subfolder2_encfiles_path = os.path.join(self.now_date_folder_enc_path,
                                                                 encfiles_subfolder2_name)

            # Encrypted folders secondary sub-folder
            self.subfolder2_encfolders_path = os.path.join(self.now_date_folder_enc_path,
                                                                   encfolders_subfolder2_name)

            # Deccrypted files secondary sub-folder
            self.subfolder2_decfiles_path = os.path.join(self.now_date_folder_dec_path,
                                                                 decfiles_subfolder2_name)

            # Deccrypted folders secondary sub-folder
            self.subfolder2_decfolders_path = os.path.join(self.now_date_folder_dec_path,
                                                                   decfolders_subfolder2_name)

            # collection folder-shorcut maker
            enc_dec_folder_shortcut_maker_dt(app_main_folder_root_var=self.collections_folder_path,
                                             years_sub_folder_root_var_enc=self.crnt_yrs_folder_path_enc,
                                             years_sub_folder_root_var_dec=self.crnt_yrs_folder_path_dec,
                                             date_sub_folder_root_var_enc=self.now_date_folder_enc_path,
                                             date_sub_folder_root_var_dec=self.now_date_folder_dec_path,
                                             subfolder2_root_var_encfiles=self.subfolder2_encfiles_path,
                                             subfolder2_root_var_decfiles=self.subfolder2_decfiles_path,
                                             subfolder2_root_var_encdirs=self.subfolder2_encfolders_path,
                                             subfolder2_root_var_decdirs=self.subfolder2_decfolders_path,
                                             folder_name_var=collections_folder_name)

            # open collection folder
            os.startfile(self.collections_folder_path)

            path_json.close()

        except FileNotFoundError:
            pass
        # pass

    def modify2(self, event):

        fg_modify_lists = ["Choose here to change path for '{}' folder.".format(collections_folder_name), "Choose here to change password.",
                           "Choose here to change encrypted folder name."]

        onechoice = wx.SingleChoiceDialog(self.wpanel, "Which settings do you wish to change?",
                                          '{} - modify settings:'.format(app_name), fg_modify_lists)

        # choosen_choice_var = onechoice.GetStringSelection()

        if onechoice.ShowModal() == wx.ID_OK:

            # print ("Choosen mode -> %s\n" % onechoice.GetStringSelection())

            if onechoice.GetStringSelection() == fg_modify_lists[0]:
                self.changedir()
            elif onechoice.GetStringSelection() == fg_modify_lists[2]:
                self.dirs_encname_changer()
                # pass
            else:
                self.pswrds_changer()
        else:
            pass
        # pass

    def restrt_fg_dirs(self):

        try:
            self.fg_dirs = FolderGuardian(parent=None, id=-1)
            self.fg_dirs.Destroy()

        except AttributeError:
            pass
        except RuntimeError:
            pass

        try:
            self.fg_files = FileGuardian(parent=None, id=-1)
            self.fg_files.Destroy()

        except AttributeError:
            pass
        except RuntimeError:
            pass

        self.Destroy()

        self.fg_files = FileGuardian(parent=None, id=-1)
        self.fg_files.ShowModal()


    def dirs_encname_changer(self):

        while True:

            enc_pass_title = "{} - Encrypted passcode entry".format(app_name)

            self.cipher_pass_input = wx.PasswordEntryDialog(self.wpanel, "Please type the encryption password:",
                                                            enc_pass_title, style=wx.TextEntryDialogStyle)

            if self.cipher_pass_input.ShowModal() == wx.ID_OK:

                # src_json_pswrd_enc = #self.json_passcode_access()

                if self.cipher_pass_input.GetValue() == "":

                    invld_err_input = wx.MessageDialog(self.wpanel, "Null values are not accepted.",
                                                       "{} - input verifier error:".format(app_name),
                                                       wx.ICON_ERROR | wx.STAY_ON_TOP)

                    invld_err_input.ShowModal()

                    # pass
                else:

                    if self.cipher_pass_input.GetValue() == self.encrypt_pass:

                        access_granted_msg_box = wx.MessageDialog(self.wpanel, "Password correct.",
                                                                  "{} - Access granted:".format(app_name),
                                                                  wx.ICON_INFORMATION | wx.STAY_ON_TOP)

                        access_granted_msg_box.ShowModal()

                        path_json = open(paths_datas_json_file_path, 'r')

                        data = path_json.read()

                        path_infos_v = json.loads(data)["path"]

                        # [Early-tests] app folders ->

                        # [Early-tests type] Main app folder path
                        self.et_collections_folder_path = os.path.join(path_infos_v, et_collections_folder_name)

                        # encrypted [Early-tests type] folder path
                        self.et_encrypted_files_folder_path = os.path.join(self.et_collections_folder_path,
                                                                           et_enc_folder_name)

                        # decrypted [Early-tests type] folder path
                        self.et_decrypted_files_folder_path = os.path.join(self.et_collections_folder_path,
                                                                           et_dec_folder_name)

                        # [Early-tests type] real-time 'Year' folder in 'Encrypted files' folder path
                        self.et_crnt_yrs_folder_path_enc = os.path.join(self.et_encrypted_files_folder_path, dt_yyyy)

                        # [Early-tests type] real-time 'Year' folder in 'Decrypted files' folder path
                        self.et_crnt_yrs_folder_path_dec = os.path.join(self.et_decrypted_files_folder_path, dt_yyyy)

                        # [Early-tests type] real-time 'date' folder in 'Encrypted files' folder path
                        self.et_now_date_folder_enc_path = os.path.join(self.et_crnt_yrs_folder_path_enc, dt_date)

                        # [Early-tests type] real-time 'date' folder in 'Decrypted files' folder path
                        self.et_now_date_folder_dec_path = os.path.join(self.et_crnt_yrs_folder_path_dec, dt_date)

                        # os.startfile(now_date_sub_folder_path)

                        # [Early-tests type] folder-shorcut maker
                        # enc_dec_folder_shortcut_maker_dt(app_main_folder_root_var=self.et_collections_folder_path,years_sub_folder_root_var_enc=self.et_crnt_yrs_folder_path_enc,years_sub_folder_root_var_dec=self.et_crnt_yrs_folder_path_dec,date_sub_folder_root_var_enc=self.et_now_date_folder_enc_path,date_sub_folder_root_var_dec=self.et_now_date_folder_dec_path,folder_name_var=et_collections_folder_name)

                        # Encrypted-name folder
                        # self.enc_item_name_folder_path = os.path.join(self.now_date_folder_enc_path,epoch_miliseconds_str)

                        # Main app folders ->

                        # Main collections folder path
                        self.collections_folder_path = os.path.join(path_infos_v, collections_folder_name)

                        # encrypted folder path
                        self.encrypted_files_folder_path = os.path.join(self.collections_folder_path, enc_folder_name)

                        # decrypted folder path
                        self.decrypted_files_folder_path = os.path.join(self.collections_folder_path, dec_folder_name)

                        # real-time 'years' folder in 'Encrypted files' folder path
                        self.crnt_yrs_folder_path_enc = os.path.join(self.encrypted_files_folder_path, dt_yyyy)

                        # real-time 'years' folder in 'Decrypted files' folder path
                        self.crnt_yrs_folder_path_dec = os.path.join(self.decrypted_files_folder_path, dt_yyyy)

                        # real-time 'date' folder in 'Encrypted files' folder path
                        self.now_date_folder_enc_path = os.path.join(self.crnt_yrs_folder_path_enc, dt_date)

                        # real-time 'date' folder in 'Decrypted files' folder path
                        self.now_date_folder_dec_path = os.path.join(self.crnt_yrs_folder_path_dec, dt_date)

                        # Encrypted files secondary sub-folder
                        self.subfolder2_encfiles_path = os.path.join(self.now_date_folder_enc_path,
                                                                     encfiles_subfolder2_name)

                        # Encrypted folders secondary sub-folder
                        self.subfolder2_encfolders_path = os.path.join(self.now_date_folder_enc_path,
                                                                       encfolders_subfolder2_name)

                        # Deccrypted files secondary sub-folder
                        self.subfolder2_decfiles_path = os.path.join(self.now_date_folder_dec_path,
                                                                     decfiles_subfolder2_name)

                        # Deccrypted folders secondary sub-folder
                        self.subfolder2_decfolders_path = os.path.join(self.now_date_folder_dec_path,
                                                                       decfolders_subfolder2_name)

                        # collection folder-shorcut maker
                        enc_dec_folder_shortcut_maker_dt(app_main_folder_root_var=self.collections_folder_path,
                                                         years_sub_folder_root_var_enc=self.crnt_yrs_folder_path_enc,
                                                         years_sub_folder_root_var_dec=self.crnt_yrs_folder_path_dec,
                                                         date_sub_folder_root_var_enc=self.now_date_folder_enc_path,
                                                         date_sub_folder_root_var_dec=self.now_date_folder_dec_path,
                                                         subfolder2_root_var_encfiles=self.subfolder2_encfiles_path,
                                                         subfolder2_root_var_decfiles=self.subfolder2_decfiles_path,
                                                         subfolder2_root_var_encdirs=self.subfolder2_encfolders_path,
                                                         subfolder2_root_var_decdirs=self.subfolder2_decfolders_path,
                                                         folder_name_var=collections_folder_name)

                        delay(0.16)

                        enc_filedir_dlgbox = wx.FileDialog(self.wpanel, "Please choose encryption file:", self.subfolder2_encfolders_path, "",
                                                       wildcard="All files (*.*)|*.*; | Encrypted files (*.enc) | *.enc;",
                                                       style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

                        if enc_filedir_dlgbox.ShowModal() == wx.ID_OK:
                            enc_complete_file_rt = enc_filedir_dlgbox.GetPath()

                            enc_fl_basename = os.path.basename(enc_complete_file_rt)
                            try:

                                json_fl_r = open(json_folder_backups_file_path, "r")

                                json_src_data = json.load(json_fl_r)

                                json_src_data["encrypted_zip_folder_name"] = enc_fl_basename.replace('.enc', '')

                                json_fl_w = open(json_file_backups_file_path, "w")

                                json.dump(json_src_data, json_fl_w)

                                json_fl_r.close()

                                json_fl_w.close()

                                update_made_msg = wx.MessageDialog(self.wpanel, "Encrypted folder name changed.",
                                                                       "Encrypted Folder Name update - Complete:",
                                wx.OK | wx.ICON_INFORMATION)

                                update_made_msg.ShowModal()

                                self.restrt()

                                break

                            except FileNotFoundError:

                                backup_dirs_infos = {
                                "encrypted_zip_folder_name": enc_fl_basename.replace('.enc', '')
                                   }

                                # Tranfers data And then stores it on the json file
                                jfl = open(json_folder_backups_file_path, "w")

                                json.dump(backup_dirs_infos, jfl)

                                jfl.close()

                                save_made_msg = wx.MessageDialog(self.wpanel, "Encrypted folder name saved.",
                                                                     "Encrypted Folder Name save - Complete:",
                                wx.OK | wx.ICON_INFORMATION)

                                save_made_msg.ShowModal()

                                self.restrt()

                                break
                        else:
                            break
                    else:

                        passcode_err_enc = wx.MessageDialog(self.wpanel, "Wrong password.",
                                                            "{} - passcode verifier error".format(app_name),
                                                            wx.ICON_ERROR | wx.STAY_ON_TOP)

                        passcode_err_enc.ShowModal()
            else:
                break
        pass

    def pswrds_changer(self):

        fg_modify_pswrds_lists = ['Choose here to change password for encryption.              ', 'Choose here to change password for decryption.         ']

        onechoice_pswrds = wx.SingleChoiceDialog(self.wpanel, "Which password do you wish to change?",
                                                 '{} - modify passwords:'.format(app_name), fg_modify_pswrds_lists)

        # choosen_choice_var_pswrds = onechoice_pswrds.GetStringSelection()

        if onechoice_pswrds.ShowModal() == wx.ID_OK:

            # print ("YT saver mode, %s\n" % onechoice.GetStringSelection())

            if onechoice_pswrds.GetStringSelection() == fg_modify_pswrds_lists[0]:

                # self.changeenc()

                while True:

                    enc_pass_title = "{} - Encryption passcode entry".format(app_name)

                    self.cipher_pass_input = wx.PasswordEntryDialog(self.wpanel, "Please type the encryption password:",
                                                                    enc_pass_title, style=wx.TextEntryDialogStyle)

                    if self.cipher_pass_input.ShowModal() == wx.ID_OK:

                        # src_json_pswrd_enc = #self.json_passcode_access()

                        if self.cipher_pass_input.GetValue() == "":

                            invld_passwrd_err_input = wx.MessageDialog(self.wpanel, "Null passwords are not accepted.",
                                                                       "{} input verifier error - Password invalid:".format(
                                                                           app_name), wx.ICON_ERROR | wx.STAY_ON_TOP)

                            invld_passwrd_err_input.ShowModal()

                            # pass

                        else:

                            if self.cipher_pass_input.GetValue() == self.encrypt_pass:

                                access_granted_msg_box = wx.MessageDialog(self.wpanel, "Password correct.",
                                                                          "{} - Access granted:".format(app_name),
                                                                          wx.ICON_INFORMATION | wx.STAY_ON_TOP)

                                access_granted_msg_box.ShowModal()

                                delay(0.16)

                                modify_enc_pass_title = "{} - Modify encryption passcode entry:".format(app_name)

                                self.modify_cipher_pass_input = wx.PasswordEntryDialog(self.wpanel,
                                                                                       "Please type the encryption password to be modified.",
                                                                                       modify_enc_pass_title,
                                                                                       style=wx.TextEntryDialogStyle)

                                if self.modify_cipher_pass_input.ShowModal() == wx.ID_OK:

                                    if self.modify_cipher_pass_input.GetValue() == "":

                                        invld_err_input = wx.MessageDialog(self.wpanel, "Null values are not accepted.",
                                                                           "{} - input verifier error:".format(
                                                                               app_name),
                                                                           wx.ICON_ERROR | wx.STAY_ON_TOP)

                                        invld_err_input.ShowModal()

                                        # pass
                                    else:

                                        json_fl_r = open(passwords_json_file_path, "r")

                                        json_src_data = json.load(json_fl_r)

                                        json_src_data["encrypt_passcode"] = cipher.encrypt(bytes(str(self.modify_cipher_pass_input.GetValue()), 'utf-8')).decode()

                                        #json_src_data["encrypt_passcode"] = self.modify_cipher_pass_input.GetValue()

                                        json_fl_w = open(passwords_json_file_path, "w")

                                        json.dump(json_src_data, json_fl_w)

                                        json_fl_r.close()

                                        json_fl_w.close()

                                        update_made_msg = wx.MessageDialog(self.wpanel, "Encryption password changed.",
                                                                           "Password update - Complete",
                                                                           wx.OK | wx.ICON_INFORMATION)

                                        update_made_msg.ShowModal()

                                        self.restrt_fg_dirs()

                                        break
                                else:
                                    break
                            else:

                                passcode_err_enc = wx.MessageDialog(self.wpanel, "Wrong password.",
                                                                    "{} - passcode verifier error".format(app_name),
                                                                    wx.ICON_ERROR | wx.STAY_ON_TOP)

                                passcode_err_enc.ShowModal()
                    else:
                        break

            else:
                # pass

                # self.changedec()

                while True:

                    dec_pass_title = "{} - Decryption passcode entry:".format(app_name)

                    self.decipher_pass_input = wx.PasswordEntryDialog(self.wpanel,
                                                                      "Please type the decryption password:",
                                                                      dec_pass_title, style=wx.TextEntryDialogStyle)

                    if self.decipher_pass_input.ShowModal() == wx.ID_OK:

                        # src_json_pswrd_dec = #self.json_passcode_access()

                        if self.decipher_pass_input.GetValue() == "":

                            invld_err_input = wx.MessageDialog(self.wpanel, "Null values are not accepted.",
                                                               "{} - input verifier error:".format(app_name),
                                                               wx.ICON_ERROR | wx.STAY_ON_TOP)

                            invld_err_input.ShowModal()

                            # pass
                        else:

                            if self.decipher_pass_input.GetValue() == self.decrypt_pass:

                                access_granted_msg_box = wx.MessageDialog(self.wpanel, "Password correct.",
                                                                          "{} - Access granted:".format(app_name),
                                                                          wx.ICON_INFORMATION | wx.STAY_ON_TOP)

                                access_granted_msg_box.ShowModal()

                                delay(0.16)

                                modify_enc_pass_title = "{} - Modify decryption passcode entry:".format(app_name)

                                self.modify_decipher_pass_input = wx.PasswordEntryDialog(self.wpanel,
                                                                                         "Please type the decryption password to be modified.",
                                                                                         modify_enc_pass_title,
                                                                                         style=wx.TextEntryDialogStyle)

                                if self.modify_decipher_pass_input.ShowModal() == wx.ID_OK:

                                    if self.modify_decipher_pass_input.GetValue() == "":

                                        invld_passwrd_err_input = wx.MessageDialog(self.wpanel,
                                                                                   "Null passwords are not accepted.",
                                                                                   "{} input verifier error - Password invalid:".format(
                                                                                       app_name),
                                                                                   wx.ICON_ERROR | wx.STAY_ON_TOP)

                                        invld_passwrd_err_input.ShowModal()

                                    else:

                                        json_fl_r = open(passwords_json_file_path, "r")

                                        json_src_data = json.load(json_fl_r)

                                        json_src_data["decrypt_passcode"] = cipher.encrypt(bytes(str(self.modify_decipher_pass_input.GetValue()), 'utf-8')).decode()

                                        #json_src_data["decrypt_passcode"] = self.modify_decipher_pass_input.GetValue()

                                        json_fl_w = open(passwords_json_file_path, "w")

                                        json.dump(json_src_data, json_fl_w)

                                        json_fl_r.close()

                                        json_fl_w.close()

                                        update_made_msg = wx.MessageDialog(self.wpanel, "Decryption password changed.",
                                                                           "Password update - Complete",
                                                                           wx.OK | wx.ICON_INFORMATION)

                                        update_made_msg.ShowModal()

                                        self.restrt()

                                        break
                                else:
                                    break
                            else:

                                passcode_err_dec = wx.MessageDialog(self.wpanel, "Wrong password.",
                                                                    "{} - passcode verifier error".format(app_name),
                                                                    wx.ICON_ERROR | wx.STAY_ON_TOP)

                                passcode_err_dec.ShowModal()
                    else:
                        break
                self.json_data_fl.close()

    def changedir(self):

        while True:

            modify_dir_dlgbox = wx.DirDialog(self.wpanel, "Please choose folder (or directory) to be changed:", "",
                                             wx.DD_DEFAULT_STYLE | wx.DD_CHANGE_DIR)

            if modify_dir_dlgbox.ShowModal() == wx.ID_OK:

                usr_rt_v = modify_dir_dlgbox.GetPath()

                if usr_rt_v == "":

                    invld_err_input = wx.MessageDialog(self.wpanel, "Null values are not accepted.",
                                                       "{} - input verifier error:".format(app_name),
                                                       wx.ICON_ERROR | wx.STAY_ON_TOP)

                    invld_err_input.ShowModal()

                else:

                    try:
                        json_fl_r = open(paths_datas_json_file_path, "r")

                        json_src_data = json.load(json_fl_r)

                        json_src_data["path"] = usr_rt_v

                        json_fl_w = open(paths_datas_json_file_path, "w")

                        json.dump(json_src_data, json_fl_w)

                        json_fl_r.close()

                        json_fl_w.close()

                        update_made_msg = wx.MessageDialog(self.wpanel, "Path changed.", "Path update - Complete",
                                                           wx.OK | wx.ICON_INFORMATION)

                        update_made_msg.ShowModal()

                        # [Early-tests type] 'folder json file' operation
                        # path_json = open(et_paths_datas_json_file_path, 'r')

                        path_json = open(paths_datas_json_file_path, 'r')

                        data = path_json.read()

                        path_infos_v = json.loads(data)["path"]

                        path_json.close()

                    except FileNotFoundError:

                        settings_json = open(paths_datas_json_file_path, 'w')

                        settings_json.write("{"'"path"'":")

                        usr_path = {
                            "path": str(usr_rt_v)
                        }

                        json_settings_file_datas = open(paths_datas_json_file_path, "w")

                        json.dump(usr_path, json_settings_file_datas)

                        json_settings_file_datas.close()

                        settings_json.close()

                        settings_path_saved_msg = wx.MessageDialog(self.wpanel, "Path saved.", "Path update - Complete",
                                                                   wx.OK | wx.ICON_INFORMATION)

                        settings_path_saved_msg.ShowModal()

                        # [Early-tests type] 'folder json file' operation
                        #path_json = open(et_paths_datas_json_file_path, 'r')

                        path_json = open(paths_datas_json_file_path, 'r')

                        data = path_json.read()

                        path_infos_v = json.loads(data)["path"]

                        # et_pascode_json_exists = os.path.exists(et_settings_json_full_path)

                        # [Early-tests type] Main app folder path
                        self.et_collections_folder_path = os.path.join(path_infos_v, et_collections_folder_name)

                        # [Early-tests type] encrypted folder path
                        self.et_encrypted_files_folder_path = os.path.join(self.et_collections_folder_path,
                                                                           et_enc_folder_name)

                        # [Early-tests type]  decrypted folder path
                        self.et_decrypted_files_folder_path = os.path.join(self.et_collections_folder_path,
                                                                           et_dec_folder_name)

                        # [Early-tests type] real-time 'Year' folder in 'Encrypted files' folder path
                        self.et_crnt_yrs_folder_path_enc = os.path.join(self.et_encrypted_files_folder_path, dt_yyyy)

                        # [Early-tests type] real-time 'Year' folder in 'Decrypted files' folder path
                        self.et_crnt_yrs_folder_path_dec = os.path.join(self.et_decrypted_files_folder_path, dt_yyyy)

                        # [Early-tests type] real-time 'date' folder in 'Encrypted files' folder
                        self.et_now_date_folder_enc_path = os.path.join(self.et_crnt_yrs_folder_path_enc, dt_date)

                        # [Early-tests type] real-time 'date' folder in 'Decrypted files' folder
                        self.et_now_date_folder_dec_path = os.path.join(self.et_crnt_yrs_folder_path_dec, dt_date)

                        # [Early-tests type] Folder-shorcut maker
                        # enc_dec_folder_shortcut_maker_dt(app_main_folder_root_var=self.et_collections_folder_path,years_sub_folder_root_var_enc=self.et_crnt_yrs_folder_path_enc,years_sub_folder_root_var_dec=self.et_crnt_yrs_folder_path_dec,date_sub_folder_root_var_enc=self.et_now_date_folder_enc_path,date_sub_folder_root_var_dec=self.et_now_date_folder_dec_path,folder_name_var=et_collections_folder_name)

                        # [Early-tests type] Encrypted-name folder
                        # self.enc_item_name_folder_path = os.path.join(self.now_date_folder_enc_path,epoch_miliseconds_str)

                    # Main app folders ->

                        # Main collections folder path
                        self.collections_folder_path = os.path.join(path_infos_v, collections_folder_name)

                        # encrypted folder
                        self.encrypted_files_folder_path = os.path.join(self.collections_folder_path, enc_folder_name)

                        # decrypted folder
                        self.decrypted_files_folder_path = os.path.join(self.collections_folder_path, dec_folder_name)

                        # real-time 'Year' folder in 'Encrypted files' folder path
                        self.crnt_yrs_folder_path_enc = os.path.join(self.encrypted_files_folder_path, dt_yyyy)

                        # real-time 'Year' folder in 'Decrypted files' folder path
                        self.crnt_yrs_folder_path_dec = os.path.join(self.decrypted_files_folder_path, dt_yyyy)

                        # real-time 'date' folder in 'Encrypted files' folder
                        self.now_date_folder_enc_path = os.path.join(self.et_crnt_yrs_folder_path_enc, dt_date)

                        # real-time 'date' folder in 'Decrypted files' folder
                        self.now_date_folder_dec_path = os.path.join(self.et_crnt_yrs_folder_path_dec, dt_date)

                        # Encrypted files secondary sub-folder
                        self.subfolder2_encfiles_path = os.path.join(self.now_date_folder_enc_path,
                                                                     encfiles_subfolder2_name)

                        # Encrypted folders secondary sub-folder
                        self.subfolder2_encfolders_path = os.path.join(self.now_date_folder_enc_path,
                                                                       encfolders_subfolder2_name)

                        # Deccrypted files secondary sub-folder
                        self.subfolder2_decfiles_path = os.path.join(self.now_date_folder_dec_path,
                                                                     decfiles_subfolder2_name)

                        # Deccrypted folders secondary sub-folder
                        self.subfolder2_decfolders_path = os.path.join(self.now_date_folder_dec_path,
                                                                       decfolders_subfolder2_name)

                        # File Guardain folder-shorcut maker
                        enc_dec_folder_shortcut_maker_dt(app_main_folder_root_var=self.collections_folder_path,
                                                         years_sub_folder_root_var_enc=self.crnt_yrs_folder_path_enc,
                                                         years_sub_folder_root_var_dec=self.crnt_yrs_folder_path_dec,
                                                         date_sub_folder_root_var_enc=self.now_date_folder_enc_path,
                                                         date_sub_folder_root_var_dec=self.now_date_folder_dec_path,
                                                         subfolder2_root_var_encfiles=self.subfolder2_encfiles_path,
                                                         subfolder2_root_var_decfiles=self.subfolder2_decfiles_path,
                                                         subfolder2_root_var_encdirs=self.subfolder2_encfolders_path,
                                                         subfolder2_root_var_decdirs=self.subfolder2_decfolders_path,
                                                         folder_name_var=collections_folder_name)

                        path_json.close()
                break
            else:
                break

    def dir_opts_dlg(self):

        """ Verify 'path.json' if exists or not """
        settings_json_paths_exists = os.path.exists(paths_datas_json_file_path)

        if settings_json_paths_exists == False:

            dir_dlgbox = wx.DirDialog(self.wpanel, "Please choose directory (or Path):", "",
                                      wx.DD_DEFAULT_STYLE | wx.DD_CHANGE_DIR)

            # dir_dlgbox.Set(wDir_path)
            if dir_dlgbox.ShowModal() == wx.ID_OK:

                usr_rt_v = dir_dlgbox.GetPath()

                settings_json = open(paths_datas_json_file_path, 'w')

                settings_json.write("{"'"path"'":")

                usr_path = {
                    "path": str(usr_rt_v)
                }

                json_settings_file_datas = open(paths_datas_json_file_path, "w")

                json.dump(usr_path, json_settings_file_datas)

                json_settings_file_datas.close()

                settings_json.close()

                settings_path_saved_msg = wx.MessageDialog(self.wpanel, "Path saved.", "Path update - Complete",
                                                           wx.OK | wx.ICON_INFORMATION)

                settings_path_saved_msg.ShowModal()

            else:
                pass
        else:
            pass

        try:
            # [Early-tests type] 'folder json file' operation
            #path_json = open(et_paths_datas_json_file_path, 'r')

            path_json = open(paths_datas_json_file_path, 'r')

            data = path_json.read()

            path_infos_v = json.loads(data)["path"]

            # et_pascode_json_exists = os.path.exists(et_settings_json_full_path)

        # ''' Early-tests type app folder details  '''
            # [Early-tests type] Main app  folder path
            #self.et_collections_folder_path = os.path.join(path_infos_v, et_collections_folder_name)

            # [Early-tests type] encrypted folder path
            #self.et_encrypted_files_folder_path = os.path.join(self.et_collections_folder_path, et_enc_folder_name)

            # [Early-tests type] decrypted folder path
            #self.et_decrypted_files_folder_path = os.path.join(self.et_collections_folder_path, et_dec_folder_name)

            # [Early-tests type] real-time 'Year' folder in 'Encrypted files' folder path
            #elf.et_crnt_yrs_folder_path_enc = os.path.join(self.et_encrypted_files_folder_path, dt_yyyy)

            # [Early-tests type] real-time 'Year' folder in 'Decrypted files' folder path
            #self.et_crnt_yrs_folder_path_dec = os.path.join(self.et_decrypted_files_folder_path, dt_yyyy)

            # [Early-tests type] real-time 'date' folder in 'Encrypted files' folder path
            #self.et_now_date_folder_enc_path = os.path.join(self.et_crnt_yrs_folder_path_enc, dt_date)

            # [Early-tests type] real-time 'date' folder in 'Decrypted files' folder path
            #self.et_now_date_folder_dec_path = os.path.join(self.et_crnt_yrs_folder_path_dec, dt_date)
            # os.startfile(now_date_sub_folder_path)

            # [Early-tests type] Folder-shorcut maker
            # enc_dec_folder_shortcut_maker_dt(app_main_folder_root_var=self.et_collections_folder_path,years_sub_folder_root_var_enc=self.et_crnt_yrs_folder_path_enc,years_sub_folder_root_var_dec=self.et_crnt_yrs_folder_path_dec,date_sub_folder_root_var_enc=self.et_now_date_folder_enc_path,date_sub_folder_root_var_dec=self.et_now_date_folder_dec_path,folder_name_var=et_collections_folder_name)

        # Main app folders ->
            # Main collections folder path
            self.collections_folder_path = os.path.join(path_infos_v, collections_folder_name)

            # encrypted folder path
            self.encrypted_files_folder_path = os.path.join(self.collections_folder_path, enc_folder_name)

            # decrypted folder path
            self.decrypted_files_folder_path = os.path.join(self.collections_folder_path, dec_folder_name)

            # real-time 'Year' folder in 'Encrypted files' folder path
            self.crnt_yrs_folder_path_enc = os.path.join(self.encrypted_files_folder_path, dt_yyyy)

            # real-time 'Year' folder in 'Decrypted files' folder path
            self.crnt_yrs_folder_path_dec = os.path.join(self.decrypted_files_folder_path, dt_yyyy)

            # real-time 'date' folder in 'Encrypted files' folder path
            self.now_date_folder_enc_path = os.path.join(self.crnt_yrs_folder_path_enc, dt_date)

            # real-time 'date' folder in 'Decrypted files' folder path
            self.now_date_folder_dec_path = os.path.join(self.crnt_yrs_folder_path_dec, dt_date)

            # Encrypted files secondary sub-folder
            self.subfolder2_encfiles_path = os.path.join(self.now_date_folder_enc_path,
                                                                 encfiles_subfolder2_name)

            # Encrypted folders secondary sub-folder
            self.subfolder2_encfolders_path = os.path.join(self.now_date_folder_enc_path,
                                                                   encfolders_subfolder2_name)

            # Deccrypted files secondary sub-folder
            self.subfolder2_decfiles_path = os.path.join(self.now_date_folder_dec_path,
                                                                 decfiles_subfolder2_name)

            # Deccrypted folders secondary sub-folder
            self.subfolder2_decfolders_path = os.path.join(self.now_date_folder_dec_path,
                                                                   decfolders_subfolder2_name)

            # Folder Guardian folder-shorcut maker
            enc_dec_folder_shortcut_maker_dt(app_main_folder_root_var=self.collections_folder_path,
                                             years_sub_folder_root_var_enc=self.crnt_yrs_folder_path_enc,
                                             years_sub_folder_root_var_dec=self.crnt_yrs_folder_path_dec,
                                             date_sub_folder_root_var_enc=self.now_date_folder_enc_path,
                                             date_sub_folder_root_var_dec=self.now_date_folder_dec_path,
                                             subfolder2_root_var_encfiles=self.subfolder2_encfiles_path,
                                             subfolder2_root_var_decfiles=self.subfolder2_decfiles_path,
                                             subfolder2_root_var_encdirs=self.subfolder2_encfolders_path,
                                             subfolder2_root_var_decdirs=self.subfolder2_decfolders_path,
                                             folder_name_var=collections_folder_name)

            path_json.close()

        except FileNotFoundError:
            pass

    def decipher_folder_accesscode(self, event):

        self.dir_opts_dlg()

        # self.json_passcode_access()

        try:

            dec_pass_title = "{} - Decryption passcode entry".format(app_name)

            if os.path.exists(passwords_json_file_path) == True:

                while True:

                    self.decipher_pass_input = wx.PasswordEntryDialog(self.wpanel,
                                                                      "Please type the password for decryption:",
                                                                      dec_pass_title, style=wx.TextEntryDialogStyle)

                    if self.decipher_pass_input.ShowModal() == wx.ID_OK:

                        if self.decipher_pass_input.GetValue() == '':

                            invld_passwrd_err_input = wx.MessageDialog(self.wpanel, "Null passwords are not accepted.",
                                                                       "{} input verifier error - Password invalid:".format(
                                                                           app_name), wx.ICON_ERROR | wx.STAY_ON_TOP)

                            invld_passwrd_err_input.ShowModal()

                        else:

                            if self.decipher_pass_input.GetValue() == self.decrypt_pass:

                                # encrypt_frame(parent=self.wpanel,id=-1).Destroy()

                                # self.decryption()
                                self.decipher_folder()

                                break

                            else:
                                passcode_err_dec = wx.MessageDialog(self.wpanel, "Wrong password for decryption.",
                                                                    "{} - passcode verifier error".format(app_name),
                                                                    wx.ICON_ERROR | wx.STAY_ON_TOP)

                                passcode_err_dec.ShowModal()

                                # self.decipher_pass_input.ShowModal()
                    else:
                        break

                    self.json_data_fl.close()
            else:
                pass
        except AttributeError:
            pass

    def decipher_folder(self):

        try:

            ''' Accessing datas from 'backup' batch file '''
            try:
                # [Early-tests type] 'folder json file' operation - read
                #json_fl_read = open(et_json_folder_backups_file_path, 'r')

                # 'folder json file' operation - read
                json_fl_read = open(json_folder_backups_file_path, 'r')

                data = json_fl_read.read()

                # Get file details using dictionary 'key-value' pairs
                # json_src_file_name = json.loads(data)["file_name"]

                # json_src_file_format = json.loads(data)["file_type"]

                json_src_enc_name = json.loads(data)["encrypted_zip_folder_name"]

                # json_src_file_full_name = json.loads(data)["file_full_name"]

                # print("Encrypted namse -> "+enc_name)

                # file_full_name = "{0}.{1}".format(json_src_file_name,json_src_file_format)

                folder_full_name_json_decoded = cipher.decrypt(bytes(json_src_enc_name, 'utf-8')).decode()

                ''' Make  Deccrypted-item folder in real-time  date 'Decrypted files' folder folder'''
                # dec_item_name_id = "{0}_{1}".format(json_src_file_name,json_src_enc_name)

                # Decrypted-item folder path with real time now-date sub folder
                # dec_item_name_folder = os.path.join(self.et_now_date_folder_dec_path,file_full_name_json_decoded)

                # DirMake(dec_item_name_folder)

                # dec_complete_file_rt = os.path.join(dec_item_name_folder,file_full_name_json_decoded)

                # [Early-tests type] Decrypted folder path with real time now-date sub folder
                #et_dec_complete_file_rt = os.path.join(self.et_now_date_folder_dec_path, folder_full_name_json_decoded)

                # Decrypted folder path with real time now-date sub folder
                dec_complete_file_rt = os.path.join(self.now_date_folder_dec_path, folder_full_name_json_decoded)

                # Encrypted file source file name
                file_name_enc = '{}.enc'.format(json_src_enc_name)

                path_json = open(paths_datas_json_file_path, 'r')

                data = path_json.read()

                path_infos_v = json.loads(data)["path"]

            # Main app folders ->
                # Main collections folder path
                self.collections_folder_path = os.path.join(path_infos_v, collections_folder_name)

                # encrypted folder path
                self.encrypted_files_folder_path = os.path.join(self.collections_folder_path, enc_folder_name)

                # decrypted folder path
                self.decrypted_files_folder_path = os.path.join(self.collections_folder_path, dec_folder_name)

                # real-time 'years' folder in 'Encrypted files' folder
                self.crnt_yrs_folder_path_enc = os.path.join(self.encrypted_files_folder_path, dt_yyyy)

                # real-time 'years' folder in 'Decrypted files' folder path
                self.crnt_yrs_folder_path_dec = os.path.join(self.decrypted_files_folder_path, dt_yyyy)

                # real-time 'date' folder in 'Encrypted files' folder path
                self.now_date_folder_enc_path = os.path.join(self.crnt_yrs_folder_path_enc, dt_date)

                # real-time 'date' folder in 'Decrypted files' folder path
                self.now_date_folder_dec_path = os.path.join(self.crnt_yrs_folder_path_dec, dt_date)

                # Encrypted files secondary sub-folder
                self.subfolder2_encfiles_path = os.path.join(self.now_date_folder_enc_path, encfiles_subfolder2_name)

                # Encrypted folders secondary sub-folder
                self.subfolder2_encfolders_path = os.path.join(self.now_date_folder_enc_path,
                                                               encfolders_subfolder2_name)

                # Deccrypted files secondary sub-folder
                self.subfolder2_decfiles_path = os.path.join(self.now_date_folder_dec_path, decfiles_subfolder2_name)

                # Deccrypted folders secondary sub-folder
                self.subfolder2_decfolders_path = os.path.join(self.now_date_folder_dec_path,
                                                               decfolders_subfolder2_name)

                # collection folder-shorcut maker
                enc_dec_folder_shortcut_maker_dt(app_main_folder_root_var=self.collections_folder_path,
                                                 years_sub_folder_root_var_enc=self.crnt_yrs_folder_path_enc,
                                                 years_sub_folder_root_var_dec=self.crnt_yrs_folder_path_dec,
                                                 date_sub_folder_root_var_enc=self.now_date_folder_enc_path,
                                                 date_sub_folder_root_var_dec=self.now_date_folder_dec_path,
                                                 subfolder2_root_var_encfiles=self.subfolder2_encfiles_path,
                                                 subfolder2_root_var_decfiles=self.subfolder2_decfiles_path,
                                                 subfolder2_root_var_encdirs=self.subfolder2_encfolders_path,
                                                 subfolder2_root_var_decdirs=self.subfolder2_decfolders_path,
                                                 folder_name_var=collections_folder_name)

                # Decrypted zip folder name
                # dec_zip_file_name = {
                # Encrypted-name folder from json folder
                # enc_item_name_src_json_folder_path  = os.path.join(self.et_now_date_folder_enc_path,json_src_enc_name)

                # Encrypted-item file details with real time now-date sub folder
                # complete_file_rt_enc_json = os.path.join(enc_item_name_src_json_folder_path,file_name_enc)

                # [Early-tests type] Encrypted files details with real time now-date sub folder
                #et_complete_file_rt_enc_json = os.path.join(self.et_now_date_folder_enc_path, json_src_enc_name)

                # print('\nPath -> '+et_complete_file_rt_enc_json)

                # Encrypted files details with real time now-date sub folder
                complete_file_rt_enc_json = os.path.join(self.subfolder2_encfolders_path, file_name_enc)

                file_name , file_type = os.path.splitext(os.path.basename(folder_full_name_json_decoded))

                complete_file_rt_dec = os.path.join(self.subfolder2_decfolders_path, file_name)

                #print(complete_file_rt_dec)

                try:
                    if os.path.exists(complete_file_rt_dec) == False:
                        encrypt_fl = open(complete_file_rt_enc_json, 'rb')

                        enc_file_data = encrypt_fl.read()

                        Decrypted_file = cipher.decrypt(enc_file_data)

                        # [Early-tests type] 'folder json file' operation - read
                        #dec_fl = open(et_dec_complete_file_rt, 'wb')

                        dec_fl = open(dec_complete_file_rt, 'wb')

                        dec_fl.write(Decrypted_file)

                        dec_fl.close()

                        encrypt_fl.close()

                        json_fl_read.close()

                        # [Early-tests type] Deletes encrypted file completely
                        # os.remove(et_complete_file_rt_enc_json)

                        # Deletes encrypted item folder completely
                        # os.removedirs(enc_item_name_src_json_folder_path)

                        #  Deletes encrypted file completely
                        os.remove(complete_file_rt_enc_json)

                        # print('\n- File sucessfully decrypted..')

                        with zipfile.ZipFile(dec_complete_file_rt, 'r') as zf_dec:

                            zf_dec.extractall(complete_file_rt_dec)

                        zf_dec.close()

                        os.remove(dec_complete_file_rt)

                        delay(0.16)

                        msg_dec_succcess = wx.MessageDialog(self.wpanel,
                                                            "'{}' folder successfully decrypted.".format(file_name),
                                                            "{} - decryption info.".format(app_name),
                                                            wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)

                        msg_dec_succcess.ShowModal()
                    else:
                        try:
                            os.remove(complete_file_rt_enc_json)
                        except OSError:
                            pass

                        msg_folder_decrypted = wx.MessageDialog(self.wpanel, "'{}' folder already decrypted.".format(file_name),
                                                          "{} - decryption info.".format(app_name),
                                                          wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)

                        msg_folder_decrypted.ShowModal()

                except FileNotFoundError as fl_err:

                    print(fl_err)

                    msg_decrypted_item_missing = wx.MessageDialog(self.wpanel, "No files to be decrypted..",
                                                                  "{} - file detector error.".format(app_name),
                                                                  wx.ICON_ERROR | wx.STAY_ON_TOP)

                    msg_decrypted_item_missing.ShowModal()


                except FileExistsError:

                    delay(0.16)

                    try:
                        os.remove(complete_file_rt_enc_json)
                    except OSError:
                        pass

                    # print('\n- File already decrypted..')

                    msg_folder_decrypted = wx.MessageDialog(self.wpanel, "Folder already decrypted..",
                                                          "{} - decryption info.".format(app_name),
                                                          wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)

                    msg_folder_decrypted.ShowModal()

            except FileNotFoundError as fileNotFoundErr:

                print(str(fileNotFoundErr))

                msg_backup_json_err = wx.MessageDialog(self.wpanel, "File backup data not found.",
                                                       "{} - decryption error.".format(app_name),
                                                       wx.ICON_ERROR | wx.STAY_ON_TOP)

                msg_backup_json_err.ShowModal()

            except Exception as err:
                print(str(err))
        except NameError:
            pass

    def cipher_folder_accesscode(self, event):

        self.dir_opts_dlg()

        """ Verify 'path.json' if exists or not """
        settings_json_paths_exists = os.path.exists(paths_datas_json_file_path)

        if settings_json_paths_exists == False:

            pass

        else:

            enc_pass_title = "{} - Encryption passcode entry".format(app_name)

            try:

                if os.path.exists(passwords_json_file_path) == True:

                    while True:

                        self.cipher_pass_input = wx.PasswordEntryDialog(self.wpanel,
                                                                        "Please type the password for encryption:",
                                                                        enc_pass_title, style=wx.TextEntryDialogStyle)

                        if self.cipher_pass_input.ShowModal() == wx.ID_OK:

                            if self.cipher_pass_input.GetValue() == '':

                                invld_passwrd_err_input = wx.MessageDialog(self.wpanel,
                                                                               "Null passwords are not accepted.",
                                                                               "{} input verifier error - Password invalid:".format(
                                                                                   app_name),
                                                                               wx.ICON_ERROR | wx.STAY_ON_TOP)

                                invld_passwrd_err_input.ShowModal()

                            else:

                                if self.cipher_pass_input.GetValue() == self.encrypt_pass:

                                    # encrypt_frame(parent=self.wpanel,id=-1).Destroy()

                                    # self.decryption()
                                    self.encrypt_folders()

                                    break

                                else:
                                    passcode_err_enc = wx.MessageDialog(self.wpanel,
                                                                            "Wrong password for encryption.",
                                                                            "{} - passcode verifier error".format(
                                                                                app_name),
                                                                            wx.ICON_ERROR | wx.STAY_ON_TOP)

                                    passcode_err_enc.ShowModal()

                                        # self.decipher_pass_input.ShowModal()
                        else:
                            break
                        self.json_data_fl.close()
                else:
                    pass
            except AttributeError:
                pass

    def encrypt_folders(self):

        while True:

            dir_dlgbox = wx.DirDialog(self.wpanel, "Please choose the required folder to be encrypted:", "",
                                      wx.DD_DEFAULT_STYLE)

            if dir_dlgbox.ShowModal() == wx.ID_OK:

                path_choosen = dir_dlgbox.GetPath()

                dir_name_in = os.path.basename(path_choosen)

                #print

                zip_file_name = "{}.zip".format(dir_name_in)

                zip_name_encoded = cipher.encrypt(bytes(str(zip_file_name), 'utf-8')).decode()

                zip_file_encoded = "{}.enc".format(zip_name_encoded)

                # self.Destroy()
                try:

                    path_json = open(paths_datas_json_file_path, 'r')

                    data = path_json.read()

                    path_infos_v = json.loads(data)["path"]

                    #full_dir_path = os.path.join(dir_root_in, dir_name_in)

                    #folder_zipped_name = '{}.zip'.format(dir_name_in)

                # [Early-tests] app folders ->
                    # [Early-tests type] Main app folder path
                    #self.et_collections_folder_path = os.path.join(path_infos_v, et_collections_folder_name)

                    # encrypted [Early-tests type] folder path
                    #self.et_encrypted_files_folder_path = os.path.join(self.et_collections_folder_path,et_enc_folder_name)

                    # decrypted [Early-tests type] folder path
                    #self.et_decrypted_files_folder_path = os.path.join(self.et_collections_folder_path,et_dec_folder_name)

                    # [Early-tests type] real-time 'Year' folder in 'Encrypted files' folder path
                    #self.et_crnt_yrs_folder_path_enc = os.path.join(self.et_encrypted_files_folder_path, dt_yyyy)

                    # [Early-tests type] real-time 'Year' folder in 'Decrypted files' folder path
                    #self.et_crnt_yrs_folder_path_dec = os.path.join(self.et_decrypted_files_folder_path, dt_yyyy)

                    # [Early-tests type] real-time 'date' folder in 'Encrypted files' folder path
                    #self.et_now_date_folder_enc_path = os.path.join(self.et_crnt_yrs_folder_path_enc, dt_date)

                    # [Early-tests type] real-time 'date' folder in 'Decrypted files' folder path
                    #self.et_now_date_folder_dec_path = os.path.join(self.et_crnt_yrs_folder_path_dec, dt_date)
                    # os.startfile(now_date_sub_folder_path)

                    # [Early-tests type] folder-shorcut maker
                    # enc_dec_folder_shortcut_maker_dt(app_main_folder_root_var=self.et_collections_folder_path,years_sub_folder_root_var_enc=self.et_crnt_yrs_folder_path_enc,years_sub_folder_root_var_dec=self.et_crnt_yrs_folder_path_dec,date_sub_folder_root_var_enc=self.et_now_date_folder_enc_path,date_sub_folder_root_var_dec=self.et_now_date_folder_dec_path,folder_name_var=et_collections_folder_name)

                    # Encrypted-name folder
                    # self.enc_item_name_folder_path = os.path.join(self.now_date_folder_enc_path,epoch_miliseconds_str)

                    # [Early-tests type] compressed folder path
                    #et_compressed_dir_path = os.path.join(self.et_now_date_folder_enc_path, zip_file_name)

                    # [Early-tests type] Encrypted compressed folder path
                    #et_compressed_dir_path_enc = os.path.join(self.et_now_date_folder_enc_path, zip_file_encoded)

                # Main app folders ->
                    # Main collections folder path
                    self.collections_folder_path = os.path.join(path_infos_v, collections_folder_name)

                    # encrypted folder path
                    self.encrypted_files_folder_path = os.path.join(self.collections_folder_path, enc_folder_name)

                    # decrypted folder path
                    self.decrypted_files_folder_path = os.path.join(self.collections_folder_path, dec_folder_name)

                    # real-time 'Year' folder in 'Encrypted files' folder path
                    self.crnt_yrs_folder_path_enc = os.path.join(self.encrypted_files_folder_path, dt_yyyy)

                    # real-time 'Year' folder in 'Decrypted files' folder path
                    self.crnt_yrs_folder_path_dec = os.path.join(self.decrypted_files_folder_path, dt_yyyy)

                    # real-time 'date' folder in 'Encrypted files' folder path
                    self.now_date_folder_enc_path = os.path.join(self.crnt_yrs_folder_path_enc, dt_date)

                    # real-time 'date' folder in 'Decrypted files' folder path
                    self.now_date_folder_dec_path = os.path.join(self.crnt_yrs_folder_path_dec, dt_date)

                    # Encrypted files secondary sub-folder
                    self.subfolder2_encfiles_path = os.path.join(self.now_date_folder_enc_path,
                                                                 encfiles_subfolder2_name)

                    # Encrypted folders secondary sub-folder
                    self.subfolder2_encfolders_path = os.path.join(self.now_date_folder_enc_path,
                                                                   encfolders_subfolder2_name)

                    # Deccrypted files secondary sub-folder
                    self.subfolder2_decfiles_path = os.path.join(self.now_date_folder_dec_path,
                                                                 decfiles_subfolder2_name)

                    # Deccrypted folders secondary sub-folder
                    self.subfolder2_decfolders_path = os.path.join(self.now_date_folder_dec_path,
                                                                   decfolders_subfolder2_name)

                    # collection folder-shorcut maker
                    enc_dec_folder_shortcut_maker_dt(app_main_folder_root_var=self.collections_folder_path,
                                                     years_sub_folder_root_var_enc=self.crnt_yrs_folder_path_enc,
                                                     years_sub_folder_root_var_dec=self.crnt_yrs_folder_path_dec,
                                                     date_sub_folder_root_var_enc=self.now_date_folder_enc_path,
                                                     date_sub_folder_root_var_dec=self.now_date_folder_dec_path,
                                                     subfolder2_root_var_encfiles=self.subfolder2_encfiles_path,
                                                     subfolder2_root_var_decfiles=self.subfolder2_decfiles_path,
                                                     subfolder2_root_var_encdirs=self.subfolder2_encfolders_path,
                                                     subfolder2_root_var_decdirs=self.subfolder2_decfolders_path,
                                                     folder_name_var=collections_folder_name)

                    # Compress folder path
                    compressed_dir_path = os.path.join(self.subfolder2_encfolders_path, zip_file_name)

                    compressed_dir_path2 = os.path.join(self.subfolder2_encfolders_path, dir_name_in)

                    # Encrypted compressed folder path
                    compressed_dir_path_enc = os.path.join(self.subfolder2_encfolders_path, zip_file_encoded)

                    try:
                        if os.path.exists(compressed_dir_path_enc) == False:

                            extract_files_notify_msg = wx.MessageDialog(None, "Extracting files now.", "Notify:",
                                                                                wx.ICON_INFORMATION | wx.STAY_ON_TOP)
                            extract_files_notify_msg.ShowModal()

                            shutil.make_archive(compressed_dir_path2, format="zip", root_dir=path_choosen)

                            non_encrypt_fl = open(compressed_dir_path, 'rb')

                            non_enc_fl_data = non_encrypt_fl.read()

                            encrypted_data = cipher.encrypt(non_enc_fl_data)

                            enc_fl = open(compressed_dir_path_enc, 'wb')

                            enc_fl.write(encrypted_data)

                            # print('\n- File successfully encrypted..')

                            # msg_enc_succcess = wx.MessageDialog(self.wpanel,"'{}' file successfully encrypted.".format(self.src_file_full_name),"{} - encryption info.".format(app_name),wx.OK | wx.ICON_INFORMATION| wx.STAY_ON_TOP)

                            # msg_enc_succcess.ShowModal()

                            # wipeout()

                            backup_fl_infos = {
                                        "encrypted_zip_folder_name": zip_name_encoded
                            }

                            # Tranfers data And then stores it on the json file
                            jfl = open(json_folder_backups_file_path, "w")

                            json.dump(backup_fl_infos, jfl)

                            jfl.close()

                            enc_fl.close()

                            non_encrypt_fl.close()

                            os.remove(compressed_dir_path)

                            shutil.rmtree(path_choosen)

                            success_msg = wx.MessageDialog(self.wpanel,
                                                                   "'{}' folder successfully encrypted.".format(dir_name_in),
                            "Folder encryption - Complete:", wx.OK | wx.ICON_INFORMATION)

                            success_msg.ShowModal()

                            #delay(0.18)

                            break
                        else:

                            encrypted_folder_exists_msg = wx.MessageDialog(self.wpanel,
                                                                                   "'{}' directory or folder already encrypted and ready.".format(
                                                                                       dir_name_in), "Encryption notify:",
                                                                                   wx.ICON_INFORMATION | wx.STAY_ON_TOP)

                            encrypted_folder_exists_msg.ShowModal()

                             #delay(0.19)


                    except FileNotFoundError as err:

                        print(str(err))

                        msg_encrypted_item_missing = wx.MessageDialog(self.wpanel, "No folders to be encrypted..",
                                                                          "{} - encryption info.".format(app_name),
                                                                          wx.ICON_ERROR | wx.STAY_ON_TOP)

                        msg_encrypted_item_missing.ShowModal()


                    except FileExistsError:

                        try:

                            os.remove(compressed_dir_path2)
                        except OSError:
                            pass
                        except:
                            pass

                        try:

                            shutil.rmtree(path_choosen)
                        except shutil.Error:
                            pass
                        except Exception:
                            pass


                        msg_folder_encrypted = wx.MessageDialog(self.wpanel, "Folder already encrypted..",
                                                                  "{} - encryption info.".format(app_name),
                        wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)

                        msg_folder_encrypted.ShowModal()

                    except Exception as err:

                        print(str(err))

                        ue_err_msg = wx.MessageDialog(self.wpanel, "An unknown error occurred [{}].".format(err),
                        "Compression error:", wx.ICON_ERROR | wx.STAY_ON_TOP)

                        ue_err_msg.ShowModal()

                        break

                    path_json.close()

                except FileNotFoundError:

                    break
            else:
                break
    def exitbutton(self, event):

        ''' Asks user whether to use again as message box. if not, clears the values for the user, or exits the app if yes  '''
        yn_msgbox = wx.MessageDialog(self.wpanel, "Are you sure you want to exit the Folder Guradian?", "Yes/No",
                                     wx.YES_NO | wx.ICON_WARNING)

        yn_var = yn_msgbox.ShowModal()

        if yn_var == wx.ID_NO:

           pass

        else:
            self.Destroy()  # closes app when 'EXIT' button is click

    def Close(self, event):
        self.Destroy()  # closes app  when 'CLOSE' or 'X' on the window is pressed

    def rst(self, event):
        pass


class FileGuardian(wx.Dialog):

    def __init__(self, parent, id):

        # et_file_guardian_title = '{} - File Guardian'.format(file_name)

        file_guardian_title = '{} - File Guardian'.format(app_title)

        wx.Frame.__init__(self, parent, id,file_guardian_title, size=(657, 563))

        try:
            self.SetIcon(wx.Icon(ico_flpath))  # Sets icon on the window title bar
        except NameError:
            pass

        self.wpanel = wx.Panel(self)

        self.wpanel.SetBackgroundColour('Steel Blue')  # Sets the panel or app background

        self.Show(True)


        # Creates fonts for labels
        name_detailslbl_font = wx.Font(22, wx.ROMAN, wx.FONTSTYLE_MAX, wx.FONTWEIGHT_BOLD)

        # Creates label
        self.name1_lbl = wx.StaticText(self.wpanel, -1, "Portfolio secure 12 P.E.F ++ (210-F3.6) - \nFile Guardian", (67, 85), (22, 22),
                                             wx.TEXT_ALIGNMENT_CENTRE)

        # Sets font for the button using variable
        self.name1_lbl.SetFont(name_detailslbl_font)

        # Sets the given colour for the label text
        self.name1_lbl.SetForegroundColour('white')

        # Sets the given colour for the label ( label BG colour )
        self.name1_lbl.SetBackgroundColour('Indian red')


        # Creates  fonts for labels
        name_detailslbl_font = wx.Font(22, wx.ROMAN, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD)

        # Creates label
        self.name2_lbl = wx.StaticText(self.wpanel, -1, "Encrypting and decrypting files.", (67, 194), (24, 24), wx.TEXT_ALIGNMENT_CENTRE)  #

        # Sets font for the button using variable
        self.name2_lbl.SetFont(name_detailslbl_font)

        # Sets the given colour for the label text
        self.name2_lbl.SetForegroundColour('Black')

        # Sets the given colour for the label ( label BG colour )
        self.name2_lbl.SetBackgroundColour('White')

        # --> Buttons

        # Encrypt button

        # Creates fonts for button
        btn_click_enc_font = wx.Font(21, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        # Creates 'Encrypt' button
        self.click_enc = wx.Button(self.wpanel, label='ENCRYPT', pos=(67, 301), size=(156, 45), style=wx.BORDER_RAISED)

        # Sets font for the button using variable
        self.click_enc.SetFont(btn_click_enc_font)

        # Sets the given colour for the button text
        self.click_enc.SetForegroundColour('WHITE')

        # Sets the given colour for the button ( button BG colour )
        self.click_enc.SetBackgroundColour('DARK GREEN')

        # Sets the tooltip ( pop-up details )
        self.click_enc.SetToolTip("CLick here to encrypt a file using the fill-ups.")

        # Combines the button with its respective functions
        self.Bind(wx.EVT_BUTTON, self.cipher_file_accesscode, self.click_enc)

        # Decrypt button

        # Creates fonts for button
        btn_click_dec_font = wx.Font(21, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        # Creates 'Decrypt' button
        self.click_dec = wx.Button(self.wpanel, label='DECRYPT', pos=(412, 301), size=(156, 47), style=wx.BORDER_RAISED)

        # Sets font for the button using variable
        self.click_dec.SetFont(btn_click_dec_font)

        # Sets the given colour for the button text
        self.click_dec.SetForegroundColour('White')

        # Sets the given colour for the button ( button BG colour )
        self.click_dec.SetBackgroundColour('MEDIUM BLUE')

        # Sets tooltip (pop-up details)
        self.click_dec.SetToolTip("Click here to decrypt the encrypted file.")

        # Combines button with its respective functions
        self.Bind(wx.EVT_BUTTON, self.decipher_file_accesscode,
                  self.click_dec)

        # Exit button

        # Creates fonts for button
        btn_exit_font = wx.Font(21, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        # Creates 'Exit' button
        self.exit_btn = wx.Button(self.wpanel, label='EXIT', pos=(67, 404), size=(156, 45),
                                  style=wx.BORDER_RAISED)  # Creates 'Exit' button

        # Sets font for the button using variable
        self.exit_btn.SetFont(btn_exit_font)

        # Sets the given colour for the button text
        self.exit_btn.SetForegroundColour('WHITE')  # Sets button text colour

        # Sets the given colour for the button ( button BG colour )
        self.exit_btn.SetBackgroundColour('RED')  # Sets button BG colour

        # Sets tooltip (pop-up details)
        self.exit_btn.SetToolTip("CLick here to close.")

        # Combines button with its respective functions
        self.Bind(wx.EVT_BUTTON, self.exitbutton, self.exit_btn)

        # Access button

        # Creates fonts for button
        btn_access_font = wx.Font(21, wx.ROMAN, wx.FONTSTYLE_NORMAL,
                                  wx.FONTWEIGHT_BOLD)

        # Creates 'Access' button
        self.open_folder_btn = wx.Button(self.wpanel, label='ACCESS', pos=(242, 349), size=(156, 45),
                                         style=wx.BORDER_RAISED)

        # Sets font for the button using variable
        self.open_folder_btn.SetFont(btn_access_font)

        # Sets the given colour for the button text
        self.open_folder_btn.SetForegroundColour('White')

        # Sets the given colour for the button ( button BG colour )
        self.open_folder_btn.SetBackgroundColour('CORNFLOWER BLUE')

        # Sets tooltip (pop-up details)
        self.open_folder_btn.SetToolTip("Click here to open '{}' folder.".format(collections_folder_name))

        # Combines button with its respective functions
        self.Bind(wx.EVT_BUTTON, self.open_dir_dt,self.open_folder_btn)

        # Modify button

        # Creates fonts for the button
        btn_mod_font = wx.Font(21, wx.ROMAN, wx.FONTSTYLE_NORMAL,
                               wx.FONTWEIGHT_BOLD)  # Creates  fonts for 'Reset' button

        # Creates button
        self.modify_btn = wx.Button(self.wpanel, label='MODIFY', pos=(412, 404), size=(156, 45), style=wx.BORDER_RAISED)

        # Sets font for the button using variable
        self.modify_btn.SetFont(btn_mod_font)

        # Sets the given colour for the button text
        self.modify_btn.SetForegroundColour('Red')

        # Sets the given colour for the button ( button BG colour )
        self.modify_btn.SetBackgroundColour('Yellow')

        # Sets tooltip (pop-up details)
        self.modify_btn.SetToolTip("Click here to change settings.")

        # Combines button with its respective functions
        self.Bind(wx.EVT_BUTTON, self.modify2, self.modify_btn)

        # close window button
        self.Bind(wx.EVT_CLOSE, self.closewindow)

        # json custom passwords conatianer file
        # json_path = os.path.join(et_setting_folder_,"My_passwords.json")

        # Acessing data from the 'My_passwords' json file

        # 'X' frame btn
        #    self.Bind(wx.EVT_CLOSE,self.closeEnc)

        try:

            self.json_data_fl = open(passwords_json_file_path, "r")

            data = json.load(self.json_data_fl)

            self.decrypt_pass = cipher.decrypt(bytes(str(data["decrypt_passcode"]), 'utf-8')).decode()

            self.encrypt_pass = cipher.decrypt(bytes(str(data["encrypt_passcode"]), 'utf-8')).decode()

        except json.decoder.JSONDecodeError:
            password_json_overwrite(json_path_val=passwords_json_file_path,enc_pswrd_var=encrypt_passcode_no_encrypted,dec_pswrd_var=decrypt_passcode_no_encrypted)
        except FileNotFoundError:
            pass

    def closewindow(self, event):
        self.Destroy()

        # sys.exit()

    def dir_opts_dlg(self):

        """ Verify 'path.json' if exists or not """
        settings_json_paths_exists = os.path.exists(paths_datas_json_file_path)

        if settings_json_paths_exists == False:

            dir_dlgbox = wx.DirDialog(self.wpanel, "Please choose folder (or directory) to hold '{}' folder:".format(collections_folder_name), "",
                                      wx.DD_DEFAULT_STYLE | wx.DD_CHANGE_DIR)

            # dir_dlgbox.Set(wDir_path)
            if dir_dlgbox.ShowModal() == wx.ID_OK:

                usr_rt_v = dir_dlgbox.GetPath()

                settings_json = open(paths_datas_json_file_path, 'w')

                settings_json.write("{"'"path"'":")

                usr_path = {
                    "path": str(usr_rt_v)
                }

                json_settings_file_datas = open(paths_datas_json_file_path, "w")

                json.dump(usr_path, json_settings_file_datas)

                json_settings_file_datas.close()

                settings_json.close()

                settings_path_saved_msg = wx.MessageDialog(self.wpanel, "Path saved.", "Path update - Complete",
                                                           wx.OK | wx.ICON_INFORMATION)

                settings_path_saved_msg.ShowModal()

            else:
                pass
        else:
            pass

        try:
            # [Early-tests type] 'folder json file' operation
            #path_json = open(et_paths_datas_json_file_path, 'r')

            path_json = open(paths_datas_json_file_path, 'r')

            data = path_json.read()

            path_infos_v = json.loads(data)["path"]

            # et_pascode_json_exists = os.path.exists(et_settings_json_full_path)

            # ''' Early-tests type app folder details  '''
            # [Early-tests type] Main app  folder path
            self.et_collections_folder_path = os.path.join(path_infos_v, et_collections_folder_name)

            # [Early-tests type] encrypted folder path
            self.et_encrypted_files_folder_path = os.path.join(self.et_collections_folder_path, et_enc_folder_name)

            # [Early-tests type] decrypted folder path
            self.et_decrypted_files_folder_path = os.path.join(self.et_collections_folder_path, et_dec_folder_name)

            # [Early-tests type] real-time 'Year' folder in 'Encrypted files' folder path
            self.et_crnt_yrs_folder_path_enc = os.path.join(self.et_encrypted_files_folder_path, dt_yyyy)

            # [Early-tests type] real-time 'Year' folder in 'Decrypted files' folder path
            self.et_crnt_yrs_folder_path_dec = os.path.join(self.et_decrypted_files_folder_path, dt_yyyy)

            # [Early-tests type] real-time 'date' folder in 'Encrypted files' folder path
            self.et_now_date_folder_enc_path = os.path.join(self.et_crnt_yrs_folder_path_enc, dt_date)

            # [Early-tests type] real-time 'date' folder in 'Decrypted files' folder path
            self.et_now_date_folder_dec_path = os.path.join(self.et_crnt_yrs_folder_path_dec, dt_date)
            # os.startfile(now_date_sub_folder_path)

            # [Early-tests type] Folder-shorcut maker
            # enc_dec_folder_shortcut_maker_dt(app_main_folder_root_var=self.et_collections_folder_path,date_sub_folder_root_var_enc=self.et_now_date_folder_enc_path,date_sub_folder_root_var_dec=self.et_now_date_folder_dec_path,folder_name_var=et_collections_folder_name)

        # Main app folders ->
            # Main collections folder path
            self.collections_folder_path = os.path.join(path_infos_v, collections_folder_name)

            # encrypted folder path
            self.encrypted_files_folder_path = os.path.join(self.collections_folder_path, enc_folder_name)

            # decrypted folder path
            self.decrypted_files_folder_path = os.path.join(self.collections_folder_path, dec_folder_name)

            # real-time 'Year' folder in 'Encrypted files' folder path
            self.crnt_yrs_folder_path_enc = os.path.join(self.encrypted_files_folder_path, dt_yyyy)

            # real-time 'Year' folder in 'Decrypted files' folder path
            self.crnt_yrs_folder_path_dec = os.path.join(self.decrypted_files_folder_path, dt_yyyy)

            # real-time 'date' folder in 'Encrypted files' folder path
            self.now_date_folder_enc_path = os.path.join(self.crnt_yrs_folder_path_enc, dt_date)

            # real-time 'date' folder in 'Decrypted files' folder path
            self.now_date_folder_dec_path = os.path.join(self.crnt_yrs_folder_path_dec, dt_date)

            # Encrypted files secondary sub-folder
            self.subfolder2_encfiles_path = os.path.join(self.now_date_folder_enc_path,
                                                                 encfiles_subfolder2_name)

            # Encrypted folders secondary sub-folder
            self.subfolder2_encfolders_path = os.path.join(self.now_date_folder_enc_path,
                                                                   encfolders_subfolder2_name)

            # Deccrypted files secondary sub-folder
            self.subfolder2_decfiles_path = os.path.join(self.now_date_folder_dec_path,
                                                                 decfiles_subfolder2_name)

            # Deccrypted folders secondary sub-folder
            self.subfolder2_decfolders_path = os.path.join(self.now_date_folder_dec_path,
                                                                   decfolders_subfolder2_name)

            # collection folder-shorcut maker
            enc_dec_folder_shortcut_maker_dt(app_main_folder_root_var=self.collections_folder_path,
                                             years_sub_folder_root_var_enc=self.crnt_yrs_folder_path_enc,
                                             years_sub_folder_root_var_dec=self.crnt_yrs_folder_path_dec,
                                             date_sub_folder_root_var_enc=self.now_date_folder_enc_path,
                                             date_sub_folder_root_var_dec=self.now_date_folder_dec_path,
                                             subfolder2_root_var_encfiles=self.subfolder2_encfiles_path,
                                             subfolder2_root_var_decfiles=self.subfolder2_decfiles_path,
                                             subfolder2_root_var_encdirs=self.subfolder2_encfolders_path,
                                             subfolder2_root_var_decdirs=self.subfolder2_decfolders_path,
                                             folder_name_var=collections_folder_name)

            path_json.close()

        except FileNotFoundError:
            pass

    def open_dir_dt(self, event):

        """ Verify 'path.json' if exists or not """
        settings_json_paths_exists = os.path.exists(paths_datas_json_file_path)

        if settings_json_paths_exists == False:

            dir_dlgbox = wx.DirDialog(self.wpanel, "Please choose folder (or directory) to hold '{}' folder:".format(collections_folder_name), "",
                                      wx.DD_DEFAULT_STYLE | wx.DD_CHANGE_DIR)

            # dir_dlgbox.Set(wDir_path)
            if dir_dlgbox.ShowModal() == wx.ID_OK:

                usr_rt_v = dir_dlgbox.GetPath()

                settings_json = open(paths_datas_json_file_path, 'w')

                settings_json.write("{"'"path"'":")

                usr_path = {
                    "path": str(usr_rt_v)
                }

                json_settings_file_datas = open(paths_datas_json_file_path, "w")

                json.dump(usr_path, json_settings_file_datas)

                json_settings_file_datas.close()

                settings_json.close()

                settings_path_saved_msg = wx.MessageDialog(self.wpanel, "Path saved.", "Path update - Complete",
                                                           wx.OK | wx.ICON_INFORMATION)

                settings_path_saved_msg.ShowModal()

            else:
                pass
        else:
            pass

        try:

            # [Early-tests type] 'folder json file' operation
            #path_json = open(et_paths_datas_json_file_path, 'r')

            path_json = open(paths_datas_json_file_path, 'r')

            data = path_json.read()

            path_infos_v = json.loads(data)["path"]

            # et_pascode_json_exists = os.path.exists(et_settings_json_full_path)

            # [Early-tests type] Main app folder path
            self.et_collections_folder_path = os.path.join(path_infos_v, et_collections_folder_name)

            # encrypted [Early-tests type] folder path
            self.et_encrypted_files_folder_path = os.path.join(self.et_collections_folder_path, et_enc_folder_name)

            # decrypted [Early-tests type] folder path
            self.et_decrypted_files_folder_path = os.path.join(self.et_collections_folder_path, et_dec_folder_name)

            # [Early-tests type] real-time 'Year' folder in 'Encrypted files' folder path
            self.et_crnt_yrs_folder_path_enc = os.path.join(self.et_encrypted_files_folder_path, dt_yyyy)

            # [Early-tests type] real-time 'Year' folder in 'Decrypted files' folder path
            self.et_crnt_yrs_folder_path_dec = os.path.join(self.et_decrypted_files_folder_path, dt_yyyy)

            # [Early-tests type] real-time 'date' folder in 'Encrypted files' folder path
            self.et_now_date_folder_enc_path = os.path.join(self.et_crnt_yrs_folder_path_enc, dt_date)

            # [Early-tests type] real-time 'date' folder in 'Decrypted files' folder path
            self.et_now_date_folder_dec_path = os.path.join(self.et_crnt_yrs_folder_path_dec, dt_date)
            # os.startfile(now_date_sub_folder_path)

            # [Early-tests type] folder-shorcut
            # enc_dec_folder_shortcut_maker_dt(app_main_folder_root_var=self.et_collections_folder_path,years_sub_folder_root_var_enc=self.et_crnt_yrs_folder_path_enc,years_sub_folder_root_var_dec=self.et_crnt_yrs_folder_path_dec,date_sub_folder_root_var_enc=self.et_now_date_folder_enc_path,date_sub_folder_root_var_dec=self.et_now_date_folder_dec_path,folder_name_var=et_collections_folder_name)

            # [Early-tests type] open collection folder
            # os.startfile(self.et_collections_folder_path)

            # [Early-tests type] Main collections folder path
            self.collections_folder_path = os.path.join(path_infos_v, collections_folder_name)

            # encrypted folder path
            self.encrypted_files_folder_path = os.path.join(self.collections_folder_path, enc_folder_name)

            # decrypted folder path
            self.decrypted_files_folder_path = os.path.join(self.collections_folder_path, dec_folder_name)

            # real-time 'Year' folder in 'Encrypted files' folder path
            self.et_crnt_yrs_folder_path_enc = os.path.join(self.et_encrypted_files_folder_path, dt_yyyy)

            # real-time 'Year' folder in 'Decrypted files' folder path
            self.et_crnt_yrs_folder_path_dec = os.path.join(self.et_decrypted_files_folder_path, dt_yyyy)

        # -> App Main folders
            # real-time 'years' folder in 'Encrypted files' folder path
            self.crnt_yrs_folder_path_enc = os.path.join(self.encrypted_files_folder_path, dt_yyyy)

            # real-time 'years' folder in 'Decrypted files' folder path
            self.crnt_yrs_folder_path_dec = os.path.join(self.decrypted_files_folder_path, dt_yyyy)

            # real-time 'date' folder in 'Encrypted files' folder path
            self.now_date_folder_enc_path = os.path.join(self.crnt_yrs_folder_path_enc, dt_date)

            # real-time 'date' folder in 'Decrypted files' folder path
            self.now_date_folder_dec_path = os.path.join(self.crnt_yrs_folder_path_dec, dt_date)

            # Encrypted files secondary sub-folder
            self.subfolder2_encfiles_path = os.path.join(self.now_date_folder_enc_path,
                                                                 encfiles_subfolder2_name)

            # Encrypted folders secondary sub-folder
            self.subfolder2_encfolders_path = os.path.join(self.now_date_folder_enc_path,
                                                                   encfolders_subfolder2_name)
            # Deccrypted files secondary sub-folder
            self.subfolder2_decfiles_path = os.path.join(self.now_date_folder_dec_path,
                                                                 decfiles_subfolder2_name)

            # Deccrypted folders secondary sub-folder
            self.subfolder2_decfolders_path = os.path.join(self.now_date_folder_dec_path,
                                                                   decfolders_subfolder2_name)

            # collection folder-shorcut maker
            enc_dec_folder_shortcut_maker_dt(app_main_folder_root_var=self.collections_folder_path,
                                             years_sub_folder_root_var_enc=self.crnt_yrs_folder_path_enc,
                                             years_sub_folder_root_var_dec=self.crnt_yrs_folder_path_dec,
                                             date_sub_folder_root_var_enc=self.now_date_folder_enc_path,
                                             date_sub_folder_root_var_dec=self.now_date_folder_dec_path,
                                             subfolder2_root_var_encfiles=self.subfolder2_encfiles_path,
                                             subfolder2_root_var_decfiles=self.subfolder2_decfiles_path,
                                             subfolder2_root_var_encdirs=self.subfolder2_encfolders_path,
                                             subfolder2_root_var_decdirs=self.subfolder2_decfolders_path,
                                             folder_name_var=collections_folder_name)

            # open collection folder
            os.startfile(self.collections_folder_path)

            path_json.close()

        except FileNotFoundError:
            pass

    def modify2(self, event):

        fg_modify_lists = ["Choose here to change path for '{}' folder.".format(collections_folder_name), "Choose here to change password.",
                           "Choose here to change encrypted file name."]

        onechoice = wx.SingleChoiceDialog(self.wpanel, "Which settings do you wish to change?",
                                          '{} - modify settings:'.format(app_name), fg_modify_lists)

        # choosen_choice_var = onechoice.GetStringSelection()

        if onechoice.ShowModal() == wx.ID_OK:

            # print ("Choosen mode -> %s\n" % onechoice.GetStringSelection())

            if onechoice.GetStringSelection() == fg_modify_lists[0]:
                self.changedir()
            elif onechoice.GetStringSelection() == fg_modify_lists[2]:
                self.files_encname_changer()
                # pass
            else:
                self.pswrds_changer()
        else:
            pass
        # pass

    def files_encname_changer(self):

        while True:

            enc_pass_title = "{} - Encryption passcode entry".format(app_name)

            self.cipher_pass_input = wx.PasswordEntryDialog(self.wpanel, "Please type the encryption password:",
                                                            enc_pass_title, style=wx.TextEntryDialogStyle)

            if self.cipher_pass_input.ShowModal() == wx.ID_OK:

                # src_json_pswrd_enc = #self.json_passcode_access()

                if self.cipher_pass_input.GetValue() == "":

                    invld_err_input = wx.MessageDialog(self.wpanel, "Null values are not accepted.",
                                                       "{} - input verifier error:".format(app_name),
                                                       wx.ICON_ERROR | wx.STAY_ON_TOP)

                    invld_err_input.ShowModal()

                    # pass
                else:

                    if self.cipher_pass_input.GetValue() == self.encrypt_pass:

                        access_granted_msg_box = wx.MessageDialog(self.wpanel, "Password correct.",
                                                                  "{} - Access granted:".format(app_name),
                                                                  wx.ICON_INFORMATION | wx.STAY_ON_TOP)

                        access_granted_msg_box.ShowModal()

                        path_json = open(paths_datas_json_file_path, 'r')

                        data = path_json.read()

                        path_infos_v = json.loads(data)["path"]

                    # [Early-tests] app folders ->

                        # [Early-tests type] Main app folder path
                        self.et_collections_folder_path = os.path.join(path_infos_v, et_collections_folder_name)

                        # encrypted [Early-tests type] folder path
                        self.et_encrypted_files_folder_path = os.path.join(self.et_collections_folder_path,
                                                                           et_enc_folder_name)

                        # decrypted [Early-tests type] folder path
                        self.et_decrypted_files_folder_path = os.path.join(self.et_collections_folder_path,
                                                                           et_dec_folder_name)

                        # [Early-tests type] real-time 'Year' folder in 'Encrypted files' folder path
                        self.et_crnt_yrs_folder_path_enc = os.path.join(self.et_encrypted_files_folder_path, dt_yyyy)

                        # [Early-tests type] real-time 'Year' folder in 'Decrypted files' folder path
                        self.et_crnt_yrs_folder_path_dec = os.path.join(self.et_decrypted_files_folder_path, dt_yyyy)

                        # [Early-tests type] real-time 'date' folder in 'Encrypted files' folder path
                        self.et_now_date_folder_enc_path = os.path.join(self.et_crnt_yrs_folder_path_enc, dt_date)

                        # [Early-tests type] real-time 'date' folder in 'Decrypted files' folder path
                        self.et_now_date_folder_dec_path = os.path.join(self.et_crnt_yrs_folder_path_dec, dt_date)

                        # os.startfile(now_date_sub_folder_path)

                        # [Early-tests type] folder-shorcut maker
                        # enc_dec_folder_shortcut_maker_dt(app_main_folder_root_var=self.et_collections_folder_path,years_sub_folder_root_var_enc=self.et_crnt_yrs_folder_path_enc,years_sub_folder_root_var_dec=self.et_crnt_yrs_folder_path_dec,date_sub_folder_root_var_enc=self.et_now_date_folder_enc_path,date_sub_folder_root_var_dec=self.et_now_date_folder_dec_path,folder_name_var=et_collections_folder_name)

                        # Encrypted-name folder
                        # self.enc_item_name_folder_path = os.path.join(self.now_date_folder_enc_path,epoch_miliseconds_str)

                    # Main app folders ->

                        # Main collections folder path
                        self.collections_folder_path = os.path.join(path_infos_v, collections_folder_name)

                        # encrypted folder path
                        self.encrypted_files_folder_path = os.path.join(self.collections_folder_path, enc_folder_name)

                        # decrypted folder path
                        self.decrypted_files_folder_path = os.path.join(self.collections_folder_path, dec_folder_name)

                        # real-time 'years' folder in 'Encrypted files' folder path
                        self.crnt_yrs_folder_path_enc = os.path.join(self.encrypted_files_folder_path, dt_yyyy)

                        # real-time 'years' folder in 'Decrypted files' folder path
                        self.crnt_yrs_folder_path_dec = os.path.join(self.decrypted_files_folder_path, dt_yyyy)

                        # real-time 'date' folder in 'Encrypted files' folder path
                        self.now_date_folder_enc_path = os.path.join(self.crnt_yrs_folder_path_enc, dt_date)

                        # real-time 'date' folder in 'Decrypted files' folder path
                        self.now_date_folder_dec_path = os.path.join(self.crnt_yrs_folder_path_dec, dt_date)

                        # Encrypted files secondary sub-folder
                        self.subfolder2_encfiles_path = os.path.join(self.now_date_folder_enc_path,
                                                                     encfiles_subfolder2_name)

                        # Deccrypted files secondary sub-folder
                        self.subfolder2_decfiles_path = os.path.join(self.now_date_folder_enc_path,
                                                                     decfiles_subfolder2_name)

                        # Encrypted folders secondary sub-folder
                        self.subfolder2_encfolders_path = os.path.join(self.now_date_folder_enc_path,
                                                                       encfolders_subfolder2_name)

                        # Deccrypted folders secondary sub-folder
                        self.subfolder2_decfolders_path = os.path.join(self.now_date_folder_enc_path,
                                                                       decfolders_subfolder2_name)

                        # collection folder-shorcut maker
                        enc_dec_folder_shortcut_maker_dt(app_main_folder_root_var=self.collections_folder_path,
                                                         years_sub_folder_root_var_enc=self.crnt_yrs_folder_path_enc,
                                                         years_sub_folder_root_var_dec=self.crnt_yrs_folder_path_dec,
                                                         date_sub_folder_root_var_enc=self.now_date_folder_enc_path,
                                                         date_sub_folder_root_var_dec=self.now_date_folder_dec_path,
                                                         subfolder2_root_var_encfiles=self.subfolder2_encfiles_path,
                                                         subfolder2_root_var_decfiles=self.subfolder2_decfiles_path,
                                                         subfolder2_root_var_encdirs=self.subfolder2_encfolders_path,
                                                         subfolder2_root_var_decdirs=self.subfolder2_decfolders_path,
                                                         folder_name_var=collections_folder_name)

                        delay(0.16)

                        enc_filedir_dlgbox = wx.FileDialog(self.wpanel, "Please choose encryption file:", self.subfolder2_encfiles_path, "",
                                                           wildcard="All files (*.*)|*.*; | Encrypted files (*.enc) | *.enc;",
                                                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

                        if enc_filedir_dlgbox.ShowModal() == wx.ID_OK:
                            enc_complete_file_rt = enc_filedir_dlgbox.GetPath()

                            enc_fl_basename = os.path.basename(enc_complete_file_rt)
                            try:

                                json_fl_r = open(json_file_backups_file_path, "r")

                                json_src_data = json.load(json_fl_r)

                                json_src_data["encrypted_file_name"] = enc_fl_basename.replace('.enc', '')

                                json_fl_w = open(json_file_backups_file_path, "w")

                                json.dump(json_src_data, json_fl_w)

                                json_fl_r.close()

                                json_fl_w.close()

                                update_made_msg = wx.MessageDialog(self.wpanel, "Encrypted file name changed.",
                                                                       "Encrypted File Name update - Complete:",
                                wx.OK | wx.ICON_INFORMATION)

                                update_made_msg.ShowModal()

                                self.restrt()

                                break

                            except FileNotFoundError:

                                backup_fl_infos = {
                                        "encrypted_file_name": str(self.modify_cipher_name_input.GetValue()).replace(
                                            '.enc', '')
                                }

                                # Tranfers data And then stores it on the json file
                                jfl = open(json_file_backups_file_path, "w")

                                json.dump(backup_fl_infos, jfl)

                                jfl.close()

                                save_made_msg = wx.MessageDialog(self.wpanel, "Encryption file name saved.",
                                                                     "Encrypted File Name save - Complete:",
                                                                     wx.OK | wx.ICON_INFORMATION)

                                save_made_msg.ShowModal()

                                self.restrt()

                                break
                        else:
                            break
                    else:

                        passcode_err_enc = wx.MessageDialog(self.wpanel, "Wrong password.",
                                                            "{} - passcode verifier error".format(app_name),
                                                            wx.ICON_ERROR | wx.STAY_ON_TOP)

                        passcode_err_enc.ShowModal()
            else:
                break
        pass

    def pswrds_changer(self):

        fg_modify_pswrds_lists = ['Choose here to change password for encryption.          ', 'Choose here to change password for decryption.          ']

        onechoice_pswrds = wx.SingleChoiceDialog(self.wpanel, "Which password do you wish to change?",
                                                 '{} - modify passwords: '.format(app_name), fg_modify_pswrds_lists)

        # choosen_choice_var_pswrds = onechoice_pswrds.GetStringSelection()

        if onechoice_pswrds.ShowModal() == wx.ID_OK:

            # print ("YT saver mode, %s\n" % onechoice.GetStringSelection())

            if onechoice_pswrds.GetStringSelection() == fg_modify_pswrds_lists[0]:

                # self.changeenc()

                while True:

                    enc_pass_title = "{} - Encryption passcode entry".format(app_name)

                    self.cipher_pass_input = wx.PasswordEntryDialog(self.wpanel, "Please type the encryption password:",
                                                                    enc_pass_title, style=wx.TextEntryDialogStyle)

                    if self.cipher_pass_input.ShowModal() == wx.ID_OK:

                        # src_json_pswrd_enc = #self.json_passcode_access()

                        if self.cipher_pass_input.GetValue() == "":

                            invld_passwrd_err_input = wx.MessageDialog(self.wpanel, "Null passwords are not accepted.",
                                                                       "{} input verifier error - Password invalid:".format(
                                                                           app_name), wx.ICON_ERROR | wx.STAY_ON_TOP)

                            invld_passwrd_err_input.ShowModal()

                            # pass

                        else:

                            if self.cipher_pass_input.GetValue() == self.encrypt_pass:

                                access_granted_msg_box = wx.MessageDialog(self.wpanel, "Password correct.",
                                                                          "{} - Access granted:".format(app_name),
                                                                          wx.ICON_INFORMATION | wx.STAY_ON_TOP)

                                access_granted_msg_box.ShowModal()

                                delay(0.16)

                                modify_enc_pass_title = "{} - Modify encryption passcode entry:".format(app_name)

                                self.modify_cipher_pass_input = wx.PasswordEntryDialog(self.wpanel,
                                                                                       "Please type the encryption password to be modified.",
                                                                                       modify_enc_pass_title,
                                                                                       style=wx.TextEntryDialogStyle)

                                if self.modify_cipher_pass_input.ShowModal() == wx.ID_OK:

                                    if self.modify_cipher_pass_input.GetValue() == "":

                                        invld_err_input = wx.MessageDialog(self.wpanel, "Null values are not accepted.",
                                                                           "{} - input verifier error:".format(
                                                                               app_name),
                                                                           wx.ICON_ERROR | wx.STAY_ON_TOP)

                                        invld_err_input.ShowModal()

                                        # pass
                                    else:

                                        json_fl_r = open(passwords_json_file_path, "r")

                                        json_src_data = json.load(json_fl_r)

                                        json_src_data["encrypt_passcode"] = cipher.encrypt(bytes(str(self.modify_cipher_pass_input.GetValue()), 'utf-8')).decode()

                                        #json_src_data["encrypt_passcode"] = self.modify_cipher_pass_input.GetValue()

                                        json_fl_w = open(passwords_json_file_path, "w")

                                        json.dump(json_src_data, json_fl_w)

                                        json_fl_r.close()

                                        json_fl_w.close()

                                        update_made_msg = wx.MessageDialog(self.wpanel, "Encryption password changed.",
                                                                           "Password update - Complete",
                                                                           wx.OK | wx.ICON_INFORMATION)

                                        update_made_msg.ShowModal()

                                        self.restrt_fg_files()

                                        break
                                else:
                                    break
                            else:

                                passcode_err_enc = wx.MessageDialog(self.wpanel, "Wrong password.",
                                                                    "{} - passcode verifier error".format(app_name),
                                                                    wx.ICON_ERROR | wx.STAY_ON_TOP)

                                passcode_err_enc.ShowModal()
                    else:
                        break

            else:
                # pass

                # self.changedec()

                while True:

                    dec_pass_title = "{} - Decryption passcode entry:".format(app_name)

                    self.decipher_pass_input = wx.PasswordEntryDialog(self.wpanel,
                                                                      "Please type the decryption password:",
                                                                      dec_pass_title, style=wx.TextEntryDialogStyle)

                    if self.decipher_pass_input.ShowModal() == wx.ID_OK:

                        # src_json_pswrd_dec = #self.json_passcode_access()

                        if self.decipher_pass_input.GetValue() == "":

                            invld_err_input = wx.MessageDialog(self.wpanel, "Null values are not accepted.",
                                                               "{} - input verifier error:".format(app_name),
                                                               wx.ICON_ERROR | wx.STAY_ON_TOP)

                            invld_err_input.ShowModal()

                            # pass
                        else:

                            if self.decipher_pass_input.GetValue() == self.decrypt_pass:

                                access_granted_msg_box = wx.MessageDialog(self.wpanel, "Password correct.",
                                                                          "{} - Access granted:".format(app_name),
                                                                          wx.ICON_INFORMATION | wx.STAY_ON_TOP)

                                access_granted_msg_box.ShowModal()

                                delay(0.16)

                                modify_enc_pass_title = "{} - Modify decryption passcode entry:".format(app_name)

                                self.modify_decipher_pass_input = wx.PasswordEntryDialog(self.wpanel,
                                                                                         "Please type the decryption password to be modified.",
                                                                                         modify_enc_pass_title,
                                                                                         style=wx.TextEntryDialogStyle)

                                if self.modify_decipher_pass_input.ShowModal() == wx.ID_OK:

                                    if self.modify_decipher_pass_input.GetValue() == "":

                                        invld_passwrd_err_input = wx.MessageDialog(self.wpanel,
                                                                                   "Null passwords are not accepted.",
                                                                                   "{} input verifier error - Password invalid:".format(
                                                                                       app_name),
                                                                                   wx.ICON_ERROR | wx.STAY_ON_TOP)

                                        invld_passwrd_err_input.ShowModal()

                                    else:

                                        json_fl_r = open(passwords_json_file_path, "r")

                                        json_src_data = json.load(json_fl_r)

                                        json_src_data["decrypt_passcode"] = cipher.encrypt(bytes(str(self.modify_decipher_pass_input.GetValue()), 'utf-8')).decode()

                                        #json_src_data["decrypt_passcode"] = self.modify_decipher_pass_input.GetValue()

                                        json_fl_w = open(passwords_json_file_path, "w")

                                        json.dump(json_src_data, json_fl_w)

                                        json_fl_r.close()

                                        json_fl_w.close()

                                        update_made_msg = wx.MessageDialog(self.wpanel, "Decryption password changed.",
                                                                           "Password update - Complete",
                                                                           wx.OK | wx.ICON_INFORMATION)

                                        update_made_msg.ShowModal()

                                        self.restrt_fg_files()

                                        break
                                else:
                                    break
                            else:

                                passcode_err_dec = wx.MessageDialog(self.wpanel, "Wrong password.",
                                                                    "{} - passcode verifier error".format(app_name),
                                                                    wx.ICON_ERROR | wx.STAY_ON_TOP)

                                passcode_err_dec.ShowModal()
                    else:
                        break
                self.json_data_fl.close()

    def changedir(self):

        while True:

            modify_dir_dlgbox = wx.DirDialog(self.wpanel, "Please choose folder (or directory) to be changed:", "",
                                             wx.DD_DEFAULT_STYLE | wx.DD_CHANGE_DIR)

            if modify_dir_dlgbox.ShowModal() == wx.ID_OK:

                usr_rt_v = modify_dir_dlgbox.GetPath()

                if usr_rt_v == "":

                    invld_err_input = wx.MessageDialog(self.wpanel, "Null values are not accepted.",
                                                       "{} - input verifier error:".format(app_name),
                                                       wx.ICON_ERROR | wx.STAY_ON_TOP)

                    invld_err_input.ShowModal()

                else:

                    try:
                        json_fl_r = open(paths_datas_json_file_path, "r")

                        json_src_data = json.load(json_fl_r)

                        json_src_data["path"] = usr_rt_v

                        json_fl_w = open(paths_datas_json_file_path, "w")

                        json.dump(json_src_data, json_fl_w)

                        json_fl_r.close()

                        json_fl_w.close()

                        update_made_msg = wx.MessageDialog(self.wpanel, "Path changed.", "Path update - Complete",
                                                           wx.OK | wx.ICON_INFORMATION)

                        update_made_msg.ShowModal()

                        # [Early-tests type] 'folder json file' operation
                        #path_json = open(et_paths_datas_json_file_path, 'r')

                        path_json = open(paths_datas_json_file_path, 'r')

                        data = path_json.read()

                        path_infos_v = json.loads(data)["path"]

                        path_json.close()

                    except FileNotFoundError:

                        settings_json = open(paths_datas_json_file_path, 'w')

                        settings_json.write("{"'"path"'":")

                        usr_path = {
                            "path": str(usr_rt_v)
                        }

                        json_settings_file_datas = open(paths_datas_json_file_path, "w")

                        json.dump(usr_path, json_settings_file_datas)

                        json_settings_file_datas.close()

                        settings_json.close()

                        settings_path_saved_msg = wx.MessageDialog(self.wpanel, "Path saved.", "Path update - Complete",
                                                                   wx.OK | wx.ICON_INFORMATION)

                        settings_path_saved_msg.ShowModal()

                        # [Early-tests type] 'folder json file' operation
                        # path_json = open(et_paths_datas_json_file_path, 'r')

                        path_json = open(paths_datas_json_file_path, 'r')

                        data = path_json.read()

                        path_infos_v = json.loads(data)["path"]

                        # et_pascode_json_exists = os.path.exists(et_settings_json_full_path)

                        # [Early-tests type] Main app folder path
                        self.et_collections_folder_path = os.path.join(path_infos_v, et_collections_folder_name)

                        # [Early-tests type] encrypted folder path
                        self.et_encrypted_files_folder_path = os.path.join(self.et_collections_folder_path,
                                                                           et_enc_folder_name)

                        # [Early-tests type]  decrypted folder path
                        self.et_decrypted_files_folder_path = os.path.join(self.et_collections_folder_path,
                                                                           et_dec_folder_name)

                        # [Early-tests type] real-time 'Year' folder in 'Encrypted files' folder path
                        self.et_crnt_yrs_folder_path_enc = os.path.join(self.et_encrypted_files_folder_path, dt_yyyy)

                        # [Early-tests type] real-time 'Year' folder in 'Decrypted files' folder path
                        self.et_crnt_yrs_folder_path_dec = os.path.join(self.et_decrypted_files_folder_path, dt_yyyy)

                        # [Early-tests type] real-time 'date' folder in 'Encrypted files' folder
                        self.et_now_date_folder_enc_path = os.path.join(self.et_crnt_yrs_folder_path_enc, dt_date)


                        # [Early-tests type] real-time 'date' folder in 'Decrypted files' folder
                        self.et_now_date_folder_dec_path = os.path.join(self.et_crnt_yrs_folder_path_dec, dt_date)

                        # [Early-tests type] Folder-shorcut maker
                        # enc_dec_folder_shortcut_maker_dt(app_main_folder_root_var=self.et_collections_folder_path,years_sub_folder_root_var_enc=self.et_crnt_yrs_folder_path_enc,years_sub_folder_root_var_dec=self.et_crnt_yrs_folder_path_dec,date_sub_folder_root_var_enc=self.et_now_date_folder_enc_path,date_sub_folder_root_var_dec=self.et_now_date_folder_dec_path,folder_name_var=et_collections_folder_name)

                        # [Early-tests type] Encrypted-name folder
                        # self.enc_item_name_folder_path = os.path.join(self.now_date_folder_enc_path,epoch_miliseconds_str)

                    # Main app folders ->
                        # Main collections folder path
                        self.collections_folder_path = os.path.join(path_infos_v, collections_folder_name)

                        # encrypted folder
                        self.encrypted_files_folder_path = os.path.join(self.collections_folder_path, enc_folder_name)

                        # decrypted folder
                        self.decrypted_files_folder_path = os.path.join(self.collections_folder_path, dec_folder_name)

                        # real-time 'Year' folder in 'Encrypted files' folder path
                        self.crnt_yrs_folder_path_enc = os.path.join(self.encrypted_files_folder_path, dt_yyyy)

                        # real-time 'Year' folder in 'Decrypted files' folder path
                        self.crnt_yrs_folder_path_dec = os.path.join(self.decrypted_files_folder_path, dt_yyyy)

                        # real-time 'date' folder in 'Encrypted files' folder
                        self.et_now_date_folder_dec_path = os.path.join(self.crnt_yrs_folder_path_enc, dt_date)

                        # real-time 'date' folder in 'Decrypted files' folder
                        self.now_date_folder_dec_path = os.path.join(self.crnt_yrs_folder_path_dec, dt_date)

                        # Folder-shorcut maker
                        enc_dec_folder_shortcut_maker_dt(app_main_folder_root_var=self.collections_folder_path,years_sub_folder_root_var_enc=self.crnt_yrs_folder_path_enc,years_sub_folder_root_var_dec=self.crnt_yrs_folder_path_dec,date_sub_folder_root_var_enc=self.now_date_folder_enc_path,date_sub_folder_root_var_dec=self.now_date_folder_dec_path,folder_name_var=collections_folder_name)

                        path_json.close()
                break
            else:
                break

    def exitbutton(self, event):
        ''' Asks user whether to use again as message box. if not, clears the values for the user, or exits the app if yes  '''
        yn_msgbox = wx.MessageDialog(self.wpanel, "Are you sure you want to close '{}' ?".format(app_name), "Yes/No",
                                     wx.YES_NO | wx.ICON_WARNING | wx.STAY_ON_TOP)

        yn_var = yn_msgbox.ShowModal()

        if yn_var == wx.ID_NO:

            pass
        else:
            self.Destroy()  # closes app when 'EXIT' button is click

    def decipher_file_accesscode(self, event):

        self.dir_opts_dlg()

        # self.json_passcode_access()

        try:

            dec_pass_title = "{} - Decryption passcode entry".format(app_name)

            if os.path.exists(passwords_json_file_path) == True:

                while True:

                    self.decipher_pass_input = wx.PasswordEntryDialog(self.wpanel,
                                                                      "Please type the password for decryption:",
                                                                      dec_pass_title, style=wx.TextEntryDialogStyle)

                    if self.decipher_pass_input.ShowModal() == wx.ID_OK:

                        if self.decipher_pass_input.GetValue() == '':

                            invld_passwrd_err_input = wx.MessageDialog(self.wpanel, "Null passwords are not accepted.",
                                                                       "{} input verifier error - Password invalid:".format(
                                                                           app_name), wx.ICON_ERROR | wx.STAY_ON_TOP)

                            invld_passwrd_err_input.ShowModal()

                        else:

                            if self.decipher_pass_input.GetValue() == self.decrypt_pass:

                                # encrypt_frame(parent=self.wpanel,id=-1).Destroy()

                                # self.decryption()
                                self.decrypt_file()

                                break

                            else:
                                passcode_err_dec = wx.MessageDialog(self.wpanel, "Wrong password for decryption.",
                                                                    "{} - passcode verifier error".format(app_name),
                                                                    wx.ICON_ERROR | wx.STAY_ON_TOP)

                                passcode_err_dec.ShowModal()

                                # self.decipher_pass_input.ShowModal()
                    else:
                        break

                    self.json_data_fl.close()
            else:
                pass
        except AttributeError:
            pass

    def decrypt_file(self):

        try:

            ''' Accessing datas from 'backup' batch file '''
            try:
                json_fl_read = open(json_file_backups_file_path, 'r')

                data = json_fl_read.read()

                # Get file details using dictionary 'key-value' pairs
                # json_src_file_name = json.loads(data)["file_name"]

                # json_src_file_format = json.loads(data)["file_type"]

                json_src_enc_name = json.loads(data)["encrypted_file_name"]

                # json_src_file_full_name = json.loads(data)["file_full_name"]

                # print("Encrypted namse -> "+enc_name)

                # file_full_name = "{0}.{1}".format(json_src_file_name,json_src_file_format)

                file_full_name_json_decoded = cipher.decrypt(bytes(json_src_enc_name, 'utf-8')).decode()

                ''' Make  Deccrypted-item folder in real-time  date 'Decrypted files' folder folder'''
                # dec_item_name_id = "{0}_{1}".format(json_src_file_name,json_src_enc_name)

                # Decrypted-item folder path with real time now-date sub folder
                # dec_item_name_folder = os.path.join(self.et_now_date_folder_dec_path,file_full_name_json_decoded)

                # DirMake(dec_item_name_folder)

                # dec_complete_file_rt = os.path.join(dec_item_name_folder,file_full_name_json_decoded)

                # [Early-tests type] Decrypted folder path with real time now-date sub folder
                # dec_complete_file_rt = os.path.join(self.et_now_date_folder_dec_path,file_full_name_json_decoded)

                # Encrypted file source file name
                file_name_enc = '{}.enc'.format(json_src_enc_name)

                path_json = open(paths_datas_json_file_path, 'r')

                data = path_json.read()

                path_infos_v = json.loads(data)["path"]

                # Main app folders ->
                # Main collections folder path
                self.collections_folder_path = os.path.join(path_infos_v, collections_folder_name)

                # encrypted folder path
                self.encrypted_files_folder_path = os.path.join(self.collections_folder_path, enc_folder_name)

                # decrypted folder path
                self.decrypted_files_folder_path = os.path.join(self.collections_folder_path, dec_folder_name)

                # real-time 'years' folder in 'Encrypted files' folder
                self.crnt_yrs_folder_path_enc = os.path.join(self.encrypted_files_folder_path, dt_yyyy)

                # real-time 'years' folder in 'Decrypted files' folder path
                self.crnt_yrs_folder_path_dec = os.path.join(self.decrypted_files_folder_path, dt_yyyy)

                # real-time 'date' folder in 'Encrypted files' folder path
                self.now_date_folder_enc_path = os.path.join(self.crnt_yrs_folder_path_enc, dt_date)

                # real-time 'date' folder in 'Decrypted files' folder path
                self.now_date_folder_dec_path = os.path.join(self.crnt_yrs_folder_path_dec, dt_date)

                # Encrypted files secondary sub-folder
                self.subfolder2_encfiles_path = os.path.join(self.now_date_folder_enc_path, encfiles_subfolder2_name)

                # Encrypted folders secondary sub-folder
                self.subfolder2_encfolders_path = os.path.join(self.now_date_folder_enc_path,
                                                               encfolders_subfolder2_name)

                # Deccrypted files secondary sub-folder
                self.subfolder2_decfiles_path = os.path.join(self.now_date_folder_dec_path, decfiles_subfolder2_name)

                # Deccrypted folders secondary sub-folder
                self.subfolder2_decfolders_path = os.path.join(self.now_date_folder_dec_path,decfolders_subfolder2_name)

                # collection folder-shorcut maker
                enc_dec_folder_shortcut_maker_dt(app_main_folder_root_var=self.collections_folder_path,
                                                 years_sub_folder_root_var_enc=self.crnt_yrs_folder_path_enc,
                                                 years_sub_folder_root_var_dec=self.crnt_yrs_folder_path_dec,
                                                 date_sub_folder_root_var_enc=self.now_date_folder_enc_path,
                                                 date_sub_folder_root_var_dec=self.now_date_folder_dec_path,
                                                 subfolder2_root_var_encfiles=self.subfolder2_encfiles_path,
                                                 subfolder2_root_var_decfiles=self.subfolder2_decfiles_path,
                                                 subfolder2_root_var_encdirs=self.subfolder2_encfolders_path,
                                                 subfolder2_root_var_decdirs=self.subfolder2_decfolders_path,
                                                 folder_name_var=collections_folder_name)

                # Encrypted-name folder from json folder
                # enc_item_name_src_json_folder_path  = os.path.join(self.et_now_date_folder_enc_path,json_src_enc_name)

                # Encrypted-item file details with real time now-date sub folder
                # complete_file_rt_enc_json = os.path.join(enc_item_name_src_json_folder_path,file_name_enc)

                # [Early-tests type] Encrypted files details with real time now-date sub folder
                # complete_file_rt_enc_json = os.path.join(self.et_now_date_folder_enc_path,file_name_enc)

                # Decrypted folder path with real time now-date sub folder
                dec_complete_file_rt = os.path.join(self.subfolder2_decfiles_path, file_full_name_json_decoded)

                # Encrypted files details with real time now-date sub folder
                complete_file_rt_enc_json = os.path.join(self.subfolder2_encfiles_path, file_name_enc)

                # print(complete_file_rt_enc)
                try:
                    if os.path.exists(dec_complete_file_rt)== False:
                        encrypt_fl = open(complete_file_rt_enc_json, 'rb')

                        enc_file_data = encrypt_fl.read()

                        Decrypted_file = cipher.decrypt(enc_file_data)

                        dec_fl = open(dec_complete_file_rt, 'wb')

                        dec_fl.write(Decrypted_file)

                        dec_fl.close()

                        encrypt_fl.close()

                        json_fl_read.close()

                        # Deletes encrypted file completely
                        os.remove(complete_file_rt_enc_json)

                        # Deletes encrypted item folder completely
                        # os.removedirs(enc_item_name_src_json_folder_path)

                        # print('\n- File sucessfully decrypted..')

                        delay(0.16)

                        msg_dec_succcess = wx.MessageDialog(self.wpanel,
                                                            "'{}' file successfully decrypted.".format(file_full_name_json_decoded),
                                                            "{} - decryption info.".format(app_name),
                                                            wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)

                        msg_dec_succcess.ShowModal()

                    else:
                        try:
                            os.remove(complete_file_rt_enc_json)
                        except OSError:
                            pass

                        # print('\n- File already decrypted..')

                        msg_file_decrypted = wx.MessageDialog(self.wpanel, "'{}' file successfully decrypted.".format(file_full_name_json_decoded),
                                                            "{} - decryption info.".format(app_name),
                                                            wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)

                        msg_file_decrypted.ShowModal()
                except FileNotFoundError as fl_err:

                    # print(fl_err)

                    msg_decrypted_item_missing = wx.MessageDialog(self.wpanel, "No files to be decrypted..",
                                                                  "{} - file detector error.".format(app_name),
                                                                  wx.ICON_ERROR | wx.STAY_ON_TOP)

                    msg_decrypted_item_missing.ShowModal()

                except FileExistsError:

                    delay(0.16)

                    try:
                        os.remove(complete_file_rt_enc_json)
                    except OSError:
                        pass

                    # print('\n- File already decrypted..')

                    msg_file_decrypted = wx.MessageDialog(self.wpanel, "File already decrypted..",
                                                          "{} - decryption info.".format(app_name),
                                                          wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)

                    msg_file_decrypted.ShowModal()

            except FileNotFoundError:

                msg_backup_json_err = wx.MessageDialog(self.wpanel, "File backup data not found.",
                                                       "{} - decryption error.".format(app_name),
                                                       wx.ICON_ERROR | wx.STAY_ON_TOP)

                msg_backup_json_err.ShowModal()


        except NameError:
            pass

    def restrt_fg_files(self):

        try:
            self.fg_dirs = FolderGuardian(parent=None, id=-1)
            self.fg_dirs.Destroy()

        except AttributeError:
            pass
        except RuntimeError:
            pass

        try:
            self.fg_files = FileGuardian(parent=None, id=-1)
            self.fg_files.Destroy()

        except AttributeError:
            pass
        except RuntimeError:
            pass

        self.Destroy()

        self.fg_dirs = FolderGuardian(parent=None, id=-1)
        self.fg_dirs.ShowModal()

    def cipher_file_accesscode(self, event):

        self.dir_opts_dlg()

        # self.json_passcode_access()

        """ Verify 'path.json' if exists or not """
        settings_json_paths_exists = os.path.exists(paths_datas_json_file_path)

        if settings_json_paths_exists == False:

            pass

        else:

            enc_pass_title = "{} - Encryption passcode entry".format(app_name)

            try:

                if os.path.exists(passwords_json_file_path) == True:

                    while True:

                        self.cipher_pass_input = wx.PasswordEntryDialog(self.wpanel,
                                                                        "Please type the password for encryption:",
                                                                        enc_pass_title, style=wx.TextEntryDialogStyle)

                        if self.cipher_pass_input.ShowModal() == wx.ID_OK:

                            if self.cipher_pass_input.GetValue() == '':

                                invld_passwrd_err_input = wx.MessageDialog(self.wpanel,
                                                                               "Null passwords are not accepted.",
                                                                               "{} input verifier error - Password invalid:".format(
                                                                                   app_name),
                                                                               wx.ICON_ERROR | wx.STAY_ON_TOP)

                                invld_passwrd_err_input.ShowModal()

                            else:

                                if self.cipher_pass_input.GetValue() == self.encrypt_pass:

                                    # encrypt_frame(parent=self.wpanel,id=-1).Destroy()

                                    # self.decryption()
                                    self.encrypt_file()

                                    break

                                else:
                                    passcode_err_dec = wx.MessageDialog(self.wpanel,
                                                                            "Wrong password for decryption.",
                                                                            "{} - passcode verifier error".format(
                                                                                app_name),
                                                                            wx.ICON_ERROR | wx.STAY_ON_TOP)

                                    passcode_err_dec.ShowModal()

                                    # self.decipher_pass_input.ShowModal()
                        else:
                            break
                        self.json_data_fl.close()
                else:
                    pass
            except AttributeError:
                pass

    def encrypt_file(self):

        try:

            while True:

                filedir_dlgbox = wx.FileDialog(self.wpanel, "Please choose the required file to be encrypted:", "", "",
                                               wildcard="All files (*.*)|*.*; | Microsoft Word Document (*.docx) |*.docx; | Microsoft Excel (*.xlsx) |*.xlsx; | Microsoft Excel Macro (*.xlsm) |*.xlsm; | Compressed Zip (*.zip) |*.zip; | Notepad (*.txt) |*.txt; | JPEG (*.jpeg) |*.Jpeg; | PNG (*.png) |*.png; | JPEG (*.jpeg) |*.jpeg; | Python (*.py) |*.py; | Python (no console) (*.pyw) |*.pyw; | MP4 (*.mp4) |*.mp4; | WEBM (*.webm) |*.webm; | M4A (*.m4a)|*.m4a; | M4V (*.m4v) | *.m4v;",
                                               style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
                #PyServerAuto-PackagesLists.txt
                if filedir_dlgbox.ShowModal() == wx.ID_OK:
                    complete_file_rt = filedir_dlgbox.GetPath()

                    file_name, file_format = os.path.splitext(os.path.basename(complete_file_rt))

                    self.src_file_full_name = "{0}{1}".format(file_name, file_format)

                    src_fl_exists = os.path.exists(complete_file_rt)

                    # print(complete_file_rt)

                    self.str_enc_name = cipher.encrypt(bytes(str(self.src_file_full_name), 'utf-8')).decode()

                    file_name_enc = '{}.enc'.format(self.str_enc_name)

                    # Encrypted-item file path with real-time now-date sub folder
                    # enc_item_name_folder_path = os.path.join(self.et_now_date_folder_enc_path,self.str_enc_name)

                    # DirMake(enc_item_name_folder_path)

                    # complete_item_file_rt_enc = os.path.join(enc_item_name_folder_path,file_name_enc)

                    # print(complete_file_rt_enc)

                    # [Early-tests type] Encrypted file path with real-time now-date sub folder
                    # complete_file_rt_enc = os.path.join(self.et_now_date_folder_enc_path,file_name_enc)

                    # Encrypted file path with real-time now-date sub folder
                    complete_file_rt_enc = os.path.join(self.subfolder2_encfiles_path, file_name_enc)

                    try:

                        non_encrypt_fl = open(complete_file_rt, 'rb')

                        non_enc_fl_data = non_encrypt_fl.read()

                        encrypted_data = cipher.encrypt(non_enc_fl_data)

                        enc_fl = open(complete_file_rt_enc, 'wb')

                        enc_fl.write(encrypted_data)

                        # print('\n- File successfully encrypted..')

                        msg_enc_succcess = wx.MessageDialog(self.wpanel, "'{}' file successfully encrypted.".format(
                                self.src_file_full_name), "{} - encryption info.".format(app_name),
                                                                wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)

                        msg_enc_succcess.ShowModal()

                        # wipeout()

                        backup_fl_infos = {
                                "encrypted_file_name": self.str_enc_name
                        }

                        # Tranfers data And then stores it on the json file
                        jfl = open(json_file_backups_file_path, "w")

                        json.dump(backup_fl_infos, jfl)

                        jfl.close()

                        enc_fl.close()

                        non_encrypt_fl.close()

                        os.remove(complete_file_rt)

                        break

                    except FileNotFoundError:

                        msg_encrypted_item_missing = wx.MessageDialog(self.wpanel, "No Files to be encrypted..",
                                                                          "{} - encryption info.".format(app_name),
                                                                          wx.ICON_ERROR | wx.STAY_ON_TOP)

                        msg_encrypted_item_missing.ShowModal()


                    except FileExistsError:

                        try:

                            os.remove(complete_file_rt)

                        except OSError:
                            pass

                        delay(0.16)

                        # print('\n- File already encrypted..')

                        msg_file_encrypted = wx.MessageDialog(self.wpanel, "File already encrypted..",
                                                                  "{} - encryption info.".format(app_name),
                                                                  wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)

                        msg_file_encrypted.ShowModal()


                else:
                    break

        except NameError:
            pass


if __name__ == '__main__':
    # AskDir()

    # [Early-tests type] database folder maker
    # DirMake(path_val=et_database_folder_path)

    # [Early-tests type] settings folder maker
    # DirMake(path_val=et_settings_folder_path)

    # [Early-tests type] backups folder maker
    # DirMake(path_val=et_backups_folder_path)

    # [Early-tests type] password json file maker
    # password_json_make(json_path_val=et_passwords_json_file_path)

    # database folder maker
    DirMake(path_val=database_folder_path)

    # settings folder maker
    DirMake(path_val=settings_folder_path)

    # backups folder maker
    DirMake(path_val=backups_folder_path)

    # password json file maker
    password_json_make(json_path_val=passwords_json_file_path)

    app = wx.App()

    encrypt_window = appUI(parent=None, id=-1)

    encrypt_window.Show()

    app.MainLoop()
