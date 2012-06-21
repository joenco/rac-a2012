import wx
from app import Aplicacion
    
if __name__ == '__main__':
    app = wx.PySimpleApp()

    chat = Aplicacion()
    chat.SetTitle("Representante de Atencion al Cliente")
    chat.SetSize((320,480))
    chat.Centre()
    chat.Show()

    app.MainLoop()
