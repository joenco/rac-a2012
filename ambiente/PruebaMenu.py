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
        #ESTA PARTE DEL CODIGO CREA UN BOX PARA ESCRIBIR PRO LO HACE EN UNA VENTANA APARTE HAY QUE VER COMO AGREGARSELA A LA VENTANA PRINCIPAL
        box = wx.TextEntryDialog(self,"Write","write in here")
        #wx.TextEntryDialog(panel,"Write","write in here")        
        #if box.ShowModal() == wx.ID_OK:
        #    answer=box.GetValue()
        #custom = wx.StaticText(panel,-1,answer,(10,10),(300,200),wx.ALIGN_CENTER)
        custom = wx.StaticText(panel,-1,"Buenas noches",(10,10),(300,200),wx.ALIGN_CENTER)
        custom.SetForegroundColour('black')
        custom.SetBackgroundColour('white')
        
        
if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=javier(parent=None,id=1)
    frame.Show()
    app.MainLoop()
    