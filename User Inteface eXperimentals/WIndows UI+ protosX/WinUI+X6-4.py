import wx
#from wx import EVT_STC
import time

from wx.core import EVT_CLOSE, Frame


class testUI(wx.Frame):

    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Windows UI+ experimental 6-4', size=(642,327),style = wx.DEFAULT_FRAME_STYLE & ~wx.MAXIMIZE_BOX ^ wx.RESIZE_BORDER)

        wpanel = wx.Panel(self)
        wpanel.SetBackgroundColour('white')

    #lbl "Name"

        lblfont = wx.Font(18, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) 

        custom = wx.StaticText(wpanel,-1,"Text:",(33,38),(22,22),wx.TEXT_ALIGNMENT_CENTRE)

        custom.SetFont(lblfont) 

        custom.SetForegroundColour('White')

        custom.SetBackgroundColour('Red')

     #   custom.SetPosition(True)

     #   custom.SetFont()
    

    # txt feild 

        fieldfont = wx.Font(18, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) 

        self.textCtrl = wx.TextCtrl(wpanel, pos=(99,35),size =(490,32.1), style = wx.TE_HT_ON_TEXT &~ wx.TEXT_ALIGNMENT_JUSTIFIED &~ wx.TE_WORDWRAP)

        self.textCtrl.SetFont(fieldfont) 


    # btn print

        btnprintfont = wx.Font(18, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) 

        self.printbtn = wx.Button(wpanel,label='Click here',pos=(280,156),size=(122,34),style=wx.BORDER_RAISED)

        self.printbtn.SetFont(btnprintfont) 

        self.printbtn.SetForegroundColour('White')

        self.printbtn.SetBackgroundColour('Dark Green')

       # self.wbtn.SetForegroundColour('Black')

        #self.Bind(wx.EVT_STC,self.print)

        self.Bind(wx.EVT_BUTTON,self.printtxt,self.printbtn)

#        self.wbtn.Bind(wx.EVT_KEY_DOWN, self.onKeyPress)

    #   btn exit


        btn_exit_font = wx.Font(18, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) 

        self.exit_btn = wx.Button(wpanel,label='Exit',pos=(280,200),size=(122,34),style=wx.BORDER_RAISED)

        self.exit_btn.SetFont(btn_exit_font) 

        self.exit_btn.SetForegroundColour('White')

        self.exit_btn.SetBackgroundColour('Red')

       # self.wbtn.SetForegroundColour('Black')

        #self.Bind(wx.EVT_STC,self.print)

        self.Bind(wx.EVT_BUTTON,self.exitbutton,self.exit_btn)

       # self.Bind(wx.EVT_CLOSE,self.exitClose)    

    # accents

        accentfont = wx.Font(18, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) 

        self.accent_lists = ['en','fr','zh-CN','zh-TW','pt','es']
        
        self.tdl_lists = ['com.au','co.uk','com','ca','co.in','ie','co.za','ca','fr','com.br','pt','com.mx','es']

        self.accentlbl = wx.StaticText(wpanel, -1, "Select accent:", (31, 103))
        
        self.accentComboBox = wx.ComboBox(wpanel, -1, "en", (94.8, 139),(78,56),self.accent_lists, wx.CB_READONLY)


        self.accentlbl.SetFont(accentfont) 

        self.accentlbl.SetForegroundColour('White')

        self.accentlbl.SetBackgroundColour('Blue')

        #self.accentComboBox.GetStringSelection(0)

    #Tdls

        tdlfont = wx.Font(18, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) 

        self.tdllbl = wx.StaticText(wpanel, -1, "Select top domain level:", (334, 103))
        
        self.tdlComboBox = wx.ComboBox(wpanel, -1, "com", (498.1, 139),(81,56),self.tdl_lists, wx.CB_READONLY)

        #self.tdlComboBox.GetStringSelection(0)


        self.tdllbl.SetFont(tdlfont) 

        self.tdllbl.SetForegroundColour('White')

        self.tdllbl.SetBackgroundColour('Black')

    # status bar
      #  wstatus_bar = self.CreateStatusBar()

    def printtxt(self,event):
   #     self.wbtn.SetForegroundColour('Black')
        print("\nYou said %s." % self.textCtrl.GetValue())


        print("\nYour tdl is %s." % self.tdlComboBox.GetStringSelection())

        print("\nYour language accent is %s.\n" % self.accentComboBox.GetStringSelection())

   #     self.wbtn.SetForegroundColour('white')
        # status bar
        teskcomplete_bar = self.CreateStatusBar()

        teskcomplete_bar.SetStatusText("Text -2-Mp3: Complete")
    

        time.sleep(2.16)
        teskcomplete_bar.Destroy()

        self.textCtrl.Clear()

        self.tdlComboBox.SetValue("com")

        self.accentComboBox.SetValue("en")


#        self.printbtn.Disable()


  #      break




    def exitbutton(self,event):
        self.Close(True)

    def exitClose(self,event):
        self.Destroy()



if __name__=='__main__':

    app=wx.App()

    frame = testUI(parent=None,id=-1)

    frame.Show()

    app.MainLoop()
