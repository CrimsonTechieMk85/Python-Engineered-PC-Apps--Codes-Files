import wx



class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title =title, size = (800,600))



        panel = MyPanel(self)


class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)


        #self.textCtrl = wx.TextCtrl(self, style = wx.TE_PASSWORD)
        #self.textCtrl = wx.TextCtrl(self, style = wx.TE_MULTILINE)
        #self.textCtrl = wx.TextCtrl(self, style = wx.TE_READONLY)


        self.textCtrl = wx.TextCtrl(self, size = (200,100), style = wx.TE_MULTILINE)

        #self.textCtrl.Bind(wx.EVT_SET_FOCUS, self.highlightText)





class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(parent=None, title="Text Control")
        self.frame.Show()
        return True



app = MyApp()
app.MainLoop()