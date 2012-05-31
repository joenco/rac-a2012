import wx

if __name__=='__main__':
    app=wx.PySimpleApp()
    
    names=['sarah','lucky','javier']
    modal = wx.SingleChoiceDialog(None,"Whats ur name","Chat",names)
    if modal.ShowModal() == wx.ID_OK:
        print "your name is %s\n" % modal.GetStringSelection()
    modal.Destroy()    