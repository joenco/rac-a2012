import wx

class javier(wx.Frame):
    
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Chat')
        panel = wx.Panel(self)
        
        status=self.CreateStatusBar()
        menubar=wx.MenuBar()
        file = wx.Menu()
        edit=wx.Menu()
        file.Append(wx.NewId(),"New","Create New Chat")
        edit.Append(wx.NewId(),"Undo","Undo")
        menubar.Append(file,"File")
        menubar.Append(edit,"Edit")
        self.SetMenuBar(menubar)
        
if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=javier(parent=None,id=1)
    frame.Show()
    app.MainLoop()
    