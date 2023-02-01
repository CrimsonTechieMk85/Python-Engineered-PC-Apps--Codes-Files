import re
from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import winshell
from win32com.client import Dispatch 
import os
import json
import time 
from PySide2.QtCore import QTimer
from PySide2.QtWidgets import QApplication , QMessageBox
from PyQt5.QtWidgets import QFileDialog, QWidget , QInputDialog , QLineEdit
import csv
import mysql.connector
import pandas as pd
import string
import random
import sys
'''Source files'''
# cdir = os.path.dirname(os.path.realpath(__file__))# curent working directory or the 'Now'-location of the file.

cdir = os.getcwd()

# --------------------------------------------------------------------------------------------------

''' Real-Time Date&Time datas '''
# Time
dt_clockH = datetime.datetime.now().strftime("%I")

dt_clockM = datetime.datetime.now().strftime("%M")

dt_clockS = datetime.datetime.now().strftime("%S")

dt_clockMS = datetime.datetime.now().strftime("%f")

epoch_miliseconds = int(time.time() * 1000)

dt_TMR = "{0}:{1}:{2}".format(dt_clockH,dt_clockM,dt_clockS)

dt_time= "{0}:{1}".format(dt_clockH,dt_clockM)

dt_DN = datetime.datetime.now().strftime('%p').lower()

# Date
dt_dd = datetime.datetime.now().strftime("%d")

dt_mm = datetime.datetime.now().strftime("%m")

dt_yyyy = datetime.datetime.now().strftime("%Y")

dt_wdys = datetime.datetime.now().strftime("%A").lower()

dt_mnths = datetime.datetime.now().strftime("%B")

dt_mnths_no = datetime.datetime.now().strftime("%m")

dt_date = "{0}-{1}-{2}".format(dt_dd,dt_mm,dt_yyyy)

dt_mnthsno_mnths = "{0}-{1}".format(dt_mnths_no,dt_mnths)

 
# Current file name infos
'''File name & File extension'''
file_name, file_type = os.path.splitext(os.path.basename(os.path.abspath(__file__)))

''' 1st attempt - Settings file path '''
# 1st [First] attempt - App Json files details
ft_json_name = '{}_datas'.format(file_name)

ft_paths_infos_flname_json= '{}.json'.format(ft_json_name)

ft_path_datas_json_fl_rt = os.path.join(cdir,ft_paths_infos_flname_json)

''' 1st attempt - App Details '''
# 1st [First] attempt - App title ISA
ft_app_title = "I.S.A 1st attempt: mySQ2EXCEL Exporter [X0-{}]".format(file_name)

# 1st [First] attempt - audio folder with app name
ft_main_folder_name = '{} excel files'.format(file_name)

# -----------------------------------------------------------------------------------------


# =======================================================================================\

#                     App infos

# --------------------------------------------------------------------------------
''' Folder names '''
# Audio folder with app name
app_folder_name = 'MySQL2Excel Exporter 3-105 [I.S.A]'
main_folder_name = '{} excel files'.format(app_folder_name)

# -----------------------------------------------------------------------------------------

''' Settings file path '''
# Path json files details
jsonfl1_name = 'path3105_datas'

json_fl1_name = '{}.json'.format(jsonfl1_name)

path_json_fl1_rt = os.path.join(cdir,json_fl1_name)

# Path json files details
jsonfl2_name = 'mySQL3105_datas'

json_fl2_name = '{}.json'.format(jsonfl2_name)

json_fl2_rt = os.path.join(cdir,json_fl2_name)

# App title
app_title = "MySQL 2 Excel: Exporter 3-105 [Improved.Simplified.Alternative]"

# App Version
app_version = "Finalized 93 (version 0.7.2-12)"

# Number leters to be generated
gen_rand_letters_no = 15

# ---------------------------------------------------------------------------

# Key-Value pairs
# Keys
k1 = "mysql_host"
k2 = "mysql_db"
k3 = "mysql_user"
k4 = "mysql_password"
k5 = "mysql_table"

# ------------------------------------------------------------------------------

#-> Log file details
# Logs folder
log_dirname = "Logs"
logs_folder_path = os.path.join(cdir,log_dirname)
# Log files
logfl_name = "Log_{}".format(dt_date)
log_fl = "{}.log".format(logfl_name)
logfl_path = os.path.join(logs_folder_path,log_fl)
        
class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

    # Set APP BG
        self.palette = QtGui.QPalette()
        self.brush = QtGui.QBrush(QtGui.QColor(33, 192, 162))
        self.brush.setStyle(QtCore.Qt.SolidPattern)
        self.palette.setBrush(QtGui.QPalette.Window, self.brush)
        MainWindow.setPalette(self.palette)

    # Set app icon
        returned_icofl_path = self.icon_fls()
        MainWindow.setWindowIcon(QtGui.QIcon(returned_icofl_path))
        
    # Main frame
        self.mainframe = QtWidgets.QFrame(self.centralwidget)
        self.mainframe.setGeometry(QtCore.QRect(10, 10, 781, 561))
        self.mainframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainframe.setObjectName("mainframe")

    # Button frame
        self.btns_frame = QtWidgets.QFrame(self.mainframe)
        self.btns_frame.setGeometry(QtCore.QRect(10, 10, 751, 511))
        self.btns_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.btns_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.btns_frame.setObjectName("btns_frame")

        # -> Export all button
        self.exprt_all_btn = QtWidgets.QPushButton(self.btns_frame)
        self.exprt_all_btn.setGeometry(QtCore.QRect(20, 90, 311, 121))
        font = QtGui.QFont()
        font.setPointSize(45)
        self.exprt_all_btn.setFont(font)
        self.exprt_all_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exprt_all_btn.setObjectName("exprt_all_btn")

        # -> Access button
        self.access_btn_2 = QtWidgets.QPushButton(self.btns_frame)
        self.access_btn_2.setGeometry(QtCore.QRect(390, 300, 351, 121))

        font = QtGui.QFont()
        font.setPointSize(45)
        self.access_btn_2.setFont(font)
        self.access_btn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.access_btn_2.setObjectName("access_btn_2")

        # -> Exit button
        self.exit_btn_3 = QtWidgets.QPushButton(self.btns_frame)
        self.exit_btn_3.setGeometry(QtCore.QRect(20, 300, 311, 121))
        font = QtGui.QFont()
        font.setPointSize(45)
        self.exit_btn_3.setFont(font)
        self.exit_btn_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exit_btn_3.setStatusTip("")
        self.exit_btn_3.setShortcut("")
        self.exit_btn_3.setObjectName("exit_btn_3")

        # -> Export filter button
        self.exprt_filter_btn5 = QtWidgets.QPushButton(self.btns_frame)
        self.exprt_filter_btn5.setGeometry(QtCore.QRect(390, 90, 341, 121))
        font = QtGui.QFont()
        font.setPointSize(45)
        self.exprt_filter_btn5.setFont(font)
        self.exprt_filter_btn5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exprt_filter_btn5.setStatusTip("")
        self.exprt_filter_btn5.setShortcut("")
        self.exprt_filter_btn5.setObjectName("exprt_filter_btn5")

        # Main window
        MainWindow.setCentralWidget(self.centralwidget)

        # Menu bar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        
        # Menu options
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")

        # Settings options
        self.menuSettings = QtWidgets.QMenu(self.menuOptions)
        self.menuSettings.setToolTipsVisible(True)
        self.menuSettings.setObjectName("menuSettings")

        # MySQL DB settings option
        self.menuMySQL_DB_setttings = QtWidgets.QMenu(self.menuSettings)
        self.menuMySQL_DB_setttings.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menuMySQL_DB_setttings.setStatusTip("")
        self.menuMySQL_DB_setttings.setObjectName("menuMySQL_DB_setttings")

        # MySQL account credentails
        self.menuChange_app_s_MySQL_account_credentials = QtWidgets.QMenu(self.menuMySQL_DB_setttings)
        self.menuChange_app_s_MySQL_account_credentials.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menuChange_app_s_MySQL_account_credentials.setObjectName("menuChange_app_s_MySQL_account_credentials")
        MainWindow.setMenuBar(self.menubar)

        # Status bar
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Change path option
        self.actionChange_path = QtWidgets.QAction(MainWindow)
        self.actionChange_path.setObjectName("actionChange_path")

        # Change MySQL user name
        self.actionChange_MySQL_user_name = QtWidgets.QAction(MainWindow)
        self.actionChange_MySQL_user_name.setObjectName("actionChange_MySQL_user_name")

        # Change MySQL user password
        self.actionChnage_MySQL_user_password = QtWidgets.QAction(MainWindow)
        self.actionChnage_MySQL_user_password.setObjectName("actionChnage_MySQL_user_password")

        # Change spp's MySQL DB
        self.actionChange_app_s_MySql_Database_name = QtWidgets.QAction(MainWindow)
        self.actionChange_app_s_MySql_Database_name.setObjectName("actionChange_app_s_MySql_Database_name")
        
        # Change app's MySQL Table
        self.actionChange_app_s_MySQL_Table_name = QtWidgets.QAction(MainWindow)
        self.actionChange_app_s_MySQL_Table_name.setObjectName("actionChange_app_s_MySQL_Table_name")
        
        # Open folder option
        self.menuOpen_folders_3 = QtWidgets.QMenu(MainWindow)
        self.menuOpen_folders_3.setObjectName("menuOpen_folders_3")

        # Open excel files folder
        self.actionOpen_xcelfls_folder = QtWidgets.QAction(MainWindow)
        self.actionOpen_xcelfls_folder.setObjectName("actionOpen_xcelfls_folder")

        # Open log file
        self.actionOpen_Log_file = QtWidgets.QAction(MainWindow)
        self.actionOpen_Log_file.setObjectName("actionOpen_Log_file")

        # Open logs folder
        self.actionOpen_Logs_folder = QtWidgets.QAction(MainWindow)
        self.actionOpen_Logs_folder.setObjectName("actionOpen_Logs_folder")

        # Change_MySQL_user_name - looks\functions
        self.menuChange_app_s_MySQL_account_credentials.addAction(self.actionChange_MySQL_user_name)
        self.menuChange_app_s_MySQL_account_credentials.addSeparator()
        self.menuChange_app_s_MySQL_account_credentials.addAction(self.actionChnage_MySQL_user_password)
        
        # Change_MySQL_DB - looks\functions
        self.menuMySQL_DB_setttings.addAction(self.actionChange_app_s_MySql_Database_name)
        self.menuMySQL_DB_setttings.addSeparator()

        # Change_MySQL_Table - looks\functions
        self.menuMySQL_DB_setttings.addAction(self.actionChange_app_s_MySQL_Table_name)
        self.menuMySQL_DB_setttings.addSeparator()

        # MySQL_DB_setttings - looks\functions
        self.menuMySQL_DB_setttings.addAction(self.menuChange_app_s_MySQL_account_credentials.menuAction())
        self.menuSettings.addAction(self.actionChange_path)
        self.menuSettings.addSeparator()

        # menuSettings - looks\functions
        self.menuSettings.addAction(self.menuMySQL_DB_setttings.menuAction())
        self.menuOptions.addAction(self.menuSettings.menuAction())
        self.menuOptions.addSeparator()

        # menuOptions - looks\functions for Open folder option
        self.menuOptions.addAction(self.menuOpen_folders_3.menuAction())
        self.menuOptions.addSeparator()

        # menuOptions - looks\functions for Open excel files folder option
        self.menuOpen_folders_3.addAction(self.actionOpen_xcelfls_folder)

        # menuOptions - looks\functions for Open logs folder option
        self.menuOpen_folders_3.addAction(self.actionOpen_Logs_folder)

        # menuOptions - looks\functions for Open logs file option
        self.menuOptions.addAction(self.actionOpen_Log_file)

        self.menubar.addAction(self.menuOptions.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", app_title))

        self.mainframe.setStatusTip(_translate("MainWindow",app_version))
        
    # Button
        # Export button
        self.exprt_all_btn.setText(_translate("MainWindow", "Export all"))
        self.exprt_all_btn.setStatusTip(_translate("MainWindow", "Click here to export all records as excel file. (Ctrl+E)"))
        self.exprt_all_btn.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.exprt_all_btn.setStyleSheet("background-color : green; color: white")
        self.exprt_all_btn.clicked.connect(self.mysql2excel_all)
        
        # Access button
        self.access_btn_2.setText(_translate("MainWindow", "Access"))
        self.access_btn_2.setStatusTip(_translate("MainWindow", "Click here to access 'Excel files' folder. (Ctrl+O)"))
        self.access_btn_2.setStyleSheet("background-color : yellow; color: black")
        self.access_btn_2.clicked.connect(self.openfolder)
        
        # Exit button
        self.exit_btn_3.setText(_translate("MainWindow", "Exit"))
        self.exit_btn_3.setShortcut(_translate("MainWindow","Esc"))
        self.exit_btn_3.setStatusTip(_translate("MainWindow", "Click here to exit the app. (Press Esc)"))
        self.exit_btn_3.setStyleSheet("background-color : red; color: white")
        self.exit_btn_3.clicked.connect(self.exit)
        
        # Export filter button
        self.exprt_filter_btn5.setText(_translate("MainWindow", "Export Filter"))
        self.exprt_filter_btn5.setStatusTip(_translate("MainWindow", "Click here to export selected records as excel file. (Ctrl+Shift+E)"))
        self.exprt_filter_btn5.setShortcut(_translate("MainWindow", "Ctrl+Shift+E"))
        self.exprt_filter_btn5.setStyleSheet("background-color : Blue; color: white")
        self.exprt_filter_btn5.clicked.connect(self.mysql2excel_filtered)
        
        
    # Options
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        # self.menuSettings.setToolTip(_translate("MainWindow", "Change app settings"))
        # self.menuSettings.setStatusTip(_translate("MainWindow", "Change app settings"))
        
    # First child option
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuOpen_folders_3.setTitle(_translate("MainWindow", "Access folders"))

        self.actionOpen_Log_file.setText(_translate("MainWindow","Open Log file"))
        self.actionOpen_Log_file.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.actionOpen_Log_file.triggered.connect(self.open_logfl)

        
    # Second child option
        # Open folder (Ctrl+O) option
        self.actionOpen_xcelfls_folder.setText(_translate("MainWindow", "Open 'Excel files' folder"))
        self.actionOpen_xcelfls_folder.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionOpen_xcelfls_folder.triggered.connect(self.openfolder)
      
        # Open Logs folder (Ctrl+O+L) option
        self.actionOpen_Logs_folder.setText(_translate("MainWindow", "Open Logs folder"))
        self.actionOpen_Logs_folder.setShortcut(_translate("MainWindow", "Ctrl+Shift+L"))
        self.actionOpen_Logs_folder.triggered.connect(self.open_logsfolder)

        #-> Change path (Ctrl+P)
        self.actionChange_path.setText(_translate("MainWindow", "Change folder (or Directory)"))
        # self.actionChange_path.setToolTip(_translate("MainWindow", "Change path for '{}' folder".format(main_folder_name)))
        self.actionChange_path.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionChange_path.triggered.connect(self.chngpath)

        # self.menuMySQL_DB_setttings.setToolTip(_translate("MainWindow", "Click here to change app\'s MySQL credentils"))
        self.menuMySQL_DB_setttings.setTitle(_translate("MainWindow", "Change MySQL DB setttings"))
        self.menuChange_app_s_MySQL_account_credentials.setTitle(_translate("MainWindow", "Change app\'s MySQL account credentials"))
        
    # Third child option

        #-> Change app\'s MySQL Database name (Ctrl+Sift+B)
        self.actionChange_app_s_MySql_Database_name.setText(_translate("MainWindow", "Change MySQL Database name"))
        # self.actionChange_app_s_MySql_Database_name.setIconText(_translate("MainWindow", "Change MySQL Database name"))
        # self.actionChange_app_s_MySql_Database_name.setToolTip(_translate("MainWindow", "Change MySQL Database name"))
        self.actionChange_app_s_MySql_Database_name.setText(_translate("MainWindow", "Change app\'s MySQL Database name"))
        self.actionChange_app_s_MySql_Database_name.setShortcut(_translate("MainWindow", "Ctrl+Shift+B"))
        self.actionChange_app_s_MySql_Database_name.triggered.connect(self.chngapp3_mysql_dbname)
        
        # Change app\'s MySQL Table name (Ctrl+Sift+T)
        self.actionChange_app_s_MySQL_Table_name.setText(_translate("MainWindow", "Change MySQL Table name"))
        self.actionChange_app_s_MySQL_Table_name.setText(_translate("MainWindow", "Change app\'s MySQL Table name"))
        self.actionChange_app_s_MySQL_Table_name.setShortcut(_translate("MainWindow", "Ctrl+Shift+T"))
        self.actionChange_app_s_MySQL_Table_name.triggered.connect(self.chngapp3_mysql_tblname)
        
    # Fourth child optiopn

      # Options from Change app\'s MySQL account credentials

        # Change app's MySQL account name
        self.actionChange_MySQL_user_name.setText(_translate("MainWindow", "Change MySQL user name"))
        self.actionChange_MySQL_user_name.setText(_translate("MainWindow", "Change MySQL user name"))
        self.actionChange_MySQL_user_name.setShortcut(_translate("MainWindow", "Ctrl+Shift+U"))
        self.actionChange_MySQL_user_name.triggered.connect(self.chngapp3_mysql_username)
        
        # Change app's MySQL account password
        self.actionChnage_MySQL_user_password.setText(_translate("MainWindow", "Chnage MySQL user password"))
        self.actionChnage_MySQL_user_password.setText(_translate("MainWindow", "Change MySQL user password"))
        self.actionChnage_MySQL_user_password.setShortcut(_translate("MainWindow", "Ctrl+Shift+P"))
        self.actionChnage_MySQL_user_password.triggered.connect(self.chngapp3_mysql_userpasword)

    def apps_log_sys(self,logerr_msg,err_msgtitle,err_msgtxt):

        try:
            os.makedirs(logs_folder_path)
        except OSError:
            pass
        # logs_folder_path = os.path.join(logdirs6_path,log_dirname6)
        log_err = f"\n<{dt_date}\{dt_time}> , Error: {str(logerr_msg)}\n<________________________________________>\n"
        self.msg_autoClose(msg_text=f"Error cause: \n{str(err_msgtxt)} .                      ",msg_title=err_msgtitle,close_tmr=4,msg_icon=QMessageBox.Critical)
        
        with open(logfl_path,"a") as logfl_w6:
            logfl_w6.writelines(log_err)

    def save_mysql(self):

        # Save requiries as a json file
        if os.path.exists(json_fl2_rt)== False:

            while True:
 
                host = QInputDialog(self)
                host.setWindowTitle(r"MySQL Host\IP Address entry:")
                host.setLabelText("Please enter the your system host address (or Ip Address):")
                host.setTextEchoMode(QLineEdit.Normal)
                host.setTextValue("localhost")
                host.setStyleSheet(
                        """
                        
                        QLabel{
                            font-size:20px;
                
                            font-family:Arial;
                        }
                        QLineEdit{
                            font-size:20px;
                            font-family:Arial;
                        }
                        QPushButton{
                            font-size:20px;                         
                        }
                        """
                    )
                host.setFixedSize(400, 240)
                okPressed1 = host.exec_()
                host_txtval1 = host.textValue()

                if okPressed1 and host_txtval1 != '':

                    while True:

                        db = QInputDialog(self)
                    
                        db.setWindowTitle("MySQL user database name entry:")
                        db.setLabelText("Please enter the name of your MySQL database:")
                        db.setTextEchoMode(QLineEdit.Normal)
                        # db.setTextValue("localhost")

                        db.setFixedSize(400, 240)


                        db.setStyleSheet(
                            """
                            
                            QLabel{
                                font-size:20px;
                    
                                font-family:Arial;
                            }
                            QLineEdit{
                                font-size:20px;
                                font-family:Arial;
                            }
                            QPushButton{
                                font-size:20px;                         
                            }
                            """
                        )

                        okPressed2 = db.exec_()
                        db_txtval2 = db.textValue() 
                        
                        if okPressed2 and db_txtval2 != '':

                            while True:
        
                                user_name = QInputDialog(self)
                        
                                user_name.setWindowTitle("MySQL user name entry:")
                                user_name.setLabelText("Please enter your MySQL user name:")
                                user_name.setTextEchoMode(QLineEdit.Normal)
                                user_name.setTextValue("root")

                                user_name.setFixedSize(400, 240)


                                user_name.setStyleSheet(
                                    """
                                    
                                    QLabel{
                                        font-size:20px;
                            
                                        font-family:Arial;
                                    }
                                    QLineEdit{
                                        font-size:20px;
                                        font-family:Arial;
                                    }
                                    QPushButton{
                                        font-size:20px;                         
                                    }
                                    """
                                )

                                okPressed3 = user_name.exec_()
                                usr_name_txtval3 = user_name.textValue() 
                                
                            
                                if okPressed3 and usr_name_txtval3 != '':

                                    while True:

                                        passwrd = QInputDialog(self)
                                
                                        passwrd.setWindowTitle("MySQL user password entry:")
                                        passwrd.setLabelText("Please enter your MySQL password:")
                                        passwrd.setTextEchoMode(QLineEdit.Password)
                        
                                        passwrd.setFixedSize(400, 240)


                                        passwrd.setStyleSheet(
                                            """
                                            
                                            QLabel{
                                                font-size:20px;
                                    
                                                font-family:Arial;
                                            }
                                            QLineEdit{
                                                font-size:20px;
                                                font-family:Arial;
                                            }
                                            QPushButton{
                                                font-size:20px;                         
                                            }
                                            """
                                        )

                                        okPressed4 = passwrd.exec_()
                                        passwrd_txtval4 = passwrd.textValue() 

                                        if okPressed4 and passwrd_txtval4 != '':

                                            while True:

                                                tbl = QInputDialog(self)
                                    
                                                tbl.setWindowTitle("MySQL Table name entry:")
                                                tbl.setLabelText("Please enter the name of your MySQL table:")
                                
                                                tbl.setFixedSize(400, 240)


                                                tbl.setStyleSheet(
                                                    """
                                                    
                                                    QLabel{
                                                        font-size:20px;
                                            
                                                        font-family:Arial;
                                                    }
                                                    QLineEdit{
                                                        font-size:20px;
                                                        font-family:Arial;
                                                    }
                                                    QPushButton{
                                                        font-size:20px;                         
                                                    }
                                                    """
                                                )

                                                okPressed5 = tbl.exec_()
                                                tbl_txtval5 = tbl.textValue() 

                                                if okPressed5 and tbl_txtval5 != '':
                    
                                                    self.mysql_infos_save_json(jsonfl3_path=json_fl2_rt,key1=k1,key2=k2,key3=k3,key4=k4,key5=k5,value1=host_txtval1,value2=db_txtval2.lower(),value3=usr_name_txtval3.lower(),value4=passwrd_txtval4,value5=tbl_txtval5.lower())
                                                    break
                                                elif okPressed5 and tbl_txtval5 == '':
                                                    self.msg_autoClose(msg_text="Invalid input.                        ",msg_title="Input Verifer - Error:",close_tmr=3,msg_icon=QMessageBox.Critical)
                                                else:
                                                    break
                                            
                                            break
                                        elif okPressed4 and passwrd_txtval4 == '':
                                            self.msg_autoClose(msg_text="Invalid input.                        ",msg_title="Input Verifer - Error:",close_tmr=3,msg_icon=QMessageBox.Critical)
                                        else:
                                            break
                                
                                    break
                                elif okPressed3 and usr_name_txtval3 == '':
                                    self.msg_autoClose(msg_text="Invalid input.                        ",msg_title="Input Verifer - Error:",close_tmr=3,msg_icon=QMessageBox.Critical)
                                else:
                                    break
                        
                            break
                        elif okPressed2 and db_txtval2 == '':
                            self.msg_autoClose(msg_text="Invalid input.                        ",msg_title="Input Verifer - Error:",close_tmr=3,msg_icon=QMessageBox.Critical)
                        else:
                            break

                    break
                elif okPressed1 and host_txtval1 == '':
                    self.msg_autoClose(msg_text="Invalid input.                        ",msg_title="Input Verifer - Error:",close_tmr=3,msg_icon=QMessageBox.Critical)
                else:
                    break
        else:
            pass
    
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
            
    def mysql2excel_all(self):
        self.save_path_json()
        # print("Excel made.")

        # - Values - Encrypted
        # v1 = encrypted_mysql_host
        # v2 = encrypted_mysql_db
        # v3 = encrypted_mysql_user
        # v4 = encrypted_mysql_password
        # v5 = "emp_tbl1"

        # - Values - Normal
        # v1 = host_v
        # v2 = db_v
        # v3 = usr_v
        # v4 = passwrd_v
        # v5 = "emp_tbl1"
      
        # pass

        # Random String for 15 letters
        rand_str = ''.join(random.choices(string.ascii_letters, k=gen_rand_letters_no))

        if os.path.exists(path_json_fl1_rt) == True:

            try:

                self.save_mysql()

                if os.path.exists(json_fl2_rt)==True:

                    returned_mysql_host, returned_mysql_db , returned_mysql_user , returned_mysql_password  , returned_mysql_table = self.read_mysql_infos_json(jsonfl_path=json_fl2_rt,key1=k1,key2=k2,key3=k3,key4=k4,key5=k5)

                    self.msg_autoClose(msg_text=f"Started to export the table '{returned_mysql_table}' as excel file.                      ",msg_title="My2Excel Export - Started:",close_tmr=2,msg_icon=QMessageBox.Information)
                            
                    # print(f"\nMySQL _> Host: {returned_mysql_host} | DB: {returned_mysql_db} | User: {returned_mysql_user} | Password: {returned_mysql_password} | Table: {returned_mysql_table}")
                            
                    # Connecting with mySQL DB
                    connection = mysql.connector.connect(host=returned_mysql_host,database=returned_mysql_db,user=returned_mysql_user,password=returned_mysql_password)

                    # Connect with DB & Extract datas
                    cursor = connection.cursor()

                    # Requesting query to get table from mySQL DB
                    sql_q1= "select * from {};".format(returned_mysql_table)
                        
                    # Execute mySQL query
                    cursor.execute(sql_q1)

                    # Fetches\Extracts data based on the query (sql_q)
                    mysql_tbl_data_all = cursor.fetchall()
    
                    # Shows table columns as tuple string
                    # print("\n"+str(mysql_tbl_data_all))

                    # Get column names as list
                    cols_name_lsts = [i[0] for i in cursor.description]

                    # Print columns list element
                    print("\n MySQL Table columns as lists: "+str(cols_name_lsts))

                    l1 = []
                
                    for n in range(0,len(mysql_tbl_data_all),1):
                        # Convert each tuple element into list by appending to empty list (i.e; l1)
                        for row1 in mysql_tbl_data_all:
                            # print(row1[n])
                            l1.append(row1[n])
                        break

                    # Print rows list element
                    # print("\n MySQL Table rows as lists: "+str(l1))

                    # Extracting path (Date folder location) from fintion using return
                    returned_path_dt_date = self.get_json_paths()

                    # Commma seperated file details
                    csvfl1_name = "{0}_{1}_MySQL-CSV".format(returned_mysql_table,returned_mysql_db)

                    csvfl1 = "{}.csv".format(csvfl1_name)

                    csvfl1_path = os.path.join(returned_path_dt_date,csvfl1)

                    # Excel file details
                    xlsxfl2_name = "{0}_{1}_MySQL-Xcel_{2}".format(returned_mysql_table,returned_mysql_db,rand_str)

                    xlsxfl2 = "{}.xlsx".format(xlsxfl2_name)

                    xlsxfl2_path = os.path.join(returned_path_dt_date,xlsxfl2)

                    # Store the mySQL data into CSV (.csv) file
                    with open(csvfl1_path, 'w', newline='') as csvfl_w:
                        # read the CSV file
                        csv_writer = csv.writer(csvfl_w)

                        csv_writer.writerow(cols_name_lsts)

                        # Iterate (Loop) into each row (Having values as list seprated by comma)
                        for row in mysql_tbl_data_all:
                            csv_writer.writerow(row)

                    # print("\n-> MySQL table saved into CSV file.")

                    # Read the csv file
                    pd_r_csv = pd.read_csv(csvfl1_path)

                    # Write the Excel (.xlsx) file
                    pd_w_excel = pd.ExcelWriter(xlsxfl2_path)

                    # saving xlsx file
                    pd_r_csv.to_excel(pd_w_excel, index=False)
                
                    pd_w_excel.save()
                                
                    # Remove the csv file
                    os.remove(csvfl1_path)

                    # print("\n-> CSV into Excel (.xlsx) file.")

                    self.msg_autoClose(msg_text=f"MySQL table '{returned_mysql_table}' sucessfully exported as excel file. \n(Excel file name: {xlsxfl2})                      ",msg_title="My2Excel Export - Success:",close_tmr=6)

                    cursor.close()
                else:
                    pass
            except Exception as err:
                
                self.apps_log_sys(logerr_msg=str(err),err_msgtitle="MySQL2Excel: Exporter - Generic Error:",err_msgtxt=str(err))

        else:
            pass
        
    def mysql2excel_filtered(self):

        self.save_path_json()
        # print("Excel made.")

        # - Values - Encrypted
        # v1 = encrypted_mysql_host
        # v2 = encrypted_mysql_db
        # v3 = encrypted_mysql_user
        # v4 = encrypted_mysql_password
        # v5 = "emp_tbl1"

        # - Values - Normal
        # v1 = host_v
        # v2 = db_v
        # v3 = usr_v
        # v4 = passwrd_v
        # v5 = "emp_tbl1"

        # Random String for 15 letters
        rand_str = ''.join(random.choices(string.ascii_letters, k=gen_rand_letters_no))
      
        # pass
 
        if os.path.exists(path_json_fl1_rt) == True:

            try:
                self.save_mysql()

                if os.path.exists(json_fl2_rt)== True:
                    returned_mysql_host, returned_mysql_db , returned_mysql_user , returned_mysql_password  , returned_mysql_table = self.read_mysql_infos_json(jsonfl_path=json_fl2_rt,key1=k1,key2=k2,key3=k3,key4=k4,key5=k5)

                    # print(f"\nMySQL _> Host: {returned_mysql_host} | DB: {returned_mysql_db} | User: {returned_mysql_user} | Password: {returned_mysql_password} | Table: {returned_mysql_table}")
                        
                    # Connecting with mySQL DB
                    connection = mysql.connector.connect(host=returned_mysql_host,database=returned_mysql_db,user=returned_mysql_user,password=returned_mysql_password)

                    # Connect with DB & Extract datas
                    cursor = connection.cursor()

                    while True:

                        tbl8_cols = QInputDialog(self)
                        tbl8_cols.setWindowTitle("Filter MySQL database - column name entry:")
                        tbl8_cols.setLabelText(f"Please enter the value to be use as filter from '{tbl8_cols_name2_txtval}' column.")
                        tbl8_cols.setTextEchoMode(QLineEdit.Normal)
                        tbl8_cols.setStyleSheet(
                            """
                                QLabel{
                                font-size:20px;
                                font-family:Arial;
                                }
                                QLineEdit{
                                    font-size:20px;
                                    font-family:Arial;
                                    }
                                QPushButton{
                                    font-size:20px;                         
                                    }
                                """
                            )
                        tbl8_cols.resize(400, 240)
                        okPressed8_2 = tbl8_cols.exec_()
                        tbl8_cols_name2_txtval = tbl8_cols.textValue()
                        if okPressed8_2==True and tbl8_cols_name2_txtval != '':

                            filter_conditions_lists = ("=", ">", "<", ">=","<=","!=","BETWEEN","LIKE","IN")
                    
                            filter_conditions_item, ok = QInputDialog.getItem(self, "select conditon:", 
                                        "Condtions used to filter mySQL Table:", filter_conditions_lists, 0, False)
                                        
                            if ok==True and filter_conditions_item:

                                if filter_conditions_item != "BETWEEN":

                                    while True:

                                        tbl9_value = QInputDialog(self)
                                        tbl9_value.setWindowTitle("Filter MySQL database - value name entry:")
                                        tbl9_value.setLabelText(f"Please enter the value to be use as filter from '{tbl8_cols_name2_txtval}' column.")
                                        tbl9_value.setTextEchoMode(QLineEdit.Normal)
                                        tbl9_value.setStyleSheet(
                                            """
                                            QLabel{
                                                font-size:20px;
                                                font-family:Arial;
                                                }
                                            QLineEdit{
                                                font-size:20px;
                                                font-family:Arial;
                                                }
                                            QPushButton{
                                                font-size:20px;                         
                                                }
                                            """
                                            )
                                        tbl9_value.resize(400, 240)
                                        okPressed9_2 = tbl9_value.exec_()
                                        tbl9_txtval = tbl9_value.textValue()

                                        if okPressed9_2==True and tbl9_txtval != '':

                                            self.msg_autoClose(msg_text=f"Started to export the table '{returned_mysql_table}' as excel file.                      ",msg_title="My2Excel Export - Started:",close_tmr=2,msg_icon=QMessageBox.Information)

                                            # Requesting query to get filtered table from mySQL DB
                                            sql_q = "select * from {0} where {1}{2}'{3}';".format(returned_mysql_table,tbl8_cols_name2_txtval,filter_conditions_item,tbl9_txtval)

                                            # print(sql_q1)
                                            
                                            # print(sql_q)
                                            cursor.execute(sql_q)

                                            # Fetches\Extracts data based on the query (sql_q)
                                            mysql_tbl_data_filtered = cursor.fetchall()

                                            # print(str(mysql_tbl_data_filtered))

                                            # Get mySQL column names as list
                                            cols_name_lsts = [i[0] for i in cursor.description]

                                            # Print columns list element
                                            print("\n MySQL Table columns as lists: "+str(cols_name_lsts))
            
                                            l1 = []
                                                
                                            for n in range(0,len(mysql_tbl_data_filtered),1):
                                                # Convert each tuple element into list by appending to empty list (i.e; l1)
                                                for row1 in mysql_tbl_data_filtered:
                                                    # print(row1[n])
                                                    l1.append(row1[n])
                                                break

                                            # Print rows list element
                                            print("\n MySQL Table rows as lists: "+str(l1))

                                            # Extracting path (Date folder location) from fintion using return
                                            returned_path_dt_date = self.get_json_paths()

                                            # print("Returned path: "+returned_path_dt_date)

                                            # Commma seperated file details
                                            csvfl1_name = "{0}_{1}_MySQL-FilteredCSV".format(returned_mysql_table,returned_mysql_db)

                                            csvfl1 = "{}.csv".format(csvfl1_name)

                                            csvfl1_path = os.path.join(returned_path_dt_date,csvfl1)

                                            # Excel file details
                                            xlsxfl2_name = "{0}_{1}_MySQL-FilteredXcel_{2}".format(returned_mysql_table,returned_mysql_db,rand_str)

                                            xlsxfl2 = "{}.xlsx".format(xlsxfl2_name)

                                            xlsxfl2_path = os.path.join(returned_path_dt_date,xlsxfl2)

                                            if len(l1)==0 or len(cols_name_lsts)==0:

                                                self.apps_log_sys(logerr_msg="Data feteched is empty or query is incorrect.",err_msgtitle="MySQL2Excel: Exporter - Result empty or Incorrect Query",err_msgtxt="Data feteched is empty or query is incorrect")

                                            else:

                                                # Store the mySQL data into CSV (.csv) file
                                                with open(csvfl1_path, 'w', newline='') as csvfl_w:
                                                    # read the CSV file
                                                    csv_writer = csv.writer(csvfl_w)

                                                    csv_writer.writerow(cols_name_lsts)

                                                    # Iterate (Loop) into each row (Having values as list seprated by comma)
                                                    for row in mysql_tbl_data_filtered:
                                                        csv_writer.writerow(row)

                                                # print("\n-> MySQL table saved into CSV file.")

                                                # Read the csv file
                                                pd_r_csv = pd.read_csv(csvfl1_path)

                                                # Write the Excel (.xlsx) file
                                                pd_w_excel = pd.ExcelWriter(xlsxfl2_path)

                                                # saving xlsx file
                                                pd_r_csv.to_excel(pd_w_excel, index=False)
                                        
                                                pd_w_excel.save()
                                                        
                                                # Remove the csv file
                                                os.remove(csvfl1_path)

                                                # print("\n-> CSV into Excel (.xlsx) file.")

                                                self.msg_autoClose(msg_text=f"MySQL filtered table '{returned_mysql_table}' sucessfully exported as excel file. \n(Excel file name: {xlsxfl2})                      ",msg_title="My2Excel Export - Success:",close_tmr=3,msg_icon=QMessageBox.Information)

                                                # os.startfile(csvfl1_path)
                                                # os.startfile(xlsxfl2_path)

                                                break

                                        elif okPressed9_2==True and tbl9_txtval == '':
                                            self.msg_autoClose(msg_text="Invalid input.                        ",msg_title="Input Verifer - Error:",close_tmr=3,msg_icon=QMessageBox.Critical)
                                        else:
                                            # pass

                                            break

                                elif filter_conditions_item == "IN" :

                                    while True:
                                    
                                        tbl8_v1 = QInputDialog(self)
                                        tbl8_v1.setWindowTitle("Filter MySQL database - first value entry:")
                                        tbl8_v1.setLabelText("Please type the first value:")
                                        tbl8_v1.setTextEchoMode(QLineEdit.Normal)
                                        tbl8_v1.setStyleSheet(
                                            """
                                            QLabel{
                                                font-size:20px;
                                                font-family:Arial;
                                                }
                                            QLineEdit{
                                                font-size:20px;
                                                font-family:Arial;
                                                }
                                            QPushButton{
                                                font-size:20px;                         
                                                }
                                            """
                                            )
                                        tbl8_v1.resize(400, 240)
                                        tbl8_v1_okPressed1 = tbl8_v1.exec_()
                                        tbl8_first_val1A = tbl8_v1.textValue()

                                        if tbl8_v1_okPressed1==True and tbl8_first_val1A != '':
                                            while True:
                                            
                                                tbl8_v2 = QInputDialog(self)
                                                tbl8_v2.setWindowTitle("Filter MySQL database - second value entry:")
                                                tbl8_v2.setLabelText("Please type the second value or cancel to only use the first value:")
                                                tbl8_v2.setTextEchoMode(QLineEdit.Normal)
                                                tbl8_v2.setStyleSheet(
                                                    """
                                                    QLabel{
                                                        font-size:20px;
                                                        font-family:Arial;
                                                        }
                                                    QLineEdit{
                                                        font-size:20px;
                                                        font-family:Arial;
                                                        }
                                                    QPushButton{
                                                        font-size:20px;                         
                                                        }
                                                    """
                                                    )
                                                tbl8_v2.resize(400, 240)
                                                tbl8_v2_okPressed2 = tbl8_v2.exec_()
                                                tbl8_second_val1B = tbl8_v2.textValue()
                                                if tbl8_v2_okPressed2==True and tbl8_second_val1B != '':
                                                    self.msg_autoClose(msg_text=f"Started to export the table '{returned_mysql_table}' as excel file.                      ",msg_title="My2Excel Export - Started:",close_tmr=2,msg_icon=QMessageBox.Information)

                                                    sql_q = "select * from {0} WHERE {1} IN ({2} , {3});".format(returned_mysql_table,tbl8_cols_name2_txtval,tbl8_first_val1A,tbl8_second_val1B)
                                                    
                                                    # Execute mySQL query
                                                    cursor.execute(sql_q)

                                                    # Fetches\Extracts data based on the query (sql_q)
                                                    mysql_tbl_data_filtered = cursor.fetchall()                                       

                                                    print(str(mysql_tbl_data_filtered))

                                                    # Get mySQL column names as list
                                                    cols_name_lsts = [i[0] for i in cursor.description]

                                                    # Print columns list element
                                                    print("\n MySQL Table columns as lists: "+str(cols_name_lsts))
                    
                                                    l1 = []
                                                        
                                                    for n in range(0,len(mysql_tbl_data_filtered),1):
                                                        # Convert each tuple element into list by appending to empty list (i.e; l1)
                                                        for row1 in mysql_tbl_data_filtered:
                                                            # print(row1[n])
                                                            l1.append(row1[n])
                                                        break
                                                        
                                                    # Print rows list element
                                                    # print("\n MySQL Table rows as lists: "+str(l1))

                                                    # Extracting path (Date folder location) from fintion using return
                                                    returned_path_dt_date = self.get_json_paths()

                                                    # Commma seperated file details
                                                    csvfl1_name = "{0}_{1}_MySQL-FilteredCSV".format(returned_mysql_table,returned_mysql_db)

                                                    csvfl1 = "{}.csv".format(csvfl1_name)

                                                    csvfl1_path = os.path.join(returned_path_dt_date,csvfl1)

                                                    # Excel file details
                                                    xlsxfl2_name = "{0}_{1}_MySQL-FilteredXcel_{2}".format(returned_mysql_table,returned_mysql_db,rand_str)

                                                    xlsxfl2 = "{}.xlsx".format(xlsxfl2_name)

                                                    xlsxfl2_path = os.path.join(returned_path_dt_date,xlsxfl2)


                                                    if len(l1)==0 or len(cols_name_lsts)==0:

                                                        self.apps_log_sys(logerr_msg="Data feteched is empty or query is incorrect.",err_msgtitle="MySQL2Excel: Exporter - Result empty or Incorrect Query",err_msgtxt="Data feteched is empty or query is incorrect")

                                                    else:

                                                        # Store the mySQL data into CSV (.csv) file
                                                        with open(csvfl1_path, 'w', newline='') as csvfl_w:
                                                            # read the CSV file
                                                            csv_writer = csv.writer(csvfl_w)

                                                            csv_writer.writerow(cols_name_lsts)

                                                            # Iterate (Loop) into each row (Having values as list seprated by comma)
                                                            for row in mysql_tbl_data_filtered:
                                                                csv_writer.writerow(row)

                                                        # print("\n-> MySQL table saved into CSV file.")

                                                        # Read the csv file
                                                        pd_r_csv = pd.read_csv(csvfl1_path)

                                                        # Write the Excel (.xlsx) file
                                                        pd_w_excel = pd.ExcelWriter(xlsxfl2_path)

                                                        # saving xlsx file
                                                        pd_r_csv.to_excel(pd_w_excel, index=False)
                                                
                                                        pd_w_excel.save()
                                                                
                                                        # Remove the csv file
                                                        os.remove(csvfl1_path)

                                                        # print("\n-> CSV into Excel (.xlsx) file.")

                                                        self.msg_autoClose(msg_text=f"MySQL filtered table '{returned_mysql_table}' sucessfully exported as excel file. \n(Excel file name: {xlsxfl2})                      ",msg_title="My2Excel Export - Success:",close_tmr=3,msg_icon=QMessageBox.Information)

                                                        break
                                                elif tbl8_v2_okPressed2==False and tbl8_second_val1B != '':
                                                    self.msg_autoClose(msg_text=f"Started to export the table '{returned_mysql_table}' as excel file.                      ",msg_title="My2Excel Export - Started:",close_tmr=2,msg_icon=QMessageBox.Information)

                                                    sql_q = "select * from {0} WHERE {1} IN ({2});".format(returned_mysql_table,tbl8_cols_name2_txtval,tbl8_first_val1A)

                                                    # Execute mySQL query
                                                    cursor.execute(sql_q)

                                                    # Fetches\Extracts data based on the query (sql_q)
                                                    mysql_tbl_data_filtered = cursor.fetchall() 

                                                    # Get mySQL column names as list
                                                    cols_name_lsts = [i[0] for i in cursor.description]

                                                    # Print columns list element
                                                    print("\n MySQL Table columns as lists: "+str(cols_name_lsts))

                                                    l1 = []
                                            
                                                    for n in range(0,len(mysql_tbl_data_filtered),1):
                                                        # Convert each tuple element into list by appending to empty list (i.e; l1)
                                                        for row1 in mysql_tbl_data_filtered:
                                                            # print(row1[n])
                                                            l1.append(row1[n])
                                                        break

                                                    # Print rows list element
                                                    # print("\n MySQL Table rows as lists: "+str(l1))

                                                    # Extracting path (Date folder location) from fintion using return
                                                    returned_path_dt_date = self.get_json_paths()

                                                    # Commma seperated file details
                                                    csvfl1_name = "{0}_{1}_MySQL-FilteredCSV".format(returned_mysql_table,returned_mysql_db)

                                                    csvfl1 = "{}.csv".format(csvfl1_name)

                                                    csvfl1_path = os.path.join(returned_path_dt_date,csvfl1)

                                                    # Excel file details
                                                    xlsxfl2_name = "{0}_{1}_MySQL-FilteredXcel_{2}".format(returned_mysql_table,returned_mysql_db,rand_str)

                                                    xlsxfl2 = "{}.xlsx".format(xlsxfl2_name)

                                                    xlsxfl2_path = os.path.join(returned_path_dt_date,xlsxfl2)

                                                    if len(l1)==0 or len(cols_name_lsts)==0:

                                                        self.apps_log_sys(logerr_msg="Data feteched is empty or query is incorrect.",err_msgtitle="MySQL2Excel: Exporter - Result empty or Incorrect Query",err_msgtxt="Data feteched is empty or query is incorrect")

                                                    else:

                                                        # Store the mySQL data into CSV (.csv) file
                                                        with open(csvfl1_path, 'w', newline='') as csvfl_w:
                                                            # read the CSV file
                                                            csv_writer = csv.writer(csvfl_w)

                                                            csv_writer.writerow(cols_name_lsts)

                                                            # Iterate (Loop) into each row (Having values as list seprated by comma)
                                                            for row in mysql_tbl_data_filtered:
                                                                csv_writer.writerow(row)

                                                        # print("\n-> MySQL table saved into CSV file.")

                                                        # Read the csv file
                                                        pd_r_csv = pd.read_csv(csvfl1_path)

                                                        # Write the Excel (.xlsx) file
                                                        pd_w_excel = pd.ExcelWriter(xlsxfl2_path)

                                                        # saving xlsx file
                                                        pd_r_csv.to_excel(pd_w_excel, index=False)
                                                
                                                        pd_w_excel.save()
                                                                
                                                        # Remove the csv file
                                                        os.remove(csvfl1_path)

                                                        # print("\n-> CSV into Excel (.xlsx) file.")

                                                        self.msg_autoClose(msg_text=f"MySQL filtered table '{returned_mysql_table}' sucessfully exported as excel file. (Excel file name: {xlsxfl2})                      ",msg_title="My2Excel Export - Success:",close_tmr=6)

                                                        break  
                                                elif tbl8_v2_okPressed2==True and tbl8_second_val1B == '':
                                                    self.msg_autoClose(msg_text="Invalid input.                        ",msg_title="Input Verifer - Error:",close_tmr=3,msg_icon=QMessageBox.Critical)
                                                else:
                                                    # pass
                                                    break
                                            
                                        elif tbl8_v1_okPressed1==True and tbl8_first_val1A == '':
                                            self.msg_autoClose(msg_text="Invalid input.                        ",msg_title="Input Verifer - Error:",close_tmr=3,msg_icon=QMessageBox.Critical)
                                        else:
                                            # pass
                                            break
                                        
                                else:
                                    while True:

                                        tbl8_cond1 = QInputDialog(self)
                                        tbl8_cond1.setWindowTitle( "Filter MySQL database - first value entry:")
                                        tbl8_cond1.setLabelText("Please type the first value:")
                                        tbl8_cond1.setTextEchoMode(QLineEdit.Normal)
                                        tbl8_cond1.setStyleSheet(
                                                """
                                                QLabel{
                                                    font-size:20px;
                                                    font-family:Arial;
                                                    }
                                                QLineEdit{
                                                    font-size:20px;
                                                    font-family:Arial;
                                                    }
                                                QPushButton{
                                                    font-size:20px;                         
                                                    }
                                                """
                                                )
                                        tbl8_cond1.resize(400, 240)
                                        tbl8_cond1_okPressed = tbl8_cond1.exec_()
                                        tbl8_cond1_txtval = tbl8_cond1.textValue()

                                        if tbl8_cond1_okPressed==True and tbl8_cond1_txtval != '':

                                            while True:
                                        
                                                tbl8_cond2 = QInputDialog(self)
                                                tbl8_cond2.setWindowTitle( "Filter MySQL database - first value entry:")
                                                tbl8_cond2.setLabelText("Please type the first value:")
                                                tbl8_cond2.setTextEchoMode(QLineEdit.Normal)
                                                tbl8_cond2.setStyleSheet(
                                                        """
                                                        QLabel{
                                                            font-size:20px;
                                                            font-family:Arial;
                                                            }
                                                        QLineEdit{
                                                            font-size:20px;
                                                            font-family:Arial;
                                                            }
                                                        QPushButton{
                                                            font-size:20px;                         
                                                            }
                                                        """
                                                        )
                                                tbl8_cond2.resize(400, 240)
                                                tbl8_cond2_okPressed3 = tbl8_cond2.exec_()
                                                tbl8_cond2_txtval= tbl8_cond2.textValue()
                                                if tbl8_cond2_okPressed3 and tbl8_cond2_txtval != '':
                                                    self.msg_autoClose(msg_text=f"Started to export the table '{returned_mysql_table}' as excel file.                      ",msg_title="My2Excel Export - Started:",close_tmr=2,msg_icon=QMessageBox.Information)

                                                    sql_q = "select * from {0} WHERE {1} BETWEEN {2} AND {3};".format(returned_mysql_table,tbl8_cols_name2_txtval,tbl8_cond1_txtval,tbl8_cond2_txtval)
                                                    
                                                    # Execute mySQL query
                                                    cursor.execute(sql_q)

                                                    # Fetches\Extracts data based on the query (sql_q)
                                                    mysql_tbl_data = cursor.fetchall()

                                                    # Get MySQL column name as list
                                                    cols_name_lsts = [i[0] for i in cursor.description]

                                                    # Print columns list element
                                                    print("\n MySQL Table columns as lists: "+str(cols_name_lsts))
                
                                                    l1 = []
                                            
                                                    for n in range(0,len(mysql_tbl_data),1):
                                                        # Convert each tuple element into list by appending to empty list (i.e; l1)
                                                        for row1 in mysql_tbl_data:
                                                            # print(row1[n])
                                                            l1.append(row1[n])
                                                        break

                                                    # Print rows list element
                                                    # print("\n MySQL Table rows as lists: "+str(l1))

                                                    # Extracting path (Date folder location) from fintion using return
                                                    returned_path_dt_date = self.get_json_paths()

                                                    # Commma seperated file details
                                                    csvfl1_name = "{0}_{1}_MySQL-FilteredCSV".format(returned_mysql_table,returned_mysql_db)

                                                    csvfl1 = "{}.csv".format(csvfl1_name)

                                                    csvfl1_path = os.path.join(returned_path_dt_date,csvfl1)

                                                    # Excel file details
                                                    xlsxfl2_name = "{0}_{1}_MySQL-FilteredXcel_{2}".format(returned_mysql_table,returned_mysql_db,rand_str)

                                                    xlsxfl2 = "{}.xlsx".format(xlsxfl2_name)

                                                    xlsxfl2_path = os.path.join(returned_path_dt_date,xlsxfl2)

                                                    if len(l1)==0 or len(cols_name_lsts)==0:

                                                        self.apps_log_sys(logerr_msg="Data feteched is empty or query is incorrect.",err_msgtitle="MySQL2Excel: Exporter - Result empty or Incorrect Query",err_msgtxt="Data feteched is empty or query is incorrect")

                                                    else:

                                                        # Store the mySQL data into CSV (.csv) file
                                                        with open(csvfl1_path, 'w', newline='') as csvfl_w:
                                                            # read the CSV file
                                                            csv_writer = csv.writer(csvfl_w)

                                                            csv_writer.writerow(cols_name_lsts)

                                                            # Iterate (Loop) into each row (Having values as list seprated by comma)
                                                            for row in mysql_tbl_data_filtered:
                                                                csv_writer.writerow(row)

                                                                # print("\n-> MySQL table saved into CSV file.")

                                                            # Read the csv file
                                                            pd_r_csv = pd.read_csv(csvfl1_path)

                                                            # Write the Excel (.xlsx) file
                                                            pd_w_excel = pd.ExcelWriter(xlsxfl2_path)

                                                            # saving xlsx file
                                                            pd_r_csv.to_excel(pd_w_excel, index=False)
                                                
                                                            pd_w_excel.save()
                                                                
                                                            # Remove the csv file
                                                            os.remove(csvfl1_path)

                                                            # print("\n-> CSV into Excel (.xlsx) file.")

                                                            self.msg_autoClose(msg_text=f"MySQL filtered table '{returned_mysql_table}' sucessfully exported as excel file. (Excel file name: {xlsxfl2})                      ",msg_title="My2Excel Export - Success:",close_tmr=2,msg_icon=QMessageBox.Information)

                                                            break
                                                elif tbl8_cond2_okPressed3 and tbl8_cond2_txtval == '':
                                                    self.msg_autoClose(msg_text="Invalid input.                        ",msg_title="Input Verifer - Error:",close_tmr=3,msg_icon=QMessageBox.Critical)
                                                else:
                                                    # pass
                                                    break
                                        elif tbl8_cond1_okPressed==True and tbl8_cond1_txtval == '':
                                            self.msg_autoClose(msg_text="Invalid input.                        ",msg_title="Input Verifer - Error:",close_tmr=3,msg_icon=QMessageBox.Critical)
                                        else:
                                            # pass
                                            break
                            else:
                                pass

                        elif okPressed8_2==True and tbl8_cols_name2_txtval == '':
                            self.msg_autoClose(msg_text="Invalid input.                        ",msg_title="Input Verifer - Error:",close_tmr=3,msg_icon=QMessageBox.Critical)
                            
                        elif okPressed8_2==False and tbl8_cols_name2_txtval == '':
                            pass
                            break
                        else:
                            # self.msg_autoClose(msg_text=f"MySQL2Excel: Exporter failed, cause: {returned_mysql_table} mySQL table already exported as excel file. \n  (Excel file name: {xlsxfl2})                      ",msg_title="My2Excel Export - Failed:",close_tmr=6)
                            pass
                            break
                    cursor.close()

                else:
                    pass
            except Exception as err:

                self.apps_log_sys(logerr_msg=str(err),err_msgtitle="MySQL2Excel: Exporter - Generic Error:",err_msgtxt=str(err))
            
        else:
            pass
    
    def mysql_infos_save_json(self,jsonfl3_path,key1,value1,key2,value2,key3,value3,key4,value4,key5,value5):

        infos = {
            key1:value1,
            key2:value2,
            key3:value3,
            key4:value4,
            key5:value5
    
        }
        with open(jsonfl3_path,'w') as jsonfl3_w:
            json.dump(infos,jsonfl3_w)

        self.msg_autoClose(msg_text="Thank you for your kind co-operation. MySQL credentails saved and ready to use.                        ",msg_title="MySQL credentails update - Complete:",close_tmr=2,msg_icon=QMessageBox.Information)
           
    def open_logsfolder(self):

        try:
            os.makedirs(logs_folder_path)
        except OSError:
            pass

        os.startfile(logs_folder_path)

    def open_logfl(self):

        try:
            os.makedirs(logs_folder_path)
        except OSError:
            pass

        if os.path.exists(log_fl)==False:
            with open(logfl_path,"w",encoding="utf-8") as logfl_w6:
                logfl_w6.writable()
        else:
            pass

        os.startfile(logfl_path) 

    def read_mysql_infos_json(self,jsonfl_path,key1,key2,key3,key4,key5):

        jsonfl_r = open(jsonfl_path,'r')

        json_data = jsonfl_r.read()

        json_v1 = json.loads(json_data)[key1] 
        json_v2 = json.loads(json_data)[key2] 
        json_v3 = json.loads(json_data)[key3] 
        json_v4 = json.loads(json_data)[key4] 
        json_v5 = json.loads(json_data)[key5]

        jsonfl_r.close()

        return json_v1, json_v2, json_v3, json_v4, json_v5

    def foldershortcut_maker_dt(self,path1,path2,path3,path4):

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
        # ft_path = os.path.join(desktop, '{} - Shortcut.lnk'.format(ft_main_folder_name))
        path = os.path.join(desktop, '{} - Shortcut.lnk'.format(main_folder_name))
        
        target_rt = path1
        wDir_rt = path1
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = target_rt
        shortcut.WorkingDirectory = wDir_rt
        shortcut.save()

    def delay(self,var):
        time.sleep(var) 

    def msg_autoClose(self,msg_title,msg_text,close_tmr,msg_icon):

        qm = QMessageBox()
        qm.setIcon(msg_icon)
        qm.setWindowTitle(msg_title)
        qm.setText(msg_text)
        qm.setStandardButtons(QMessageBox.Ok)
        QTimer.singleShot(close_tmr*1000,lambda : qm.done(0))
        qm.setFixedWidth(800+len(msg_text))
        qm.setFixedHeight(1755+len(msg_title))
        qm.exec_()
        
    def read_path_json(self,jsonfl_path1,k1):
        with open(jsonfl_path1,'r') as pathjson_fl_r:
            data = pathjson_fl_r.read()

            path_infos_v = json.loads(data)[k1]

        return path_infos_v  

    def json_write_infos(self,json_flpath1,keys1,val1):

        infos = {
            keys1: str(val1)

                            }
        with open(json_flpath1,'w') as json_fl_w:
            json.dump(infos,json_fl_w)

    def json_mysql_update_infos(self,json_flpath2,keys2,info,msg_txt2,msg_title2):

        with open(json_flpath2,'r') as json_data_r:
            json_src_data = json.load(json_data_r)

            json_src_data[keys2] = info

            with open(json_flpath2,'w') as json_fl_w:
                json.dump(json_src_data,json_fl_w)

        self.msg_autoClose(msg_text=msg_txt2+"                        ",msg_title=msg_title2,close_tmr=3,msg_icon=QMessageBox.Information)
        
    def json_update_infos(self,json_flpath3,keys3,info3):

        with open(json_flpath3,'r') as json_data_r:
            json_src_data = json.load(json_data_r)

            json_src_data[keys3] = info3

            with open(json_flpath3,'w') as json_fl_w:
                json.dump(json_src_data,json_fl_w)

    def chngapp3_mysql_host(self):

        while True:

            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(17)

            host2_v1 = QInputDialog(self)
            host2_v1.setWindowTitle("Modify app's MySQL Host:")
            host2_v1.setLabelText("Please enter the new MySQL host to be changed:")
            host2_v1.setTextValue("root")
            host2_v1.setTextEchoMode(QLineEdit.Normal)
            host2_v1.setStyleSheet(
                                """
                                
                                QLabel{
                                    font-size:20px;
                        
                                    font-family:Arial;
                                }
                                QLineEdit{
                                    font-size:20px;
                                    font-family:Arial;
                                }
                                QPushButton{
                                    font-size:20px;                         
                                }
                                """
                            )
            host2_v1.resize(400, 240)
            host2_v1_txt = host2_v1.textValue()
            okPressed1_2 = host2_v1.exec_()

            # host2_v1, okPressed1_2 = QInputDialog.getText(self, "Get MySQL Host","Please enter the name of your MySQL host:", QLineEdit.Normal, "localhost")

            if okPressed1_2==True and host2_v1_txt != '':

                if os.path.exists(json_fl2_rt)==True:

                    self.json_mysql_update_infos(json_flpath2=json_fl2_rt,info=str(host2_v1_txt),keys2=k1,msg_title2="MySQL host update - Complete:",msg_txt2="MySQL host succesfully changed.")
            
                    break
                else:
                    self.msg_autoClose(msg_text="Opps! Sorry, could not update\modify MySQL credentails. Seeking alternative....                                                  ",msg_title="MySQL change - Error:",close_tmr=2,msg_icon=QMessageBox.Critical)

                    self.save_mysql()
            elif okPressed1_2==True and host2_v1_txt == '':
                self.msg_autoClose(msg_text="Invalid input.                        ",msg_title="Input Verifer - Error:",close_tmr=3,msg_icon=QMessageBox.Critical)
            elif okPressed1_2==False and host2_v1_txt == '':
                break
            elif okPressed1_2==False and host2_v1_txt != '':
                break
            else:
                pass

        # print("\n_> MySQL: Host changed.")
    
    def chngapp3_mysql_username(self):

        while True:

            usr2_v3 = QInputDialog(self)
            usr2_v3.setWindowTitle("Modify app's MySQL user:")
            usr2_v3.setLabelText("Please enter new MySQL user name to be changed:")
            usr2_v3.setTextValue("root")
            usr2_v3.setTextEchoMode(QLineEdit.Normal)
            usr2_v3.setStyleSheet(
                """
                QLabel{
                    font-size:20px;
                    font-family:Arial;
                    }
                QLineEdit{
                    font-size:20px;
                    font-family:Arial;
                    }
                QPushButton{
                    font-size:20px;                         
                    }
                """
                )
            usr2_v3.resize(400, 240)
            usr2_v3_txt = usr2_v3.textValue()
            okPressed3_2 = usr2_v3.exec_()
            
            if okPressed3_2==True and usr2_v3_txt != '':

                if os.path.exists(json_fl2_rt)==True:
                    
                    self.json_mysql_update_infos(json_flpath2=json_fl2_rt,info=usr2_v3_txt.lower(),keys2=k3,msg_title2="MySQL user update - Complete:",msg_txt2="MySQL host succesfully changed.")

                    break
                else:
                    self.msg_autoClose(msg_text="Opps! Sorry, could not update\modify MySQL credentails. Seeking alternative....                                                  ",msg_title="MySQL change - Error:",close_tmr=3,msg_icon=QMessageBox.Critical)

                    self.save_mysql()
            elif okPressed3_2==True and usr2_v3_txt == '':
                self.msg_autoClose(msg_text="Invalid input.                        ",msg_title="Input Verifer - Error:",close_tmr=3,msg_icon=QMessageBox.Critical)
            elif okPressed3_2==False and usr2_v3_txt == '':
                break
            elif okPressed3_2==False and usr2_v3_txt != '':
                break
            else:
                pass
        
        # print("\n_> MySQL: User name changed.")

    def chngapp3_mysql_userpasword(self):

        while True:
    
            passwrd2_v4 = QInputDialog(self)
            passwrd2_v4.setWindowTitle("Modify app's MySQL password:")
            passwrd2_v4.setLabelText("Please enter new MySQL password to be changed:")
            passwrd2_v4.setTextEchoMode(QLineEdit.Password)
            passwrd2_v4.setStyleSheet(
                """
                QLabel{
                    font-size:20px;
                    font-family:Arial;
                    }
                QLineEdit{
                    font-size:20px;
                    font-family:Arial;
                    }
                QPushButton{
                    font-size:20px;                         
                    }
                """
                )
            passwrd2_v4.resize(400, 240)
            okPressed4_2 = passwrd2_v4.exec_()
            passwrd2_v4_txt = passwrd2_v4.textValue()
        
  
            if okPressed4_2==True and passwrd2_v4_txt != '':

                if os.path.exists(json_fl2_rt)==True:

                    self.json_mysql_update_infos(json_flpath2=json_fl2_rt,info=passwrd2_v4,keys2=k4,msg_title2="MySQL user update - Complete:",msg_txt2="MySQL user succesfully changed.")
                
                    break
                else:
                    self.msg_autoClose(msg_text="Opps! Sorry, could not update\modify MySQL credentails. Seeking alternative....                                                  ",msg_title="MySQL change - Error:",close_tmr=6)

                    self.save_mysql()
            elif okPressed4_2==True and passwrd2_v4_txt == '':
                self.msg_autoClose(msg_text="Invalid input.                        ",msg_title="Input Verifer - Error:",close_tmr=3,msg_icon=QMessageBox.Critical)
            elif okPressed4_2==False and passwrd2_v4_txt == '':
                break
            else:
                pass
          
        # print("\n_> MySQL: Password changed.")

    def chngapp3_mysql_tblname(self):
          
        while True:
        
            tbl2_v5 = QInputDialog(self)
            tbl2_v5.setWindowTitle("Modify app's MySQL table:")
            tbl2_v5.setLabelText("Please enter new MySQL table to name be changed:")
            tbl2_v5.setTextEchoMode(QLineEdit.Normal)
            tbl2_v5.setStyleSheet(
                """
                QLabel{
                    font-size:20px;
                    font-family:Arial;
                    }
                QLineEdit{
                    font-size:20px;
                    font-family:Arial;
                    }
                QPushButton{
                    font-size:20px;                         
                    }
                """
                )
            tbl2_v5.resize(400, 240)
            okPressed5_2 = tbl2_v5.exec_()
            tbl2_v5_txt = tbl2_v5.textValue()
                # tbl2_v5, okPressed5_2 = QInputDialog.getText(self, "Modify app's MySQL table:","Please enter the name of your MySQL table:", QLineEdit.Normal, "")
            
            if okPressed5_2 and tbl2_v5_txt != '':
                if os.path.exists(json_fl2_rt)==True:

                    self.json_mysql_update_infos(json_flpath2=json_fl2_rt,info=tbl2_v5_txt.lower(),keys2=k5,msg_title2="MySQL table update - Complete:",msg_txt2="MySQL table succesfully changed.")

                    break
                else:
                    self.msg_autoClose(msg_text="Opps! Sorry, could not update\modify MySQL credentails. Seeking alternative....                                                  ",msg_title="MySQL change - Error:",close_tmr=6)

                    self.save_mysql()
            elif okPressed5_2==True and tbl2_v5_txt == '':
                self.msg_autoClose(msg_text="Invalid input.                        ",msg_title="Input Verifer - Error:",close_tmr=3,msg_icon=QMessageBox.Critical)
            
            elif okPressed5_2==False and tbl2_v5_txt == '':
                break
            else:
                pass

        # print("\n_> MySQL: Table name changed.")

    def chngapp3_mysql_dbname(self):

        while True:
 
            db2 = QInputDialog(self)
            db2.setWindowTitle("Modify app's MySQL database:")
            db2.setLabelText("Please enter new MySQL database to be changed:")
            db2.setTextEchoMode(QLineEdit.Normal)
            db2.setStyleSheet(
                """
                QLabel{
                    font-size:20px;
                    font-family:Arial;
                    }
                QLineEdit{
                    font-size:20px;
                    font-family:Arial;
                    }
                QPushButton{
                    font-size:20px;                         
                    }
                """
                )
            db2.resize(400, 240)
            okPressed2_2 = db2.exec_()
            db2_v2_txt = db2.textValue()

            # db2_v2, okPressed2_2 = QInputDialog.getText(self, "Modify app's MySQL database:","Please enter the name of your MySQL database:", QLineEdit.Normal, "")

            if okPressed2_2==True and db2_v2_txt != '':
                if os.path.exists(json_fl2_rt)==True:
 
                    self.json_mysql_update_infos(json_flpath2=json_fl2_rt,info=db2_v2_txt.lower(),keys2=k2,msg_title2="MySQL data base update - Complete:",msg_txt2="MySQL data base succesfully changed.")

                    break
                else:
                    self.msg_autoClose(msg_text="Opps! Sorry, could not update\modify MySQL credentails. Seeking alternative....                                                  ",msg_title="MySQL update - Error:",close_tmr=6)

                    self.save_mysql()
            elif okPressed2_2==True and db2_v2_txt == '':
                self.msg_autoClose(msg_text="Invalid input.                        ",msg_title="Input Verifer - Error:",close_tmr=2,msg_icon=QMessageBox.Critical)
            elif okPressed2_2==False and db2_v2_txt == '':
                break
            else:
                pass
        # pass

        # print("\n_> MySQL: DB name changed.")


    def exit(self):

        # returned_icofl_path = self.icon_fls()

        # print(returned_icofl_path)

        w_yn_msg = QMessageBox()

        w_yn_msg.setIcon(QMessageBox.Warning)
       
        w_yn_msg.setText("Are you sure you want to exit the app?")
      
        w_yn_msg.setWindowTitle("Exit -Yes/No:")
      
        w_yn_msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        w_msg_returnValue = w_yn_msg.exec()

        if w_msg_returnValue == QMessageBox.No:
            pass
        elif w_msg_returnValue == QMessageBox.Yes:
            # app = QtWidgets.QApplication(sys.argv)
            # sys.exit(app.exec_())
            sys.exit()
        else:
            pass

    def openfolder(self):
        """ Verify '.json' if exists or not """
        path_json_fl1_exists = os.path.exists(path_json_fl1_rt)

        if path_json_fl1_exists == False:
            
            dir_dialog_title = "Please choose folder (or directory) to hold '{}' folder:".format(main_folder_name)
            dir_dlgbox = QFileDialog.getExistingDirectory(self, caption=dir_dialog_title)
           
            if dir_dlgbox:

                usr_rt_v = dir_dlgbox.replace("/","\\")

                self.json_write_infos(json_flpath1=path_json_fl1_rt,keys1="path",val1=usr_rt_v)

                self.msg_autoClose(msg_text="Path saved successfully.                        ",msg_title="Path save - Complete:",close_tmr=2,msg_icon=QMessageBox.Information)

                #sys.exit()
            else:
                pass
        else:
            pass

        try:

            returned_path = self.read_path_json(jsonfl_path1=path_json_fl1_rt,k1="path")

            # print(f'Returned path: {returned_path}')
            # App main folder path 
            app_main_folder_v = os.path.join(returned_path,main_folder_name)

            # Current year folder path 
            now_yrs_sub_folder_v = os.path.join(app_main_folder_v,dt_yyyy)

            # Current month number-month folder path 
            now_mnthsno_mnths_sub_folder_v = os.path.join(now_yrs_sub_folder_v,dt_mnthsno_mnths)

            # Current date folder path '''
            now_date_sub_folder_v = os.path.join(now_mnthsno_mnths_sub_folder_v,dt_date)

            self.foldershortcut_maker_dt(path1=app_main_folder_v,path3=now_mnthsno_mnths_sub_folder_v,path4=now_date_sub_folder_v,path2=now_yrs_sub_folder_v)
        
            os.startfile(now_date_sub_folder_v)

        except FileNotFoundError:
            pass

    def get_json_paths(self):

        try:

            returned_path = self.read_path_json(jsonfl_path1=path_json_fl1_rt,k1="path")

            # App main folder path 
            app_main_folder_v = os.path.join(returned_path,main_folder_name)

            # Current year folder path 
            now_yrs_sub_folder_v = os.path.join(app_main_folder_v,dt_yyyy)

            # Current month number-month folder path 
            now_mnthsno_mnths_sub_folder_v = os.path.join(now_yrs_sub_folder_v,dt_mnthsno_mnths)

            # Current date folder path '''
            now_date_sub_folder_v = os.path.join(now_mnthsno_mnths_sub_folder_v,dt_date)

            self.foldershortcut_maker_dt(path1=app_main_folder_v,path3=now_mnthsno_mnths_sub_folder_v,path4=now_date_sub_folder_v,path2=now_yrs_sub_folder_v)
        
            return now_date_sub_folder_v

        except FileNotFoundError:
            pass
    
    def chngpath(self):

        dir_dialog_title = "Please choose folder (or directory) to be changed for '{}' folder:".format(main_folder_name)
        
        chngdir_dlgbox = QFileDialog.getExistingDirectory(self, caption=dir_dialog_title)
           
        if chngdir_dlgbox:

            usr_chng_rt_v = chngdir_dlgbox.replace("/","\\")

            # print(usr_chng_rt_v)

            try:

                self.json_update_infos(json_flpath3=path_json_fl1_rt,keys3="path",info3=usr_chng_rt_v)
                
                returned_path = self.read_path_json(jsonfl_path1=path_json_fl1_rt,k1="path")

                # AppName audio folder path 
                app_main_folder_v = os.path.join(returned_path,main_folder_name)

                # Current year folder path
                now_yrs_sub_folder_v = os.path.join(app_main_folder_v,dt_yyyy)

                # Current month number-month folder path
                now_mnthsno_mnths_sub_folder_v = os.path.join(now_yrs_sub_folder_v,dt_mnthsno_mnths)

                # Current date folder path
                now_date_sub_folder_v = os.path.join(now_mnthsno_mnths_sub_folder_v,dt_date)

                self.foldershortcut_maker_dt(path1=app_main_folder_v,path3=now_mnthsno_mnths_sub_folder_v,path4=now_date_sub_folder_v,path2=now_yrs_sub_folder_v)

                self.msg_autoClose(msg_text="Path changed successfully.      ",msg_title="Path update - Complete:",close_tmr=2,msg_icon=QMessageBox.Information)

            except FileNotFoundError:

                usr_rt_v = chngdir_dlgbox.replace("/","\\")

                self.json_write_infos(json_flpath1=path_json_fl1_rt,keys1="path",val1=usr_rt_v)

                returned_path = self.read_path_json(jsonfl_path1=path_json_fl1_rt,k1="path")

                # AppName audio folder path 
                app_main_folder_v = os.path.join(returned_path,main_folder_name)

                # Current year folder path
                now_yrs_sub_folder_v = os.path.join(app_main_folder_v,dt_yyyy)

                # Current month number-month folder path
                now_mnthsno_mnths_sub_folder_v = os.path.join(now_yrs_sub_folder_v,dt_mnthsno_mnths)

                # Current date folder path
                now_date_sub_folder_v = os.path.join(now_mnthsno_mnths_sub_folder_v,dt_date)

                self.foldershortcut_maker_dt(path1=app_main_folder_v,path3=now_mnthsno_mnths_sub_folder_v,path4=now_date_sub_folder_v,path2=now_yrs_sub_folder_v)

                self.msg_autoClose(msg_text="Path saved successfully.               ",msg_title="Path save - Complete:",close_tmr=2,msg_icon=QMessageBox.Information)

            else:
                pass 
            # print("\n> Path changed")
        else:
            pass

    def save_path_json(self):
        """ Verify '.json' if exists or not """
        path_json_fl1_exists = os.path.exists(path_json_fl1_rt)

        if path_json_fl1_exists == False:
            
            dir_dialog_title = "Please choose folder (or directory) to hold '{}' folder:".format(main_folder_name)
            dir_dlgbox = QFileDialog.getExistingDirectory(self, caption=dir_dialog_title)
           
            if dir_dlgbox:

                usr_rt_v = dir_dlgbox.replace("/","\\")

                self.json_write_infos(json_flpath1=path_json_fl1_rt,keys1="path",val1=usr_rt_v)

                self.msg_autoClose(msg_text="Path saved successfully.                        ",msg_title="Path save - Complete:",close_tmr=2,msg_icon=QMessageBox.Information)

                #sys.exit()
            else:
                pass
        else:
            pass
        # pass

if __name__ == "__main__":   
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
