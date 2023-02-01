import wx
#from wx import EVT_STC
import time

from wx.core import EVT_CLOSE, Frame


class testUI(wx.Frame):

    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Windows UI+ experimental 6', size=(634,321),style = wx.DEFAULT_FRAME_STYLE & ~wx.MAXIMIZE_BOX ^ wx.RESIZE_BORDER)

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

        self.textCtrl = wx.TextCtrl(wpanel, pos=(108,35),size =(367,32.1), style = wx.TE_HT_ON_TEXT &~ wx.TEXT_ALIGNMENT_JUSTIFIED &~ wx.TE_WORDWRAP)

        self.textCtrl.SetFont(fieldfont) 

    # btn print

        btnfont = wx.Font(18, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) 

        self.wbtn = wx.Button(wpanel,label='Print',pos=(489,36),size=(90,34),style=wx.BORDER_RAISED)

        self.wbtn.SetFont(btnfont) 

        self.wbtn.SetForegroundColour('White')

        self.wbtn.SetBackgroundColour('Red')

       # self.wbtn.SetForegroundColour('Black')

        #self.Bind(wx.EVT_STC,self.print)

        self.Bind(wx.EVT_BUTTON,self.printtxt,self.wbtn)

#        self.wbtn.Bind(wx.EVT_KEY_DOWN, self.onKeyPress)
    #btn clodse

        self.Bind(wx.EVT_CLOSE,self.exitClose)    

    # accents

        accentfont = wx.Font(18, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) 

        accent_lists = ['en','fr','zh-CN','zh-TW','pt','es']
        
        tdl_lists = ['com.au','co.uk','com','ca','co.in','ie','co.za','ca','fr','com.br','pt','com.mx','es']

        self.accentlbl = wx.StaticText(wpanel, -1, "Select accent:", (31, 103))
        
        self.accentComboBox = wx.ComboBox(wpanel, -1, "en", (94.8, 139),(78,56),accent_lists, wx.CB_SIMPLE)


        self.accentlbl.SetFont(accentfont) 

        self.accentlbl.SetForegroundColour('White')

        self.accentlbl.SetBackgroundColour('Blue')

        #self.accentComboBox.GetStringSelection(0)

    #Tdls

        tdlfont = wx.Font(18, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) 

        self.tdllbl = wx.StaticText(wpanel, -1, "Select top domain level:", (334, 103))
        
        self.tdlComboBox = wx.ComboBox(wpanel, -1, "com", (498.1, 139),(81,56),tdl_lists, wx.CB_SIMPLE)

        #self.tdlComboBox.GetStringSelection(0)


        self.tdllbl.SetFont(tdlfont) 

        self.tdllbl.SetForegroundColour('White')

        self.tdllbl.SetBackgroundColour('Black')

    def printtxt(self,event):
   #     self.wbtn.SetForegroundColour('Black')
        print("\nYou said %s." % self.textCtrl.GetValue())


        print("\nYour tdl is %s." % self.tdlComboBox.GetStringSelection())

        print("\nYour language accent is %s.\n" % self.accentComboBox.GetStringSelection())

   #     self.wbtn.SetForegroundColour('white')


    def exitClose(self,event):
        self.Destroy()





if __name__=='__main__':

    app=wx.App()

    frame = testUI(parent=None,id=-1)

    frame.Show()

    app.MainLoop()
