from msilib import type_binary
from msilib.schema import tables
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
from cryptography.fernet import Fernet
from PyQt5.QtWidgets import QFileDialog, QWidget , QInputDialog , QLineEdit
import csv
import mysql.connector
import pandas as pd
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

''' px - SSettings file path '''
# pX [Prototype] - eXperimental App Json files details
px_json_name = '{}_datas'.format(file_name)

px_paths_infos_flname_json= '{}.json'.format(px_json_name)

px_path_datas_json_fl_rt = os.path.join(cdir,px_paths_infos_flname_json)

''' pX - App Details '''
# pX [Prototype] - eXperimental App title ISA
px_app_title = "I.S.A Prototype: mySQ2EXCEL Exporter [X0-{}]".format(file_name)

# pX [Prototype] - eXperimental audio folder with app name
px_main_folder_name = '{} excel files'.format(file_name)

# -----------------------------------------------------------------------------------------


# =======================================================================================\

#                     App infos

# --------------------------------------------------------------------------------
''' Folder names '''
# Audio folder with app name
app_folder_name = 'MySQL2Excel Exporter 1-105 (Credentails Secured-type) [I.S.A]'
main_folder_name = '{} excel files'.format(app_folder_name)

# -----------------------------------------------------------------------------------------

''' Settings file path '''
# Path json files details
jsonfl1_name = 'path1105_datas'

json_fl1_name = '{}.json'.format(jsonfl1_name)

path_json_fl1_rt = os.path.join(cdir,json_fl1_name)

# Path json files details
jsonfl2_name = 'mySQL1105_datas'

json_fl2_name = '{}.json'.format(jsonfl2_name)

json_fl2_rt = os.path.join(cdir,json_fl2_name)

# App title
app_title = "MySQL 2 Excel: Exporter 1-105 (Credentails Secured-type) [Improved.Simplified.Alternative]"

# ---------------------------------------------------------------------------

# encryptor key
key = "54NxGh1jHbQKeUl_mHM0PXg363MkmtFsrpgRGA1rI2g="

cipher = Fernet(key)

# Key-Value pairs
# Keys
k1 = "mysql_host"
k2 = "mysql_db"
k3 = "mysql_user"
k4 = "mysql_password"
k5 = "mysql_table"
        

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

    # Main 
        # -> Main frame
        self.mainframe = QtWidgets.QFrame(self.centralwidget)
        self.mainframe.setGeometry(QtCore.QRect(10, 10, 781, 561))
        self.mainframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainframe.setObjectName("mainframe")

    # Button
        # -> Button frame
        self.btns_frame = QtWidgets.QFrame(self.mainframe)
        self.btns_frame.setGeometry(QtCore.QRect(10, 10, 751, 511))
        self.btns_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.btns_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.btns_frame.setObjectName("btns_frame")

        # -> Export Button
        self.exprt_btn = QtWidgets.QPushButton(self.btns_frame)
        self.exprt_btn.setGeometry(QtCore.QRect(50, 80, 251, 111))
        font = QtGui.QFont()
        font.setPointSize(45)
        self.exprt_btn.setFont(font)
        self.exprt_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exprt_btn.setObjectName("exprt_btn")
 

        # -> Access Open Button
        self.access_btn_2 = QtWidgets.QPushButton(self.btns_frame)
        self.access_btn_2.setGeometry(QtCore.QRect(460, 80, 251, 111))
        font = QtGui.QFont()
        font.setPointSize(45)
        self.access_btn_2.setFont(font)
        self.access_btn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.access_btn_2.setObjectName("access_btn_2")


        # -> Exit Button
        self.exit_btn_3 = QtWidgets.QPushButton(self.btns_frame)
        self.exit_btn_3.setGeometry(QtCore.QRect(260, 340, 251, 111))
        font = QtGui.QFont()
        font.setPointSize(45)
        self.exit_btn_3.setFont(font)
        self.exit_btn_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exit_btn_3.setObjectName("exit_btn_3")

    # Widgets
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")

    # Options
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuOptions.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.menuSettings = QtWidgets.QMenu(self.menuOptions)
        self.menuSettings.setToolTipsVisible(True)
        self.menuSettings.setObjectName("menuSettings")

        self.menuMySQL_DB_setttings = QtWidgets.QMenu(self.menuSettings)
        self.menuMySQL_DB_setttings.setStatusTip("")
        self.menuMySQL_DB_setttings.setObjectName("menuMySQL_DB_setttings")

        self.menuChange_app_s_MySQL_account_credentials = QtWidgets.QMenu(self.menuMySQL_DB_setttings)
        self.menuChange_app_s_MySQL_account_credentials.setObjectName("menuChange_app_s_MySQL_account_credentials")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.actionChange_path = QtWidgets.QAction(MainWindow)
        self.actionChange_path.setObjectName("actionChange_path")

        self.actionOpen_logsfolder_4 = QtWidgets.QAction(MainWindow)
        self.actionOpen_logsfolder_4.setObjectName("actionOpen_logsfolder_4")

        self.actionChange_MySQL_Table_name = QtWidgets.QAction(MainWindow)
        self.actionChange_MySQL_Table_name.setObjectName("actionChange_MySQL_Table_name")

        self.actionChange_MySQL_user_name = QtWidgets.QAction(MainWindow)
        self.actionChange_MySQL_user_name.setObjectName("actionChange_MySQL_user_name")

        self.actionChange_app_s_MySql_Database_name = QtWidgets.QAction(MainWindow)
        self.actionChange_app_s_MySql_Database_name.setObjectName("actionChange_app_s_MySql_Database_name")

        self.actionChange_app_s_MySQL_Table = QtWidgets.QAction(MainWindow)
        self.actionChange_app_s_MySQL_Table.setObjectName("actionChange_app_s_MySQL_Table")

        self.actionChange_MySQL_account_user_name = QtWidgets.QAction(MainWindow)
        self.actionChange_MySQL_account_user_name.setObjectName("actionChange_MySQL_account_user_name")

        self.actionChange_MySQL_account_password_2 = QtWidgets.QAction(MainWindow)
        self.actionChange_MySQL_account_password_2.setObjectName("actionChange_MySQL_account_password_2")

        self.actionOpen_folder_3 = QtWidgets.QAction(MainWindow)
        self.actionOpen_folder_3.setObjectName("actionOpen_folder_3")

        self.menuChange_app_s_MySQL_account_credentials.addAction(self.actionChange_MySQL_account_user_name)
        self.menuChange_app_s_MySQL_account_credentials.addSeparator()

        self.menuChange_app_s_MySQL_account_credentials.addAction(self.actionChange_MySQL_account_password_2)

        self.menuMySQL_DB_setttings.addAction(self.actionChange_app_s_MySql_Database_name)
        self.menuMySQL_DB_setttings.addSeparator()

        self.menuMySQL_DB_setttings.addAction(self.actionChange_app_s_MySQL_Table)
        self.menuMySQL_DB_setttings.addSeparator()

        self.menuMySQL_DB_setttings.addAction(self.menuChange_app_s_MySQL_account_credentials.menuAction())
        self.menuSettings.addAction(self.actionChange_path)
        self.menuSettings.addSeparator()

        self.menuSettings.addAction(self.menuMySQL_DB_setttings.menuAction())
        self.menuOptions.addAction(self.menuSettings.menuAction())
        self.menuOptions.addSeparator()
        
        self.menuOptions.addAction(self.actionOpen_folder_3)
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menuOptions.addSeparator()

        self.menuOptions.addAction(self.actionOpen_logsfolder_4)
        self.menubar.addAction(self.menuOptions.menuAction())
        # self.menuOptions.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def apps_log_sys(self,logdirs6_path,logfl_path6,infos6):

        try:
            os.makedirs(logdirs6_path)
        except OSError:
            pass
        # logs_folder_path = os.path.join(logdirs6_path,log_dirname6)

        with open(logfl_path6,"a") as logfl_w6:
            logfl_w6.writelines(infos6)

        # pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", app_title))

    # Buttons 

        # -> Export button
        self.exprt_btn.setToolTip(_translate("MainWindow", "Click here to export MySQL Table as excel (Ctrl+E)."))
        self.exprt_btn.setStatusTip(_translate("MainWindow", "Convert MySQL Table as excel table",))
        self.exprt_btn.setText(_translate("MainWindow", "Export"))
        self.exprt_btn.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.exprt_btn.clicked.connect(self.mysql2excel)

        # -> Access button
        self.access_btn_2.setToolTip(_translate("MainWindow", "Click here to  open '{}' sub folder (Ctrl+O).".format(dt_date)))
        self.access_btn_2.setText(_translate("MainWindow", "Access"))
        self.access_btn_2.clicked.connect(self.openfolder)

        # -> Exit button
        self.exit_btn_3.setToolTip(_translate("MainWindow", "Click here to exit the app."))
        self.exit_btn_3.setText(_translate("MainWindow", "Exit"))
        self.exit_btn_3.clicked.connect(self.exit)

        
    # Options
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))

    # First child option

        #-> Settings     
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))

        #-> Open Folder 
        self.actionOpen_folder_3.setText(_translate("MainWindow", "Open '{}' sub folder".format(dt_date)))
        # self.actionOpen_folder_3.setToolTip(_translate("MainWindow", "Open folder"))
        self.actionOpen_folder_3.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionOpen_folder_3.triggered.connect(self.openfolder)

        #-> Open Logs 
        self.actionOpen_logsfolder_4.setText(_translate("MainWindow", "Open logs folder"))
        self.actionOpen_logsfolder_4.setToolTip(_translate("MainWindow", "Open logs folder"))
        self.actionOpen_logsfolder_4.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.actionOpen_logsfolder_4.triggered.connect(self.open_logsfolder)

    # Second child option from Settings option

        #-> Change path
        self.actionChange_path.setText(_translate("MainWindow", "Change folder (or Directory)"))
        # self.actionChange_path.setToolTip(_translate("MainWindow", "Change path for '{}' folder".format(main_folder_name)))
        self.actionChange_path.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionChange_path.triggered.connect(self.chngpath)

        # -> Change MySQL DB settings
        self.menuMySQL_DB_setttings.setTitle(_translate("MainWindow", "Change MySQL DB setttings"))
        
    # Third child option from Change MySQL DB setttings option

        #-> Change MySQL Database name     
        self.actionChange_app_s_MySql_Database_name.setText(_translate("MainWindow", "Change app\'s MySQL Database name"))
        self.actionChange_app_s_MySql_Database_name.triggered.connect(self.chngapp3_mysql_dbname)

        #-> Change app's MySQL table name
        self.actionChange_app_s_MySQL_Table.setText(_translate("MainWindow", "Change app\'s MySQL Table name"))
        self.actionChange_app_s_MySQL_Table.triggered.connect(self.chngapp3_mysql_tblname)

        #-> Change app's MySQL account credentials
        self.menuChange_app_s_MySQL_account_credentials.setTitle(_translate("MainWindow", "Change app\'s MySQL account credentials"))
    
    # Fourth child Options from Change app's MySQL account credentials options

        # Change app's MySQL account password
        self.actionChange_MySQL_account_password_2.setText(_translate("MainWindow", "Change app\'s MySQL user password"))
        self.actionChange_MySQL_account_password_2.setShortcut(_translate("MainWindow", "Ctrl+Shift+P"))
        self.actionChange_MySQL_account_password_2.triggered.connect(self.chngapp3_mysql_userpasword)

        # Change app's MySQL account name
        self.actionChange_MySQL_account_user_name.setText(_translate("MainWindow", "Change app\'s MySQL user name"))
        self.actionChange_MySQL_account_user_name.setShortcut(_translate("MainWindow", "Ctrl+Shift+U"))
        self.actionChange_MySQL_account_user_name.triggered.connect(self.chngapp3_mysql_username)
     
    def save_mysql(self):

        # Save requiries as a json file
        if os.path.exists(json_fl2_rt)== False:
            host_v1, okPressed1 = QInputDialog.getText(self, "Get user MySQL user","Please the type name of your MySQL host:", QLineEdit.Normal, "localhost")

            if okPressed1 and host_v1 != '':
                db_v2, okPressed2 = QInputDialog.getText(self, "Get user MySQL user","Please the type name of your MySQL database:", QLineEdit.Normal, "")
                
                if okPressed2 and db_v2 != '':

                    usr_v3, okPressed3 = QInputDialog.getText(self, "Get user MySQL user","Please the type your MySQL user name:", QLineEdit.Normal, "root")

                    if okPressed3 and usr_v3 != '':

                        passwrd_v4, okPressed4 = QInputDialog.getText(self, "Get user MySQL user","Please the type your MySQL password:", QLineEdit.Password, "")

                        if okPressed4 and passwrd_v4 != '':

                            tbl_v5, okPressed5 = QInputDialog.getText(self, "Get user MySQL user","Please the type name of your MySQL table:", QLineEdit.Normal, "")

                            if okPressed5 and tbl_v5 != '':

                                # Encrypted MySQL credentails 
                                encrypted_mysql_host = cipher.encrypt(bytes(str(host_v1), 'utf-8')).decode()
                                encrypted_mysql_db = cipher.encrypt(bytes(str(db_v2.lower()), 'utf-8')).decode()
                                encrypted_mysql_user = cipher.encrypt(bytes(str(usr_v3.lower()), 'utf-8')).decode()
                                encrypted_mysql_password = cipher.encrypt(bytes(str(passwrd_v4), 'utf-8')).decode()
                                encrypted_mysql_table = cipher.encrypt(bytes(str(tbl_v5.lower()), 'utf-8')).decode()
                                
                                # Normal 
                                # self.mysql_infos_save_json(jsonfl3_path=json_fl2_rt,key1=k1,key2=k2,key3=k3,key4=k4,key5=k5,value1=host_v1,value2=db_v2.lower(),value3=usr_v3.lower(),value4=passwrd_v4,value5=tbl_v5.lower())
                            
                                # Encrypted
                                self.mysql_infos_save_json(jsonfl3_path=json_fl2_rt,key1=k1,key2=k2,key3=k3,key4=k4,key5=k5,value1=encrypted_mysql_host,value2=encrypted_mysql_db,value3=encrypted_mysql_user,value4=encrypted_mysql_password,value5=encrypted_mysql_table)
                            elif okPressed5 and tbl_v5 == '':
                                self.msg_autoClose(msg_text="Invlaid input.                        ",msg_title="Input Verifer - Error:",close_tmr=6)
                            else:
                                pass

                        elif okPressed4 and passwrd_v4 == '':
                            self.msg_autoClose(msg_text="Invlaid input.                        ",msg_title="Input Verifer - Error:",close_tmr=6)
                        else:
                            pass
                    elif okPressed3 and usr_v3 == '':
                        self.msg_autoClose(msg_text="Invlaid input.                        ",msg_title="Input Verifer - Error:",close_tmr=6)
                    else:
                        pass
                elif okPressed2 and db_v2 == '':
                    self.msg_autoClose(msg_text="Invlaid input.                        ",msg_title="Input Verifer - Error:",close_tmr=6)
                else:
                    pass

            elif okPressed1 and host_v1 == '':
                self.msg_autoClose(msg_text="Invlaid input.                        ",msg_title="Input Verifer - Error:",close_tmr=6)
            else:
                pass
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
            
    def mysql2excel(self):
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

        """ Verify '.json' if exists or not """
        path_json_fl1_exists = os.path.exists(path_json_fl1_rt)

        if path_json_fl1_exists == True:


            try:

                self.save_mysql()

                if os.path.exists(json_fl2_rt)== True:
                    returned_mysql_host, returned_mysql_db , returned_mysql_user , returned_mysql_password  , returned_mysql_table = self.read_mysql_infos_json(jsonfl_path=json_fl2_rt,key1=k1,key2=k2,key3=k3,key4=k4,key5=k5)

                    
                    # print(f"\nMySQL _> Host: {returned_mysql_host} | DB: {returned_mysql_db} | User: {returned_mysql_user} | Password: {returned_mysql_password} | Table: {returned_mysql_table}")
                    
                    # Connecting with mySQL DB
                    # connection = mysql.connector.connect(host=returned_mysql_host,database=returned_mysql_db,user=returned_mysql_user,password=returned_mysql_password)


                    # Decoded MySQL credentails from json file 
                    decoded_json_mysql_host = cipher.decrypt(bytes(returned_mysql_host, 'utf-8')).decode()
                    decoded_json_mysql_db = cipher.decrypt(bytes(returned_mysql_db, 'utf-8')).decode()
                    decoded_json_mysql_user = cipher.decrypt(bytes(returned_mysql_user, 'utf-8')).decode()
                    decoded_json_mysql_password = cipher.decrypt(bytes(returned_mysql_password, 'utf-8')).decode()
                    decoded_json_mysql_table = cipher.decrypt(bytes(returned_mysql_table, 'utf-8')).decode()
                    
                    # print(f"\nMySQL decoded _> Host: {decoded_json_mysql_host} | DB: {decoded_json_mysql_db} | User: {decoded_json_mysql_user} | Password: {decoded_json_mysql_password} | Table: {decoded_json_mysql_table}")
                    
                    # Connecting with mySQL DB with decoded parameters
                    connection = mysql.connector.connect(host=decoded_json_mysql_host,database=decoded_json_mysql_db,user=decoded_json_mysql_user,password=decoded_json_mysql_password)
                    
                    # Connect with DB & Extract datas
                    cursor1 = connection.cursor()

                    # Requesting query to get table from mySQL DB
                    sql_q = "select * from {}".format(returned_mysql_table)
                
                    cursor1.execute(sql_q)

                    # Fetches\Extracts data based on the query (sql_q)
                    mysql_data = cursor1.fetchall()

                    # Shows table contents list
                    # print("\n"+str(mysql_data))

                    # Requesting query to get table column names from mySQL DB
                    sql_q1 = "SHOW columns FROM {}".format(decoded_json_mysql_table)

                    # Connect with DB & Extract datas
                    cursor2 = connection.cursor()
                    
                    cursor2.execute(sql_q1)
            
                    # Fetches\Extracts data based on the query (sql_q1)
                    mysql_tbl1_columns = cursor2.fetchall()

                    # Shows table columns as tuple string
                    # print("\n"+str(mysql_tbl1_columns))

                    l1 = []
        
                    for n in range(0,len(mysql_tbl1_columns),1):
                        # Convert each tuple element into list by appending to empty list (i.e; l1)
                        for row1 in mysql_tbl1_columns:
                            # print(row1[n])
                            l1.append(row1[n])
                        break

                    # Print l1 list element
                    # print("\n MySQL Table columns as lists: "+str(l1))

                    # Extracting path (Date folder location) from fintion using return
                    returned_path_dt_date = self.get_json_paths()

                    # Commma seperated file details
                    csvfl1_name = "{0}_{1}_MySQL-CSV".format(decoded_json_mysql_table,decoded_json_mysql_db)

                    csvfl1 = "{}.csv".format(csvfl1_name)

                    csvfl1_path = os.path.join(returned_path_dt_date,csvfl1)

                    # Excel file details
                    xlsxfl2_name = "{0}_{1}_MySQL-Xcel".format(decoded_json_mysql_table,decoded_json_mysql_db)

                    xlsxfl2 = "{}.xlsx".format(xlsxfl2_name)

                    xlsxfl2_path = os.path.join(returned_path_dt_date,xlsxfl2)

                    while True:

                        if os.path.exists(xlsxfl2_path)==False:# Read json

                            # Store the mySQL data into CSV (.csv) file
                            with open(csvfl1_path, 'w', newline='') as csvfl_w:
                                # read the CSV file
                                csv_writer = csv.writer(csvfl_w)

                                csv_writer.writerow(l1)

                                # Iterate (Loop) into each row (Having values as list seprated by comma)
                                for row in mysql_data:
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

                            self.msg_autoClose(msg_text=f"MySQL table '{decoded_json_mysql_table}' sucessfully exported as excel file ({xlsxfl2}).                      ",msg_title="My2Excel Export - Success:",close_tmr=6)

                            # os.startfile(csvfl1_path)

                        else:
                            self.msg_autoClose(msg_text=f"MySQL2Excel: Exporter failed, cause: '{decoded_json_mysql_table}' mySQL table already exported as excel file ({xlsxfl2}).                      ",msg_title="My2Excel Export - Failed:",close_tmr=6)

                            del_yn_msg = QMessageBox()

                            del_yn_msg.setIcon(QMessageBox.Question)
                                                
                            del_yn_msg.setText(f"Do you wish to delete the '{xlsxfl2}' excel file")
                                                
                            del_yn_msg.setWindowTitle("Delete - Yes/No:")
                                                
                            del_yn_msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

                            del_msg_returnValue = del_yn_msg.exec()

                            print(del_msg_returnValue)

                            if del_msg_returnValue == QMessageBox.No:
                                break
                            elif del_msg_returnValue == QMessageBox.Yes:
                                os.remove(xlsxfl2_path)

                                self.msg_autoClose(msg_text=f"'{xlsxfl2}' sucessfully deleted.                      ",msg_title="Delete - Success:",close_tmr=6)
                            else:
                                pass
            
            except mysql.connector.Error as err:

                log_err = f"\n<{dt_date}\{dt_time}> , Error: {str(err)}\n<________________________________________>\n"
                self.msg_autoClose(msg_text=f"Error cause: \n{str(err)} .                      ",msg_title="MySQL2Excel: Exporter Generic Error:",close_tmr=4)

                # Log file details
                log_dirname = "Logs"
                logs_folder_path = os.path.join(cdir,log_dirname)
                logfl_name = "Log_{}".format(dt_date)
                log_fl = "{}.log".format(logfl_name)

                logfl_path = os.path.join(logs_folder_path,log_fl)
                self.apps_log_sys(logfl_path6=logfl_path,logdirs6_path=logs_folder_path,infos6=log_err)
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

        self.msg_autoClose(msg_text="Thank you for your kind co-operation. MySQL credentails saved and ready to use.                        ",msg_title="MySQL credentails update - Complete:",close_tmr=6)
           
    def open_logsfolder(self):

        log_dirname = "Logs"
        logs_folder_path = os.path.join(cdir,log_dirname)

        try:
            os.makedirs(logs_folder_path)
        except OSError:
            pass

        os.startfile(logs_folder_path)

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
        # px_path = os.path.join(desktop, '{} - Shortcut.lnk'.format(px_main_folder_name))
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

    def msg_autoClose(self,msg_title,msg_text,close_tmr):

        qm = QMessageBox()
        qm.setWindowTitle(msg_title)
        qm.setText(msg_text)
        qm.setStandardButtons(QMessageBox.Ok)
        QTimer.singleShot(close_tmr*1000,lambda : qm.done(0))
        qm.setFixedWidth(800)
        qm.setFixedHeight(1755)
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

        self.msg_autoClose(msg_text=msg_txt2+"                        ",msg_title=msg_title2,close_tmr=6)

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
            host2_v1.setLabelText("Please enter new MySQL host to be changed:")
            host2_v1.setTextValue("root")
            host2_v1.setTextEchoMode(QLineEdit.Normal)
            host2_v1.setFont(font)
            host2_v1.resize(400, 240)
            host2_v1_txt = host2_v1.textValue()
            okPressed1_2 = host2_v1.exec_()

            if okPressed1_2==True and host2_v1_txt != '':

                if os.path.exists(json_fl2_rt)==True:
                    encrypted_mysql_host2_v1 = cipher.encrypt(bytes(str(host2_v1_txt), 'utf-8')).decode()

                    
                    self.json_mysql_update_infos(json_flpath2=json_fl2_rt,info=encrypted_mysql_host2_v1,keys2=k1,msg_title2="MySQL host update - Complete:",msg_txt2="MySQL host succesfully changed.")
            
                    break
                else:
                    self.msg_autoClose(msg_text="Opps! Sorry, could not update\modify MySQL credentails. Seeking alternative....                                                  ",msg_title="MySQL change - Error:",close_tmr=6)

                    self.save_mysql()
            elif okPressed1_2==True and host2_v1_txt == '':
                self.msg_autoClose(msg_text="Invalid input.                        ",msg_title="Input Verifer - Error:",close_tmr=3)
            elif okPressed1_2==False and host2_v1_txt == '':
                break
            elif okPressed1_2==False and host2_v1_txt != '':
                break
            else:
                pass

        # print("\n_> MySQL: Host changed.")
    
    def chngapp3_mysql_username(self):

        while True:

            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(17)

            usr2_v3 = QInputDialog(self)
            usr2_v3.setWindowTitle("Modify app's MySQL user:")
            usr2_v3.setLabelText("Please the type your MySQL user name to be changed:")
            usr2_v3.setTextValue("root")
            usr2_v3.setTextEchoMode(QLineEdit.Normal)
            usr2_v3.setFont(font)
            usr2_v3.resize(400, 240)
            usr2_v3_txt = usr2_v3.textValue()
            okPressed3_2 = usr2_v3.exec_()
            
            if okPressed3_2==True and usr2_v3_txt != '':

                if os.path.exists(json_fl2_rt)==True:
                    encrypted_mysql_user2 = cipher.encrypt(bytes(str(usr2_v3_txt.lower()), 'utf-8')).decode()
                    
                    self.json_mysql_update_infos(json_flpath2=json_fl2_rt,info=encrypted_mysql_user2,keys2=k3,msg_title2="MySQL user update - Complete:",msg_txt2="MySQL host succesfully changed.")

                    break
                else:
                    self.msg_autoClose(msg_text="Opps! Sorry, could not update\modify MySQL credentails. Seeking alternative....                                                  ",msg_title="MySQL change - Error:",close_tmr=6)

                    self.save_mysql()
            elif okPressed3_2==True and usr2_v3_txt == '':
                self.msg_autoClose(msg_text="Invalid input.                        ",msg_title="Input Verifer - Error:",close_tmr=3)
            elif okPressed3_2==False and usr2_v3_txt == '':
                break
            elif okPressed3_2==False and usr2_v3_txt != '':
                break
            else:
                pass
        
        # print("\n_> MySQL: User name changed.")

    def chngapp3_mysql_userpasword(self):

        while True:

            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(17)
    
            passwrd2_v4 = QInputDialog(self)
            passwrd2_v4.setWindowTitle("Modify app's MySQL password:")
            passwrd2_v4.setLabelText('"Please the type your MySQL password to be changed:"')
            passwrd2_v4.setTextEchoMode(QLineEdit.Password)
            passwrd2_v4.setFont(font)
            passwrd2_v4.resize(400, 240)
            okPressed4_2 = passwrd2_v4.exec_()
            passwrd2_v4_txt = passwrd2_v4.textValue()
        
            if okPressed4_2==True and passwrd2_v4_txt != '':

                if os.path.exists(json_fl2_rt)==True:
                
                    encrypted_mysql_password2 = cipher.encrypt(bytes(str(passwrd2_v4), 'utf-8')).decode()

                    self.json_mysql_update_infos(json_flpath2=json_fl2_rt,info=encrypted_mysql_password2,keys2=k4,msg_title2="MySQL user update - Complete:",msg_txt2="MySQL user succesfully changed.")
                
                    break
                else:
                    self.msg_autoClose(msg_text="Opps! Sorry, could not update\modify MySQL credentails. Seeking alternative....                                                  ",msg_title="MySQL change - Error:",close_tmr=6)

                    self.save_mysql()
            elif okPressed4_2==True and passwrd2_v4_txt == '':
                self.msg_autoClose(msg_text="Invalid input.                        ",msg_title="Input Verifer - Error:",close_tmr=3)
            elif okPressed4_2==False and passwrd2_v4_txt == '':
                break
            else:
                pass
          
        # print("\n_> MySQL: Password changed.")

    def chngapp3_mysql_tblname(self):
          
        while True:

            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(17)
        
            tbl2_v5 = QInputDialog(self)
            tbl2_v5.setWindowTitle("Modify app's MySQL table:")
            tbl2_v5.setLabelText("Please enter new MySQL table name be changed:")
            tbl2_v5.setTextEchoMode(QLineEdit.Normal)
            tbl2_v5.setFont(font)
            tbl2_v5.resize(400, 240)
            okPressed5_2 = tbl2_v5.exec_()
            tbl2_v5_txt = tbl2_v5.textValue()
                    
            if okPressed5_2 and tbl2_v5_txt != '':
                if os.path.exists(json_fl2_rt)==True:
                    encrypted_mysql_table2 = cipher.encrypt(bytes(str(tbl2_v5_txt.lower()), 'utf-8')).decode()
                    
                    self.json_mysql_update_infos(json_flpath2=json_fl2_rt,info=encrypted_mysql_table2,keys2=k5,msg_title2="MySQL table update - Complete:",msg_txt2="MySQL table succesfully changed.")

                    break
                else:
                    self.msg_autoClose(msg_text="Opps! Sorry, could not update\modify MySQL credentails. Seeking alternative....                                                  ",msg_title="MySQL change - Error:",close_tmr=6)

                    self.save_mysql()
            elif okPressed5_2==True and tbl2_v5_txt == '':
                self.msg_autoClose(msg_text="Invalid input.                        ",msg_title="Input Verifer - Error:",close_tmr=3)
            
            elif okPressed5_2==False and tbl2_v5_txt == '':
                break
            else:
                pass

        # print("\n_> MySQL: Table name changed.")

    def chngapp3_mysql_dbname(self):

        while True:

            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(17)
        
            db2_v2 = QInputDialog(self)
            db2_v2.setWindowTitle("Modify app's MySQL database:")
            db2_v2.setLabelText("Please enter new MySQL database be changed:")
            db2_v2.setTextEchoMode(QLineEdit.Normal)
            db2_v2.setFont(font)
            db2_v2.resize(400, 240)
            okPressed2_2 = db2_v2.exec_()
            db2_v2_txt = db2_v2.textValue()

            # db2_v2, okPressed2_2 = QInputDialog.getText(self, "Modify app's MySQL database:","Please enter new MySQL database:", QLineEdit.Normal, "")

            if okPressed2_2==True and db2_v2_txt != '':
                if os.path.exists(json_fl2_rt)==True:
                    encrypted_mysql_db2 = cipher.encrypt(bytes(str(db2_v2_txt.lower()), 'utf-8')).decode()

                    self.json_mysql_update_infos(json_flpath2=json_fl2_rt,info=encrypted_mysql_db2,keys2=k2,msg_title2="MySQL data base update - Complete:",msg_txt2="MySQL data base succesfully changed.")

                    break
                else:
                    self.msg_autoClose(msg_text="Opps! Sorry, could not update\modify MySQL credentails. Seeking alternative....                                                  ",msg_title="MySQL update - Error:",close_tmr=6)

                    self.save_mysql()
            elif okPressed2_2==True and db2_v2_txt == '':
                self.msg_autoClose(msg_text="Invalid input.                        ",msg_title="Input Verifer - Error:",close_tmr=2)
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
      
        w_yn_msg.setWindowTitle("Yes/No:")
      
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

                self.msg_autoClose(msg_text="Path saved successfully.                        ",msg_title="Path save - Complete:",close_tmr=6)

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

                self.msg_autoClose(msg_text="Path changed successfully.      ",msg_title="Path update - Complete:",close_tmr=3)

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

                self.msg_autoClose(msg_text="Path saved successfully.               ",msg_title="Path save - Complete:",close_tmr=3)

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

                self.msg_autoClose(msg_text="Path saved successfully.                        ",msg_title="Path save - Complete:",close_tmr=6)

                #sys.exit()
            else:
                pass
        else:
            pass
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
