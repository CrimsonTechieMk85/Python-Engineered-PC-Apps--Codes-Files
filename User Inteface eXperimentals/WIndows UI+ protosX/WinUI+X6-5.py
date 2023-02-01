''' importing prefrences or getting required datas from the modules'''
import wx# for GUI apps using 'Wxpython'

import time # for 'time-delays' activities

import os # for file and folder operation

'''Source files'''

wDir_path = os.path.dirname(os.path.realpath(__file__))# curent working directory or the 'Now'-location of the file.

#icon source image file -> eg: 'image_file_name'.ico
ico_file = "101_robo_download_zEr_icon.ico"


# Combining ico file and current working directory to form complete ico file path
ico_flpath = os.path.join(wDir_path,ico_file)

# using 'class' or "blueprint" to extract all the 'frame' supports existing within the 'wx' module for GUI apps
class testUI(wx.Frame):

    # Starts frame upon user request or 'CLICKING' the app  
    def __init__(self,parent,id):
        
        # Window (Frame) with parametres i.e (frame, parent=None,id=-1.'window title',size=(int,int),style=wx.(obj))
        wx.Frame.__init__(self,parent,id,'Windows UI+ experimental 6-5', size=(642,327),style = wx.DEFAULT_FRAME_STYLE & ~wx.MAXIMIZE_BOX ^ wx.RESIZE_BORDER)

        self.SetIcon(wx.Icon(ico_flpath))# sets icon on the window title bar

        self.wpanel = wx.Panel(self)# setting 'container' to have wxpython GUI parts

        self.wpanel.SetBackgroundColour('Light orange')# sets the panel or app background as 'light blue'

    #Text

        # creates fonts for 'Text' input field
        lblfont = wx.Font(18, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) 

        self.custom_txt_lbl = wx.StaticText(self.wpanel,-1,"Text:",(33,38),(22,22),wx.TEXT_ALIGNMENT_CENTRE)

        self.custom_txt_lbl.SetFont(lblfont)# sets font for the 'Text' label using variable 'textfieldfont'

        self.custom_txt_lbl.SetForegroundColour('White')# sets the 'Text' label text colour as white

        self.custom_txt_lbl.SetBackgroundColour('Red')# sets the 'Text' label colour as red

        # text input field font
        textfieldfont = wx.Font(18, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) 

        # creates text input field
        self.textCtrl = wx.TextCtrl(self.wpanel, pos=(99,35),size =(490,32.1), style = wx.TE_HT_ON_TEXT &~ wx.TEXT_ALIGNMENT_JUSTIFIED &~ wx.TE_WORDWRAP)

        self.textCtrl.SetFont(textfieldfont)#sets font for the text input field using variable 'textfieldfont'

        self.textCtrl.SetForegroundColour('Red')#sets input field text as red


    #click here
 
        # creates fonts for click button
        btn_click_font = wx.Font(18, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) 

        # combines 'Exit' button with its functions
        self.click_btn = wx.Button(self.wpanel,label='Click here',pos=(280,156),size=(122,34),style=wx.BORDER_RAISED)

        self.click_btn.SetFont(btn_click_font)# sets 'Click here' button font using variable 'btn_click_font'

        self.click_btn.SetForegroundColour('White')# sets 'Click here' button text as white

        self.click_btn.SetBackgroundColour('Dark Green')# sets 'Click here' button as dark green

        #self.wbtn.SetForegroundColour('Black')

        #self.Bind(wx.EVT_STC,self.print)

        self.Bind(wx.EVT_BUTTON,self.printtxt,self.click_btn)# combines 'Click here' button with its functions

    #Exit

        # creates fonts for exit button
        btn_exit_font = wx.Font(18, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)# Creates  fonts for 'Exit' button 

        # Exit button 

        # creates  'Exit' button  
        self.exit_btn = wx.Button(self.wpanel,label='Exit',pos=(280,200),size=(122,34),style=wx.BORDER_RAISED)

        self.exit_btn.SetFont(btn_exit_font)# sets font for the exit button using variable 'btn_exit_font'

        self.exit_btn.SetForegroundColour('White')# sets 'Exit' button text as white

        self.exit_btn.SetBackgroundColour('Red')# sets 'Exit' button coloer as red

        self.Bind(wx.EVT_BUTTON,self.exitbutton,self.exit_btn)# combines 'Exit' button with its functions


    # Accents

        # creates  fonts for tdl
        accentfont = wx.Font(18, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) 
        
        ## label accent  

        # creates  'Select accent' label appear on the panel  
        self.accentlbl = wx.StaticText(self.wpanel, -1, "Select accent:", (31, 103))# 

        self.accentlbl.SetFont(accentfont)# sets 'Select accent:" label fonts uing parameters from 'accentfont' variable 

        self.accentlbl.SetForegroundColour('White')# sets the 'Select accent:' label text colour as white

        self.accentlbl.SetBackgroundColour('Blue')# sets the 'Select accent:' label colour as 'Black' 

        # collection or lists conataining accent items
        self.accent_lists = ['en','fr','zh-CN','zh-TW','pt','es']
        
        # accents comboboox
        self.accentComboBox = wx.ComboBox(self.wpanel, -1, "en", (94.8, 139),(78,56),self.accent_lists, wx.CB_READONLY)

        self.accentComboBox.SetFont(accentfont)# sets fonts for the accent items containing in the 'acccent' combobox

        #self.accentComboBox.SetForegroundColour('Black')

        #self.accentComboBox.SetBackgroundColour('Light Orange')


    #Tdls

        # collection or lists conataining tdl items
        self.tdl_lists = ['com.au','co.uk','com','ca','co.in','ie','co.za','ca','fr','com.br','pt','com.mx','es']

        # Creates  fonts for tdl
        tdlfont = wx.Font(18, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) 

        ## label tdl

        # Creates  'Select Top.Domain.Level (tdl):' label appear on the panel
        self.tdllbl = wx.StaticText(self.wpanel, -1, "Select Top.Domain.Level (tdl):", (269, 103))

        self.tdllbl.SetFont(tdlfont)# sets 'Select Top.Domain.Level (tdl):" label fonts uing parameters from 'tdlfont' variable 

        self.tdllbl.SetForegroundColour('White')# sets 'Select Top.Domain.Level (tdl):" label text as white 

        self.tdllbl.SetBackgroundColour('Black')# sets 'Select Top.Domain.Level (tdl):" label background as black 

        # Creates  Top.Domain.Level (tdl) combobox box with 'tdl' items from list (tdl_lists)
        self.tdlComboBox = wx.ComboBox(self.wpanel, -1, "com", (498.1, 139),(81,56),self.tdl_lists, wx.CB_READONLY)

        self.tdlComboBox.SetFont(tdlfont)# sets fonts for the tdl items containing in the 'tdl' combobox

        #self.tdlComboBox.SetForegroundColour('white')

        #self.tdlComboBox.SetBackgroundColour('black')


    def printtxt(self,event):

        text_in = self.textCtrl.GetValue()# gets the text value that within input field


        tdl_in = self.tdlComboBox.GetStringSelection()# gets the tdl value that from the tdl combobox

        accent_in = self.accentComboBox.GetStringSelection()# gets the accemt value that from the accent combobox

  
        print("\nYou said %s." % text_in)# shows the text value on console


        print("\nYour tdl is %s." % tdl_in)#  shows the tdl value on console

        print("\nYour language accent is %s.\n" % accent_in)# shows the languge code value on console

        teskcomplete_bar = self.CreateStatusBar()# creates status bar

        teskcomplete_bar.SetStatusText("Text to audio file (.Mp3): Complete")# shows that the text has been converted into audio file sw=ucessfully
    

        time.sleep(2.18)# time delay for 2.18 seconds
       

        ''' Asks user whether to use again as message box. if yes, clears the values for the user, or exits the app if no  '''
        yn_msgbox = wx.MessageDialog(self.wpanel,"Do you wish use the app again?","",wx.YES_NO)

        yn_var = yn_msgbox.ShowModal()

        if yn_var == wx.ID_YES:
            teskcomplete_bar.Destroy()# clears the status bar

            self.textCtrl.Clear()#  clears texts that exists within the input feilds

            self.tdlComboBox.SetValue("com")# setting the tdl combobox back to default

            self.accentComboBox.SetValue("en")# setting the accent combobox back to default
     
        else:
            self.Destroy()# closes app  when task is not required again


    def exitbutton(self,event):
        self.Close(True)# closes app when 'EXIT' button is click

    def exitClose(self,event):
        self.Destroy()# closes app  when 'CLOSE' or 'X' on the window is pressed



if __name__=='__main__':

    app=wx.App()# Start the app

    frame = testUI(parent=None,id=-1)# Gives parametres or infos to the class or 'Frame' components

    frame.Show()# Shows the commponents existed within the app

    app.MainLoop()# loops the window as systems close apps within milliseconds or more
