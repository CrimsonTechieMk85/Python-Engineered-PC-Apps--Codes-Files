import wx
#from wx import EVT_STC
import time

from wx.core import EVT_CLOSE, Frame


class testUI(wx.Frame):

    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Windows UI+ experimental', size=(545,300),style = wx.DEFAULT_FRAME_STYLE & ~wx.MAXIMIZE_BOX ^ wx.RESIZE_BORDER)

        wpanel = wx.Panel(self)
        wpanel.SetBackgroundColour('white')

    #lbl "Name"

        font = wx.Font(18, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) 

        custom = wx.StaticText(wpanel,-1,"NAME:",(20,38),(22,22),wx.TEXT_ALIGNMENT_CENTRE)

        custom.SetFont(font) 

        custom.SetForegroundColour('White')

        custom.SetBackgroundColour('Red')

     #   custom.SetPosition(True)

     #   custom.SetFont()
    

    # txt feild 

        self.textCtrl = wx.TextCtrl(wpanel, pos=(108,35),size =(367,32.1), style = wx.TE_HT_ON_TEXT &~ wx.TEXT_ALIGNMENT_JUSTIFIED &~ wx.TE_WORDWRAP)

        self.textCtrl.SetFont(font) 

    # btn print

        self.wbtn = wx.Button(wpanel,label='Print',pos=(200,89),size=(90,56),style=wx.BORDER_RAISED)

        self.wbtn.SetFont(font) 

        self.wbtn.SetForegroundColour('White')

        self.wbtn.SetBackgroundColour('Red')

       # self.wbtn.SetForegroundColour('Black')

        #self.Bind(wx.EVT_STC,self.print)

        self.Bind(wx.EVT_BUTTON,self.printtxt,self.wbtn)

#        self.wbtn.Bind(wx.EVT_KEY_DOWN, self.onKeyPress)


        self.Bind(wx.EVT_CLOSE,self.exitClose)    


    def printtxt(self,event):
   #     self.wbtn.SetForegroundColour('Black')
        print("\nYou are %s." % self.textCtrl.GetValue())

   #     self.wbtn.SetForegroundColour('white')


    def exitClose(self,event):
        self.Destroy()





if __name__=='__main__':

    app=wx.App()

    frame = testUI(parent=None,id=-1)

    frame.Show()

    app.MainLoop()
