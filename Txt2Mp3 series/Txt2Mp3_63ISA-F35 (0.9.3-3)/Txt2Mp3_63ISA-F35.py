''' importing prefrences or getting required datas from the modules'''
 
import os  # for file and folder operation

import time  # for 'time-self.delays' activities

from gtts.tts import gTTSError

from playsound import playsound# for playing audio files

import winshell# mimic windows powershell activities

from win32com.client import Dispatch# Creates a Dispatch based COM object using win32 modules

import datetime
import json
from gtts import gTTS# using google-text-to-speech (gtts) service
from PySide2.QtCore import QTimer
from PySide2.QtWidgets import QApplication , QMessageBox
import speech_recognition as sr
import wx
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QPushButton, QFileDialog, QVBoxLayout
import string
import random

'''Source files'''
#cdir = os.path.dirname(os.path.realpath(__file__))# curent working directory or the 'Now'-location of the file.

cdir = os.getcwd()

for file in os.listdir(cdir):
    
    #print(file)
    if '.ico' in file:
        try:
            ico_flpath =os.path.join(cdir,file)
        except OSError:
            pass
    else:
        pass

# --------------------------------------------------------------------------------------------------

# Time
dt_clockH = datetime.datetime.now().strftime("%I")

dt_clockM = datetime.datetime.now().strftime("%M")

dt_clockS = datetime.datetime.now().strftime("%S")

dt_clockMS = datetime.datetime.now().strftime("%f")

epoch_miliseconds = int(time.time() * 1000)

dt_TMR = f"{dt_clockH}:{dt_clockM}:{dt_clockS}"

dt_time= f"{dt_clockH}:{dt_clockM}"

dt_DN = datetime.datetime.now().strftime('%p').lower()

# Date
dt_dd = datetime.datetime.now().strftime("%d")

dt_mm = datetime.datetime.now().strftime("%m")

dt_yyyy = datetime.datetime.now().strftime("%Y")

dt_wdys = datetime.datetime.now().strftime("%A").lower()

dt_mnths = datetime.datetime.now().strftime("%B")

dt_mnths_no = datetime.datetime.now().strftime("%m")

dt_date = f"{dt_dd}-{dt_mm}-{dt_yyyy}"

dt_mnthsno_mnths = f"{dt_mnths_no}-{dt_mnths}"
 
# Current file name infos
'''File name & File extension'''
file_name, file_type = os.path.splitext(os.path.basename(os.path.abspath(__file__)))
 
# --------------------------------------------------------------------------------
''' Folder names '''
# Audio folder with app name
app_folder_name = 'Txt2Mp3 6.3 [I.S.A]'
main_folder_name = '{} audios'.format(app_folder_name)

# -----------------------------------------------------------------------------------------

''' Settings file path '''
# App Json files details
paths_name_json = 'path_datas'

json_fl_name = '{}.json'.format(paths_name_json)

paths_datas_json_file_path = os.path.join(cdir,json_fl_name)

# App title
app_title = "Txt2Mp3 6.3 [Improved.Simplified.Alternative]"

# Random String
rand_str = ''.join(random.choices(string.ascii_letters, k=15))

# Logs Folder
log_dirname = "Logs"
logs_folder_path = os.path.join(cdir,log_dirname)

# Log file details
logfl_name = f"Log_{dt_date}"
log_fl = f"{logfl_name}.log"

logfl_path = os.path.join(logs_folder_path,log_fl)

class isaUI(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        # Set APP BG 
        self.palette = QtGui.QPalette()
        self.brush = QtGui.QBrush(QtGui.QColor(33, 192, 162))
        self.brush.setStyle(QtCore.Qt.SolidPattern)
        self.palette.setBrush(QtGui.QPalette.Window, self.brush)
        MainWindow.setPalette(self.palette)


        # Set app icon
        returned_icofl_path = self.icon_fls()
        MainWindow.setWindowIcon(QtGui.QIcon(returned_icofl_path))  

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(30, 19, 741, 511))

        font = QtGui.QFont()
        font.setPointSize(16)
        self.frame_2.setFont(font)
        self.frame_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

    # Text
    # -> Text frame

        self.frame_Text = QtWidgets.QFrame(self.frame_2)
        self.frame_Text.setGeometry(QtCore.QRect(80, 50, 651, 91))
 
        self.frame_Text.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Text.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Text.setObjectName("frame_Text")

    # Text input field
        self.txt_In = QtWidgets.QLineEdit(self.frame_Text)
        self.txt_In.setGeometry(QtCore.QRect(40, 20, 591, 51))
        self.txt_In.setToolTip("")
        self.txt_In.setToolTipDuration(3)
        self.txt_In.setObjectName("txt_In")

        font = QtGui.QFont()
        font.setPointSize(28)
        self.txt_In.setToolTipDuration(-2)
        self.txt_In.setFont(font)
        self.txt_In.setObjectName("txt_In")

    # Text label
        self.text_Lbl = QtWidgets.QLabel(self.frame_2)
        self.text_Lbl.setGeometry(QtCore.QRect(22, 70, 93, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.text_Lbl.setFont(font)
        self.text_Lbl.setScaledContents(True)
        self.text_Lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.text_Lbl.setWordWrap(False)
        self.text_Lbl.setObjectName("text_Lbl")

    # Select Accent
        # -> Select Accent label
        self.accent_Lbl = QtWidgets.QLabel(self.frame_2)
        self.accent_Lbl.setGeometry(QtCore.QRect(29, 170, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.accent_Lbl.setFont(font)
        self.accent_Lbl.setScaledContents(True)
        self.accent_Lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.accent_Lbl.setWordWrap(False)
        self.accent_Lbl.setObjectName("accent_Lbl")

        # -> Accent Combo box
        self.accent_comboBox = QtWidgets.QComboBox(self.frame_2)
        self.accent_comboBox.setGeometry(QtCore.QRect(100, 220, 121, 71))

        font = QtGui.QFont()
        font.setPointSize(26)
        self.accent_comboBox.setFont(font)
        self.accent_comboBox.setObjectName("accent_comboBox")
        self.accent_comboBox.addItem("")
        self.accent_comboBox.addItem("")
        self.accent_comboBox.addItem("")
        self.accent_comboBox.addItem("")
        self.accent_comboBox.addItem("")
        self.accent_comboBox.addItem("")

    # Select TDL
        # -> Select tdl label
        self.tdl_Lbl = QtWidgets.QLabel(self.frame_2)
        self.tdl_Lbl.setGeometry(QtCore.QRect(312, 170, 378, 41))

        font = QtGui.QFont()
        font.setPointSize(20)
        self.tdl_Lbl.setFont(font)

        self.tdl_Lbl.setScaledContents(True)
        self.tdl_Lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.tdl_Lbl.setWordWrap(False)
        self.tdl_Lbl.setObjectName("tdl_Lbl")

        # -> TDL Combo Box
        self.tdl_comboBox = QtWidgets.QComboBox(self.frame_2)
        self.tdl_comboBox.setGeometry(QtCore.QRect(520, 220, 171, 71))

        font = QtGui.QFont()
        font.setPointSize(26)
        self.tdl_comboBox.setFont(font)

        self.tdl_comboBox.setObjectName("tdl_comboBox")
        self.tdl_comboBox.addItem("")
        self.tdl_comboBox.addItem("")
        self.tdl_comboBox.addItem("")
        self.tdl_comboBox.addItem("")
        self.tdl_comboBox.addItem("")
        self.tdl_comboBox.addItem("")
        self.tdl_comboBox.addItem("")
        self.tdl_comboBox.addItem("")
        self.tdl_comboBox.addItem("")
        self.tdl_comboBox.addItem("")
        self.tdl_comboBox.addItem("")
        self.tdl_comboBox.addItem("")
        self.tdl_comboBox.addItem("")


    # Button
        # -> Button font
        font = QtGui.QFont()
        font.setPointSize(19)
 
        # -> Button frame
        self.btn_frame = QtWidgets.QFrame(self.frame_2)
        self.btn_frame.setGeometry(QtCore.QRect(60, 310, 661, 181))
        self.btn_frame.setFont(font)
        self.btn_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.btn_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.btn_frame.setObjectName("btn_frame")

        # -> Modify button
        self.modify_btn = QtWidgets.QPushButton(self.btn_frame)
        self.modify_btn.setGeometry(QtCore.QRect(30, 30, 151, 51))
        self.modify_btn.setObjectName("modify_btn")

        # -> Convert button
        self.convert_Btn = QtWidgets.QPushButton(self.btn_frame)
        self.convert_Btn.setGeometry(QtCore.QRect(240, 30, 151, 51))
        self.convert_Btn.setObjectName("convert_Btn")

        # -> Reset button
        self.reset_btn = QtWidgets.QPushButton(self.btn_frame)
        self.reset_btn.setGeometry(QtCore.QRect(450, 30, 151, 51))
        self.reset_btn.setObjectName("reset_btn")

        # -> Access button
        self.access_btn = QtWidgets.QPushButton(self.btn_frame)
        self.access_btn.setGeometry(QtCore.QRect(450, 110, 151, 51))
        self.access_btn.setObjectName("access_btn")

        # -> Play2Mp3 button
        self.playMp3_btn = QtWidgets.QPushButton(self.btn_frame)
        self.playMp3_btn.setGeometry(QtCore.QRect(240, 110, 151, 51))
        self.playMp3_btn.setObjectName("playMp3_btn")

        # -> Exit button
        self.exitBtn = QtWidgets.QPushButton(self.btn_frame)
        self.exitBtn.setGeometry(QtCore.QRect(30, 110, 151, 51))
        self.exitBtn.setObjectName("exitBtn")
        MainWindow.setCentralWidget(self.centralwidget)

    # Menu
        # -> Menubar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuSettings = QtWidgets.QMenu(self.menuOptions)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)

        # -> Statusbar
        # -> Statusbar font
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # -> Change path option
        self.actionChange_path = QtWidgets.QAction(MainWindow)
        self.actionChange_path.setObjectName("actionChange_path")

        # -> Open audio folder path
        self.actionOpen_folder = QtWidgets.QAction(MainWindow)
        self.actionOpen_folder.setObjectName("actionOpen_folder")

        # -> Open log folder path
        self.actionOpenLogs_folder = QtWidgets.QAction(MainWindow)
        self.actionOpenLogs_folder.setObjectName("actionOpenLogs_folder")

        # -> Open log file
        self.actionOpenLog_file = QtWidgets.QAction(MainWindow)
        self.actionOpenLog_file.setObjectName("actionOpenLog_file")

        # Addind options to the menubar
        self.menuSettings.addAction(self.actionChange_path)
        self.menuOptions.addAction(self.menuSettings.menuAction())
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionOpen_folder)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionOpenLogs_folder)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionOpenLog_file)
        self.menubar.addAction(self.menuOptions.menuAction())


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # front view items
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", app_title))

    # Tdl label
        self.text_Lbl.setText(_translate("MainWindow", "Text:"))

    # Text input box
        self.txt_In.setToolTip(_translate("MainWindow","Please type your text here."))

    # Tdl combo box items
        self.accent_comboBox.setItemText(0, _translate("MainWindow", "en"))
        self.accent_comboBox.setItemText(1, _translate("MainWindow", "fr"))
        self.accent_comboBox.setItemText(2, _translate("MainWindow", "zh-CN"))
        self.accent_comboBox.setItemText(3, _translate("MainWindow", "zh-TW"))
        self.accent_comboBox.setItemText(4, _translate("MainWindow", "pt"))
        self.accent_comboBox.setItemText(5, _translate("MainWindow", "es"))

    # Tdl combo box items
        self.tdl_comboBox.setItemText(0, _translate("MainWindow", "com.au"))
        self.tdl_comboBox.setItemText(1, _translate("MainWindow", "co.uk"))
        self.tdl_comboBox.setItemText(2, _translate("MainWindow", "com"))
        self.tdl_comboBox.setItemText(3, _translate("MainWindow", "ca"))
        self.tdl_comboBox.setItemText(4, _translate("MainWindow", "co.in"))
        self.tdl_comboBox.setItemText(5, _translate("MainWindow", "ie"))
        self.tdl_comboBox.setItemText(6, _translate("MainWindow", "co.za"))
        self.tdl_comboBox.setItemText(7, _translate("MainWindow", "ca"))
        self.tdl_comboBox.setItemText(8, _translate("MainWindow", "fr"))
        self.tdl_comboBox.setItemText(9, _translate("MainWindow", "com.br"))
        self.tdl_comboBox.setItemText(10, _translate("MainWindow", "pt"))
        self.tdl_comboBox.setItemText(11, _translate("MainWindow", "com.mx"))
        self.tdl_comboBox.setItemText(12, _translate("MainWindow", "es"))

    # Accent label
        self.accent_Lbl.setText(_translate("MainWindow", "Select Accent:"))

    # Tdl label
        self.tdl_Lbl.setText(_translate("MainWindow", "Select Top.Level.Domain (Tdl):"))


    # GUI Buttons:

    # -> Modify button
        self.modify_btn.setText(_translate("MainWindow", "Change path"))
        self.modify_btn.setStatusTip("Click to to change path. (Ctrl+P)")

    #-> Convert button
        self.convert_Btn.setText(_translate("MainWindow", "Convert"))
        self.convert_Btn.setShortcut(_translate("MainWindow", "Return"))
        self.convert_Btn.setStatusTip(_translate("MainWindow", "Click here to convert texts into audio file. (Press Enter)"))

    # -> Reset button
        self.reset_btn.setText(_translate("MainWindow", "Reset"))
        self.reset_btn.setText(_translate("MainWindow", "Reset"))
        self.reset_btn.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.reset_btn.setStatusTip(_translate("MainWindow", "Click here to clear values. (Ctrl+Z)"))

    # -> Access button
        self.access_btn.setText(_translate("MainWindow", "Access"))
        # self.access_btn.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.access_btn.setStatusTip(_translate("MainWindow", "Click here to access audios. (Press Ctrl+O)"))

    # -> PlayMP3 button
        self.playMp3_btn.setText(_translate("MainWindow", "PlayMp3"))
        self.playMp3_btn.setStatusTip(_translate("MainWindow", "Click here to play audios."))

    # -> Exit button
        self.exitBtn.setText(_translate("MainWindow", "Exit"))
        self.exitBtn.setStatusTip(_translate("MainWindow", "Click here to exit. (Press Esc)"))
        self.exitBtn.setShortcut(_translate("MainWindow", "Esc"))

    # GUI options
        # -> Options 
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))

        # -> Settings
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))

        # -> Change path
        self.actionChange_path.setText(_translate("MainWindow", "Change path"))
        self.actionChange_path.setShortcut(_translate("MainWindow", "Ctrl+P"))

        # -> Open folder
        self.actionOpen_folder.setText(_translate("MainWindow", "Access audios"))
        self.actionOpen_folder.setShortcut(_translate("MainWindow", "Ctrl+O"))

        # -> Open logs folder
        self.actionOpenLogs_folder.setText(_translate("MainWindow", "Open log folder"))

        # -> Open log file
        self.actionOpenLog_file.setText(_translate("MainWindow", "Open log file"))
        self.actionOpenLog_file.setShortcut(_translate("MainWindow", "Ctrl+L"))
        # self.actionOpenLog_folder.setShortcut(_translate("MainWindow", "Ctrl+O"))

    # Button events:

    # Options actions
        # -> Open folder (Ctrl+O)
        self.actionOpen_folder.triggered.connect(self.access_audios)

        # -> Change path (Ctrl+P)
        self.actionChange_path.triggered.connect(self.chngpath)

        # -> Open logs folder
        self.actionOpenLogs_folder.triggered.connect(self.open_logsfolder)

        # -> Open log file (Ctrl+L)
        self.actionOpenLog_file.triggered.connect(self.open_logsfl)

    # GUI button actions
        # -> Convert button
        self.convert_Btn.clicked.connect(self.txt2mp3)

        # -> PlayMp3 button
        self.playMp3_btn.clicked.connect(self.playMp3)

        # -> Modify button (Change path)
        self.modify_btn.clicked.connect(self.chngpath)

        # -> Exit button
        self.exitBtn.clicked.connect(self.exit)

        # -> Open folder
        self.access_btn.clicked.connect(self.access_audios)

        # -> Reset Button
        self.reset_btn.clicked.connect(self.reset)

    # GUI button colors
        # -> Modify button
        self.modify_btn.setStyleSheet("background-color : brown; color: white")
        
        # -> Convert button
        self.convert_Btn.setStyleSheet("background-color : green; color: white")
        
        # -> PlayMp3 button
        self.playMp3_btn.setStyleSheet("background-color : yellow; color: red")
        
        # -> Exit button
        self.exitBtn.setStyleSheet("background-color : red; color: white")
        
        # -> Access folder button
        self.access_btn.setStyleSheet("background-color : blue; color: white")
        
        # -> Reset button
        self.reset_btn.setStyleSheet("background-color : purple; color: white")

    # GUI label colors 
        # -> Text label
        self.text_Lbl.setStyleSheet("background-color : brown; color: white")

        # -> Text label
        self.accent_Lbl.setStyleSheet("background-color : black; color: white")

        # -> Text label
        self.tdl_Lbl.setStyleSheet("background-color : black; color: white")

    # GUI input box colors 
        # -> text input box
        self.txt_In.setStyleSheet("color: brown")
 
    def access_audios(self):

        self.save_path_json()

        if os.path.exists(paths_datas_json_file_path) == True:
            returned_now_date_sub_folder_v = self.get_json_paths()
            os.startfile(returned_now_date_sub_folder_v)
        else:
            pass  

    def open_logsfolder(self):

        try:
            os.makedirs(logs_folder_path)
        except OSError:
            pass
 
        os.startfile(logs_folder_path)

    def open_logsfl(self):
    
        try:
            os.makedirs(logs_folder_path)
        except OSError:
            pass

        if os.path.exists(logfl_path)==False:
            with open(logfl_path,"w") as logfl_w6:
                logfl_w6.writable()
        else:
            pass
        os.startfile(logfl_path)  

    def save_path_json(self):
 
        if os.path.exists(paths_datas_json_file_path) == False:
            
            dir_dialog_title = "Please choose folder (or directory) to hold '{}' folder:".format(main_folder_name)
            dir_dlgbox = QFileDialog.getExistingDirectory(self, caption=dir_dialog_title)
           
            if dir_dlgbox:

                usr_rt_v = dir_dlgbox.replace("/","\\")

                self.save_json(json_flpath1=paths_datas_json_file_path,keys1="path",val1=usr_rt_v)

                self.msg_autoClose(msg_text="Path saved.                        ",msg_title="Path update - Complete",close_tmr=3,msg_icon=QMessageBox.Information)

                #sys.exit()
            else:
                pass
        else:
            pass

    def chngpath(self):
        dir_dialog_title = "Please choose folder (or directory) to be changed:"
        
        chngdir_dlgbox = QFileDialog.getExistingDirectory(self, caption=dir_dialog_title)
           
        if chngdir_dlgbox:

            usr_chng_rt_v = chngdir_dlgbox.replace("/","\\")

            # print(usr_chng_rt_v)

            if os.path.exists(paths_datas_json_file_path)==True:

                self.update_json(json_flpath3=paths_datas_json_file_path,keys3="path",info3=usr_chng_rt_v,msg_title3="Path update - Complete:",msg_txt3="Path changed successfully.      ")

                self.get_json_paths()
            else:
                self.save_path_json()
        else:
            pass

    def get_json_paths(self):

        try:

            returned_path = self.read_json(jsonfl_path1=paths_datas_json_file_path,k1="path")

            ''' AppName audio folder path '''
            app_audio_folder_v = os.path.join(returned_path,main_folder_name)

            ''' Current year folder path '''
            now_yrs_sub_folder_v = os.path.join(app_audio_folder_v,dt_yyyy)

            ''' Current month number-month folder path '''
            now_mnthsno_mnths_sub_folder_v = os.path.join(now_yrs_sub_folder_v,dt_mnthsno_mnths)

            ''' Current date folder path '''
            now_date_sub_folder_v = os.path.join(now_mnthsno_mnths_sub_folder_v,dt_date)

            dir_lsts = [app_audio_folder_v , now_yrs_sub_folder_v , now_mnthsno_mnths_sub_folder_v , now_date_sub_folder_v]

            self.appMp3s_foldershortcut_maker_lsts(paths_1=dir_lsts,folder_name=main_folder_name)
            
            self.delay(0.16)
        
            return now_date_sub_folder_v
        except FileNotFoundError:
            pass

    def read_json(self,jsonfl_path1,k1):
        with open(jsonfl_path1,'r') as pathjson_fl_r:
            data = pathjson_fl_r.read()

            infos_v = json.loads(data)[k1]

        return infos_v

    def save_json(self,json_flpath1,keys1,val1):

        infos = {
            keys1: str(val1)

                            }
        with open(json_flpath1,'w') as json_fl_w:
            json.dump(infos,json_fl_w)  

    def update_json(self,json_flpath3,keys3,info3,msg_txt3,msg_title3):

        with open(json_flpath3,'r') as json_data_r:
            json_src_data = json.load(json_data_r)

            json_src_data[keys3] = info3

            with open(json_flpath3,'w') as json_fl_w:
                json.dump(json_src_data,json_fl_w)

        self.msg_autoClose(msg_text=msg_txt3+"                        ",msg_title=msg_title3+"                        ",close_tmr=3,msg_icon=QMessageBox.Information)
    
    def playMp3(self):
 
        self.save_path_json()      

        if os.path.exists(paths_datas_json_file_path) == True:

            returned_now_date_sub_folder_v = self.get_json_paths()

            fl_dialog_title = f"Please choose audio to be played from '{main_folder_name}' folder :"

            wild_cards = "Mp3 (*.mp3);;Waveform Audio File Format (*.wav)"
    
            # file_enc1 , check_enc1 = QFileDialog.getOpenFileName(self, "Choose file to be encrypted:","", "All Files (*);;Notepad (*.txt);;JPEG (*.jpeg);;PNG (*.png);; Mp3 (*.mp3);;MP4 (*.mp4);;Microsoft Word Document (*.docx)")
            file_enc1 , check_enc1 = QFileDialog.getOpenFileName(self, fl_dialog_title,returned_now_date_sub_folder_v, wild_cards)
            if check_enc1:
                file_choosen_re = file_enc1.replace("/","\\")

                playsound(file_choosen_re)

            else:
                pass
    
    def txt2mp3(self):

        self.save_path_json()

        txtsrc_in = str(self.txt_In.text())
        accentsrc_in = str(self.accent_comboBox.currentText())
        tdlsrc_in = str(self.tdl_comboBox.currentText())

        print(txtsrc_in+" "+accentsrc_in+" "+tdlsrc_in)
 
        if os.path.exists(paths_datas_json_file_path) == True:

            returned_now_date_sub_folder_v = self.get_json_paths()
      
            self.gtts_v(path_gtts_audio=returned_now_date_sub_folder_v,txt=txtsrc_in,accent=accentsrc_in,tdl=tdlsrc_in)
 
        else:
            pass

    def gtts_v(self,path_gtts_audio,txt,accent,tdl):

        try:
                
            audio_name_mp3 = f"Audio_{rand_str}.mp3"

            audio_full_path = os.path.join(path_gtts_audio,audio_name_mp3)

            self.gtts_audios(text_val=txt,lang_val=accent,tdl_val=tdl,audio_root_val=audio_full_path)
            
            self.msg_autoClose(msg_text=f"'{txt}' text sucessfully converted into '{audio_name_mp3}' audio file.",msg_title="Text to audio file (.Mp3) status - Complete",close_tmr=3)
            
            returned_msg_outs = self.yn_msgbox(txt5="Do you wish to play the audio?",title5="Play audio - Yes/No?",msg_icon=QMessageBox.Question)

            if returned_msg_outs == QMessageBox.No:
                pass
            elif returned_msg_outs == QMessageBox.Yes:
                playsound(audio_full_path)
            else:
                pass
            # Active when there is no text to convert
        except AssertionError as assertion_err:

            self.delay(0.16)
 
            self.apps_log_sys(logerr_msg=assertion_err,err_msgtitle="Assertion Error - Text cannot be converted into audio.",err_msgtxt="No words to convert into audio file (.mp3)")

            self.delay(0.19)

            self.msg_autoClose(msg_text="Seeking alternative.....",msg_title="Notify",close_tmr=3,msg_icon=QMessageBox.Information)

            try:
                r=sr.Recognizer()

                m = sr.Microphone()

                with m as source:

                    self.msg_autoClose(msg_text="You can speak now.              ",msg_title="Text-2-Speech: Google-Speech Recognition",close_tmr=3,msg_icon=QMessageBox.Information)

                    r.pause_threshold=2

                    audio = r.listen(source)

                try:
                        
                    str_sr_var=r.recognize_google(audio,language=f"{accent}-{tdl}")

                    audio_name_mp3_sr = f"Audio-SpeehRec_{rand_str}.mp3"

                    audio_full_path_sr = os.path.join(path_gtts_audio,audio_name_mp3_sr)
                    
                    self.gtts_audios(text_val=str(str_sr_var),lang_val=accent,tdl_val=tdl,audio_root_val=audio_full_path_sr)
                    
                    self.msg_autoClose(msg_text=f"'{str_sr_var}' text sucessfully converted into '{audio_name_mp3_sr}' audio file.",msg_title="Text to audio file (.Mp3) status - Complete",close_tmr=3,msg_icon=QMessageBox.Information)
                
                    returned_msg_outs = self.yn_msgbox(txt5="Do you wish to play the audio?",title5="Play audio - Yes/No?",msg_icon=QMessageBox.Question)

                    if returned_msg_outs == QMessageBox.No:
                        pass
                    elif returned_msg_outs == QMessageBox.Yes:
                        playsound(audio_full_path_sr)
                    else:
                        pass
                
                except sr.UnknownValueError as sr_ue_err:

                    self.txt_In.setText("")#            clears texts that exists within the input feilds

                    self.tdl_comboBox.setCurrentText("en")# setting the tdl combobox back to default

                    self.accent_comboBox.setCurrentText("com.au")# setting the accent combobox back to default

                    self.delay(0.16)

                    self.apps_log_sys(logerr_msg=str(sr_ue_err),err_msgtitle="Speech-Recognition Unknown Error: ",err_msgtxt="Oops! Didn't catch that.")
                           
                except sr.RequestError as sr_req_err:

                    # self.txt_In.setText("")#            clears texts that exists within the input feilds

                    self.tdl_comboBox.setCurrentText("en")# setting the tdl combobox back to default

                    self.accent_comboBox.setCurrentText("com.au")# setting the accent combobox back to default

                    self.apps_log_sys(logerr_msg=str(sr_req_err),err_msgtitle="Speech-Recognition Connection Error: ",err_msgtxt="Opps! couldn't request results from Google Speech Recognition service at the moment. So please check the device network is online and ready.")

                # Active when there is program run time error     
                except RuntimeError as runtime_err:

                    self.apps_log_sys(logerr_msg=str(runtime_err),err_msgtitle="Runtime Error: ",err_msgtxt="Program did not function properly.")

                    self.delay(0.16)

                    self.txt_In.setText("")#            clears texts that exists within the input feilds

                    self.tdl_comboBox.setCurrentText("en")# setting the tdl combobox back to default

                    self.accent_comboBox.setCurrentText("com.au")# setting the accent combobox back to default

                    sys.exit()

                    # self.delay(0.16)

                    # os.startfile(os.path.basename(__file__))

                    # Active there is no internet connection 'google Text-to-speech' (gTTS) server
                except gTTSError as gtts_err:

                    os.remove(audio_full_path_sr)

                    self.txt_In.setText("")#            clears texts that exists within the input feilds

                    self.tdl_comboBox.setCurrentText("en")# setting the tdl combobox back to default

                    self.accent_comboBox.setCurrentText("com.au")# setting the accent combobox back to default

                    self.delay(0.16)

                    self.apps_log_sys(logerr_msg=gtts_err,err_msgtitle="Connection Error - Systems Offline: ",err_msgtxt="Opps! couldn't convert text into audio because of no internet connection at the moment. So please check the device network is online and ready.")

                # Active when an error is not recognizible\Generic         
                except Exception as generic_err:

                    os.remove(audio_full_path_sr)

                    self.txt_In.setText("")#            clears texts that exists within the input feilds

                    self.tdl_comboBox.setCurrentText("en")# setting the tdl combobox back to default

                    self.accent_comboBox.setCurrentText("com.au")# setting the accent combobox back to default
                            
                    self.delay(0.16)

                    self.apps_log_sys(logerr_msg=str(generic_err),err_msgtitle="Generic Error: ",err_msgtxt=str(generic_err))
        
            except KeyboardInterrupt:
                pass
                # Active when there is program run time error     
            except RuntimeError as runtime_err:

                self.apps_log_sys(logerr_msg=str(runtime_err),err_msgtitle="Runtime Error: ",err_msgtxt="Program did not function properly.")

                self.delay(0.16)

                self.txt_In.setText("")#            clears texts that exists within the input feilds

                self.tdl_comboBox.setCurrentText("en")# setting the tdl combobox back to default

                self.accent_comboBox.setCurrentText("com.au")# setting the accent combobox back to default

                sys.exit()

                # self.delay(0.16)

                # os.startfile(os.path.basename(__file__))
            except Exception as generic_err:

                self.txt_In.setText("")#            clears texts that exists within the input feilds

                self.tdl_comboBox.setCurrentText("en")# setting the tdl combobox back to default

                self.accent_comboBox.setCurrentText("com.au")# setting the accent combobox back to default
                        
                self.delay(0.16)

                self.apps_log_sys(logerr_msg=generic_err,err_msgtitle="Generic error:",err_msgtxt=str(generic_err))

        # Active there is no internet connection 'google Text-to-speech' (gTTS) server
        except gTTSError as gtts_err:

            os.remove(audio_full_path)

            self.txt_In.setText("")#            clears texts that exists within the input feilds

            self.tdl_comboBox.setCurrentText("en")# setting the tdl combobox back to default

            self.accent_comboBox.setCurrentText("com.au")# setting the accent combobox back to default

            self.delay(0.16)

            self.apps_log_sys(logerr_msg=gtts_err,err_msgtitle="Connection Error - Systems Offline: ",err_msgtxt="Opps! couldn't convert text into audio because of no internet connection at the moment. So please check the device network is online and ready.")
 
            # Active when an error is not recognizible         
        except Exception as generic_err:

            os.remove(audio_full_path)

            self.txt_In.setText("")#            clears texts that exists within the input feilds

            self.tdl_comboBox.setCurrentText("en")# setting the tdl combobox back to default

            self.accent_comboBox.setCurrentText("com.au")# setting the accent combobox back to default
                    
            self.delay(0.16)

            self.apps_log_sys(logerr_msg=generic_err,err_msgtitle="Generic errror",err_msgtxt=str(generic_err))
   
    def appMp3s_foldershortcut_maker_lsts(self,paths_1,folder_name):

        for dir in paths_1:

            try:
                os.makedirs(dir)
            except OSError:
                pass
            
            
            if dir == paths_1[0]:
                shortcut_fl = f'{folder_name} - Shortcut.lnk'

                desktop = winshell.desktop()
                path = os.path.join(desktop, shortcut_fl)

                ''' Make 'AppName' using "shortcut maker" protcol '''
                # 'if' -> if shortcut is not found at system desktop, creates it
                # Or 'else' -> skips 'shortcut maker' protocol if the json is found

                target = dir
                wDir = dir
                if os.path.exists(path)== False:
                    # file_name, file_type = os.path.splitext(os.path.basename(os.path.realpath(__file__)))
                    shell = Dispatch('WScript.Shell')
                    shortcut = shell.CreateShortCut(path)
                    shortcut.Targetpath = target
                    shortcut.WorkingDirectory = wDir
                    shortcut.save()
                else:
                    pass
            else:
                pass

    def delay(self,var):
        time.sleep(var)# time self.delay seconnds for each sequence or activities

    def gtts_audios(self,text_val,lang_val,tdl_val,audio_root_val):

        gtts_audios_dl = gTTS(text=text_val,lang=lang_val,slow=False,lang_check=True,tld=tdl_val)

        gtts_audios_dl.save(audio_root_val)

    def apps_log_sys(self,logerr_msg,err_msgtitle,err_msgtxt):

        # Log file details
        log_dirname = "Logs"
        logs_folder_path = os.path.join(cdir,log_dirname)
        logfl_name = f"Log_{dt_date}"
        log_fl = f"{logfl_name}.log"

        try:
            os.makedirs(logs_folder_path)
        except OSError:
            pass
        # logs_folder_path = os.path.join(logdirs6_path,log_dirname6)
        log_err = f"\n<{dt_date}\{dt_time}> , Error: {str(logerr_msg)}\n<________________________________________>\n"
        self.msg_autoClose(msg_text=f"Error cause: \n{str(err_msgtxt)} .                      ",msg_title=err_msgtitle,close_tmr=4,msg_icon=QMessageBox.Critical)

        logfl_path = os.path.join(logs_folder_path,log_fl)
        
        with open(logfl_path,"a") as logfl_w6:
            logfl_w6.writelines(log_err)

    def yn_msgbox(self,txt5,title5,msg_icon):

        # returned_icofl_path = self.icon_fls()

        # print(returned_icofl_path)

        yn_msg = QMessageBox()

        yn_msg.setIcon(msg_icon)

        yn_msg.setIcon(QMessageBox.Warning)

        yn_msg.setText(txt5)
      
        yn_msg.setWindowTitle(title5)
              
        yn_msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        msg_button_out = yn_msg.exec()

        return msg_button_out

    def msg_autoClose(self,msg_title,msg_text,close_tmr,msg_icon):

        qm = QMessageBox()
        qm.setIcon(msg_icon)
        qm.setWindowTitle(msg_title)
        qm.setText(msg_text)
        qm.setStandardButtons(QMessageBox.Ok)
        QTimer.singleShot(close_tmr*1000,lambda : qm.done(0))
        qm.setFixedWidth(800)
        qm.setFixedHeight(1755)
        qm.exec_()

    def icon_fls(self):
        for file in os.listdir(cdir):
    
            # print(file)
            
            if '.ico' in file:
                try:
                    icon_flpath =os.path.join(cdir,file)
                    return icon_flpath
                except OSError:
                    pass
            else:
                pass
    
    def exit(self):

        returned_msg_outs = self.yn_msgbox(txt5="Are you sure you want to exit the app?",title5="Exit -Yes/No:",msg_icon=QMessageBox.Warning)

        if returned_msg_outs == QMessageBox.No:
            pass
        elif returned_msg_outs == QMessageBox.Yes:
            # app = QtWidgets.QApplication(sys.argv)
            # sys.exit(app.exec_())
            sys.exit()
        else:
            pass
    
    def reset(self):
        self.txt_In.setText("")
        self.accent_comboBox.setCurrentText("en") 
        self.tdl_comboBox.setCurrentText("com.au")
    
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = isaUI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
